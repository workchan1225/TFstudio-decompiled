# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: realtime_truncation.pyc (Python 3.11)

from typing import Union
from typing_extensions import Literal, TypeAlias
from realtime_truncation_retention_ratio import RealtimeTruncationRetentionRatio
__all__ = [
    'RealtimeTruncation']
RealtimeTruncation: TypeAlias = Union[(Literal[('auto', 'disabled')], RealtimeTruncationRetentionRatio)]
