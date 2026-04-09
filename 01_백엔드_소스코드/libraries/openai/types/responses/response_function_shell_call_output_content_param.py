# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: response_function_shell_call_output_content_param.pyc (Python 3.11)

from __future__ import annotations
from typing import Union
from typing_extensions import Literal, Required, TypeAlias, TypedDict
__all__ = [
    'ResponseFunctionShellCallOutputContentParam',
    'Outcome',
    'OutcomeTimeout',
    'OutcomeExit']

def OutcomeTimeout():
    '''OutcomeTimeout'''
    type: "Required[Literal['timeout']]" = 'Indicates that the shell call exceeded its configured time limit.'

OutcomeTimeout = <NODE:27>(OutcomeTimeout, 'OutcomeTimeout', TypedDict, total = False)

def OutcomeExit():
    '''OutcomeExit'''
    type: "Required[Literal['exit']]" = 'Indicates that the shell commands finished and returned an exit code.'

OutcomeExit = <NODE:27>(OutcomeExit, 'OutcomeExit', TypedDict, total = False)
Outcome: 'TypeAlias' = Union[(OutcomeTimeout, OutcomeExit)]

def ResponseFunctionShellCallOutputContentParam():
    '''ResponseFunctionShellCallOutputContentParam'''
    stdout: 'Required[str]' = 'Captured stdout and stderr for a portion of a shell tool call output.'

ResponseFunctionShellCallOutputContentParam = <NODE:27>(ResponseFunctionShellCallOutputContentParam, 'ResponseFunctionShellCallOutputContentParam', TypedDict, total = False)
