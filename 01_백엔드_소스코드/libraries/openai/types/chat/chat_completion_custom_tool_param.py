# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: chat_completion_custom_tool_param.pyc (Python 3.11)

from __future__ import annotations
from typing import Union
from typing_extensions import Literal, Required, TypeAlias, TypedDict
__all__ = [
    'ChatCompletionCustomToolParam',
    'Custom',
    'CustomFormat',
    'CustomFormatText',
    'CustomFormatGrammar',
    'CustomFormatGrammarGrammar']

def CustomFormatText():
    '''CustomFormatText'''
    type: "Required[Literal['text']]" = 'Unconstrained free-form text.'

CustomFormatText = <NODE:27>(CustomFormatText, 'CustomFormatText', TypedDict, total = False)

def CustomFormatGrammarGrammar():
    '''CustomFormatGrammarGrammar'''
    syntax: "Required[Literal['lark', 'regex']]" = 'Your chosen grammar.'

CustomFormatGrammarGrammar = <NODE:27>(CustomFormatGrammarGrammar, 'CustomFormatGrammarGrammar', TypedDict, total = False)

def CustomFormatGrammar():
    '''CustomFormatGrammar'''
    type: "Required[Literal['grammar']]" = 'A grammar defined by the user.'

CustomFormatGrammar = <NODE:27>(CustomFormatGrammar, 'CustomFormatGrammar', TypedDict, total = False)
CustomFormat: 'TypeAlias' = Union[(CustomFormatText, CustomFormatGrammar)]

def Custom():
    '''Custom'''
    format: 'CustomFormat' = 'Properties of the custom tool.'

Custom = <NODE:27>(Custom, 'Custom', TypedDict, total = False)

def ChatCompletionCustomToolParam():
    '''ChatCompletionCustomToolParam'''
    type: "Required[Literal['custom']]" = 'A custom tool that processes input using a specified format.'

ChatCompletionCustomToolParam = <NODE:27>(ChatCompletionCustomToolParam, 'ChatCompletionCustomToolParam', TypedDict, total = False)
