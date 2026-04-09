# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: utils.pyc (Python 3.11)

from __future__ import annotations
import importlib
import logging
import unicodedata
from codecs import IncrementalDecoder
from encodings.aliases import aliases
from functools import lru_cache
from re import findall
from typing import Generator
from _multibytecodec import MultibyteIncrementalDecoder
from constant import ENCODING_MARKS, IANA_SUPPORTED_SIMILAR, RE_POSSIBLE_ENCODING_INDICATION, UNICODE_RANGES_COMBINED, UNICODE_SECONDARY_RANGE_KEYWORD, UTF8_MAXIMAL_ALLOCATION, COMMON_CJK_CHARACTERS
is_accentuated = (lambda character = None:
