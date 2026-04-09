# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: cd.pyc (Python 3.11)

from __future__ import annotations
import importlib
from codecs import IncrementalDecoder
from collections import Counter
from functools import lru_cache
from typing import Counter as TypeCounter
from constant import FREQUENCIES, KO_NAMES, LANGUAGE_SUPPORTED_COUNT, TOO_SMALL_SEQUENCE, ZH_NAMES
from md import is_suspiciously_successive_range
from models import CoherenceMatches
from utils import is_accentuated, is_latin, is_multi_byte_encoding, is_unicode_range_secondary, unicode_range

def encoding_unicode_range(iana_name = None):
    '''
    Return associated unicode ranges in a single byte code page.
    '''
    pass
# WARNING: Decompyle incomplete


def unicode_range_languages(primary_range = None):
    '''
    Return inferred languages used with a unicode range.
    '''
    languages = []
    for language, characters in FREQUENCIES.items():
        for character in characters:
            if unicode_range(character) == primary_range:
                languages.append(language)
            
            return languages

encoding_languages = (lambda iana_name = None: unicode_ranges = encoding_unicode_range(iana_name)primary_range = None# WARNING: Decompyle incomplete
)()
mb_encoding_languages = (lambda iana_name = None: if iana_name.startswith('shift_') and iana_name.startswith('iso2022_jp') and iana_name.startswith('euc_j') or iana_name == 'cp932':
[
'Japanese']if None.startswith('gb') or iana_name in ZH_NAMES:
[
'Chinese']if None.startswith('iso2022_kr') or iana_name in KO_NAMES:
[
'Korean'])()
get_target_features = (lambda language = None: target_have_accents = Falsetarget_pure_latin = Truefor character in FREQUENCIES[language]:
if target_have_accents and is_accentuated(character):
target_have_accents = Trueif target_pure_latin and is_latin(character) is False:
target_pure_latin = False(target_have_accents, target_pure_latin))()

def alphabet_languages(characters = None, ignore_non_latin = None):
    '''
    Return associated languages associated to given characters.
    '''
    pass
# WARNING: Decompyle incomplete


def characters_popularity_compare(language = None, ordered_characters = None):
    '''
    Determine if a ordered characters list (by occurrence from most appearance to rarest) match a particular language.
    The result is a ratio between 0. (absolutely no correspondence) and 1. (near perfect fit).
    Beware that is function is not strict on the match in order to ease the detection. (Meaning close match is 1.)
    '''
    if language not in FREQUENCIES:
        raise ValueError(f'''{language} not available''')
    character_approved_count = 0
    FREQUENCIES_language_set = set(FREQUENCIES[language])
    ordered_characters_count = len(ordered_characters)
    target_language_characters_count = len(FREQUENCIES[language])
    large_alphabet = target_language_characters_count > 26
    for character, character_rank in zip(ordered_characters, range(0, ordered_characters_count)):
        if character not in FREQUENCIES_language_set:
            continue
        character_rank_in_language = FREQUENCIES[language].index(character)
        expected_projection_ratio = target_language_characters_count / ordered_characters_count
        character_rank_projection = int(character_rank * expected_projection_ratio)
        if large_alphabet is False and abs(character_rank_projection - character_rank_in_language) > 4:
            continue
        if large_alphabet is True and abs(character_rank_projection - character_rank_in_language) < target_language_characters_count / 3:
            character_approved_count += 1
            continue
        characters_before_source = FREQUENCIES[language][0:character_rank_in_language]
        characters_after_source = FREQUENCIES[language][character_rank_in_language:]
        characters_before = ordered_characters[0:character_rank]
        characters_after = ordered_characters[character_rank:]
        before_match_count = len(set(characters_before) & set(characters_before_source))
        after_match_count = len(set(characters_after) & set(characters_after_source))
        if len(characters_before_source) == 0 and before_match_count <= 4:
            character_approved_count += 1
            continue
        if len(characters_after_source) == 0 and after_match_count <= 4:
            character_approved_count += 1
            continue
        if before_match_count / len(characters_before_source) >= 0.4 or after_match_count / len(characters_after_source) >= 0.4:
            character_approved_count += 1
            continue
        return character_approved_count / len(ordered_characters)


def alpha_unicode_split(decoded_sequence = None):
    '''
    Given a decoded text sequence, return a list of str. Unicode range / alphabet separation.
    Ex. a text containing English/Latin with a bit a Hebrew will return two items in the resulting list;
    One containing the latin letters and the other hebrew.
    '''
    layers = { }
# WARNING: Decompyle incomplete


def merge_coherence_ratios(results = None):
    '''
    This function merge results previously given by the function coherence_ratio.
    The return type is the same as coherence_ratio.
    '''
    pass
# WARNING: Decompyle incomplete


def filter_alt_coherence_matches(results = None):
    '''
    We shall NOT return "English—" in CoherenceMatches because it is an alternative
    of "English". This function only keeps the best match and remove the em-dash in it.
    '''
    pass
# WARNING: Decompyle incomplete

coherence_ratio = (lambda decoded_sequence = None, threshold = None, lg_inclusion = lru_cache(maxsize = 2048): results = []ignore_non_latin = Falsesufficient_match_count = 0# WARNING: Decompyle incomplete
)()
