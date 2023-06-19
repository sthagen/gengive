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
__version__ = '2023.6.19+parent.365b32fd'
# [[[end]]] (checksum: 9dc45f1fac14aaef6add1a675c4d9f13)
__version_info__ = tuple(
    e if '-' not in e else e.split('-')[0] for part in __version__.split('+') for e in part.split('.') if e != 'parent'
)
__all__: List[str] = []
