# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: _path.pyc (Python 3.11)

'''Utilities for working with paths.'''
from collections.abc import Sequence
from contextlib import suppress

def normalize_path_segments(segments = None):
    """Drop '.' and '..' from a sequence of str segments"""
    resolved_path = []
    for seg in segments:
        if seg == '..':
            suppress(IndexError)
            resolved_path.pop()
            None(None, None)
        else:
            with None:
                if not None:
                    pass
        if seg != '.':
            resolved_path.append(seg)
        if segments and segments[-1] in ('.', '..'):
            resolved_path.append('')
    return resolved_path


def normalize_path(path = None):
    prefix = ''
    if path and path[0] == '/':
        prefix = '/'
        path = path[1:]
    segments = path.split('/')
    return prefix + '/'.join(normalize_path_segments(segments))
