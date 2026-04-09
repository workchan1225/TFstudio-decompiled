# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: extension_types.pyc (Python 3.11)

from __future__ import annotations
import json
from typing import TYPE_CHECKING
import pyarrow
from pandas.compat import pa_version_under14p1
from pandas.core.dtypes.dtypes import IntervalDtype, PeriodDtype
from pandas.core.arrays.interval import VALID_CLOSED
if TYPE_CHECKING:
    from pandas._typing import IntervalClosedType

class ArrowPeriodType(pyarrow.ExtensionType):
    
    def __init__(self = None, freq = None):
        self._freq = freq
        pyarrow.ExtensionType.__init__(self, pyarrow.int64(), 'pandas.period')

    freq = (lambda self: self._freq)()
    
    def __arrow_ext_serialize__(self = None):
        metadata = {
            'freq': self.freq }
        return json.dumps(metadata).encode()

    __arrow_ext_deserialize__ = (lambda cls = None, storage_type = None, serialized = classmethod: metadata = json.loads(serialized.decode())ArrowPeriodType(metadata['freq']))()
    
    def __eq__(self, other):
