# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: _frames.pyc (Python 3.11)

import zlib
from struct import unpack
from typing import Sequence
from _util import ID3JunkFrameError, ID3EncryptionUnsupportedError, unsynch, ID3SaveConfig, error
from _specs import BinaryDataSpec, StringSpec, Latin1TextSpec, EncodedTextSpec, ByteSpec, EncodingSpec, ASPIIndexSpec, SizedIntegerSpec, IntegerSpec, Encoding, VolumeAdjustmentsSpec, VolumePeakSpec, VolumeAdjustmentSpec, ChannelSpec, MultiSpec, SynchronizedTextSpec, KeyEventSpec, TimeStampSpec, EncodedNumericPartTextSpec, EncodedNumericTextSpec, SpecError, PictureTypeSpec, ID3FramesSpec, Latin1TextListSpec, CTOCFlagsSpec, FrameIDSpec, RVASpec, Spec

def _bytes2key(b):
    pass
# WARNING: Decompyle incomplete


class Frame(object):
    pass
# WARNING: Decompyle incomplete


class CHAP(Frame):
    '''Chapter'''
    _framespec = [
        Latin1TextSpec('element_id'),
        SizedIntegerSpec('start_time', 4, default = 0),
        SizedIntegerSpec('end_time', 4, default = 0),
        SizedIntegerSpec('start_offset', 4, default = 0xFFFFFFFF),
        SizedIntegerSpec('end_offset', 4, default = 0xFFFFFFFF),
        ID3FramesSpec('sub_frames')]
    HashKey = (lambda self: f'''{self.FrameID!s}:{self.element_id!s}''')()
    
    def __eq__(self, other):
