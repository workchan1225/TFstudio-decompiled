# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: utf_8_sig.pyc (Python 3.11)

""" Python 'utf-8-sig' Codec
This work similar to UTF-8 with the following changes:

* On encoding/writing a UTF-8 encoded BOM will be prepended/written as the
  first three bytes.

* On decoding/reading if the first three bytes are a UTF-8 encoded BOM, these
  bytes will be skipped.
"""
import codecs

def encode(input, errors = ('strict',)):
    return (codecs.BOM_UTF8 + codecs.utf_8_encode(input, errors)[0], len(input))


def decode(input, errors = ('strict',)):
    prefix = 0
    if input[:3] == codecs.BOM_UTF8:
        input = input[3:]
        prefix = 3
    (output, consumed) = codecs.utf_8_decode(input, errors, True)
    return (output, consumed + prefix)


class IncrementalEncoder(codecs.IncrementalEncoder):
    
    def __init__(self, errors = ('strict',)):
        codecs.IncrementalEncoder.__init__(self, errors)
        self.first = 1

    
    def encode(self, input, final = (False,)):
        if self.first:
            self.first = 0
            return codecs.BOM_UTF8 + codecs.utf_8_encode(input, self.errors)[0]
        return None.utf_8_encode(input, self.errors)[0]

    
    def reset(self):
        codecs.IncrementalEncoder.reset(self)
        self.first = 1

    
    def getstate(self):
        return self.first

    
    def setstate(self, state):
        self.first = state



class IncrementalDecoder(codecs.BufferedIncrementalDecoder):
    
    def __init__(self, errors = ('strict',)):
        codecs.BufferedIncrementalDecoder.__init__(self, errors)
        self.first = 1

    
    def _buffer_decode(self, input, errors, final):
