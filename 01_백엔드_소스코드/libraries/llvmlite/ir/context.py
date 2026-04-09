# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: context.pyc (Python 3.11)

from llvmlite.ir import _utils
from llvmlite.ir import types

class Context(object):
    
    def __init__(self):
        self.scope = _utils.NameScope()
        self.identified_types = { }

    
    def get_identified_type(self, name, packed = (False,)):
        if name not in self.identified_types:
            self.scope.register(name)
            ty = types.IdentifiedStructType(self, name, packed)
            self.identified_types[name] = ty
        else:
            ty = self.identified_types[name]
        return ty


global_context = Context()
