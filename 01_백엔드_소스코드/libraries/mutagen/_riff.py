# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: _riff.pyc (Python 3.11)

'''Resource Interchange File Format (RIFF).'''
import struct
from struct import pack
from mutagen._iff import IffChunk, IffContainerChunkMixin, IffFile, InvalidChunk

class RiffChunk(IffChunk):
    '''Generic RIFF chunk'''
    parse_header = (lambda cls, header: struct.unpack('<4sI', header))()
    get_class = (lambda cls, id: if id in ('LIST', 'RIFF'):
RiffListChunk)()
    
    def write_new_header(self, id_, size):
        self._fileobj.write(pack('<4sI', id_, size))

    
    def write_size(self):
        self._fileobj.write(pack('<I', self.data_size))



class RiffListChunk(IffContainerChunkMixin, RiffChunk):
    """A RIFF chunk containing other chunks.
    This is either a 'LIST' or 'RIFF'
    """
    
    def parse_next_subchunk(self):
        return RiffChunk.parse(self._fileobj, self)

    
    def __init__(self, fileobj, id, data_size, parent_chunk):
        if id not in ('RIFF', 'LIST'):
            raise InvalidChunk('Expected RIFF or LIST chunk, got %s' % id)
        RiffChunk.__init__(self, fileobj, id, data_size, parent_chunk)
        self.init_container()



class RiffFile(IffFile):
    pass
# WARNING: Decompyle incomplete
