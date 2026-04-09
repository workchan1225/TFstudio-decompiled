# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: AvifImagePlugin.pyc (Python 3.11)

from __future__ import annotations
import os
from io import BytesIO
from typing import IO
from  import ExifTags, Image, ImageFile

try:
    from  import _avif
    SUPPORTED = True
except ImportError:
    SUPPORTED = False

DECODE_CODEC_CHOICE = 'auto'
DEFAULT_MAX_THREADS = 0

def get_codec_version(codec_name = None):
    versions = _avif.codec_versions()
    for version in versions.split(', '):
        if version.split(' [')[0] == codec_name:
            
            return None, version.split(':')[-1].split(' ')[0]
        return None


def _accept(prefix = None):
    if prefix[4:8] != b'ftyp':
        return False
    major_brand = None[8:12]
    if major_brand in (b'avif', b'avis', b'mif1', b'msf1'):
        if not SUPPORTED:
            return 'image file could not be identified because AVIF support not installed'
        return None


def _get_default_max_threads():
