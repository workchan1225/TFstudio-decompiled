# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: reader.pyc (Python 3.11)

__all__ = [
    'Reader',
    'ReaderError']
from error import YAMLError, Mark
import codecs
import re

class ReaderError(YAMLError):
    
    def __init__(self, name, position, character, encoding, reason):
        self.name = name
        self.character = character
        self.position = position
        self.encoding = encoding
        self.reason = reason

    
    def __str__(self):
        if isinstance(self.character, bytes):
            return '\'%s\' codec can\'t decode byte #x%02x: %s\n  in "%s", position %d' % (self.encoding, ord(self.character), self.reason, self.name, self.position)
        return None % (self.character, self.reason, self.name, self.position)



class Reader(object):
    
    def __init__(self, stream):
        self.name = None
        self.stream = None
        self.stream_pointer = 0
        self.eof = True
        self.buffer = ''
        self.pointer = 0
        self.raw_buffer = None
        self.raw_decode = None
        self.encoding = None
        self.index = 0
        self.line = 0
        self.column = 0
        if isinstance(stream, str):
            self.name = '<unicode string>'
            self.check_printable(stream)
            self.buffer = stream + '\x00'
            return None
        if None(stream, bytes):
            self.name = '<byte string>'
            self.raw_buffer = stream
            self.determine_encoding()
            return None
        self.stream = None
        self.name = getattr(stream, 'name', '<file>')
        self.eof = False
        self.raw_buffer = None
        self.determine_encoding()

    
    def peek(self, index = (0,)):
        
        try:
            return self.buffer[self.pointer + index]
        except IndexError:
            self.update(index + 1)
            return 


    
    def prefix(self, length = (1,)):
        if self.pointer + length >= len(self.buffer):
            self.update(length)
        return self.buffer[self.pointer:self.pointer + length]

    
    def forward(self, length = (1,)):
        if self.pointer + length + 1 >= len(self.buffer):
            self.update(length + 1)
    # WARNING: Decompyle incomplete

    
    def get_mark(self):
        pass
    # WARNING: Decompyle incomplete

    
    def determine_encoding(self):
        pass
    # WARNING: Decompyle incomplete

    NON_PRINTABLE = re.compile('[^\t\n\r -~ -퟿-�𐀀-􏿿]')
    
    def check_printable(self, data):
        match = self.NON_PRINTABLE.search(data)
        if match:
            character = match.group()
            position = self.index + (len(self.buffer) - self.pointer) + match.start()
            raise ReaderError(self.name, position, ord(character), 'unicode', 'special characters are not allowed')

    
    def update(self, length):
        pass
    # WARNING: Decompyle incomplete

    
    def update_raw(self, size = (4096,)):
        data = self.stream.read(size)
    # WARNING: Decompyle incomplete
