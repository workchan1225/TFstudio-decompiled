# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: eoo.pyc (Python 3.11)

from pyasn1.type import base
from pyasn1.type import tag
__all__ = [
    'endOfOctets']

class EndOfOctets(base.SimpleAsn1Type):
    defaultValue = 0
    tagSet = tag.initTagSet(tag.Tag(tag.tagClassUniversal, tag.tagFormatSimple, 0))
    _instance = None
    
    def __new__(cls, *args, **kwargs):
        pass
    # WARNING: Decompyle incomplete


endOfOctets = EndOfOctets()
