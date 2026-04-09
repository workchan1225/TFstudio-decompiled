# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: scene_staging_plan.pyc (Python 3.11)

from __future__ import annotations
import re
from typing import Any, Dict, List, Optional
from scene_semantic_contract import resolve_scene_semantic_contract
_TENSION_PATTERN = re.compile('\\b(?:panic|danger|risk|storm|flood|threat|urgent|tense|fear|warning|attack|chase|escape|rescue|bind(?:s|ing)?|chain(?:s|ed)?|drag(?:s|ging)?|pull(?:s|ing)?|restrain(?:s|ed|ing)?)\\b|(?:긴장|위험|위기|태풍|홍수|위협|공포|불안|패닉|경고|공격|추격|탈출|구조|쇠사슬|묶|결박|끌|붙잡)', re.IGNORECASE)
_RELIEF_PATTERN = re.compile('\\b(?:relief|comfort|reassure|safe|survive|recover|calm|embrace|hug)\\b|(?:안도|안심|안정|위로|진정|안전|살아남|회복|포옹|껴안)', re.IGNORECASE)
_CONFRONTATION_PATTERN = re.compile('\\b(?:argu(?:e|ing)|confront|oppose|challenge|fight|debate)\\b|(?:논쟁|대치|맞서|충돌|싸우|반박)', re.IGNORECASE)
_EXPLANATION_PATTERN = re.compile('\\b(?:explain|presentation|briefing|lecture|teach|point(?:ing)? to|show(?:ing)?)\\b|(?:설명|발표|브리핑|강의|가르치|가리키|보여주)', re.IGNORECASE)
_RECIPROCAL_EXCHANGE_PATTERN = re.compile('\\b(?:talk(?:s|ing)?|speak(?:s|ing)?|conversation|dialogue|exchange(?:s|ing)?|look(?:s|ing)? at each other|face(?:s|ing)? each other|toward each other|listen(?:s|ing)? to|comfort(?:s|ing)?|console(?:s|ing)?|rebuttal)\\b|(?:서로|마주보|대화|주고받|응답|반박|위로|달래|듣고)', re.IGNORECASE)
_GENERIC_ENVIRONMENT_EYELINE = re.compile('\\b(?:distant|mountain|horizon|sky|landscape|far|panorama)\\b|(?:먼|산|지평선|하늘|풍경)', re.IGNORECASE)
_DIALOGUE_SCENE_FAMILIES = {
    'character_relation',
    'emotion_reaction'}
_DIALOGUE_BLOCKED_EYELINE_MARKERS = ('evidence surface', 'audience', 'primary presenter')
_DIALOGUE_BLOCKED_POSE_MARKERS = ('presenting', 'explanation gesture', 'deliver information')
_DIALOGUE_BLOCKED_ORIENTATION_MARKERS = ('toward evidence', 'focal presenter')
_DRAG_ABDUCTION_PATTERN = re.compile('\\b(?:drag(?:s|ged|ging)?|abduct(?:s|ed|ing)?|pull(?:s|ed|ing)?\\s+away|lead(?:s|ing)?\\s+away|taken\\s+away|carry\\s+off|haul(?:s|ed|ing)?)\\b|(?:끌려[가간]|끌고\\s*[가간나]|잡아끌|데려[가간]|끌어내|이끌고|납치|강제로\\s*[데끌])', re.IGNORECASE)
_SUPERNATURAL_PATTERN = re.compile('\\b(?:demon|ghost|spirit|reaper|supernatural|monster|creature|apparition|evil\\s+spirit|dark\\s+force|undead|phantom|specter)\\b|(?:악귀|귀신|저승사자|사신|요괴|괴물|망령|혼령|원귀|악령|어둠의\\s*[힘존])', re.IGNORECASE)
_AWAKENING_BATTLE_PATTERN = re.compile('\\b(?:awaken(?:s|ed|ing)?|unleash(?:es|ed|ing)?|final\\s+(?:battle|stand|fight)|showdown|decisive|power\\s+up|transform(?:s|ed|ing)?|rise(?:s|d)?\\s+(?:up|against))\\b|(?:각성|결전|최후|결투|대결|힘을\\s*[깨모폭]|변신|일어서|맞서\\s*싸우|폭발)', re.IGNORECASE)
_WITNESS_OBSERVATION_PATTERN = re.compile('\\b(?:witness(?:es|ing)?|watch(?:es|ing)?\\s+from|observe(?:s|d|ing)?\\s+from|onlooker|bystander|from\\s+(?:afar|a\\s+distance|the\\s+(?:crowd|doorway|background)))\\b|(?:지켜보|목격|멀리서|바라보|구경|먼발치|뒤에서\\s*[보바]|문틈|문가에서)', re.IGNORECASE)
_EMOTIONAL_PARTING_PATTERN = re.compile('\\b(?:farewell|goodbye|part(?:s|ed|ing)\\s+ways?|leave(?:s|ing)?\\s+behind|walk(?:s|ing)?\\s+away|turn(?:s|ed|ing)?\\s+(?:away|back)|disappear(?:s|ed|ing)?)\\b|(?:이별|작별|헤어[지짐]|돌아[보서]|사라[지짐진]|떠나|뒤돌아|등을\\s*[돌보]|마지막으로)', re.IGNORECASE)

def _normalize_text(value = None):
