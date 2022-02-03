# -*- coding: utf-8 -*-
# pylint: disable=expression-not-assigned,line-too-long
"""Render text (Danish: gengive tekst)."""
import base64
import datetime as dti
import hashlib
import json
import os
import pathlib
import shutil
import sys
from typing import Dict, Generator, Iterator, List, Optional, Tuple, Union

import markdown
from markdown.extensions import attr_list  # types: ignore  # noqa: F401
from markdown.extensions import codehilite  # types: ignore  # noqa: F401
from markdown.extensions import fenced_code  # types: ignore  # noqa: F401
from markdown.extensions import meta  # types: ignore  # noqa: F401
from markdown.extensions import tables  # types: ignore  # noqa: F401
from markdown.extensions import toc  # types: ignore  # noqa: F401

BINDER_PREFIX = 'bind-'
BINDER_POSTFIX = '.txt'
BUFFER_BYTES = 2 << 15
CONFIG_NAME = 'render-config.json'
DEBUG_VAR = 'GENGIVE_DEBUG'
DEBUG = os.getenv(DEBUG_VAR)
DEFAULT_CONFIG_NAME = '.gengive.json'
DEFAULT_TARGET = 'default'
ENCODING = 'utf-8'
ENCODING_ERRORS_POLICY = 'ignore'
HIDDEN = '.'
PUBLISHER_ROOT_STR = os.getenv('GENGIVE_PUBLISHER_ROOT', '')
PUBLISHER_ROOT = pathlib.Path(PUBLISHER_ROOT_STR) if PUBLISHER_ROOT_STR else pathlib.Path.cwd()
RENDER_ROOT_STR = os.getenv('GENGIVE_RENDER_ROOT', '')
RENDER_ROOT = pathlib.Path(RENDER_ROOT_STR) if RENDER_ROOT_STR else pathlib.Path.cwd()
MEDIA_FOLDER_NAMES = os.getenv('GENGIVE_MEDIA_FOLDER_NAMES', 'diagrams,images,pictures').split(',')
NON_MANUSCRIPT_FOLDERS = os.getenv('GENGIVE_NON_MANUSCRIPT_FOLDERS', 'bin,render')
REPORT_TIMESTAMP_FORMAT = '%Y-%m-%d %H:%M:%S UTC'

PathType = pathlib.Path
ModelType = Dict[
    str, Union[float, int, str, PathType, List[str], List[PathType], Dict[str, str], List[Dict[str, Union[int, str]]]]
]

STDIN, STDOUT = 'STDIN', 'STDOUT'
DISPATCH = {
    STDIN: sys.stdin,
    STDOUT: sys.stdout,
}


def describe_file(file_path: PathType) -> Tuple[str, Union[dti.datetime, None], int]:
    """Yield sha256 hash, modification date, and byte size tuple of file."""
    if not file_path.is_file():
        return 'cafebabe' * 8, None, 0
    file_stats = file_path.stat()
    file_size_bytes = file_stats.st_size
    file_timestamp = dti.datetime.utcfromtimestamp(file_stats.st_mtime)
    with open(file_path, 'rb') as handle:
        sha256_hash = hashlib.sha256()  # noqa
        for byte_block in iter(lambda in_f=handle: in_f.read(BUFFER_BYTES), b''):  # type: ignore
            sha256_hash.update(byte_block)

        return sha256_hash.hexdigest(), file_timestamp, file_size_bytes


def workspace_path() -> PathType:
    """Derive the workspace from the module path of this script."""
    return PUBLISHER_ROOT


def manuscripts_available(workspace: PathType) -> Generator[str, None, None]:
    """Retrieve a sorted sequence of available manuscripts adhering to naming convention."""
    for candidate in sorted(
        thing.name for thing in workspace.iterdir() if thing.is_dir() and not thing.name.startswith(HIDDEN)
    ):
        if candidate not in NON_MANUSCRIPT_FOLDERS:
            yield candidate


def variants_available(manuscript_path: PathType) -> Generator[str, None, None]:
    """Retrieve a sorted sequence of available targets (variants) for manuscript adhering to naming conventions."""
    for candidate in sorted(
        thing.name for thing in manuscript_path.iterdir() if thing.is_file() and thing.name.startswith(BINDER_PREFIX)
    ):
        if candidate.endswith(BINDER_POSTFIX) and len(candidate) > len(BINDER_PREFIX + BINDER_POSTFIX):
            yield candidate.replace(BINDER_PREFIX, '').replace(BINDER_POSTFIX, '').lower()


def parse_request(root_path: PathType, argv: List[str]) -> Tuple[int, str, PathType, str, str, str, PathType]:
    """Verify the request and yield the quadruplet of error code, message, root_path, manuscript, and variant.
    The shape of argv shall be verified already to contain manuscript and variant as the only two string items.
    If error code is 0 message is empty and manuscript as well as variant are valid.
    else error code can be used as process return code and message is non-empty.
    """
    command, publisher_root_str, manuscript, variant, render_root_str = argv[:]
    publisher_root = pathlib.Path(publisher_root_str)
    render_root = pathlib.Path(render_root_str)
    if command == 'verify':
        print('Note: Dry run - verification mode.')

    if manuscript:
        m_path = pathlib.Path(manuscript)
        if m_path.is_dir():
            publisher_root = m_path.parent
            manuscript = m_path.name
            print(f'Updating publisher root from {root_path} to {publisher_root} ...')

    print(f'Retrieving manuscript folders below publisher root {publisher_root} ...')
    manuscripts = tuple(manuscripts_available(publisher_root))
    for available in sorted(manuscripts):
        print(f'- {available}')

    if manuscript not in manuscripts:
        message = f'Document({manuscript}) is not available within publisher root {publisher_root}'
        return 1, message, publisher_root, '', '', '', render_root

    print(f'Identifying variants defined for document({manuscript}) ...')
    manuscript_path = publisher_root / manuscript
    variants = tuple(variants_available(manuscript_path))
    for available in sorted(variants):
        print(f'- {available}')

    if variant not in variants:
        message = (
            f'Target({variant}) is not defined for document({manuscript})'
            f' - you may want to add a {manuscript}/bind-{variant}.txt file'
        )
        return 1, message, publisher_root, '', '', '', render_root

    print(
        f'Requested rendering document({manuscript}) for target({variant})'
        f' below {render_root}/render/{manuscript}/{variant}/ ...'
    )
    return 0, '', publisher_root, command, manuscript, variant, render_root


def load_config(config_folder: PathType, variant: str) -> Tuple[int, str, Dict[str, str]]:
    """Load the render configuration for the variant of the manuscript.
    If error code is 0 message is empty and the dict contains the mappings for rendition.
    Else error code can be used as process return code and message is non-empty.
    """
    config_path = config_folder / CONFIG_NAME
    if not config_path.is_file() or not config_path.stat().st_size:
        return 1, f'Configuration at {config_path} is no file or empty', {}

    with open(config_path, 'rt', encoding=ENCODING) as handle:
        full_config = json.load(handle)

    if not full_config.get(variant):
        return 1, f'Configuration at {config_path} lacks the variant key {variant} or the value is empty', {}

    config = full_config[variant]
    if not config.get('name'):
        return 1, f'Configuration at {config_path} for variant key {variant} lacks name (non-empty) entry', {}

    if ' ' in config['name']:
        return 1, f'The value of the {variant} "name" member SHALL NOT contain spaces in {config_path}', {}

    if config.get('css'):
        css_path = config_folder / config['css']
        if not css_path.is_file():
            return 1, f'The value of the {variant} "css" member if present SHALL be a file path {css_path}', {}
        with open(css_path, 'rt', encoding=ENCODING) as handle:
            config['css_declarations'] = handle.read()

    return 0, '', config


def load_binder(binder_folder: PathType, variant: str) -> Tuple[int, str, List[PathType]]:
    """Load the binder for the variant of the manuscript.
    If error code is 0 message is empty and the list contains the file paths for binding all files into a single file.
    Else error code can be used as process return code and message is non-empty.
    """
    binder_path = binder_folder / f'bind-{variant}.txt'
    if not binder_path.is_file() or not binder_path.stat().st_size:
        return 1, f'Binder at {binder_path} is no file or empty', []

    with open(binder_path, 'rt', encoding=ENCODING) as handle:
        binder = [binder_folder / line.strip() for line in handle.readlines() if line.strip()]

    if not binder:
        return 1, f'Binder has no entries at {binder_path}', []

    if not all(path.is_file() for path in binder):
        failing = [path.name for path in binder if not path.is_file()]
        return 1, f'Failed to find files for binder entries: ({", ".join(failing)}) in {binder_path}', []

    return 0, '', binder


def bind_parts(binder: List[PathType], collation_path: PathType) -> List[str]:
    """Given a list of paths read those files and write the concat document to collation path.
    Return the in memory document as lis of lines.
    """
    in_mem_doc = []
    for path in binder:
        with open(path, 'rt', encoding=ENCODING) as handle:
            part = [line.rstrip('\n').replace('\r', '') for line in handle.readlines()]
            if part:
                in_mem_doc.extend(part)
                in_mem_doc.append('')  # TODO(sthagen) use re-format later
    with open(collation_path, 'wt', encoding=ENCODING) as handle:
        handle.write('\n'.join(in_mem_doc))

    return in_mem_doc


def render_html(collation_path: PathType, collation_name: str, html_path: PathType, css: str) -> None:
    """Render the HTML from the markdown."""
    extensions = ['attr_list', 'codehilite', 'fenced_code', 'tables', 'toc']

    md_processor = markdown.Markdown(extensions=extensions, output_format='html')
    with open(collation_path, 'rt', encoding=ENCODING) as handle:
        html_body_content = md_processor.convert(handle.read())

    prefix = f"""<!DOCTYPE html>
    <html lang="en">
      <head>
        <meta charset="utf-8">
        <meta name="description" content="Some Documents '{collation_name}'.">
        <meta name="viewport" content="width=device-width, initial-scale=1">
          <style>
            {css}
          </style>
        <title>{collation_name}</title>
      </head>
    <body>
    """
    postfix = """
    </body>
    </html>
    """
    with open(html_path, 'wt', encoding=ENCODING) as writer:
        writer.write(prefix)
        writer.write(html_body_content)
        writer.write(postfix)


def extract_media_selection(in_mem_md_doc, manuscript_path: PathType):  # type: ignore
    """Extract the select media collection from intersection of file tree and document analysis."""
    condition_asset_mentions = []
    for line in in_mem_md_doc:
        if any(f'{name}/' in line for name in MEDIA_FOLDER_NAMES):
            condition_asset_mentions.append(line)
    lines_with_asset_mentions = '\n'.join(condition_asset_mentions)

    media_selection = []
    for asset_folder_name in MEDIA_FOLDER_NAMES:
        for path_str in sorted(pathlib.Path(manuscript_path / asset_folder_name).glob('**/*')):
            asset_path_str = str(pathlib.Path(asset_folder_name, path_str.name)).replace('\\', '/')
            if asset_path_str in lines_with_asset_mentions:
                media_selection.append(asset_path_str)

    return media_selection


def copy_media_assets(manuscript_path: PathType, media_selection: List[str], html_folder: PathType) -> None:
    """Copy select media assets from the MEDIA_FOLDER_NAMES folders to the render tree."""
    for asset_folder_name in MEDIA_FOLDER_NAMES:
        for path_str in sorted(pathlib.Path(manuscript_path / asset_folder_name).glob('**/*')):
            asset_path_str = str(pathlib.Path(asset_folder_name, path_str.name)).replace('\\', '/')
            if asset_path_str in media_selection:
                src = manuscript_path / asset_path_str
                (html_folder / asset_folder_name).mkdir(parents=True, exist_ok=True)
                dest = html_folder / asset_path_str
                shutil.copy2(src, dest)


def collect_asset_descriptions(media_selection, manuscript_path: PathType):  # type: ignore
    """LATER"""
    asset_descriptions = []
    for asset_folder_name in MEDIA_FOLDER_NAMES:
        for path_str in sorted(pathlib.Path(manuscript_path / asset_folder_name).glob('**/*')):
            asset_path_str = str(pathlib.Path(asset_folder_name, path_str.name)).replace('\\', '/')
            if asset_path_str in media_selection:
                src_path = manuscript_path / asset_folder_name / path_str.name
                a_hash, mod_at, size_bytes = describe_file(src_path)
                asset_descriptions.append((asset_path_str, a_hash, mod_at, size_bytes))
                if mod_at is None:
                    print(f'ERROR: media asset file ({src_path}) is not accessible for report of request?')
                    return 1

    asset_descriptions_reshaped = []
    for path_str, a_hash, mod_at, size_bytes in asset_descriptions:  # type: ignore
        asset_descriptions_reshaped.append(
            {
                'asset_path_str': path_str,
                'asset_hash_sha256': a_hash,
                'asset_data_version': mod_at.strftime(REPORT_TIMESTAMP_FORMAT) if mod_at else None,
                'asset_size_bytes': size_bytes,
            }
        )

    return asset_descriptions_reshaped


def document_rendering(model: ModelType, collation_folder: PathType, stdout: bool = False) -> None:
    """Provide necessary and sufficient information linking the renditions with request time information.
    The timestamps, manuscript, variant, as well as checksums identifying source and target files,
    """
    collation_report_path = collation_folder / 'render-info.json'

    report: ModelType = {**model}
    for key in report.keys():
        if isinstance(report[key], List) and report[key]:
            values: List[PathType] = report[key]  # type: ignore
            if isinstance(values[0], PathType):
                report[key] = [str(value) for value in values]
        elif isinstance(report[key], pathlib.Path):
            report[key] = str(report[key])

    if not stdout:
        with open(collation_report_path, 'wt', encoding=ENCODING) as handle:
            json.dump(report, handle, indent=2)
    else:
        print(json.dumps(report, indent=2))


def reader(path: str) -> Iterator[str]:
    """Context wrapper / generator to read the lines."""
    with open(pathlib.Path(path), 'rt', encoding=ENCODING) as handle:
        for line in handle:
            yield line


def verify_request(argv: Optional[List[str]]) -> Tuple[int, str, List[str]]:
    """Fail with grace."""
    if not argv or len(argv) != 3:
        return 2, 'received wrong number of arguments', ['']

    command, wun, two = argv
    if command not in ('render' 'verify',):
        return 2, 'received unknown command', ['']

    if command == 'verify':
        inp, config = wun, two

        if inp:
            if not pathlib.Path(str(inp)).is_file():
                return 1, 'source is no file', ['']

        if not config:
            return 2, 'configuration missing', ['']

        config_path = pathlib.Path(str(config))
        if not config_path.is_file():
            return 1, f'config ({config_path}) is no file', ['']
        if not ''.join(config_path.suffixes).lower().endswith('.json'):
            return 1, 'config has no .json extension', ['']

        return 0, '', argv

    manuscript, target = wun, two

    if manuscript:
        if not pathlib.Path(str(manuscript)).is_dir():
            return 1, 'manuscript is no folder', ['']

    if not target:
        return 2, 'target missing', ['']

    return 0, '', argv


def main(argv: Union[List[str], None] = None) -> int:
    """Drive the request, discover, rendering, and reporting processes."""
    argv = sys.argv[1:] if argv is None else argv

    if not argv or not isinstance(argv, list) or len(argv) != 5:
        print('For usage info: render --help')
        return 2

    processing_start = dti.datetime.utcnow()
    root_path = workspace_path()
    error_code, message, root_path, command, manuscript, variant, render_path = parse_request(root_path, argv)
    if error_code:
        print(f'ERROR: {message}')
        return error_code
    model: ModelType = {
        'request_parameters': argv,
        'processing_start': processing_start.strftime(REPORT_TIMESTAMP_FORMAT),
        'manuscript': manuscript,
        'variant': variant,
    }
    manuscript_path = root_path / manuscript
    error_code, message, render_config = load_config(manuscript_path, variant)
    if error_code:
        print(f'ERROR: {message}')
        return error_code
    css = render_config.get('css_declarations', '')
    if css:
        render_config['css_declarations'] = base64.b64encode(css.encode(ENCODING)).decode(ENCODING)
    a_path = manuscript_path / CONFIG_NAME
    a_hash, mod_at, size_bytes = describe_file(a_path)
    if mod_at is None:
        print(f'ERROR: configuration file ({a_path}) is not accessible for report of request?')
        return 1

    model = {
        **model,
        'manuscript_path': manuscript_path,
        'config_path': a_path,
        'config_hash_sha256': a_hash,
        'config_data_version': mod_at.strftime(REPORT_TIMESTAMP_FORMAT),
        'config_size_bytes': size_bytes,
        'render_config': render_config,
    }

    error_code, message, binder = load_binder(manuscript_path, variant)
    if error_code:
        print(f'ERROR: {message}')
        return error_code
    a_path = manuscript_path / f'bind-{variant}.txt'
    a_hash, mod_at, size_bytes = describe_file(a_path)
    if mod_at is None:
        print(f'ERROR: binder definition file ({a_path}) is not accessible for report of request?')
        return 1

    model = {
        **model,
        'binder_path': a_path,
        'binder_hash_sha256': a_hash,
        'binder_data_version': mod_at.strftime(REPORT_TIMESTAMP_FORMAT),
        'binder_size_bytes': size_bytes,
        'binder': binder,
    }

    print('Binder analysis OK, all files resolve. Sequence of binding will be:')
    for rank, part in enumerate(binder, start=1):
        print(f'{rank :>2d}: {part}')

    collation_folder = render_path / 'render' / manuscript / variant
    collation_folder.mkdir(parents=True, exist_ok=True)
    collation_name = f'{render_config["name"]}.md'
    collation_path = collation_folder / collation_name
    if command == 'verify':
        document_rendering(model, collation_folder, stdout=True)
        return 0

    print(f'Binding source documents from ({manuscript}) for target({variant}) to {collation_path} ...')
    in_mem_md_doc = bind_parts(binder, collation_path)
    lines_written = len(in_mem_md_doc)
    print(f'- Written {lines_written} lines from {len(binder)} parts to {collation_path}')
    a_hash, mod_at, size_bytes = describe_file(collation_path)
    if mod_at is None:
        print(f'ERROR: collation markdown file ({collation_path}) is not accessible for report of request?')
        return 1

    model = {
        **model,
        'collation_folder': collation_folder,
        'collation_name': collation_name,
        'collation_path': collation_path,
        'collation_hash_sha256': a_hash,
        'collation_data_version': mod_at.strftime(REPORT_TIMESTAMP_FORMAT),
        'collation_size_bytes': size_bytes,
        'lines_written': lines_written,
    }

    html_folder = collation_folder / 'html'
    html_folder.mkdir(parents=True, exist_ok=True)
    html_name = f'{render_config["name"]}.html'
    html_path = html_folder / html_name
    print(f'Writing HTML rendition from ({manuscript}) for target({variant}) to {html_path} ...')

    print(f'Creating HTML rendition of document({manuscript}) for target({variant}) below {html_folder}/ ...')
    render_html(collation_path, collation_name, html_path, css=css)
    a_hash, mod_at, size_bytes = describe_file(html_path)
    if mod_at is None:
        print(f'ERROR: rendered HTML file ({html_path}) is not accessible for report of request?')
        return 1

    model = {
        **model,
        'html_folder': html_folder,
        'html_name': html_name,
        'html_path': html_path,
        'html_hash_sha256': a_hash,
        'html_data_version': mod_at.strftime(REPORT_TIMESTAMP_FORMAT),
        'html_size_bytes': size_bytes,
    }

    print('Determine set of media assets in use ...')
    media_selection = extract_media_selection(in_mem_md_doc, manuscript_path)

    print(f'Copying the per conventions {len(MEDIA_FOLDER_NAMES)} media asset folders from source to target ...')
    copy_media_assets(manuscript_path, media_selection, html_folder)

    model['asset_descriptions'] = collect_asset_descriptions(media_selection, manuscript_path)

    print(f'Done. Entrypoint is {html_path}')
    processing_stop = dti.datetime.utcnow()
    model = {
        **model,
        'processing_stop': processing_stop.strftime(REPORT_TIMESTAMP_FORMAT),
        'processing_duration_seconds': (processing_stop - processing_start).total_seconds(),
        'render_config': render_config,
    }
    document_rendering(model, collation_folder)
    return 0
