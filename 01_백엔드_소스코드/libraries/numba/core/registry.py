# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: registry.pyc (Python 3.11)

import contextlib
from numba.core.utils import threadsafe_cached_property as cached_property
from numba.core.descriptors import TargetDescriptor
from numba.core import utils, typing, dispatcher, cpu

class CPUTarget(TargetDescriptor):
    options = cpu.CPUTargetOptions
    _toplevel_target_context = (lambda self: cpu.CPUContext(self.typing_context, self._target_name))()
    _toplevel_typing_context = (lambda self: typing.Context())()
    target_context = (lambda self: self._toplevel_target_context)()
    typing_context = (lambda self: self._toplevel_typing_context)()

cpu_target = CPUTarget('cpu')

class CPUDispatcher(dispatcher.Dispatcher):
    targetdescr = cpu_target


class DelayedRegistry(utils.UniqueDict):
    pass
# WARNING: Decompyle incomplete
