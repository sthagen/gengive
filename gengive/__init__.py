"""Render text (Danish: gengive tekst)."""
import os
from typing import List

APP_NAME = 'Render text (Danish: gengive tekst).'
APP_ALIAS = 'gengive'
APP_ENV = 'GENGIVE'
DEBUG = bool(os.getenv(f'{APP_ENV}_DEBUG', ''))
VERBOSE = bool(os.getenv(f'{APP_ENV}_VERBOSE', ''))
QUIET = False
STRICT = bool(os.getenv(f'{APP_ENV}_STRICT', ''))
ENCODING = 'utf-8'
ENCODING_ERRORS_POLICY = 'ignore'
DEFAULT_CONFIG_NAME = '.gengive.json'
DEFAULT_LF_ONLY = 'YES'

# [[[fill git_describe()]]]
__version__ = '2022.11.28+parent.a11a1ad1'
# [[[end]]] (checksum: 5ab1f5b5be679090479cca5ee795b198)
__version_info__ = tuple(
    e if '-' not in e else e.split('-')[0] for part in __version__.split('+') for e in part.split('.') if e != 'parent'
)
__all__: List[str] = []
