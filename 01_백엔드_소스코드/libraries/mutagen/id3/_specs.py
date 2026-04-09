# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: _specs.pyc (Python 3.11)

import struct
import codecs
from struct import unpack, pack
from _util import total_ordering, decode_terminated, enum, flags, cdata, encode_endian, intround, bchr
from _util import BitPaddedInt, is_valid_frame_id
PictureType = <NODE:12>()
CTOCFlags = <NODE:12>()

class SpecError(Exception):
    pass


class Spec(object):
    handle_nodata = False
    
    def __init__(self, name, default):
        self.name = name
        self.default = default

    
    def __hash__(self):
        raise TypeError('Spec objects are unhashable')

    
    def _validate23(self, frame, value, **kwargs):
        '''Return a possibly modified value which, if written,
        results in valid id3v2.3 data.
        '''
        return value

    
    def read(self, header, frame, data):
        '''
        Returns:
            (value: object, left_data: bytes)
        Raises:
            SpecError
        '''
        raise NotImplementedError

    
    def write(self, config, frame, value):
        '''
        Returns:
            bytes: The serialized data
        Raises:
            SpecError
        '''
        raise NotImplementedError

    
    def validate(self, frame, value):
        '''
        Returns:
            the validated value
        Raises:
            ValueError
            TypeError
        '''
        raise NotImplementedError



class ByteSpec(Spec):
    pass
# WARNING: Decompyle incomplete


class PictureTypeSpec(ByteSpec):
    pass
# WARNING: Decompyle incomplete


class CTOCFlagsSpec(ByteSpec):
    
    def read(self, header, frame, data):
        (value, data) = ByteSpec.read(self, header, frame, data)
        return (CTOCFlags(value), data)

    
    def validate(self, frame, value):
        value = ByteSpec.validate(self, frame, value)
    # WARNING: Decompyle incomplete



class IntegerSpec(Spec):
    
    def read(self, header, frame, data):
        return (int(BitPaddedInt(data, bits = 8)), b'')

    
    def write(self, config, frame, value):
        return BitPaddedInt.to_str(value, bits = 8, width = -1)

    
    def validate(self, frame, value):
        return value



class SizedIntegerSpec(Spec):
    
    def __init__(self, name, size, default):
        self.name, self._SizedIntegerSpec__sz = name, size
        self.default = default

    
    def read(self, header, frame, data):
        return (int(BitPaddedInt(data[:self._SizedIntegerSpec__sz], bits = 8)), data[self._SizedIntegerSpec__sz:])

    
    def write(self, config, frame, value):
        return BitPaddedInt.to_str(value, bits = 8, width = self._SizedIntegerSpec__sz)

    
    def validate(self, frame, value):
        return value


Encoding = <NODE:12>()

class EncodingSpec(ByteSpec):
    pass
# WARNING: Decompyle incomplete


class StringSpec(Spec):
    pass
# WARNING: Decompyle incomplete


class RVASpec(Spec):
    pass
# WARNING: Decompyle incomplete


class FrameIDSpec(StringSpec):
    pass
# WARNING: Decompyle incomplete


class BinaryDataSpec(Spec):
    pass
# WARNING: Decompyle incomplete


def iter_text_fixups(data, encoding):
    '''Yields a series of repaired text values for decoding'''
    pass
# WARNING: Decompyle incomplete


class EncodedTextSpec(Spec):
    pass
# WARNING: Decompyle incomplete


class MultiSpec(Spec):
    pass
# WARNING: Decompyle incomplete


class EncodedNumericTextSpec(EncodedTextSpec):
    pass


class EncodedNumericPartTextSpec(EncodedTextSpec):
    pass


class Latin1TextSpec(Spec):
    pass
# WARNING: Decompyle incomplete


class ID3FramesSpec(Spec):
    pass
# WARNING: Decompyle incomplete


class Latin1TextListSpec(Spec):
    pass
# WARNING: Decompyle incomplete

ID3TimeStamp = <NODE:12>()

class TimeStampSpec(EncodedTextSpec):
    pass
# WARNING: Decompyle incomplete


class ChannelSpec(ByteSpec):
    (OTHER, MASTER, FRONTRIGHT, FRONTLEFT, BACKRIGHT, BACKLEFT, FRONTCENTRE, BACKCENTRE, SUBWOOFER) = range(9)


class VolumeAdjustmentSpec(Spec):
    
    def read(self, header, frame, data):
        (value,) = unpack('>h', data[0:2])
        return (value / 512, data[2:])

    
    def write(self, config, frame, value):
        number = intround(value * 512)
        if not  <= -32768, number or -32768, number <= 32767:
            pass
        
        raise SpecError('not in range')
        return pack('>h', number)

    
    def validate(self, frame, value):
        pass
    # WARNING: Decompyle incomplete



class VolumePeakSpec(Spec):
    
    def read(self, header, frame, data):
        peak = 0
        data_array = bytearray(data)
        bits = data_array[0]
        vol_bytes = min(4, bits + 7 >> 3)
        if vol_bytes + 1 > len(data):
            raise SpecError('not enough frame data')
        shift = (8 - (bits & 7) & 7) + (4 - vol_bytes) * 8
        for i in range(1, vol_bytes + 1):
            peak *= 256
            peak += data_array[i]
            peak *= 2 ** shift
            return (float(peak) / 2147483647, data[1 + vol_bytes:])

    
    def write(self, config, frame, value):
        number = intround(value * 32768)
        if not  <= 0, number or 0, number <= 65535:
            pass
        
        raise SpecError('not in range')
        return b'\x10' + pack('>H', number)

    
    def validate(self, frame, value):
        pass
    # WARNING: Decompyle incomplete



class SynchronizedTextSpec(EncodedTextSpec):
    
    def read(self, header, frame, data):
        texts = []
        (encoding, term) = self._encodings[frame.encoding]
    # WARNING: Decompyle incomplete

    
    def write(self, config, frame, value):
        data = []
        (encoding, term) = self._encodings[frame.encoding]
        for text, time in value:
            text = encode_endian(text, encoding, le = True) + term
        except UnicodeEncodeError:
            e = None
            raise SpecError(e)
            e = None
            del e
        data.append(text + struct.pack('>I', time))
        continue
        return b''.join(data)

    
    def validate(self, frame, value):
        return value



class KeyEventSpec(Spec):
    
    def read(self, header, frame, data):
        events = []
    # WARNING: Decompyle incomplete

    
    def write(self, config, frame, value):
        return (lambda .0: pass# WARNING: Decompyle incomplete
)(value())

    
    def validate(self, frame, value):
        return list(value)



class VolumeAdjustmentsSpec(Spec):
    
    def read(self, header, frame, data):
        adjustments = { }
    # WARNING: Decompyle incomplete

    
    def write(self, config, frame, value):
        value.sort()
        return (lambda .0: pass# WARNING: Decompyle incomplete
)(value())

    
    def validate(self, frame, value):
        return list(value)



class ASPIIndexSpec(Spec):
    
    def read(self, header, frame, data):
        if frame.b == 16:
            format = 'H'
            size = 2
        elif frame.b == 8:
            format = 'B'
            size = 1
        else:
            raise SpecError('invalid bit count in ASPI (%d)' % frame.b)
        indexes = data[:frame.N * size]
        data = data[frame.N * size:]
        
        try:
            return (list(struct.unpack('>' + format * frame.N, indexes)), data)
        except struct.error:
            e = None
            raise SpecError(e)
            e = None
            del e


    
    def write(self, config, frame, values):
        if frame.b == 16:
            format = 'H'
        elif frame.b == 8:
            format = 'B'
        else:
            raise SpecError('frame.b must be 8 or 16')
    # WARNING: Decompyle incomplete

    
    def validate(self, frame, values):
        return list(values)
