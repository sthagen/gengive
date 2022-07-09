# -*- coding: utf-8 -*-
# pylint: disable=line-too-long,missing-docstring,reimported,unused-import,unused-variable
import click
import pytest

from gengive import cli


def test_main_legacy_ok(capsys):
    assert cli.main(['render', '.', 'examples/bar', 'default', '.']) == 0
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
        '- Written 39 lines from 1 parts to ',
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
        cli.render(manuscript='examples/bar', target='default', publisher_root='.', render_root='.', verify=True)
    out, err = capsys.readouterr()
    base64css = (
        'aHRtbCB7Zm9udC1mYW1pbHk6ICJJVEMgRnJhbmtsaW4gR290aGljIFN0ZCBCayBDZCIsIFZlcmRhbmEsIEFyaWFsLCBzYW5zLXNlcml'
        'mO30KYSB7Y29sb3I6ICMwYzJkODI7fQpiIHtmb250LXdlaWdodDogNjAwO30KaDEge2ZvbnQtd2VpZ2h0OiAzMDA7IHRleHQtdHJhbn'
        'Nmb3JtOiBjYXBpdGFsaXplO30KaDIge2ZvbnQtd2VpZ2h0OiAyMDA7fQpsaSB7bGluZS1oZWlnaHQ6IDEuNTt9CnRhYmxlIHt0YWJsZ'
        'S1sYXlvdXQ6IGZpeGVkOyB3aWR0aDogOTAlOyBiYWNrZ3JvdW5kLWNvbG9yOiAjZmZmZmZmOyBtYXJnaW46IDIwcHg7CmJvcmRlci1j'
        'b2xsYXBzZTogY29sbGFwc2U7fQp0ZCwgdGgge3dvcmQtd3JhcDogYnJlYWstd29yZDsgYm9yZGVyOiBzb2xpZCAxcHggIzY2NjY2Njt'
        '9CnRoIHtiYWNrZ3JvdW5kLWNvbG9yOiAjMGMyZDgyOyBjb2xvcjogI2ZmZmZmZjsgZm9udC1zaXplOiA3NSU7IGZvbnQtd2VpZ2h0Oi'
        'AzMDA7fQp0ZCB7dmVydGljYWwtYWxpZ246IHRvcDsgZm9udC1zaXplOiA2NyU7IHBhZGRpbmc6IDJweDt9CnRhYmxlIGNhcHRpb24ge'
        '2ZvbnQtc2l6ZTogMTIwJTsgbWFyZ2luLWJvdHRvbTogMjBweDt9CnRib2R5IHRyOm50aC1jaGlsZChvZGQpIHtiYWNrZ3JvdW5kLWNv'
        'bG9yOiAjZGRkZGRkO30KdGJvZHkgdHI6bnRoLWNoaWxkKGV2ZW4pIHtiYWNrZ3JvdW5kLWNvbG9yOiAjZmZmZmZmO30K'
    )
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
        '    "."',
        '    "examples/bar",',
        '    "default"',
        '    "."',
        '  ],',
        '  "processing_start": "',
        '  "manuscript": "bar",',
        '  "variant": "default",',
        '  "manuscript_path": "examples/bar",',
        '  "config_path": "examples/bar/render-config.json",',
        '  "config_hash_sha256": "517504611aa99a0eae8b34721765904ac068119afa36ad60fe1e45a0956b7006",',
        '  "config_data_version": "',
        '  "config_size_bytes": 92,',
        '  "render_config": {',
        '    "name": "the-name-of-the-thing"',
        '    "css": "styles/default.css"',
        f'    "css_declarations": "{base64css}"',
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
