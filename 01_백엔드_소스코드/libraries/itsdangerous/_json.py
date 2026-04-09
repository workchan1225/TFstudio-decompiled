# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: _json.pyc (Python 3.11)

from __future__ import annotations
import json as _json
import typing as t

class _CompactJSON:
    '''Wrapper around json module that strips whitespace.'''
    loads = (lambda payload = None: _json.loads(payload))()
    dumps = (lambda obj = None: kwargs.setdefault('ensure_ascii', False)kwargs.setdefault('separators', (',', ':'))# WARNING: Decompyle incomplete
)()
