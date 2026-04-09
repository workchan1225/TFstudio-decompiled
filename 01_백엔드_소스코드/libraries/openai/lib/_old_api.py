# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: _old_api.pyc (Python 3.11)

from __future__ import annotations
from typing import TYPE_CHECKING, Any
from typing_extensions import override
from _utils import LazyProxy
from _exceptions import OpenAIError
INSTRUCTIONS = '\n\nYou tried to access openai.{symbol}, but this is no longer supported in openai>=1.0.0 - see the README at https://github.com/openai/openai-python for the API.\n\nYou can run `openai migrate` to automatically upgrade your codebase to use the 1.0.0 interface. \n\nAlternatively, you can pin your installation to the old version, e.g. `pip install openai==0.28`\n\nA detailed migration guide is available here: https://github.com/openai/openai-python/discussions/742\n'

class APIRemovedInV1(OpenAIError):
    pass
# WARNING: Decompyle incomplete


def APIRemovedInV1Proxy():
    '''APIRemovedInV1Proxy'''
    pass
# WARNING: Decompyle incomplete

APIRemovedInV1Proxy = <NODE:27>(APIRemovedInV1Proxy, 'APIRemovedInV1Proxy', LazyProxy[Any])
SYMBOLS = [
    'Edit',
    'File',
    'Audio',
    'Image',
    'Model',
    'Engine',
    'Customer',
    'FineTune',
    'Embedding',
    'Completion',
    'Deployment',
    'Moderation',
    'ErrorObject',
    'FineTuningJob',
    'ChatCompletion']
__locals = locals()
for symbol in SYMBOLS:
    __locals[symbol] = APIRemovedInV1Proxy(symbol = symbol)
    return None
