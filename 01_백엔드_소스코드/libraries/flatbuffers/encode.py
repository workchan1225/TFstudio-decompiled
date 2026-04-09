# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: encode.pyc (Python 3.11)

from  import number_types as N
from  import packer
from compat import memoryview_type
from compat import NumpyRequiredForThisFeature, import_numpy
np = import_numpy()
FILE_IDENTIFIER_LENGTH = 4

def Get(packer_type, buf, head):
    '''Get decodes a value at buf[head] using `packer_type`.'''
    return packer_type.unpack_from(memoryview_type(buf), head)[0]


def GetVectorAsNumpy(numpy_type, buf, count, offset):
    '''GetVecAsNumpy decodes values starting at buf[head] as

  `numpy_type`, where `numpy_type` is a numpy dtype.
  '''
    pass
# WARNING: Decompyle incomplete


def Write(packer_type, buf, head, n):
    '''Write encodes `n` at buf[head] using `packer_type`.'''
    packer_type.pack_into(buf, head, n)
