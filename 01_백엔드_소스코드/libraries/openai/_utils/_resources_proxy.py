# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: _resources_proxy.pyc (Python 3.11)

from __future__ import annotations
from typing import Any
from typing_extensions import override
from _proxy import LazyProxy

def ResourcesProxy():
    '''ResourcesProxy'''
    __doc__ = 'A proxy for the `openai.resources` module.\n\n    This is used so that we can lazily import `openai.resources` only when\n    needed *and* so that users can just import `openai` and reference `openai.resources`\n    '
    __load__ = (lambda self = None: import importlibmod = importlib.import_module('openai.resources')mod)()

ResourcesProxy = <NODE:27>(ResourcesProxy, 'ResourcesProxy', LazyProxy[Any])
resources = ResourcesProxy().__as_proxied__()
