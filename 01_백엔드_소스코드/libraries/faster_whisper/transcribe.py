# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: transcribe.pyc (Python 3.11)

import itertools
import json
import logging
import os
import zlib
from dataclasses import asdict, dataclass
from inspect import signature
from math import ceil
from typing import BinaryIO, Iterable, List, Optional, Tuple, Union
from warnings import warn
import ctranslate2
import numpy as np
import tokenizers
from tqdm import tqdm
from faster_whisper.audio import decode_audio, pad_or_trim
from faster_whisper.feature_extractor import FeatureExtractor
from faster_whisper.tokenizer import _LANGUAGE_CODES, Tokenizer
from faster_whisper.utils import download_model, format_timestamp, get_end, get_logger
from faster_whisper.vad import SpeechTimestampsMap, VadOptions, collect_chunks, get_speech_timestamps
Word = <NODE:12>()
Segment = <NODE:12>()
TranscriptionOptions = <NODE:12>()
TranscriptionInfo = <NODE:12>()

class BatchedInferencePipeline:
    
    def __init__(self, model):
        self.model = model
        self.last_speech_timestamp = 0

    
    def forward(self, features, tokenizer, chunks_metadata, options):
        pass
    # WARNING: Decompyle incomplete

    
    def generate_segment_batched(self = None, features = None, tokenizer = None, options = ('features', np.ndarray, 'tokenizer', Tokenizer, 'options', TranscriptionOptions)):
        pass
    # WARNING: Decompyle incomplete

    
    def transcribe(self, audio, language, task, log_progress, beam_size, best_of, patience, length_penalty, repetition_penalty, no_repeat_ngram_size, temperature, compression_ratio_threshold, log_prob_threshold, no_speech_threshold, condition_on_previous_text, prompt_reset_on_temperature, initial_prompt, prefix, suppress_blank, suppress_tokens, without_timestamps, max_initial_timestamp, word_timestamps, prepend_punctuations, append_punctuations, multilingual, vad_filter, vad_parameters, max_new_tokens, chunk_length, clip_timestamps, hallucination_silence_threshold = None, batch_size = None, hotwords = None, language_detection_threshold = (None, 'transcribe', False, 5, 5, 1, 1, 1, 0, [
        0,
        0.2,
        0.4,
        0.6,
        0.8,
        1], 2.4, -1, 0.6, True, 0.5, None, None, True, [
        -1], True, 1, False, '"\'“¿([{-', '"\'.。,，!！?？:：”)]}、', False, True, None, None, None, None, None, 8, None, 0.5, 1), language_detection_segments = ('audio', Union[(str, BinaryIO, np.ndarray)], 'language', Optional[str], 'task', str, 'log_progress', bool, 'beam_size', int, 'best_of', int, 'patience', float, 'length_penalty', float, 'repetition_penalty', float, 'no_repeat_ngram_size', int, 'temperature', Union[(float, List[float], Tuple[(float, ...)])], 'compression_ratio_threshold', Optional[float], 'log_prob_threshold', Optional[float], 'no_speech_threshold', Optional[float], 'condition_on_previous_text', bool, 'prompt_reset_on_temperature', float, 'initial_prompt', Optional[Union[(str, Iterable[int])]], 'prefix', Optional[str], 'suppress_blank', bool, 'suppress_tokens', Optional[List[int]], 'without_timestamps', bool, 'max_initial_timestamp', float, 'word_timestamps', bool, 'prepend_punctuations', str, 'append_punctuations', str, 'multilingual', bool, 'vad_filter', bool, 'vad_parameters', Optional[Union[(dict, VadOptions)]], 'max_new_tokens', Optional[int], 'chunk_length', Optional[int], 'clip_timestamps', Optional[List[dict]], 'hallucination_silence_threshold', Optional[float], 'batch_size', int, 'hotwords', Optional[str], 'language_detection_threshold', Optional[float], 'language_detection_segments', int, 'return', Tuple[(Iterable[Segment], TranscriptionInfo)])):
        '''transcribe audio in chunks in batched fashion and return with language info.

        Arguments:
            audio: Path to the input file (or a file-like object), or the audio waveform.
            language: The language spoken in the audio. It should be a language code such
                as "en" or "fr". If not set, the language will be detected in the first 30 seconds
                of audio.
            task: Task to execute (transcribe or translate).
            log_progress: whether to show progress bar or not.
            beam_size: Beam size to use for decoding.
            best_of: Number of candidates when sampling with non-zero temperature.
            patience: Beam search patience factor.
            length_penalty: Exponential length penalty constant.
            repetition_penalty: Penalty applied to the score of previously generated tokens
                (set > 1 to penalize).
            no_repeat_ngram_size: Prevent repetitions of ngrams with this size (set 0 to disable).
            temperature: Temperature for sampling. If a list or tuple is passed,
                only the first value is used.
            initial_prompt: Optional text string or iterable of token ids to provide as a
                prompt for the each window.
            suppress_blank: Suppress blank outputs at the beginning of the sampling.
            suppress_tokens: List of token IDs to suppress. -1 will suppress a default set
                of symbols as defined in `tokenizer.non_speech_tokens()`.
            without_timestamps: Only sample text tokens.
            word_timestamps: Extract word-level timestamps using the cross-attention pattern
                and dynamic time warping, and include the timestamps for each word in each segment.
                Set as False.
            prepend_punctuations: If word_timestamps is True, merge these punctuation symbols
                with the next word
            append_punctuations: If word_timestamps is True, merge these punctuation symbols
                with the previous word
            multilingual: Perform language detection on every segment.
            vad_filter: Enable the voice activity detection (VAD) to filter out parts of the audio
                without speech. This step is using the Silero VAD model
                https://github.com/snakers4/silero-vad.
            vad_parameters: Dictionary of Silero VAD parameters or VadOptions class (see available
                parameters and default values in the class `VadOptions`).
            max_new_tokens: Maximum number of new tokens to generate per-chunk. If not set,
                the maximum will be set by the default max_length.
            chunk_length: The length of audio segments. If it is not None, it will overwrite the
                default chunk_length of the FeatureExtractor.
            clip_timestamps: Optionally provide list of dictionaries each containing "start" and
                "end" keys that specify the start and end of the voiced region within
                `chunk_length` boundary. vad_filter will be ignored if clip_timestamps is used.
            batch_size: the maximum number of parallel requests to model for decoding.
            hotwords:
                Hotwords/hint phrases to the model. Has no effect if prefix is not None.
            language_detection_threshold: If the maximum probability of the language tokens is
                higher than this value, the language is detected.
            language_detection_segments: Number of segments to consider for the language detection.

        Unused Arguments
            compression_ratio_threshold: If the gzip compression ratio is above this value,
                treat as failed.
            log_prob_threshold: If the average log probability over sampled tokens is
                below this value, treat as failed.
            no_speech_threshold: If the no_speech probability is higher than this value AND
                the average log probability over sampled tokens is below `log_prob_threshold`,
                consider the segment as silent.
            condition_on_previous_text: If True, the previous output of the model is provided
                as a prompt for the next window; disabling may make the text inconsistent across
                windows, but the model becomes less prone to getting stuck in a failure loop,
                such as repetition looping or timestamps going out of sync. Set as False
            prompt_reset_on_temperature: Resets prompt if temperature is above this value.
                Arg has effect only if condition_on_previous_text is True. Set at 0.5
            prefix: Optional text to provide as a prefix at the beginning of each window.
            max_initial_timestamp: The initial timestamp cannot be later than this, set at 0.0.
            hallucination_silence_threshold: Optional[float]
                When word_timestamps is True, skip silent periods longer than this threshold
                (in seconds) when a possible hallucination is detected. set as None.
        Returns:
          A tuple with:

            - a generator over transcribed segments
            - an instance of TranscriptionInfo
        '''
        pass
    # WARNING: Decompyle incomplete

    
    def _batched_segments_generator(self, features, tokenizer, chunks_metadata, batch_size, options, log_progress):
        pass
    # WARNING: Decompyle incomplete



class WhisperModel:
    
    def __init__(self, model_size_or_path, device, device_index, compute_type, cpu_threads, num_workers, download_root = None, local_files_only = None, files = None, revision = ('auto', 0, 'default', 0, 1, None, False, None, None, None), use_auth_token = ('model_size_or_path', str, 'device', str, 'device_index', Union[(int, List[int])], 'compute_type', str, 'cpu_threads', int, 'num_workers', int, 'download_root', Optional[str], 'local_files_only', bool, 'files', dict, 'revision', Optional[str], 'use_auth_token', Optional[Union[(str, bool)]]), **model_kwargs):
        '''Initializes the Whisper model.

        Args:
          model_size_or_path: Size of the model to use (tiny, tiny.en, base, base.en,
            small, small.en, distil-small.en, medium, medium.en, distil-medium.en, large-v1,
            large-v2, large-v3, large, distil-large-v2, distil-large-v3, large-v3-turbo, or turbo),
            a path to a converted model directory, or a CTranslate2-converted Whisper model ID from
            the HF Hub. When a size or a model ID is configured, the converted model is downloaded
            from the Hugging Face Hub.
          device: Device to use for computation ("cpu", "cuda", "auto").
          device_index: Device ID to use.
            The model can also be loaded on multiple GPUs by passing a list of IDs
            (e.g. [0, 1, 2, 3]). In that case, multiple transcriptions can run in parallel
            when transcribe() is called from multiple Python threads (see also num_workers).
          compute_type: Type to use for computation.
            See https://opennmt.net/CTranslate2/quantization.html.
          cpu_threads: Number of threads to use when running on CPU (4 by default).
            A non zero value overrides the OMP_NUM_THREADS environment variable.
          num_workers: When transcribe() is called from multiple Python threads,
            having multiple workers enables true parallelism when running the model
            (concurrent calls to self.model.generate() will run in parallel).
            This can improve the global throughput at the cost of increased memory usage.
          download_root: Directory where the models should be saved. If not set, the models
            are saved in the standard Hugging Face cache directory.
          local_files_only:  If True, avoid downloading the file and return the path to the
            local cached file if it exists.
          files: Load model files from the memory. This argument is a dictionary mapping file names
            to file contents as file-like or bytes objects. If this is set, model_path acts as an
            identifier for this model.
          revision:
            An optional Git revision id which can be a branch name, a tag, or a
            commit hash.
          use_auth_token: HuggingFace authentication token or True to use the
            token stored by the HuggingFace config folder.
        '''
        self.logger = get_logger()
        (tokenizer_bytes, preprocessor_bytes) = (None, None)
        if files:
            model_path = model_size_or_path
            tokenizer_bytes = files.pop('tokenizer.json', None)
            preprocessor_bytes = files.pop('preprocessor_config.json', None)
        elif os.path.isdir(model_size_or_path):
            model_path = model_size_or_path
        else:
            model_path = download_model(model_size_or_path, local_files_only = local_files_only, cache_dir = download_root, revision = revision, use_auth_token = use_auth_token)
    # WARNING: Decompyle incomplete

    supported_languages = (lambda self = None: list(_LANGUAGE_CODES) if self.model.is_multilingual else [
'en'])()
    
    def _get_feature_kwargs(self = None, model_path = None, preprocessor_bytes = None):
        pass
    # WARNING: Decompyle incomplete

    
    def transcribe(self, audio, language, task, log_progress, beam_size, best_of, patience, length_penalty, repetition_penalty, no_repeat_ngram_size, temperature, compression_ratio_threshold, log_prob_threshold, no_speech_threshold, condition_on_previous_text, prompt_reset_on_temperature, initial_prompt, prefix, suppress_blank, suppress_tokens, without_timestamps, max_initial_timestamp, word_timestamps, prepend_punctuations, append_punctuations, multilingual, vad_filter, vad_parameters, max_new_tokens, chunk_length, clip_timestamps = None, hallucination_silence_threshold = None, hotwords = None, language_detection_threshold = (None, 'transcribe', False, 5, 5, 1, 1, 1, 0, [
        0,
        0.2,
        0.4,
        0.6,
        0.8,
        1], 2.4, -1, 0.6, True, 0.5, None, None, True, [
        -1], False, 1, False, '"\'“¿([{-', '"\'.。,，!！?？:：”)]}、', False, False, None, None, None, '0', None, None, 0.5, 1), language_detection_segments = ('audio', Union[(str, BinaryIO, np.ndarray)], 'language', Optional[str], 'task', str, 'log_progress', bool, 'beam_size', int, 'best_of', int, 'patience', float, 'length_penalty', float, 'repetition_penalty', float, 'no_repeat_ngram_size', int, 'temperature', Union[(float, List[float], Tuple[(float, ...)])], 'compression_ratio_threshold', Optional[float], 'log_prob_threshold', Optional[float], 'no_speech_threshold', Optional[float], 'condition_on_previous_text', bool, 'prompt_reset_on_temperature', float, 'initial_prompt', Optional[Union[(str, Iterable[int])]], 'prefix', Optional[str], 'suppress_blank', bool, 'suppress_tokens', Optional[List[int]], 'without_timestamps', bool, 'max_initial_timestamp', float, 'word_timestamps', bool, 'prepend_punctuations', str, 'append_punctuations', str, 'multilingual', bool, 'vad_filter', bool, 'vad_parameters', Optional[Union[(dict, VadOptions)]], 'max_new_tokens', Optional[int], 'chunk_length', Optional[int], 'clip_timestamps', Union[(str, List[float])], 'hallucination_silence_threshold', Optional[float], 'hotwords', Optional[str], 'language_detection_threshold', Optional[float], 'language_detection_segments', int, 'return', Tuple[(Iterable[Segment], TranscriptionInfo)])):
        '''Transcribes an input file.

        Arguments:
          audio: Path to the input file (or a file-like object), or the audio waveform.
          language: The language spoken in the audio. It should be a language code such
            as "en" or "fr". If not set, the language will be detected in the first 30 seconds
            of audio.
          task: Task to execute (transcribe or translate).
          log_progress: whether to show progress bar or not.
          beam_size: Beam size to use for decoding.
          best_of: Number of candidates when sampling with non-zero temperature.
          patience: Beam search patience factor.
          length_penalty: Exponential length penalty constant.
          repetition_penalty: Penalty applied to the score of previously generated tokens
            (set > 1 to penalize).
          no_repeat_ngram_size: Prevent repetitions of ngrams with this size (set 0 to disable).
          temperature: Temperature for sampling. It can be a tuple of temperatures,
            which will be successively used upon failures according to either
            `compression_ratio_threshold` or `log_prob_threshold`.
          compression_ratio_threshold: If the gzip compression ratio is above this value,
            treat as failed.
          log_prob_threshold: If the average log probability over sampled tokens is
            below this value, treat as failed.
          no_speech_threshold: If the no_speech probability is higher than this value AND
            the average log probability over sampled tokens is below `log_prob_threshold`,
            consider the segment as silent.
          condition_on_previous_text: If True, the previous output of the model is provided
            as a prompt for the next window; disabling may make the text inconsistent across
            windows, but the model becomes less prone to getting stuck in a failure loop,
            such as repetition looping or timestamps going out of sync.
          prompt_reset_on_temperature: Resets prompt if temperature is above this value.
            Arg has effect only if condition_on_previous_text is True.
          initial_prompt: Optional text string or iterable of token ids to provide as a
            prompt for the first window.
          prefix: Optional text to provide as a prefix for the first window.
          suppress_blank: Suppress blank outputs at the beginning of the sampling.
          suppress_tokens: List of token IDs to suppress. -1 will suppress a default set
            of symbols as defined in `tokenizer.non_speech_tokens()`.
          without_timestamps: Only sample text tokens.
          max_initial_timestamp: The initial timestamp cannot be later than this.
          word_timestamps: Extract word-level timestamps using the cross-attention pattern
            and dynamic time warping, and include the timestamps for each word in each segment.
          prepend_punctuations: If word_timestamps is True, merge these punctuation symbols
            with the next word
          append_punctuations: If word_timestamps is True, merge these punctuation symbols
            with the previous word
          multilingual: Perform language detection on every segment.
          vad_filter: Enable the voice activity detection (VAD) to filter out parts of the audio
            without speech. This step is using the Silero VAD model
            https://github.com/snakers4/silero-vad.
          vad_parameters: Dictionary of Silero VAD parameters or VadOptions class (see available
            parameters and default values in the class `VadOptions`).
          max_new_tokens: Maximum number of new tokens to generate per-chunk. If not set,
            the maximum will be set by the default max_length.
          chunk_length: The length of audio segments. If it is not None, it will overwrite the
            default chunk_length of the FeatureExtractor.
          clip_timestamps:
            Comma-separated list start,end,start,end,... timestamps (in seconds) of clips to
             process. The last end timestamp defaults to the end of the file.
             vad_filter will be ignored if clip_timestamps is used.
          hallucination_silence_threshold:
            When word_timestamps is True, skip silent periods longer than this threshold
             (in seconds) when a possible hallucination is detected
          hotwords:
            Hotwords/hint phrases to provide the model with. Has no effect if prefix is not None.
          language_detection_threshold: If the maximum probability of the language tokens is higher
           than this value, the language is detected.
          language_detection_segments: Number of segments to consider for the language detection.
        Returns:
          A tuple with:

            - a generator over transcribed segments
            - an instance of TranscriptionInfo
        '''
        pass
    # WARNING: Decompyle incomplete

    
    def _split_segments_by_timestamps(self, tokenizer, tokens, time_offset = None, segment_size = None, segment_duration = None, seek = ('tokenizer', Tokenizer, 'tokens', List[int], 'time_offset', float, 'segment_size', int, 'segment_duration', float, 'seek', int, 'return', List[List[int]])):
        pass
    # WARNING: Decompyle incomplete

    
    def generate_segments(self, features = None, tokenizer = None, options = None, log_progress = (None,), encoder_output = ('features', np.ndarray, 'tokenizer', Tokenizer, 'options', TranscriptionOptions, 'encoder_output', Optional[ctranslate2.StorageView], 'return', Iterable[Segment])):
        pass
    # WARNING: Decompyle incomplete

    
    def encode(self = None, features = None):
        if self.model.device == 'cuda':
            pass
        to_cpu = len(self.model.device_index) > 1
        if features.ndim == 2:
            features = np.expand_dims(features, 0)
        features = get_ctranslate2_storage(features)
        return self.model.encode(features, to_cpu = to_cpu)

    
    def generate_with_fallback(self, encoder_output = None, prompt = None, tokenizer = None, options = ('encoder_output', ctranslate2.StorageView, 'prompt', List[int], 'tokenizer', Tokenizer, 'options', TranscriptionOptions, 'return', Tuple[(ctranslate2.models.WhisperGenerationResult, float, float, float)])):
        decode_result = None
        all_results = []
        below_cr_threshold_results = []
        max_initial_timestamp_index = int(round(options.max_initial_timestamp / self.time_precision))
    # WARNING: Decompyle incomplete

    
    def get_prompt(self, tokenizer = None, previous_tokens = None, without_timestamps = None, prefix = (False, None, None), hotwords = ('tokenizer', Tokenizer, 'previous_tokens', List[int], 'without_timestamps', bool, 'prefix', Optional[str], 'hotwords', Optional[str], 'return', List[int])):
        prompt = []
        if not (previous_tokens or hotwords) and prefix:
            prompt.append(tokenizer.sot_prev)
            if not hotwords and prefix:
                hotwords_tokens = tokenizer.encode(' ' + hotwords.strip())
                if len(hotwords_tokens) >= self.max_length // 2:
                    hotwords_tokens = hotwords_tokens[:self.max_length // 2 - 1]
                prompt.extend(hotwords_tokens)
            if previous_tokens:
                prompt.extend(previous_tokens[-(self.max_length // 2 - 1):])
        prompt.extend(tokenizer.sot_sequence)
        if without_timestamps:
            prompt.append(tokenizer.no_timestamps)
        if prefix:
            prefix_tokens = tokenizer.encode(' ' + prefix.strip())
            if len(prefix_tokens) >= self.max_length // 2:
                prefix_tokens = prefix_tokens[:self.max_length // 2 - 1]
            if not without_timestamps:
                prompt.append(tokenizer.timestamp_begin)
            prompt.extend(prefix_tokens)
        return prompt

    
    def add_word_timestamps(self, segments, tokenizer, encoder_output, num_frames = None, prepend_punctuations = None, append_punctuations = None, last_speech_timestamp = ('segments', List[dict], 'tokenizer', Tokenizer, 'encoder_output', ctranslate2.StorageView, 'num_frames', int, 'prepend_punctuations', str, 'append_punctuations', str, 'last_speech_timestamp', float, 'return', float)):
        pass
    # WARNING: Decompyle incomplete

    
    def find_alignment(self, tokenizer = None, text_tokens = None, encoder_output = None, num_frames = (7,), median_filter_width = ('tokenizer', Tokenizer, 'text_tokens', List[int], 'encoder_output', ctranslate2.StorageView, 'num_frames', int, 'median_filter_width', int, 'return', List[dict])):
        pass
    # WARNING: Decompyle incomplete

    
    def detect_language(self, audio, features = None, vad_filter = None, vad_parameters = None, language_detection_segments = (None, None, False, None, 1, 0.5), language_detection_threshold = ('audio', Optional[np.ndarray], 'features', Optional[np.ndarray], 'vad_filter', bool, 'vad_parameters', Union[(dict, VadOptions)], 'language_detection_segments', int, 'language_detection_threshold', float, 'return', Tuple[(str, float, List[Tuple[(str, float)]])])):
        '''
        Use Whisper to detect the language of the input audio or features.

        Arguments:
            audio: Input audio signal, must be a 1D float array sampled at 16khz.
            features: Input Mel spectrogram features, must be a float array with
                shape (n_mels, n_frames), if `audio` is provided, the features will be ignored.
                Either `audio` or `features` must be provided.
            vad_filter: Enable the voice activity detection (VAD) to filter out parts of the audio
                without speech. This step is using the Silero VAD model.
            vad_parameters: Dictionary of Silero VAD parameters or VadOptions class (see available
                parameters and default values in the class `VadOptions`).
            language_detection_threshold: If the maximum probability of the language tokens is
                higher than this value, the language is detected.
            language_detection_segments: Number of segments to consider for the language detection.

        Returns:
            language: Detected language.
            language_probability: Probability of the detected language.
            all_language_probs: List of tuples with all language names and probabilities.
        '''
        pass
    # WARNING: Decompyle incomplete



def restore_speech_timestamps(segments = dataclass, speech_chunks = None, sampling_rate = None):
    pass
# WARNING: Decompyle incomplete


def get_ctranslate2_storage(segment = dataclass):
    segment = np.ascontiguousarray(segment)
    segment = ctranslate2.StorageView.from_array(segment)
    return segment


def get_compression_ratio(text = None):
    text_bytes = text.encode('utf-8')
    return len(text_bytes) / len(zlib.compress(text_bytes))


def get_suppressed_tokens(tokenizer = None, suppress_tokens = None):
    if -1 in suppress_tokens:
        suppress_tokens = suppress_tokens()
        suppress_tokens.extend(tokenizer.non_speech_tokens)
# WARNING: Decompyle incomplete


def merge_punctuations(alignment = None, prepended = None, appended = None):
    i = len(alignment) - 2
    j = len(alignment) - 1
# WARNING: Decompyle incomplete
