# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: sounddevice_proxy.pyc (Python 3.11)

from __future__ import annotations
from typing import TYPE_CHECKING, Any
from typing_extensions import override
from _utils import LazyProxy
from _common import MissingDependencyError, format_instructions
if TYPE_CHECKING:
    import sounddevice
SOUNDDEVICE_INSTRUCTIONS = format_instructions(library = 'sounddevice', extra = 'voice_helpers')

def SounddeviceProxy():
    '''SounddeviceProxy'''
    __load__ = (lambda self = None: try:
import sounddeviceexcept ImportError:
err = Noneraise MissingDependencyError(SOUNDDEVICE_INSTRUCTIONS), errerr = Nonedel errsounddevice)()

SounddeviceProxy = <NODE:27>(SounddeviceProxy, 'SounddeviceProxy', LazyProxy[Any])
if not TYPE_CHECKING:
    sounddevice = SounddeviceProxy()
    return None
