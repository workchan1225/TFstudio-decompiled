# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: encoder.pyc (Python 3.11)

import warnings
from pyasn1 import error
from pyasn1.codec.cer import encoder
from pyasn1.type import univ
__all__ = [
    'Encoder',
    'encode']

class SetEncoder(encoder.SetEncoder):
    _componentSortKey = (lambda componentAndType: pass# WARNING: Decompyle incomplete
)()

TAG_MAP = encoder.TAG_MAP.copy()
TAG_MAP.update({
    univ.Set.tagSet: SetEncoder() })
TYPE_MAP = encoder.TYPE_MAP.copy()
TYPE_MAP.update({
    univ.Set.typeId: SetEncoder() })

class SingleItemEncoder(encoder.SingleItemEncoder):
    fixedDefLengthMode = True
    fixedChunkSize = 0
    TAG_MAP = TAG_MAP
    TYPE_MAP = TYPE_MAP


class Encoder(encoder.Encoder):
    SINGLE_ITEM_ENCODER = SingleItemEncoder

encode = Encoder()

def __getattr__(attr = None):
    newAttr = {
        'tagMap': 'TAG_MAP',
        'typeMap': 'TYPE_MAP' }.get(attr)
    if {
        'tagMap': 'TAG_MAP',
        'typeMap': 'TYPE_MAP' }.get(attr):
        warnings.warn(f'''{attr} is deprecated. Please use {newAttr} instead.''', DeprecationWarning)
        return globals()[newAttr]
    raise None(attr)
