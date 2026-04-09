# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: disposition.pyc (Python 3.11)

'''Simple value objects for tracking what to do with files.'''
from __future__ import annotations
from typing import TYPE_CHECKING
from coverage.types import TFileDisposition
if TYPE_CHECKING:
    from coverage.plugin import FileTracer

class FileDisposition:
    has_dynamic_filename: 'bool' = 'A simple value type for recording what to do with a file.'
    
    def __repr__(self = None):
        return f'''<FileDisposition {self.canonical_filename!r}: trace={self.trace}>'''



def disposition_init(cls = None, original_filename = None):
    '''Construct and initialize a new FileDisposition object.'''
    disp = cls()
    disp.original_filename = original_filename
    disp.canonical_filename = original_filename
    disp.source_filename = None
    disp.trace = False
    disp.reason = ''
    disp.file_tracer = None
    disp.has_dynamic_filename = False
    return disp


def disposition_debug_msg(disp = None):
    '''Make a nice debug message of what the FileDisposition is doing.'''
    if disp.trace:
        msg = f'''Tracing {disp.original_filename!r}'''
        if disp.original_filename != disp.source_filename:
            msg += f''' as {disp.source_filename!r}'''
        if disp.file_tracer:
            msg += f''': will be traced by {disp.file_tracer!r}'''
        else:
            msg = f'''Not tracing {disp.original_filename!r}: {disp.reason}'''
    return msg
