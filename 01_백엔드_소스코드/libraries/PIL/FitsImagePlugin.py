# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: FitsImagePlugin.pyc (Python 3.11)

from __future__ import annotations
import gzip
import math
from  import Image, ImageFile

def _accept(prefix = None):
    return prefix.startswith(b'SIMPLE')


class FitsImageFile(ImageFile.ImageFile):
    format = 'FITS'
    format_description = 'FITS'
    
    def _open(self = None):
        pass
    # WARNING: Decompyle incomplete

    
    def _get_size(self = None, headers = None, prefix = None):
        naxis = int(headers[prefix + b'NAXIS'])
        if naxis == 0:
            return None
        if None == 1:
            return (1, int(headers[prefix + b'NAXIS1']))
        return (None(headers[prefix + b'NAXIS1']), int(headers[prefix + b'NAXIS2']))

    
    def _parse_headers(self = None, headers = None):
        prefix = b''
        decoder_name = 'raw'
        offset = 0
        if headers.get(b'XTENSION') == b"'BINTABLE'" and headers.get(b'ZIMAGE') == b'T' and headers[b'ZCMPTYPE'] == b"'GZIP_1  '":
            if not self._get_size(headers, prefix):
                no_prefix_size = (0, 0)
                number_of_bits = int(headers[b'BITPIX'])
                offset = no_prefix_size[0] * no_prefix_size[1] * (number_of_bits // 8)
                prefix = b'Z'
                decoder_name = 'fits_gzip'
                size = self._get_size(headers, prefix)
                if not size:
                    return ('', 0, ())
                self._size = None
                number_of_bits = int(headers[prefix + b'BITPIX'])
                if number_of_bits == 8:
                    self._mode = 'L'
                elif number_of_bits == 16:
                    self._mode = 'I;16'
                elif number_of_bits == 32:
                    self._mode = 'I'
                elif number_of_bits in (-32, -64):
                    self._mode = 'F'
        if decoder_name == 'raw':
            args = (self.mode, 0, -1)
        else:
            args = (number_of_bits,)
        return (decoder_name, offset, args)



class FitsGzipDecoder(ImageFile.PyDecoder):
    _pulls_fd = True
    
    def decode(self = None, buffer = None):
        pass
    # WARNING: Decompyle incomplete


Image.register_open(FitsImageFile.format, FitsImageFile, _accept)
Image.register_decoder('fits_gzip', FitsGzipDecoder)
Image.register_extensions(FitsImageFile.format, [
    '.fit',
    '.fits'])
