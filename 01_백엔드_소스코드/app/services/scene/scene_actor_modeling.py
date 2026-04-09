# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: scene_actor_modeling.pyc (Python 3.11)

'''
Generalized scene actor modeling utilities.

Separates registered character binding from visible actor composition so that
scene staging can preserve non-registered relational/group/background actors.
'''
from __future__ import annotations
import re
from typing import Any, Dict, List, Optional, Sequence
from utils.character_name_matcher import build_exact_character_identity_map, normalize_character_name
from scene_framing_policy import build_scene_framing_policy
_ACTOR_TYPE_PRIORITY = {
    'registered_character': 6,
    'unregistered_named_actor': 5,
    'relational_role_actor': 4,
    'occupational_or_social_role_actor': 3,
    'group_actor': 2,
    'crowd_actor': 1,
    'background_actor': 0 }
_IMPORTANCE_PRIORITY = {
    'primary': 2,
    'secondary': 1,
    'background': 0 }
_COUNT_PRIORITY = {
    '1': 0,
    '2': 1,
    'few': 2,
    'many': 3,
    'crowd': 4 }
_COUNT_TO_APPROX = {
    '1': 1,
    '2': 2,
    'few': 3,
    'many': 5,
    'crowd': 8 }
_CORE_SUPPORTING_ACTOR_TYPES = {
    'relational_role_actor',
    'unregistered_named_actor',
    'occupational_or_social_role_actor'}
_BACKGROUND_EXTRA_ACTOR_TYPES = {
    'crowd_actor',
    'group_actor',
    'background_actor'}
_ACTOR_LABEL_TRAILING_STOPWORDS = {
    'in',
    'her',
    'his',
    'from',
    'kill',
    'near',
    'raid',
    'with',
    'fight',
    'guide',
    'kills',
    'raids',
    'react',
    'teach',
    'their',
    'watch',
    'while',
    'around',
    'attack',
    'behind',
    'beside',
    'fights',
    'guides',
    'reacts',
    'attacks',
    'correct',
    'guiding',
    'plunder',
    'support',
    'teaches',
    'watches',
    'corrects',
    'opposite',
    'plunders',
    'reacting',
    'supports',
    'teaching',
    'watching',
    'background',
    'correcting',
    'foreground',
    'plundering',
    'supporting'}
_ACTOR_LABEL_LEADING_STOPWORDS = {
    '또',
    '그때',
    '이후',
    '직후',
    '한편',
    '그동안',
    '그러나',
    '그리고',
    '동시에',
    '뒤에서',
    '앞에서',
    '옆에서',
    '배경에서',
    'as',
    'at',
    'by',
    'in',
    'on',
    'and',
    'but',
    'from',
    'into',
    'near',
    'when',
    'with',
    'after',
    'while',
    'across',
    'around',
    'before',
    'behind',
    'beside',
    'during',
    'inside',
    'outside',
    'through',
    'without',
    'opposite'}
_PLACEMENT_PATTERNS = (('layered_depth', re.compile('\\b(?:layered|staggered|depth|across the frame)\\b|층위|겹쳐|깊이', re.IGNORECASE)), ('dispersed', re.compile('\\b(?:surrounding|around|across|spread|scattered|throughout)\\b|둘러싸|흩어|주변', re.IGNORECASE)), ('background', re.compile('\\b(?:background|behind|rear|distance|far back)\\b|배경|뒤|멀리|후방', re.IGNORECASE)), ('foreground', re.compile('\\b(?:foreground|front|near camera|close to camera)\\b|전경|앞', re.IGNORECASE)), ('midground', re.compile('\\b(?:midground|middle distance)\\b|중경', re.IGNORECASE)), ('left', re.compile('\\bleft\\b|왼쪽', re.IGNORECASE)), ('right', re.compile('\\bright\\b|오른쪽', re.IGNORECASE)), ('center', re.compile('\\bcenter\\b|중앙', re.IGNORECASE)))
_BACKGROUND_HINT_PATTERN = re.compile('\\b(?:background|behind|rear|distance|far back|bystander)\\b|배경|뒤|멀리|후방', re.IGNORECASE)
_SPATIAL_ACTOR_CUE_PATTERN = re.compile('\\b(?:foreground|background|behind|opposite|around|surround(?:ing)?|beside|next to|in front of|near|across from|watching from)\\b|(?:전경|배경|뒤|반대편|주변|둘러싸|곁|옆|앞|맞은편)', re.IGNORECASE)
_INTERACTION_CUE_PATTERN = re.compile('\\b(?:guid(?:e|es|ing|ance)|teach(?:es|ing)?|correct(?:s|ing)?|support(?:s|ing)?|confront(?:s|ing)?|attack(?:s|ing)?|fight(?:s|ing)?|watch(?:es|ing)?|react(?:s|ing)?|protect(?:s|ing)?|kill(?:s|ing)?|threaten(?:s|ing)?)\\b|(?:가르치|지도|교정|바로잡|도와|지원|대치|공격|싸우|지켜보|반응|보호|죽이|위협)', re.IGNORECASE)
_ENGLISH_RELATIONAL_ROLE_TERMS = ('father', 'mother', 'dad', 'mom', 'parent', 'son', 'daughter', 'brother', 'sister', 'wife', 'husband', 'teacher', 'mentor', 'master', 'guardian', 'friend', 'boss', 'chief', 'leader', 'child', 'children', 'coach', 'partner', 'classmate', 'colleague', 'assistant', 'student')
_KOREAN_RELATIONAL_ROLE_TERMS = ('아버지', '어머니', '엄마', '아빠', '부친', '모친', '부모', '아들', '딸', '형', '오빠', '누나', '언니', '동생', '남편', '아내', '스승', '사부', '제자', '친구', '상관', '부하', '보호자', '선생', '아이', '자식', '코치', '동료', '조수', '학생', '멘토')
_RELATIONAL_PATTERN = '|'.join + (lambda .0: pass# WARNING: Decompyle incomplete
)(_ENGLISH_RELATIONAL_ROLE_TERMS()) + ')\\b)|(?:[가-힣A-Za-z0-9@][^,.;:!?()\\n]{0,16}?의\\s*(?:'('|'.join + (lambda .0: pass# WARNING: Decompyle incomplete
)(_KOREAN_RELATIONAL_ROLE_TERMS()) + '))')
_POSSESSIVE_RELATION_PATTERN = re.compile('\\b(?:his|her|their)\\s+(?:father|mother|dad|mom|parent|son|daughter|brother|sister|wife|husband|teacher|mentor|master|guardian|friend|boss|chief|leader|child|children)\\b', re.IGNORECASE)
_ENGLISH_QUANTIFIED_PATTERN = re.compile('\\b(?:one|two|three|four|five|\\d+|few|several|many|multiple|pair(?:\\s+of)?|group(?:\\s+of)?|dozens?\\s+of|scores?\\s+of|crowd(?:\\s+of)?)\\s+[A-Za-z][^,.;:!?()\\n]{0,28}', re.IGNORECASE)
_KOREAN_QUANTIFIED_PATTERN = re.compile('(?:여러|몇몇|많은|수많은|한\\s*무리의|무리의|\\d+\\s*명(?:의)?)\\s*[가-힣][^,.;:!?()\\n]{0,20}')
_ENGLISH_ARTICLE_ACTOR_PATTERN = re.compile('\\b(a|an|the|his|her|their|another)\\s+((?:[A-Za-z-]+\\s+){0,2}[A-Za-z-]+)(?=\\s+(?:(?:[A-Za-z-]+\\s+){0,2})?(?:stands?|sits?|walks?|runs?|holds?|watches?|looks?|speaks?|says?|turns?|guides?|helps?|supports?|corrects?|follows?|approaches?|reacts?|points?|kneels?|embraces?|fights?|waits?|moves?|gestures?|observes?|teaches?|protects?|attacks?|kills?|plunders?|raids?|background|foreground|behind|around|opposite|beside|near|with|surrounding))', re.IGNORECASE)

def _normalize_text(value = None):
