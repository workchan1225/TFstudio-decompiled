# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: _orm_types.pyc (Python 3.11)

'''ORM types that need to present specifically for **documentation only** of
the Executable.execution_options() method, which includes options that
are meaningful to the ORM.

'''
from __future__ import annotations
from util.typing import Literal
SynchronizeSessionArgument = Literal[(False, 'auto', 'evaluate', 'fetch')]
DMLStrategyArgument = Literal[('bulk', 'raw', 'orm', 'auto')]
