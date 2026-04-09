# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: typing.pyc (Python 3.11)

from __future__ import annotations
import http
import logging
from typing import TYPE_CHECKING, Any, NewType, Optional, Sequence, Union
__all__ = [
    'Data',
    'LoggerLike',
    'StatusLike',
    'Origin',
    'Subprotocol',
    'ExtensionName',
    'ExtensionParameter']
Data = Union[(str, bytes)]
if TYPE_CHECKING:
    LoggerLike = Union[(logging.Logger, logging.LoggerAdapter[Any])]
else:
    LoggerLike = Union[(logging.Logger, logging.LoggerAdapter)]
StatusLike = Union[(http.HTTPStatus, int)]
Origin = NewType('Origin', str)
Subprotocol = NewType('Subprotocol', str)
ExtensionName = NewType('ExtensionName', str)
ExtensionParameter = tuple[(str, Optional[str])]
ExtensionHeader = tuple[(ExtensionName, Sequence[ExtensionParameter])]
ConnectionOption = NewType('ConnectionOption', str)
UpgradeProtocol = NewType('UpgradeProtocol', str)
