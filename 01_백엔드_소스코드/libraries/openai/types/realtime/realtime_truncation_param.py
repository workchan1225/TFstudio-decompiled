# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: realtime_truncation_param.pyc (Python 3.11)

from __future__ import annotations
from typing import Union
from typing_extensions import Literal, TypeAlias
from realtime_truncation_retention_ratio_param import RealtimeTruncationRetentionRatioParam
__all__ = [
    'RealtimeTruncationParam']
RealtimeTruncationParam: 'TypeAlias' = Union[(Literal[('auto', 'disabled')], RealtimeTruncationRetentionRatioParam)]
