# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: util.pyc (Python 3.11)

from  import encode
from  import number_types
from  import packer

def GetSizePrefix(buf, offset):
    '''Extract the size prefix from a buffer.'''
    return encode.Get(packer.int32, buf, offset)


def GetBufferIdentifier(buf, offset, size_prefixed = (False,)):
    '''Extract the file_identifier from a buffer'''
    if size_prefixed:
        offset += number_types.UOffsetTFlags.bytewidth
    offset += number_types.UOffsetTFlags.bytewidth
    end = offset + encode.FILE_IDENTIFIER_LENGTH
    return buf[offset:end]


def BufferHasIdentifier(buf, offset, file_identifier, size_prefixed = (False,)):
    got = GetBufferIdentifier(buf, offset, size_prefixed = size_prefixed)
    return got == file_identifier


def RemoveSizePrefix(buf, offset):
    '''Create a slice of a size-prefixed buffer that has

  its position advanced just past the size prefix.
  '''
    return (buf, offset + number_types.Int32Flags.bytewidth)
