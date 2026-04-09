# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: scene_expression_plan.pyc (Python 3.11)

from __future__ import annotations
import re
from typing import Any, Dict, List, Optional
from scene_semantic_contract import resolve_scene_semantic_contract
_TENSION_PATTERN = re.compile('\\b(?:panic|danger|risk|storm|flood|threat|urgent|tense|fear|warning|attack|bind(?:s|ing)?|chain(?:s|ed)?|drag(?:s|ging)?|pull(?:s|ing)?|restrain(?:s|ed|ing)?|capture(?:s|d|ing)?|seize(?:s|d|ing)?)\\b|(?:긴장|위험|위기|태풍|홍수|위협|공포|불안|패닉|경고|공격|쇠사슬|묶|결박|끌|잡아끌|붙잡|체포)', re.IGNORECASE)
_RELIEF_PATTERN = re.compile('\\b(?:relief|comfort|reassure|safe|survive|recover|calm)\\b|(?:안도|안심|안정|위로|진정|안전|살아남|회복)', re.IGNORECASE)
_CONFRONTATION_PATTERN = re.compile('\\b(?:argu(?:e|ing)|confront|oppose|challenge|fight|debate)\\b|(?:논쟁|대치|맞서|충돌|싸우|반박)', re.IGNORECASE)
_EXPLANATION_PATTERN = re.compile('\\b(?:explain|presentation|briefing|lecture|teach|point(?:ing)? to|show(?:ing)?)\\b|(?:설명|발표|브리핑|강의|가르치|가리키|보여주)', re.IGNORECASE)
_RECIPROCAL_EXCHANGE_PATTERN = re.compile('\\b(?:talk(?:s|ing)?|speak(?:s|ing)?|conversation|dialogue|exchange(?:s|ing)?|look(?:s|ing)? at each other|face(?:s|ing)? each other|toward each other|listen(?:s|ing)? to|comfort(?:s|ing)?|console(?:s|ing)?|rebuttal)\\b|(?:서로|마주보|대화|주고받|응답|반박|위로|달래|듣고)', re.IGNORECASE)
_REACTION_OBSERVATION_PATTERN = re.compile('\\b(?:watch(?:es|ing)?|observe(?:s|d|ing)?|witness(?:es|ing)?|look(?:s|ing)? back|glance(?:s|d|ing)? back|stare(?:s|d|ing)?|sit(?:s|ting)? quietly|helpless(?:ly)?|trembl(?:e|es|ing)|worr(?:y|ied|ying)|anxious|despair|silent|quietly|in the background|in the foreground|near the doorway|through the doorway|behind|from the doorway)\\b|(?:지켜보|바라보|돌아보|응시|떨|걱정|불안|망연|조용히|배경|전경|문가|문틈|뒤에서|뒤편)', re.IGNORECASE)
_DIALOGUE_SCENE_FAMILIES = {
    'character_relation',
    'emotion_reaction'}

def _normalize_text(value = None):
