# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: scene_splitter_service.pyc (Python 3.11)

'''
SceneSplitterService - 챕터를 장면으로 분할하는 서비스

scene_image_service.py에서 추출됨 (Phase 3 리팩토링)
'''
import math
import re
from typing import Any, Dict, List, Tuple
from scene_script_unit_builder import extract_sentence_texts

class SceneSplitterService:
    '''챕터 내용을 장면으로 분할하는 서비스'''
    _BOUNDARY_PATTERNS: Tuple[(Tuple[(re.Pattern[str], str, int)], ...)] = ((re.compile('^(다음\\s*날|그날\\s*밤|그날\\s*저녁|잠시\\s*후|잠시\\s*뒤|잠깐\\s*후|며칠\\s*후|며칠\\s*뒤|이후|그\\s*후|나중에|한편|반면|그러나|하지만|Meanwhile|Later|Afterward|The next day|That night|Hours later)', flags = re.IGNORECASE), 'temporal_or_pov_shift', 4), (re.compile('^(그러던\\s*어느|어느\\s*날|어느\\s*해|그해|사흘\\s*뒤|일주일\\s*뒤|한\\s*달\\s*뒤|몇\\s*달\\s*뒤|몇\\s*년\\s*뒤|.+년이\\s*그렇게\\s*흘|.+년이\\s*지나|.+년\\s*후|.+년\\s*뒤|장례식|그\\s*뒤로|One day|Years later|Months later|Weeks later)', flags = re.IGNORECASE), 'narrative_time_jump', 4), (re.compile('(장면이\\s*바뀌|장소가\\s*바뀌|곳을\\s*옮기|이동한|도착한|떠난|향한|병원|학교|거리|집|사무실|공장|숲|바다|회의실|복도|엘리베이터|장례식장|빈소|내실|부엌|거실|편의점|중환자실|현관|hospital|school|street|home|office|factory|forest|beach|hallway|funeral|kitchen|corridor|lobby)', flags = re.IGNORECASE), 'location_shift', 3), (re.compile('(회상|과거|어린\\s*시절|현재로\\s*돌아|다시\\s*현재|플래시백|flashback|back in|returns? to the present)', flags = re.IGNORECASE), 'temporal_phase_change', 4))
    _SOFT_BREAK_TOKENS = ('그리고', '이어', '이때', '그때', '마침', 'Soon', 'Then', 'At that moment')
    split_chapter_into_equal_sentence_ranges = (lambda chapter_content = None, scene_count = None: sentences = SceneSplitterService._split_text_to_sentences(chapter_content)if not scene_count:
target_count = max(1, int(1))sentence_count = len(sentences)if sentence_count == 0:
effective_content = chapter_content.strip() if chapter_content else ''[
{
'narration': effective_content,
'anchorSentence': effective_content,
'sentenceRange': {
'start': 0,
'end': 0 },
'splitReason': 'empty_content' }]actual_scene_count = None(target_count, sentence_count)base_size = sentence_count // actual_scene_countremainder = sentence_count % actual_scene_countscenes = []start_idx = 0for scene_index in range(actual_scene_count):
segment_size = base_size + 1 if scene_index < remainder else 0end_idx = start_idx + segment_size - 1scenes.append(SceneSplitterService._build_scene_segment(sentences = sentences, start_idx = start_idx, end_idx = end_idx, split_reason = 'deterministic_equal'))start_idx = end_idx + 1scenes)()
    split_chapter_into_scenes = (lambda chapter_content = None, scene_count = None: sentences = SceneSplitterService._split_text_to_sentences(chapter_content)sentence_count = len(sentences)if not scene_count:
target_count = max(1, int(1))if sentence_count == 0:
effective_content = chapter_content.strip() if chapter_content else ''[
{
'narration': effective_content,
'anchorSentence': effective_content,
'sentenceRange': {
'start': 0,
'end': 0 },
'splitReason': 'empty_content' }]if None == 1:
[
{
'narration': sentences[0],
'anchorSentence': sentences[0],
'sentenceRange': {
'start': 0,
'end': 0 },
'splitReason': 'single_sentence' }]if None <= target_count:
enumerate(sentences)()desired_scene_size = None(2, math.ceil(sentence_count / max(1, target_count)))max_scene_size = max(desired_scene_size + 1, 4)scenes = []scene_start = 0last_split_reason = 'soft_target'for idx in range(1, sentence_count):
if len(scenes) >= target_count - 1:
passelse:
(boundary_score, boundary_reason) = SceneSplitterService._score_boundary(sentences[idx - 1], sentences[idx])current_scene_size = idx - scene_startremaining_sentences = sentence_count - idxremaining_scene_slots = max(0, target_count - len(scenes) - 1)should_split = Falsesplit_reason = 'soft_target'if boundary_score >= 4 and current_scene_size >= 1:
should_split = Trueif not boundary_reason:
split_reason = 'semantic_boundary'elif boundary_score >= 2 and current_scene_size >= desired_scene_size:
should_split = Trueif not boundary_reason:
split_reason = 'semantic_boundary'elif current_scene_size >= max_scene_size:
should_split = Truesplit_reason = 'soft_target'elif current_scene_size >= desired_scene_size and remaining_scene_slots > 0 and remaining_sentences >= 1:
should_split = Truesplit_reason = 'soft_target'if not should_split:
continuescenes.append(SceneSplitterService._build_scene_segment(sentences = sentences, start_idx = scene_start, end_idx = idx - 1, split_reason = split_reason))scene_start = idxlast_split_reason = split_reasonscenes.append(SceneSplitterService._build_scene_segment(sentences = sentences, start_idx = scene_start, end_idx = sentence_count - 1, split_reason = last_split_reason if scenes else 'full_pass'))scenes)()
    _build_scene_segment = (lambda *: scene_sentences = sentences[start_idx:end_idx + 1]narration = ' '.join(scene_sentences).strip()anchor_sentence = scene_sentences[0] if scene_sentences else ''{
'narration': narration,
'anchorSentence': anchor_sentence,
'sentenceRange': {
'start': start_idx,
'end': end_idx },
'splitReason': split_reason })()
    _score_boundary = (lambda previous_sentence = None, next_sentence = None: pass# WARNING: Decompyle incomplete
)()
    _split_text_to_sentences = (lambda text = None: if not text:
[]None(text))()
    estimate_scene_split_max_tokens = (lambda chapter_content = None, target_scene_count = None, is_informational = staticmethod, model_type = ('standard',): if not chapter_content:
content_len = len('')if not target_scene_count:
scene_count = max(1, int(1))base_tokens = 8000 if is_informational else 10000content_tokens = int(content_len * 0.25 if is_informational else 0.35)scene_tokens = scene_count * 1500 if is_informational else 2000estimated = base_tokens + content_tokens + scene_tokensupper_bound = 80000 if model_type == 'pro-hq' else 65000max(15000, min(upper_bound, estimated)))()
    build_scene_summary_from_text = (lambda text = None, max_len = None: if not text:
''first_sentence = None._split_text_to_sentences(text)summary = first_sentence[0] if first_sentence else text.strip()summary[:max_len])()


def split_chapter_into_scenes(chapter_content = None, scene_count = None):
    '''챕터 내용을 자연 경계 중심으로 분할

    SceneSplitterService.split_chapter_into_scenes()의 단축 함수
    '''
    return SceneSplitterService.split_chapter_into_scenes(chapter_content, scene_count)


def estimate_scene_split_max_tokens(chapter_content = None, target_scene_count = None, is_informational = None, model_type = ('standard',)):
    '''챕터 길이/씬 수 기반 동적 토큰 예산 계산

    SceneSplitterService.estimate_scene_split_max_tokens()의 단축 함수
    '''
    return SceneSplitterService.estimate_scene_split_max_tokens(chapter_content, target_scene_count, is_informational, model_type)
