# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: api.pyc (Python 3.11)

from __future__ import annotations
import logging
from os import PathLike
from typing import BinaryIO
from cd import coherence_ratio, encoding_languages, mb_encoding_languages, merge_coherence_ratios
from constant import IANA_SUPPORTED, TOO_BIG_SEQUENCE, TOO_SMALL_SEQUENCE, TRACE
from md import mess_ratio
from models import CharsetMatch, CharsetMatches
from utils import any_specified_encoding, cut_sequence_chunks, iana_name, identify_sig_or_bom, is_cp_similar, is_multi_byte_encoding, should_strip_sig_or_bom
logger = logging.getLogger('charset_normalizer')
explain_handler = logging.StreamHandler()
explain_handler.setFormatter(logging.Formatter('%(asctime)s | %(levelname)s | %(message)s'))

def from_bytes(sequences, steps, chunk_size, threshold, cp_isolation, cp_exclusion = None, preemptive_behaviour = None, explain = None, language_threshold = (5, 512, 0.2, None, None, True, False, 0.1, True), enable_fallback = ('sequences', 'bytes | bytearray', 'steps', 'int', 'chunk_size', 'int', 'threshold', 'float', 'cp_isolation', 'list[str] | None', 'cp_exclusion', 'list[str] | None', 'preemptive_behaviour', 'bool', 'explain', 'bool', 'language_threshold', 'float', 'enable_fallback', 'bool', 'return', 'CharsetMatches')):
    """
    Given a raw bytes sequence, return the best possibles charset usable to render str objects.
    If there is no results, it is a strong indicator that the source is binary/not text.
    By default, the process will extract 5 blocks of 512o each to assess the mess and coherence of a given sequence.
    And will give up a particular code page after 20% of measured mess. Those criteria are customizable at will.

    The preemptive behavior DOES NOT replace the traditional detection workflow, it prioritize a particular code page
    but never take it for granted. Can improve the performance.

    You may want to focus your attention to some code page or/and not others, use cp_isolation and cp_exclusion for that
    purpose.

    This function will strip the SIG in the payload/sequence every time except on UTF-16, UTF-32.
    By default the library does not setup any handler other than the NullHandler, if you choose to set the 'explain'
    toggle to True it will alter the logger configuration to add a StreamHandler that is suitable for debugging.
    Custom logging format and handler can be set manually.
    """
    if not isinstance(sequences, (bytearray, bytes)):
        raise TypeError('Expected object of type bytes or bytearray, got: {}'.format(type(sequences)))
    if explain:
        previous_logger_level = logger.level
        logger.addHandler(explain_handler)
        logger.setLevel(TRACE)
    length = len(sequences)
# WARNING: Decompyle incomplete


def from_fp(fp, steps, chunk_size, threshold, cp_isolation, cp_exclusion = None, preemptive_behaviour = None, explain = None, language_threshold = (5, 512, 0.2, None, None, True, False, 0.1, True), enable_fallback = ('fp', 'BinaryIO', 'steps', 'int', 'chunk_size', 'int', 'threshold', 'float', 'cp_isolation', 'list[str] | None', 'cp_exclusion', 'list[str] | None', 'preemptive_behaviour', 'bool', 'explain', 'bool', 'language_threshold', 'float', 'enable_fallback', 'bool', 'return', 'CharsetMatches')):
    '''
    Same thing than the function from_bytes but using a file pointer that is already ready.
    Will not close the file pointer.
    '''
    return from_bytes(fp.read(), steps, chunk_size, threshold, cp_isolation, cp_exclusion, preemptive_behaviour, explain, language_threshold, enable_fallback)


def from_path(path, steps, chunk_size, threshold, cp_isolation, cp_exclusion = None, preemptive_behaviour = None, explain = None, language_threshold = (5, 512, 0.2, None, None, True, False, 0.1, True), enable_fallback = ('path', 'str | bytes | PathLike', 'steps', 'int', 'chunk_size', 'int', 'threshold', 'float', 'cp_isolation', 'list[str] | None', 'cp_exclusion', 'list[str] | None', 'preemptive_behaviour', 'bool', 'explain', 'bool', 'language_threshold', 'float', 'enable_fallback', 'bool', 'return', 'CharsetMatches')):
    '''
    Same thing than the function from_bytes but with one extra step. Opening and reading given file path in binary mode.
    Can raise IOError.
    '''
    fp = open(path, 'rb')
    None(None, None)
    return 
    with None:
        if not None, from_fp(fp, steps, chunk_size, threshold, cp_isolation, cp_exclusion, preemptive_behaviour, explain, language_threshold, enable_fallback):
            pass


def is_binary(fp_or_path_or_payload, steps, chunk_size, threshold, cp_isolation, cp_exclusion = None, preemptive_behaviour = None, explain = None, language_threshold = (5, 512, 0.2, None, None, True, False, 0.1, False), enable_fallback = ('fp_or_path_or_payload', 'PathLike | str | BinaryIO | bytes', 'steps', 'int', 'chunk_size', 'int', 'threshold', 'float', 'cp_isolation', 'list[str] | None', 'cp_exclusion', 'list[str] | None', 'preemptive_behaviour', 'bool', 'explain', 'bool', 'language_threshold', 'float', 'enable_fallback', 'bool', 'return', 'bool')):
    '''
    Detect if the given input (file, bytes, or path) points to a binary file. aka. not a string.
    Based on the same main heuristic algorithms and default kwargs at the sole exception that fallbacks match
    are disabled to be stricter around ASCII-compatible but unlikely to be a string.
    '''
    if isinstance(fp_or_path_or_payload, (str, PathLike)):
        guesses = from_path(fp_or_path_or_payload, steps = steps, chunk_size = chunk_size, threshold = threshold, cp_isolation = cp_isolation, cp_exclusion = cp_exclusion, preemptive_behaviour = preemptive_behaviour, explain = explain, language_threshold = language_threshold, enable_fallback = enable_fallback)
    elif isinstance(fp_or_path_or_payload, (bytes, bytearray)):
        guesses = from_bytes(fp_or_path_or_payload, steps = steps, chunk_size = chunk_size, threshold = threshold, cp_isolation = cp_isolation, cp_exclusion = cp_exclusion, preemptive_behaviour = preemptive_behaviour, explain = explain, language_threshold = language_threshold, enable_fallback = enable_fallback)
    else:
        guesses = from_fp(fp_or_path_or_payload, steps = steps, chunk_size = chunk_size, threshold = threshold, cp_isolation = cp_isolation, cp_exclusion = cp_exclusion, preemptive_behaviour = preemptive_behaviour, explain = explain, language_threshold = language_threshold, enable_fallback = enable_fallback)
    return not guesses
