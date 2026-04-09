# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: _beta_builtin_memory_tool.pyc (Python 3.11)

from __future__ import annotations
from abc import abstractmethod
from typing import TYPE_CHECKING, Any, cast
from typing_extensions import override, assert_never
from _models import construct_type_unchecked
from types.beta import BetaMemoryTool20250818Param, BetaMemoryTool20250818Command, BetaCacheControlEphemeralParam, BetaMemoryTool20250818ViewCommand, BetaMemoryTool20250818CreateCommand, BetaMemoryTool20250818DeleteCommand, BetaMemoryTool20250818InsertCommand, BetaMemoryTool20250818RenameCommand, BetaMemoryTool20250818StrReplaceCommand
from _beta_functions import BetaBuiltinFunctionTool, BetaFunctionToolResultType, BetaAsyncBuiltinFunctionTool

class BetaAbstractMemoryTool(BetaBuiltinFunctionTool):
    pass
# WARNING: Decompyle incomplete


class BetaAsyncAbstractMemoryTool(BetaAsyncBuiltinFunctionTool):
    pass
# WARNING: Decompyle incomplete
