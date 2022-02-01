# -*- coding: utf-8 -*-
# pylint: disable=line-too-long,missing-docstring,reimported,unused-import,unused-variable
import pathlib

import gengive.gengive as gg


def test_gg_main():
    inp = str(pathlib.Path('tests', 'fixtures', 'empty', 'advisory.json'))
    assert gg.main(['verify', inp, '']) == 1


def test_gg_verify_request_too_few():
    assert gg.verify_request(['1']) == (2, 'received wrong number of arguments', [''])


def test_gg_verify_request_unknown_command():
    assert gg.verify_request(['unknown', 'later', 'does not matter']) == (2, 'received unknown command', [''])


def test_gg_parse_request_falsy_input():
    argv = ['verify', '', '']
    error_code, message, root_path, command, manuscript, variant = gg.parse_request(gg.workspace_path(), argv)
    assert error_code == 1
    message_start = 'Document() is not available within publisher root '
    assert message.startswith(message_start)
    assert root_path == gg.workspace_path()
    assert command == ''
    assert manuscript == ''
    assert variant == ''


def test_reader_empty():
    inp = str(pathlib.Path('tests', '__init__.py'))
    assert next(gg.reader(inp)).strip() == '# -*- coding: utf-8 -*-'
