# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: extensions.pyc (Python 3.11)

import asyncio
import collections
import itertools
import queue
import threading
from typing import AsyncIterable, Callable, Iterable, List, Optional, Union
from ctranslate2._ext import GenerationResult, GenerationStepResult, Generator, ScoringResult, TranslationResult, Translator

def register_extensions():
    '''Registers additional attributes to compiled modules.'''
    setattr(Translator, 'translate_iterable', translator_translate_iterable)
    setattr(Translator, 'score_iterable', translator_score_iterable)
    setattr(Translator, 'generate_tokens', translator_generate_tokens)
    setattr(Generator, 'generate_iterable', generator_generate_iterable)
    setattr(Generator, 'score_iterable', generator_score_iterable)
    setattr(Generator, 'generate_tokens', generator_generate_tokens)
    setattr(Generator, 'async_generate_tokens', generator_async_generate_tokens)


def translator_translate_iterable(translator = None, source = None, target_prefix = None, max_batch_size = (None, 32, 'examples'), batch_type = ('translator', Translator, 'source', Iterable[List[str]], 'target_prefix', Optional[Iterable[List[str]]], 'max_batch_size', int, 'batch_type', str, 'return', Iterable[TranslationResult]), **kwargs):
    '''Translates an iterable of tokenized examples.

    This method is built on top of :meth:`ctranslate2.Translator.translate_batch`
    to efficiently translate an arbitrarily large stream of data. It enables the
    following optimizations:

    * stream processing (the iterable is not fully materialized in memory)
    * parallel translations (if the translator has multiple workers)
    * asynchronous batch prefetching
    * local sorting by length

    Arguments:
      source: An iterable of tokenized source examples.
      target_prefix: An optional iterable of tokenized target prefixes.
      max_batch_size: The maximum batch size.
      batch_type: Whether :obj:`max_batch_size` is the number of "examples" or "tokens".
      **kwargs: Any translation options accepted by
        :meth:`ctranslate2.Translator.translate_batch`.

    Returns:
      A generator iterator over :class:`ctranslate2.TranslationResult` instances.

    Example:
      This method can be used to efficiently translate text files:

      .. code-block:: python

          # Replace by your own tokenization and detokenization functions.
          tokenize_fn = lambda line: line.strip().split()
          detokenize_fn = lambda tokens: " ".join(tokens)

          with open("input.txt") as input_file:
              source = map(tokenize_fn, input_file)
              results = translator.translate_iterable(source, max_batch_size=64)

              for result in results:
                  tokens = result.hypotheses[0]
                  target = detokenize_fn(tokens)
                  print(target)
    '''
    pass
# WARNING: Decompyle incomplete


def translator_score_iterable(translator = None, source = None, target = None, max_batch_size = (64, 'examples'), batch_type = ('translator', Translator, 'source', Iterable[List[str]], 'target', Iterable[List[str]], 'max_batch_size', int, 'batch_type', str, 'return', Iterable[ScoringResult]), **kwargs):
    '''Scores an iterable of tokenized examples.

    This method is built on top of :meth:`ctranslate2.Translator.score_batch`
    to efficiently score an arbitrarily large stream of data. It enables the
    following optimizations:

    * stream processing (the iterable is not fully materialized in memory)
    * parallel scoring (if the translator has multiple workers)
    * asynchronous batch prefetching
    * local sorting by length

    Arguments:
      source: An iterable of tokenized source examples.
      target: An iterable of tokenized target examples.
      max_batch_size: The maximum batch size.
      batch_type: Whether :obj:`max_batch_size` is the number of "examples" or "tokens".
      **kwargs: Any scoring options accepted by
        :meth:`ctranslate2.Translator.score_batch`.

    Returns:
      A generator iterator over :class:`ctranslate2.ScoringResult` instances.
    '''
    pass
# WARNING: Decompyle incomplete


def generator_generate_iterable(generator = None, start_tokens = None, max_batch_size = None, batch_type = (32, 'examples'), **kwargs):
    '''Generates from an iterable of tokenized prompts.

    This method is built on top of :meth:`ctranslate2.Generator.generate_batch`
    to efficiently run generation on an arbitrarily large stream of data. It enables
    the following optimizations:

    * stream processing (the iterable is not fully materialized in memory)
    * parallel generations (if the generator has multiple workers)
    * asynchronous batch prefetching
    * local sorting by length

    Arguments:
      start_tokens: An iterable of tokenized prompts.
      max_batch_size: The maximum batch size.
      batch_type: Whether :obj:`max_batch_size` is the number of "examples" or "tokens".
      **kwargs: Any generation options accepted by
        :meth:`ctranslate2.Generator.generate_batch`.

    Returns:
      A generator iterator over :class:`ctranslate2.GenerationResult` instances.
    '''
    pass
# WARNING: Decompyle incomplete


def generator_score_iterable(generator = None, tokens = None, max_batch_size = None, batch_type = (64, 'examples'), **kwargs):
    '''Scores an iterable of tokenized examples.

    This method is built on top of :meth:`ctranslate2.Generator.score_batch`
    to efficiently score an arbitrarily large stream of data. It enables
    the following optimizations:

    * stream processing (the iterable is not fully materialized in memory)
    * parallel scoring (if the generator has multiple workers)
    * asynchronous batch prefetching
    * local sorting by length

    Arguments:
      tokens: An iterable of tokenized examples.
      max_batch_size: The maximum batch size.
      batch_type: Whether :obj:`max_batch_size` is the number of "examples" or "tokens".
      **kwargs: Any score options accepted by
        :meth:`ctranslate2.Generator.score_batch`.

    Returns:
      A generator iterator over :class:`ctranslate2.ScoringResult` instances.
    '''
    pass
# WARNING: Decompyle incomplete


def translator_generate_tokens(translator = None, source = None, target_prefix = None, *, max_decoding_length, min_decoding_length, sampling_topk, sampling_topp, sampling_temperature, return_log_prob, repetition_penalty, no_repeat_ngram_size, disable_unk, suppress_sequences, end_token, max_input_length, use_vmap):
    '''Yields tokens as they are generated by the model.

    Arguments:
      source: Source tokens.
      target_prefix: Optional target prefix tokens.
      max_decoding_length: Maximum prediction length.
      min_decoding_length: Minimum prediction length.
      sampling_topk: Randomly sample predictions from the top K candidates.
      sampling_topp: Keep the most probable tokens whose cumulative probability exceeds this value.
      sampling_temperature: Sampling temperature to generate more random samples.
      return_log_prob: Include the token log probability in the result.
      repetition_penalty: Penalty applied to the score of previously generated tokens
        (set > 1 to penalize).
      no_repeat_ngram_size: Prevent repetitions of ngrams with this size
        (set 0 to disable).
      disable_unk: Disable the generation of the unknown token.
      suppress_sequences: Disable the generation of some sequences of tokens.
      end_token: Stop the decoding on one of these tokens (defaults to the model EOS token).
      max_input_length: Truncate inputs after this many tokens (set 0 to disable).
      use_vmap: Use the vocabulary mapping file saved in this model

    Returns:
      A generator iterator over :class:`ctranslate2.GenerationStepResult` instances.

    Note:
      This generation method is not compatible with beam search which requires a complete decoding.
    '''
    pass
# WARNING: Decompyle incomplete


def generator_generate_tokens(generator = None, prompt = None, max_batch_size = None, batch_type = None, *, max_length, min_length, sampling_topk, sampling_topp, sampling_temperature, return_log_prob, repetition_penalty, no_repeat_ngram_size, disable_unk, suppress_sequences, end_token, static_prompt, cache_static_prompt, callback):
    '''Yields tokens as they are generated by the model.

    Arguments:
      prompt: Batch of start tokens. If the decoder starts from a
        special start token like <s>, this token should be added to this input.
      max_batch_size: The maximum batch size.
      batch_type: Whether :obj:`max_batch_size` is the number of "examples" or "tokens".
      max_length: Maximum generation length.
      min_length: Minimum generation length.
      sampling_topk: Randomly sample predictions from the top K candidates.
      sampling_topp: Keep the most probable tokens whose cumulative probability exceeds this value.
      sampling_temperature: Sampling temperature to generate more random samples.
      return_log_prob: Include the token log probability in the result.
      repetition_penalty: Penalty applied to the score of previously generated tokens
        (set > 1 to penalize).
      no_repeat_ngram_size: Prevent repetitions of ngrams with this size
        (set 0 to disable).
      disable_unk: Disable the generation of the unknown token.
      suppress_sequences: Disable the generation of some sequences of tokens.
      end_token: Stop the decoding on one these tokens (defaults to the model EOS token).
      static_prompt: If the model expects a static prompt (a.k.a. system prompt)
        it can be set here to simplify the inputs and optionally cache the model
        state for this prompt to accelerate future generations.
      cache_static_prompt: Cache the model state after the static prompt and
        reuse it for future generations using the same static prompt.
      callback: Optional function that is called for each generated token when
        obj:`beam_size` is 1. If the callback function returns ``True``, the
        decoding will stop for this batch index.

    Returns:
      A generator iterator over :class:`ctranslate2.GenerationStepResult` instances.

    Note:
      This generation method is not compatible with beam search which requires a complete decoding.
    '''
    pass
# WARNING: Decompyle incomplete


def generator_async_generate_tokens(generator = None, prompt = None, max_batch_size = None, batch_type = None, *, max_length, min_length, sampling_topk, sampling_topp, sampling_temperature, return_log_prob, repetition_penalty, no_repeat_ngram_size, disable_unk, suppress_sequences, end_token, static_prompt, cache_static_prompt, callback):
    '''Yields tokens asynchronously as they are generated by the model.

    Arguments:
      prompt: Batch of start tokens. If the decoder starts from a
        special start token like <s>, this token should be added to this input.
      max_batch_size: The maximum batch size.
      batch_type: Whether :obj:`max_batch_size` is the number of "examples" or "tokens".
      max_length: Maximum generation length.
      min_length: Minimum generation length.
      sampling_topk: Randomly sample predictions from the top K candidates.
      sampling_topp: Keep the most probable tokens whose cumulative probability exceeds this value.
      sampling_temperature: Sampling temperature to generate more random samples.
      return_log_prob: Include the token log probability in the result.
      repetition_penalty: Penalty applied to the score of previously generated tokens
        (set > 1 to penalize).
      no_repeat_ngram_size: Prevent repetitions of ngrams with this size
        (set 0 to disable).
      disable_unk: Disable the generation of the unknown token.
      suppress_sequences: Disable the generation of some sequences of tokens.
      end_token: Stop the decoding on one of these tokens (defaults to the model EOS token).
      static_prompt: If the model expects a static prompt (a.k.a. system prompt)
        it can be set here to simplify the inputs and optionally cache the model
        state for this prompt to accelerate future generations.
      cache_static_prompt: Cache the model state after the static prompt and
        reuse it for future generations using the same static prompt.
      callback: Optional function that is called for each generated token when
        obj:`beam_size` is 1. If the callback function returns ``True``, the
        decoding will stop for this batch index.

    Returns:
      An async generator iterator over :class:`ctranslate2.GenerationStepResult` instances.

    Note:
      This generation method is not compatible with beam search which requires a complete decoding.
    '''
    pass
# WARNING: Decompyle incomplete


class AsyncGenerator:
    
    def __init__(self, process_func, *args, **kwargs):
        self.queue = asyncio.Queue()
        self.shutdown_event = threading.Event()
        self.iterator_task = None
        self.process_func = process_func
        self.args = args
        self.kwargs = kwargs

    
    async def producer(self):
        pass
    # WARNING: Decompyle incomplete

    
    def __aiter__(self):
        self.iterator_task = asyncio.create_task(self.producer())
        return self

    
    async def __anext__(self):
        pass
    # WARNING: Decompyle incomplete



def _generate_tokens(process_func, *args, **kwargs):
    pass
# WARNING: Decompyle incomplete


def _process_iterable(process_func, iterables, max_batch_size, batch_type, **kwargs):
    pass
# WARNING: Decompyle incomplete


def _batch_iterator(iterable, batch_size, batch_type):
    pass
# WARNING: Decompyle incomplete
