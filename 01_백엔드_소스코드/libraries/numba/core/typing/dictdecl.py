# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: dictdecl.pyc (Python 3.11)

'''
This implements the typing template for `dict()`.
'''
from  import types, errors
from templates import AbstractTemplate, Registry, signature
registry = Registry()
infer = registry.register
infer_global = registry.register_global
infer_getattr = registry.register_attr
_message_dict_support = '\nUnsupported use of `dict()` with positional or keyword argument(s). The only supported uses are `dict()` or `dict(iterable)`.\n'.strip()
DictBuiltin = <NODE:12>()
