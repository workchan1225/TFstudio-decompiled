# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: generation_types.pyc (Python 3.11)

from __future__ import annotations
import collections
import contextlib
from collections.abc import Iterable, AsyncIterable, Mapping
import dataclasses
import itertools
import json
import sys
import textwrap
from typing import Union, Any
from typing_extensions import TypedDict
import types
import google.protobuf.json_format as google
import google.api_core.exceptions as google
from google.generativeai import protos
from google.generativeai import string_utils
from google.generativeai.types import content_types
from google.generativeai.responder import _rename_schema_fields
__all__ = [
    'AsyncGenerateContentResponse',
    'BlockedPromptException',
    'StopCandidateException',
    'IncompleteIterationError',
    'BrokenResponseError',
    'GenerationConfigDict',
    'GenerationConfigType',
    'GenerationConfig',
    'GenerateContentResponse']
if sys.version_info < (3, 10):
    
    def aiter(obj):
        return obj.__aiter__()

    
    async def anext(obj, default = (None,)):
        pass
    # WARNING: Decompyle incomplete


class BlockedPromptException(Exception):
    pass


class StopCandidateException(Exception):
    pass


class IncompleteIterationError(Exception):
    pass


class BrokenResponseError(Exception):
    pass


def GenerationConfigDict():
    '''GenerationConfigDict'''
    frequency_penalty: 'float' = 'GenerationConfigDict'

GenerationConfigDict = <NODE:27>(GenerationConfigDict, 'GenerationConfigDict', TypedDict, total = False)
GenerationConfig = <NODE:12>()
GenerationConfigType = Union[(protos.GenerationConfig, GenerationConfigDict, GenerationConfig)]

def _normalize_schema(generation_config):
    response_schema = generation_config.get('response_schema', None)
# WARNING: Decompyle incomplete


def to_generation_config_dict(generation_config = None):
    pass
# WARNING: Decompyle incomplete


def _join_citation_metadatas(citation_metadatas = None):
    citation_metadatas = list(citation_metadatas)
    return citation_metadatas[-1]


def _join_safety_ratings_lists(safety_ratings_lists = None):
    ratings = { }
    blocked = collections.defaultdict(list)
    for safety_ratings_list in safety_ratings_lists:
        for rating in safety_ratings_list:
            ratings[rating.category] = rating.probability
            blocked[rating.category].append(rating.blocked)
            blocked = blocked.items()()
            safety_list = []
            for category, probability in zip(ratings.items(), blocked.values()):
                blocked = None
                safety_list.append(protos.SafetyRating(category = category, probability = probability, blocked = blocked))
                return safety_list


def _join_contents(contents = None):
    contents = tuple(contents)
    roles = contents()
    parts = []
    for content in contents:
        parts.extend(content.parts)
        merged_parts = []
        last = parts[0]
        for part in parts[1:]:
            if 'text' in last and 'text' in part:
                last = protos.Part(text = last.text + part.text)
                continue
            if 'executable_code' in last and 'executable_code' in part:
                last = protos.Part(executable_code = _join_executable_code(last.executable_code, part.executable_code))
                continue
            if 'code_execution_result' in last and 'code_execution_result' in part:
                last = protos.Part(code_execution_result = _join_code_execution_result(last.code_execution_result, part.code_execution_result))
                continue
            merged_parts.append(last)
            last = part
            merged_parts.append(last)
            return protos.Content(role = role, parts = merged_parts)


def _join_executable_code(code_1, code_2):
    return protos.ExecutableCode(language = code_1.language, code = code_1.code + code_2.code)


def _join_code_execution_result(result_1, result_2):
    return protos.CodeExecutionResult(outcome = result_2.outcome, output = result_1.output + result_2.output)


def _join_candidates(candidates = None):
    '''Joins stream chunks of a single candidate.'''
    candidates = tuple(candidates)
    index = candidates[0].index
    return None(index = _join_safety_ratings_lists, content = (lambda .0: [ c.safety_ratings for c in .0 ])(candidates()), finish_reason = None, safety_ratings = _join_citation_metadatas, citation_metadata = (lambda .0: [ c.citation_metadata for c in .0 ])(candidates()), token_count = candidates[-1].token_count)


def _join_candidate_lists(candidate_lists = None):
    '''Joins stream chunks where each chunk is a list of candidate chunks.'''
    candidates = collections.defaultdict(list)
    for candidate_list in candidate_lists:
        for candidate in candidate_list:
            candidates[candidate.index].append(candidate)
            new_candidates = []
            for index, candidate_parts in sorted(candidates.items()):
                new_candidates.append(_join_candidates(candidate_parts))
                return new_candidates


def _join_prompt_feedbacks(prompt_feedbacks = None):
    return next(iter(prompt_feedbacks))


def _join_chunks(chunks = None):
    chunks = tuple(chunks)
    if 'usage_metadata' in chunks[-1]:
        usage_metadata = chunks[-1].usage_metadata
    else:
        usage_metadata = None
    if 'model_version' in chunks[-1]:
        model_version = chunks[-1].model_version
    else:
        model_version = None
    return None(candidates = _join_prompt_feedbacks, prompt_feedback = (lambda .0: pass# WARNING: Decompyle incomplete
)(chunks()), usage_metadata = usage_metadata, model_version = model_version)

_INCOMPLETE_ITERATION_MESSAGE = 'Please let the response complete iteration before accessing the final accumulated\nattributes (or call `response.resolve()`)'

class BaseGenerateContentResponse:
    
    def __init__(self = None, done = None, iterator = None, result = (None,), chunks = ('done', 'bool', 'iterator', 'None | Iterable[protos.GenerateContentResponse] | AsyncIterable[protos.GenerateContentResponse]', 'result', 'protos.GenerateContentResponse', 'chunks', 'Iterable[protos.GenerateContentResponse] | None')):
        self._done = done
        self._iterator = iterator
        self._result = result
    # WARNING: Decompyle incomplete

    
    def to_dict(self):
        """Returns the result as a JSON-compatible dict.

        Note: This doesn't capture the iterator state when streaming, it only captures the accumulated
        `GenerateContentResponse` fields.

        >>> import json
        >>> response = model.generate_content('Hello?')
        >>> json.dumps(response.to_dict())
        """
        return type(self._result).to_dict(self._result)

    candidates = (lambda self: if not self._done:
raise IncompleteIterationError(_INCOMPLETE_ITERATION_MESSAGE)self._result.candidates)()
    parts = (lambda self: candidates = self.candidatesif not candidates:
msg = 'Invalid operation: The `response.parts` quick accessor requires a single candidate, but but `response.candidates` is empty.'if self.prompt_feedback:
raise ValueError(msg + f'''\nThis appears to be caused by a blocked prompt, see `response.prompt_feedback`: {self.prompt_feedback}''')raise ValueError(msg)if len(candidates) > 1:
raise ValueError('Invalid operation: The `response.parts` quick accessor retrieves the parts for a single candidate. This response contains multiple candidates, please use `result.candidates[index].text`.')parts = candidates[0].content.partsparts)()
    text = (lambda self: parts = self.partsif not parts:
candidate = self.candidates[0]fr = candidate.finish_reasonFinishReason = protos.Candidate.FinishReasonmsg = f'''Invalid operation: The `response.text` quick accessor requires the response to contain a valid `Part`, but none were returned. The candidate\'s [finish_reason](https://ai.google.dev/api/generate-content#finishreason) is {fr}.'''if fr is FinishReason.FINISH_REASON_UNSPECIFIED:
raise ValueError(msg)if fr is FinishReason.STOP:
raise ValueError(msg)if fr is FinishReason.MAX_TOKENS:
raise ValueError(msg)if fr is FinishReason.SAFETY:
raise ValueError(msg + f''' The candidate\'s safety_ratings are: {candidate.safety_ratings}.''', candidate.safety_ratings)if fr is FinishReason.RECITATION:
raise ValueError(msg + ' Meaning that the model was reciting from copyrighted material.')if fr is FinishReason.LANGUAGE:
raise ValueError(msg + ' Meaning the response was using an unsupported language.')if fr is FinishReason.OTHER:
raise ValueError(msg)if fr is FinishReason.BLOCKLIST:
raise ValueError(msg)if fr is FinishReason.PROHIBITED_CONTENT:
raise ValueError(msg)if fr is FinishReason.SPII:
raise ValueError(msg + ' SPII - Sensitive Personally Identifiable Information.')if fr is FinishReason.MALFORMED_FUNCTION_CALL:
raise ValueError(msg + ' Meaning that model generated a `FunctionCall` that was invalid. Setting the [Function calling mode](https://ai.google.dev/gemini-api/docs/function-calling#function_calling_mode) to `ANY` can fix this because it enables constrained decoding.')raise ValueError(msg)texts = []for part in parts:
if 'text' in part:
texts.append(part.text)continueif 'executable_code' in part:
language = part.executable_code.language.name.lower()if language == 'language_unspecified':
language = ''else:
language = f''' {language}'''texts.extend([
f'''```{language}''',
part.executable_code.code.lstrip('\n'),
'```'])continueif 'code_execution_result' in part:
outcome_result = part.code_execution_result.outcome.name.lower().replace('outcome_', '')if outcome_result == 'ok' or outcome_result == 'unspecified':
outcome_result = ''else:
outcome_result = f''' {outcome_result}'''texts.extend([
f'''```{outcome_result}''',
part.code_execution_result.output,
'```'])continuepart_type = protos.Part.pb(part).WhichOneof('data')raise ValueError(f'''Could not convert `part.{part_type}` to text.''')'\n'.join(texts))()
    prompt_feedback = (lambda self: self._result.prompt_feedback)()
    usage_metadata = (lambda self: self._result.usage_metadata)()
    model_version = (lambda self: self._result.model_version)()
    
    def __str__(self = property):
        if self._done:
            _iterator = 'None'
        else:
            _iterator = f'''<{self._iterator.__class__.__name__}>'''
        as_dict = type(self._result).to_dict(self._result, use_integers_for_enums = False, including_default_value_fields = False)
        json_str = json.dumps(as_dict, indent = 2)
        _result = f'''protos.GenerateContentResponse({json_str})'''
        _result = _result.replace('\n', '\n                    ')
        if self._error:
            _error = f''',\nerror={repr(self._error)}'''
        else:
            _error = ''
        return textwrap.dedent(f'''                response:\n                {type(self).__name__}(\n                    done={self._done},\n                    iterator={_iterator},\n                    result={_result},\n                )''') + _error

    __repr__ = __str__

rewrite_stream_error = (lambda : pass# WARNING: Decompyle incomplete
)()
GENERATE_CONTENT_RESPONSE_DOC = 'Instances of this class manage the response of the `generate_content` method.\n\n    These are returned by `GenerativeModel.generate_content` and `ChatSession.send_message`.\n    This object is based on the low level `protos.GenerateContentResponse` class which just has `prompt_feedback`\n    and `candidates` attributes. This class adds several quick accessors for common use cases.\n\n    The same object type is returned for both `stream=True/False`.\n\n    ### Streaming\n\n    When you pass `stream=True` to `GenerativeModel.generate_content` or `ChatSession.send_message`,\n    iterate over this object to receive chunks of the response:\n\n    ```\n    response = model.generate_content(..., stream=True):\n    for chunk in response:\n      print(chunk.text)\n    ```\n\n    `GenerateContentResponse.prompt_feedback` is available immediately but\n    `GenerateContentResponse.candidates`, and all the attributes derived from them (`.text`, `.parts`),\n    are only available after the iteration is complete.\n    '
ASYNC_GENERATE_CONTENT_RESPONSE_DOC = 'This is the async version of `genai.GenerateContentResponse`.'
GenerateContentResponse = <NODE:12>()
AsyncGenerateContentResponse = <NODE:12>()
