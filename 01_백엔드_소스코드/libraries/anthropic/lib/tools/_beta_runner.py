# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: _beta_runner.pyc (Python 3.11)

from __future__ import annotations
import logging
from abc import ABC, abstractmethod
from typing import TYPE_CHECKING, Any, List, Union, Generic, TypeVar, Callable, Iterable, Iterator, Coroutine, AsyncIterator
from contextlib import contextmanager, asynccontextmanager
from typing_extensions import TypedDict, override
import httpx
from _types import Body, Query, Headers, NotGiven
from _utils import consume_sync_iterator, consume_async_iterator
from types.beta import BetaMessage, BetaMessageParam
from _beta_functions import BetaFunctionTool, BetaRunnableTool, BetaAsyncFunctionTool, BetaAsyncRunnableTool, BetaBuiltinFunctionTool, BetaAsyncBuiltinFunctionTool
from _beta_compaction_control import DEFAULT_THRESHOLD, DEFAULT_SUMMARY_PROMPT, CompactionControl
from streaming._beta_messages import BetaMessageStream, BetaAsyncMessageStream
from types.beta.parsed_beta_message import ResponseFormatT, ParsedBetaMessage, ParsedBetaContentBlock
from types.beta.message_create_params import ParseMessageCreateParamsBase
from types.beta.beta_tool_result_block_param import BetaToolResultBlockParam
if TYPE_CHECKING:
    from _client import Anthropic, AsyncAnthropic
AnyFunctionToolT = TypeVar('AnyFunctionToolT', bound = Union[(BetaFunctionTool[Any], BetaAsyncFunctionTool[Any], BetaBuiltinFunctionTool, BetaAsyncBuiltinFunctionTool)])
RunnerItemT = TypeVar('RunnerItemT')
log = logging.getLogger(__name__)

def RequestOptions():
    '''RequestOptions'''
    timeout: 'float | httpx.Timeout | None | NotGiven' = 'RequestOptions'

RequestOptions = <NODE:27>(RequestOptions, 'RequestOptions', TypedDict, total = False)

def BaseToolRunner():
    '''BaseToolRunner'''
    
    def __init__(self = None, *, params, options, tools, max_iterations, compaction_control):
        self._tools_by_name = tools()
    # WARNING: Decompyle incomplete

    
    def set_messages_params(self = None, params = None):
        '''
        Update the parameters for the next API call. This invalidates any cached tool responses.

        Args:
            params (ParsedMessageCreateParamsBase[ResponseFormatT] | Callable): Either new parameters or a function to mutate existing parameters
        '''
        if callable(params):
            params = params(self._params)
        self._params = params

    
    def append_messages(self = None, *messages):
        '''Add one or more messages to the conversation history.

        This invalidates the cached tool response, i.e. if tools were already called, then they will
        be called again on the next loop iteration.
        '''
        pass
    # WARNING: Decompyle incomplete

    
    def _should_stop(self = None):
        pass
    # WARNING: Decompyle incomplete


BaseToolRunner = <NODE:27>(BaseToolRunner, 'BaseToolRunner', Generic[(AnyFunctionToolT, ResponseFormatT)])

def BaseSyncToolRunner():
    '''BaseSyncToolRunner'''
    pass
# WARNING: Decompyle incomplete

BaseSyncToolRunner = <NODE:27>(BaseSyncToolRunner, 'BaseSyncToolRunner', BaseToolRunner[(BetaRunnableTool, ResponseFormatT)], Generic[(RunnerItemT, ResponseFormatT)], ABC)

def BetaToolRunner():
    '''BetaToolRunner'''
    _handle_request = (lambda self = None: pass# WARNING: Decompyle incomplete
)()()

BetaToolRunner = <NODE:27>(BetaToolRunner, 'BetaToolRunner', BaseSyncToolRunner[(ParsedBetaMessage[ResponseFormatT], ResponseFormatT)])

def BetaStreamingToolRunner():
    '''BetaStreamingToolRunner'''
    _handle_request = (lambda self = None: pass# WARNING: Decompyle incomplete
)()()

BetaStreamingToolRunner = <NODE:27>(BetaStreamingToolRunner, 'BetaStreamingToolRunner', BaseSyncToolRunner[(BetaMessageStream[ResponseFormatT], ResponseFormatT)])

def BaseAsyncToolRunner():
    '''BaseAsyncToolRunner'''
    pass
# WARNING: Decompyle incomplete

BaseAsyncToolRunner = <NODE:27>(BaseAsyncToolRunner, 'BaseAsyncToolRunner', BaseToolRunner[(BetaAsyncRunnableTool, ResponseFormatT)], Generic[(RunnerItemT, ResponseFormatT)], ABC)

def BetaAsyncToolRunner():
    '''BetaAsyncToolRunner'''
    _handle_request = (lambda self = None: pass# WARNING: Decompyle incomplete
)()()

BetaAsyncToolRunner = <NODE:27>(BetaAsyncToolRunner, 'BetaAsyncToolRunner', BaseAsyncToolRunner[(ParsedBetaMessage[ResponseFormatT], ResponseFormatT)])

def BetaAsyncStreamingToolRunner():
    '''BetaAsyncStreamingToolRunner'''
    _handle_request = (lambda self = None: pass# WARNING: Decompyle incomplete
)()()

BetaAsyncStreamingToolRunner = <NODE:27>(BetaAsyncStreamingToolRunner, 'BetaAsyncStreamingToolRunner', BaseAsyncToolRunner[(BetaAsyncMessageStream[ResponseFormatT], ResponseFormatT)])
