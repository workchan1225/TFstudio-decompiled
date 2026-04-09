# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: chat_session_workflow_param.pyc (Python 3.11)

from __future__ import annotations
from typing import Dict, Union
from typing_extensions import Required, TypedDict
__all__ = [
    'ChatSessionWorkflowParam',
    'Tracing']

def Tracing():
    '''Tracing'''
    enabled: 'bool' = 'Optional tracing overrides for the workflow invocation.\n\n    When omitted, tracing is enabled by default.\n    '

Tracing = <NODE:27>(Tracing, 'Tracing', TypedDict, total = False)

def ChatSessionWorkflowParam():
    '''ChatSessionWorkflowParam'''
    version: 'str' = 'Workflow reference and overrides applied to the chat session.'

ChatSessionWorkflowParam = <NODE:27>(ChatSessionWorkflowParam, 'ChatSessionWorkflowParam', TypedDict, total = False)
