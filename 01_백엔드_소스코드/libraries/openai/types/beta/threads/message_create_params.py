# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: message_create_params.pyc (Python 3.11)

from __future__ import annotations
from typing import Union, Iterable, Optional
from typing_extensions import Literal, Required, TypeAlias, TypedDict
from shared_params.metadata import Metadata
from message_content_part_param import MessageContentPartParam
from code_interpreter_tool_param import CodeInterpreterToolParam
__all__ = [
    'MessageCreateParams',
    'Attachment',
    'AttachmentTool',
    'AttachmentToolFileSearch']

def MessageCreateParams():
    '''MessageCreateParams'''
    metadata: 'Optional[Metadata]' = 'MessageCreateParams'

MessageCreateParams = <NODE:27>(MessageCreateParams, 'MessageCreateParams', TypedDict, total = False)

def AttachmentToolFileSearch():
    '''AttachmentToolFileSearch'''
    type: "Required[Literal['file_search']]" = 'AttachmentToolFileSearch'

AttachmentToolFileSearch = <NODE:27>(AttachmentToolFileSearch, 'AttachmentToolFileSearch', TypedDict, total = False)
AttachmentTool: 'TypeAlias' = Union[(CodeInterpreterToolParam, AttachmentToolFileSearch)]

def Attachment():
    '''Attachment'''
    tools: 'Iterable[AttachmentTool]' = 'Attachment'

Attachment = <NODE:27>(Attachment, 'Attachment', TypedDict, total = False)
