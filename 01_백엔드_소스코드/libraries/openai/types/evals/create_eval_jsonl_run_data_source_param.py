# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: create_eval_jsonl_run_data_source_param.pyc (Python 3.11)

from __future__ import annotations
from typing import Dict, Union, Iterable
from typing_extensions import Literal, Required, TypeAlias, TypedDict
__all__ = [
    'CreateEvalJSONLRunDataSourceParam',
    'Source',
    'SourceFileContent',
    'SourceFileContentContent',
    'SourceFileID']

def SourceFileContentContent():
    '''SourceFileContentContent'''
    sample: 'Dict[str, object]' = 'SourceFileContentContent'

SourceFileContentContent = <NODE:27>(SourceFileContentContent, 'SourceFileContentContent', TypedDict, total = False)

def SourceFileContent():
    '''SourceFileContent'''
    type: "Required[Literal['file_content']]" = 'SourceFileContent'

SourceFileContent = <NODE:27>(SourceFileContent, 'SourceFileContent', TypedDict, total = False)

def SourceFileID():
    '''SourceFileID'''
    type: "Required[Literal['file_id']]" = 'SourceFileID'

SourceFileID = <NODE:27>(SourceFileID, 'SourceFileID', TypedDict, total = False)
Source: 'TypeAlias' = Union[(SourceFileContent, SourceFileID)]

def CreateEvalJSONLRunDataSourceParam():
    '''CreateEvalJSONLRunDataSourceParam'''
    type: "Required[Literal['jsonl']]" = '\n    A JsonlRunDataSource object with that specifies a JSONL file that matches the eval\n    '

CreateEvalJSONLRunDataSourceParam = <NODE:27>(CreateEvalJSONLRunDataSourceParam, 'CreateEvalJSONLRunDataSourceParam', TypedDict, total = False)
