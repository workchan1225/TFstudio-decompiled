# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: multipart.pyc (Python 3.11)

from __future__ import annotations
import re
import typing as t
from dataclasses import dataclass
from enum import auto
from enum import Enum
from datastructures import Headers
from exceptions import RequestEntityTooLarge
from http import parse_options_header

class Event:
    pass

Preamble = <NODE:12>()
Field = <NODE:12>()
File = <NODE:12>()
Data = <NODE:12>()
Epilogue = <NODE:12>()

class NeedData(Event):
    pass

NEED_DATA = NeedData()

class State(Enum):
    PREAMBLE = auto()
    PART = auto()
    DATA = auto()
    DATA_START = auto()
    EPILOGUE = auto()
    COMPLETE = auto()

LINE_BREAK = b'(?:\r\n|\n|\r)'
BLANK_LINE_RE = re.compile(b'(?:\r\n\r\n|\r\r|\n\n)', re.MULTILINE)
LINE_BREAK_RE = re.compile(LINE_BREAK, re.MULTILINE)
HEADER_CONTINUATION_RE = re.compile(b'%s[ \t]' % LINE_BREAK, re.MULTILINE)
SEARCH_EXTRA_LENGTH = 8

class MultipartDecoder:
    '''Decodes a multipart message as bytes into Python events.

    The part data is returned as available to allow the caller to save
    the data from memory to disk, if desired.

    .. versionchanged:: 3.1.4
        Handle chunks that split a``\r
`` sequence.
    '''
    
    def __init__(self = None, boundary = None, max_form_memory_size = None, *, max_parts):
        self.buffer = bytearray()
        self.complete = False
        self.max_form_memory_size = max_form_memory_size
        self.max_parts = max_parts
        self.state = State.PREAMBLE
        self.boundary = boundary
        self.preamble_re = re.compile(b'%s?--%s(--[^\\S\\n\\r]*%s?|[^\\S\\n\\r]*%s)' % (LINE_BREAK, re.escape(boundary), LINE_BREAK, LINE_BREAK), re.MULTILINE)
        self.boundary_re = re.compile(b'%s--%s(--[^\\S\\n\\r]*%s?|[^\\S\\n\\r]*%s)' % (LINE_BREAK, re.escape(boundary), LINE_BREAK, LINE_BREAK), re.MULTILINE)
        self._search_position = 0
        self._parts_decoded = 0

    
    def last_newline(self = None, data = None):
        
        try:
            last_nl = data.rindex(b'\n')
        except ValueError:
            last_nl = len(data)

        
        try:
            last_cr = data.rindex(b'\r')
        except ValueError:
            last_cr = len(data)

        return min(last_nl, last_cr)

    
    def receive_data(self = None, data = None):
        pass
    # WARNING: Decompyle incomplete

    
    def next_event(self = None):
        event = NEED_DATA
    # WARNING: Decompyle incomplete

    
    def _parse_headers(self = None, data = None):
        headers = []
        data = HEADER_CONTINUATION_RE.sub(b' ', data)
        for line in data.splitlines():
            line = line.strip()
            if line != b'':
                (name, _, value) = line.decode().partition(':')
                headers.append((name.strip(), value.strip()))
            return Headers(headers)

    
    def _parse_data(self = None, data = None, *, start):
        if start:
            match = LINE_BREAK_RE.match(data)
            data_start = t.cast(t.Match[bytes], match).end()
        else:
            data_start = 0
        boundary = b'--' + self.boundary
        if self.buffer.find(boundary) == -1:
            data_end = self.last_newline(data[data_start:]) + data_start
            del_index = self.last_newline(data[data_start:]) + data_start
            if len(data) - data_end > len(b'\n' + boundary):
                data_end = len(data)
                del_index = len(data)
            more_data = True
    # WARNING: Decompyle incomplete



class MultipartEncoder:
    
    def __init__(self = None, boundary = None):
        self.boundary = boundary
        self.state = State.PREAMBLE

    
    def send_event(self = None, event = None):
        if isinstance(event, Preamble) and self.state == State.PREAMBLE:
            self.state = State.PART
            return event.data
        if None(event, (Field, File)) and self.state in {
            State.PREAMBLE,
            State.PART,
            State.DATA}:
            data = b'\r\n--' + self.boundary + b'\r\n'
            data += b'Content-Disposition: form-data; name="%s"' % event.name.encode()
            if isinstance(event, File):
                data += b'; filename="%s"' % event.filename.encode()
            data += b'\r\n'
            for name, value in t.cast(Field, event).headers:
                if name.lower() != 'content-disposition':
                    data += f'''{name}: {value}\r\n'''.encode()
                self.state = State.DATA_START
                return data
                if isinstance(event, Data) and self.state == State.DATA_START:
                    self.state = State.DATA
                    if len(event.data) > 0:
                        return b'\r\n' + event.data
                    return None.data
                if None(event, Data) and self.state == State.DATA:
                    return event.data
                if None(event, Epilogue):
                    self.state = State.COMPLETE
                    return b'\r\n--' + self.boundary + b'--\r\n' + event.data
                raise None(f'''Cannot generate {event} in state: {self.state}''')
