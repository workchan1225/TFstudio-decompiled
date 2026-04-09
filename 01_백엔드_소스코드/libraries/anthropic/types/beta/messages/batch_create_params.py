# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: batch_create_params.pyc (Python 3.11)

from __future__ import annotations
from typing import List, Literal, Iterable
from typing_extensions import Required, Annotated, TypedDict
from _utils import PropertyInfo
from anthropic_beta_param import AnthropicBetaParam
from message_create_params import MessageCreateParamsNonStreaming
__all__ = [
    'BatchCreateParams',
    'Request',
    'RequestParamsOutputFormat']

def BatchCreateParams():
    '''BatchCreateParams'''
    betas: "Annotated[List[AnthropicBetaParam], PropertyInfo(alias='anthropic-beta')]" = 'BatchCreateParams'

BatchCreateParams = <NODE:27>(BatchCreateParams, 'BatchCreateParams', TypedDict, total = False)

def RequestParamsOutputFormat():
    '''RequestParamsOutputFormat'''
    type: "Required[Literal['json_schema']]" = 'RequestParamsOutputFormat'

RequestParamsOutputFormat = <NODE:27>(RequestParamsOutputFormat, 'RequestParamsOutputFormat', TypedDict, total = False)

def Request():
    '''Request'''
    params: 'Required[MessageCreateParamsNonStreaming]' = 'Request'

Request = <NODE:27>(Request, 'Request', TypedDict, total = False)
