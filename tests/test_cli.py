# -*- coding: utf-8 -*-
# pylint: disable=line-too-long,missing-docstring,reimported,unused-import,unused-variable
import click
import pytest

from gengive import cli


def test_main_legacy_ok(capsys):
    assert cli.main(['render', 'examples/bar', 'default']) == 0
    out, err = capsys.readouterr()
    parts = (
        'Updating publisher root from ',
        'Retrieving manuscript folders below publisher root ',
        '- bar',
        'Identifying variants defined for document(bar) ...',
        '- default',
        'Requested rendering document(bar) for target(default) below ',
        'Binder analysis OK, all files resolve. Sequence of binding will be:',
        ' 1: examples/bar/foo.md',
        'Binding source documents from (bar) for target(default) to ',
        '- Written 37 lines from 1 parts to ',
        'Writing HTML rendition from (bar) for target(default) to ',
        'Creating HTML rendition of document(bar) for target(default) below ',
        'Determine set of media assets in use ...',
        'Copying the per conventions 3 media asset folders from source to target ...',
        'Done. Entrypoint is ',
    )
    messages = out.rstrip().split('\n')
    for rank, message in enumerate(messages, start=0):
        print(message)
        assert message.startswith(parts[rank])

    assert not err


def test_version_ok(capsys):
    with pytest.raises(click.exceptions.Exit):
        cli.app_version()
    out, err = capsys.readouterr()
    assert 'version' in out.lower()
    assert not err


def test_callback():
    assert cli.callback(version=False) is None


def test_render(capsys):
    with pytest.raises(SystemExit):
        cli.render(manuscript='examples/bar', target='default', verify=True)
    out, err = capsys.readouterr()
    parts = (
        'Note: Dry run - verification mode.',
        'Updating publisher root from ',
        'Retrieving manuscript folders below publisher root ',
        '- bar',
        'Identifying variants defined for document(bar) ...',
        '- default',
        'Requested rendering document(bar) for target(default) below ',
        'Binder analysis OK, all files resolve. Sequence of binding will be:',
        ' 1: examples/bar/foo.md',
        '{',
        '  "request_parameters": [',
        '    "verify",',
        '    "examples/bar",',
        '    "default"',
        '  ],',
        '  "processing_start": "',
        '  "manuscript": "bar",',
        '  "variant": "default",',
        '  "manuscript_path": "examples/bar",',
        '  "config_path": "examples/bar/render-config.json",',
        '  "config_hash_sha256": "1a7de86e951d0d9374cee0dc1152fe781f16db072cb45985c300d4477374bd6e",',
        '  "config_data_version": "',
        '  "config_size_bytes": 59,',
        '  "render_config": {',
        '    "name": "the-name-of-the-thing"',
        '  },',
        '  "binder_path": "examples/bar/bind-default.txt",',
        '  "binder_hash_sha256": "38cf0d8e52b3020eb9e750c30998e1759657ad927462621ddd0b706b79a140c5",',
        '  "binder_data_version": "',
        '  "binder_size_bytes": 7,',
        '  "binder": [',
        '    "examples/bar/foo.md"',
        '  ]',
        '}',
    )
    messages = out.rstrip().split('\n')
    for rank, message in enumerate(messages, start=0):
        print(message)
        assert message.startswith(parts[rank])

    assert not err
