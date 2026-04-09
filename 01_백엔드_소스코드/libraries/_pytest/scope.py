# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: scope.pyc (Python 3.11)

"""
Scope definition and related utilities.

Those are defined here, instead of in the 'fixtures' module because
their use is spread across many other pytest modules, and centralizing it in 'fixtures'
would cause circular references.

Also this makes the module light to import, as it should.
"""
from __future__ import annotations
from enum import Enum
from functools import total_ordering
from typing import Literal
_ScopeName = Literal[('session', 'package', 'module', 'class', 'function')]
Scope = <NODE:12>()
_ALL_SCOPES = list(Scope)
_SCOPE_INDICES = enumerate(_ALL_SCOPES)()
HIGH_SCOPES = Scope()
