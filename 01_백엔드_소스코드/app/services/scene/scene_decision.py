# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: scene_decision.pyc (Python 3.11)

from __future__ import annotations
from copy import deepcopy
from typing import Any, Dict, Iterable, List, Optional
GENRE_PROFILE_REGISTRY: 'Dict[str, Dict[str, Any]]' = {
    'drama': {
        'genreName': 'dramatic',
        'genreBucket': 'narrative',
        'preferredFamilies': [
            'character_relation',
            'emotion_reaction',
            'response_action'] },
    'thriller': {
        'genreName': 'thriller',
        'genreBucket': 'narrative',
        'preferredFamilies': [
            'response_action',
            'event_observation',
            'evidence_explanation'] },
    'documentary': {
        'genreName': 'documentary',
        'genreBucket': 'informational',
        'preferredFamilies': [
            'event_observation',
            'evidence_explanation',
            'environment_context'] },
    'news': {
        'genreName': 'news',
        'genreBucket': 'informational',
        'preferredFamilies': [
            'event_observation',
            'evidence_explanation',
            'comparison'] },
    'info': {
        'genreName': 'informational',
        'genreBucket': 'informational',
        'preferredFamilies': [
            'evidence_explanation',
            'comparison',
            'environment_context'] },
    'informational': {
        'genreName': 'informational',
        'genreBucket': 'informational',
        'preferredFamilies': [
            'evidence_explanation',
            'comparison',
            'environment_context'] },
    'education': {
        'genreName': 'educational',
        'genreBucket': 'informational',
        'preferredFamilies': [
            'evidence_explanation',
            'comparison',
            'character_relation'] } }
NARRATIVE_GENRE_KEYS: 'frozenset[str]' = (lambda .0: pass# WARNING: Decompyle incomplete
)(GENRE_PROFILE_REGISTRY.items()())
SCENE_FAMILY_REGISTRY: 'Dict[str, Dict[str, Any]]' = {
    'event_observation': {
        'slot_keys': ('event', 'threat', 'result'),
        'default_mode': 'event_first',
        'human_required': False },
    'environment_context': {
        'slot_keys': ('environment', 'space', 'time'),
        'default_mode': 'environment_first',
        'human_required': False },
    'evidence_explanation': {
        'slot_keys': ('evidence', 'cause', 'result'),
        'default_mode': 'evidence_first',
        'human_required': False },
    'comparison': {
        'slot_keys': ('comparison', 'evidence', 'result'),
        'default_mode': 'comparison_first',
        'human_required': False },
    'character_relation': {
        'slot_keys': ('subject', 'relation', 'emotion'),
        'default_mode': 'relation_first',
        'human_required': True },
    'emotion_reaction': {
        'slot_keys': ('emotion', 'reaction', 'subject'),
        'default_mode': 'character_first',
        'human_required': True },
    'response_action': {
        'slot_keys': ('subject', 'action', 'threat'),
        'default_mode': 'event_first',
        'human_required': True },
    'explainer_scene': {
        'slot_keys': ('presentation', 'subject', 'evidence'),
        'default_mode': 'narration_support_first',
        'human_required': True } }
NONHUMAN_SCENE_FAMILIES = {
    'comparison',
    'event_observation',
    'environment_context',
    'evidence_explanation'}
STYLE_MODE_RENDER_MAP = {
    'animation': 'stylized_animation',
    'illustration': 'stylized_illustration',
    'traditional': 'stylized_traditional',
    'informational': 'stylized_informational',
    'realistic': 'realistic' }
SEMANTIC_SLOT_MARKERS: 'Dict[str, tuple[str, ...]]' = {
    'event': ('태풍', '폭우', '홍수', '재난', '붕괴', '침수', '사고', '충돌', 'storm', 'flood', 'disaster', 'collapse', 'accident', 'explosion', 'damage'),
    'environment': ('도시', '거리', '도심', '바다', '해안', '건물', '실내', '사무실', '회의실', '교실', 'city', 'street', 'office', 'meeting room', 'classroom', 'harbor', 'coast', 'room'),
    'evidence': ('증거', '수치', '데이터', '차트', '그래프', '지도', '문서', '지표', 'monitor', 'screen', 'chart', 'graph', 'data', 'evidence', 'document', 'report'),
    'comparison': ('비교', '전후', '차이', '대비', 'versus', 'compare', 'comparison', 'before', 'after'),
    'cause': ('원인', '이유', '때문', 'because', 'cause', 'reason'),
    'result': ('결과', '영향', '피해', '증가', '감소', 'result', 'impact', 'damage', 'rise', 'drop'),
    'subject': ('@', '그', '그녀', '그들', '인물', '캐릭터', '사람', 'woman', 'man', 'character', 'teacher', 'doctor', 'family', '아이', '할머니', '할아버지'),
    'relation': ('함께', '마주', '포옹', '대화', '관계', '가족', 'friend', 'together', 'embrace', 'conversation', 'relationship'),
    'emotion': ('감정', '눈물', '기쁨', '분노', '슬픔', '불안', '행복', 'sad', 'angry', 'joy', 'fear', 'tears', 'relief'),
    'reaction': ('반응', '응시', '돌아보', '움츠', '놀라', 'reaction', 'flinch', 'stare', 'recoil'),
    'action': ('달리', '걷', '붙잡', '안아', '싸우', '구조', 'point', 'run', 'walk', 'hold', 'rescue'),
    'threat': ('위협', '위기', '경고', 'risk', 'danger', 'warning', 'threat', 'panic'),
    'time': ('새벽', '밤', '오후', '아침', 'dawn', 'night', 'afternoon', 'morning'),
    'presentation': ('발표', '브리핑', '설명자', '강의', 'teacher', 'presenter', 'briefing', 'lecture', 'speaker', 'analyst') }
TEMPLATE_PENALTY_MARKERS: 'Dict[str, tuple[str, ...]]' = {
    'presenter_screen': ('발표', '브리핑', '프레젠테이션', 'monitor', 'screen', 'chart', 'graph', 'presenter', 'briefing'),
    'meeting_room': ('회의실', '사무실', 'boardroom', 'meeting room', 'office', 'conference room'),
    'static_single_portrait': ('정면', '단독', 'single portrait', 'standing alone', 'front-facing') }
GENERIC_ROLE_LABEL_MARKERS: 'tuple[str, ...]' = ('expert', 'presenter', 'analyst', 'narrator', 'speaker', 'guide', 'host', 'reporter', 'teacher', 'doctor', 'official', 'worker', 'commentator', 'anchor', 'resident', 'residents', 'citizen', 'citizens', 'student', 'students', 'user', 'users', 'employee', 'employees', 'family', 'families', 'parent', 'parents', 'child', 'children', 'passenger', 'passengers', 'driver', 'drivers', 'patient', 'patients', 'victim', 'victims', 'survivor', 'survivors', 'rescuer', 'rescuers', 'rescue worker', 'rescue workers', 'firefighter', 'firefighters', 'police officer', 'police officers', 'man', 'woman', 'person', 'people', 'figure', 'subject', '전문가', '발표자', '해설자', '화자', '진행자', '사회자', '기자', '선생', '의사', '공무원', '노동자', '주민', '시민', '학생', '사용자', '직원', '가족', '부모', '아이', '승객', '운전자', '환자', '피해자', '생존자', '구조대원', '소방관', '경찰', '남성', '여성', '사람', '인물', '주인공')
ANONYMOUS_HUMAN_ROLE_MARKERS: 'tuple[str, ...]' = ('resident', 'citizen', 'student', 'teacher', 'doctor', 'patient', 'worker', 'employee', 'family', 'parent', 'child', 'user', 'customer', 'commuter', 'passenger', 'driver', 'victim', 'survivor', 'rescuer', 'rescue worker', 'firefighter', 'police officer', 'neighbor', 'bystander', 'witness', 'resident', '주민', '시민', '학생', '교사', '선생', '의사', '환자', '직원', '노동자', '가족', '부모', '아이', '사용자', '고객', '통근자', '승객', '운전자', '피해자', '생존자', '구조대원', '소방관', '경찰', '이웃', '목격자')
ANONYMOUS_HUMAN_EVENT_MARKERS: 'tuple[str, ...]' = ('rescue', 'evacuate', 'escape', 'survive', 'suffer', 'struggle', 'wait for help', 'react', 'cry', 'comfort', 'protect', 'help', 'support', 'teach', 'learn', 'work', 'use', 'operate', 'isolate', 'exclude', 'confront', 'fight', 'injured', 'wounded', 'rescued', 'trapped', 'homeless', 'rescue', '구조', '대피', '탈출', '생존', '피해', '고통', '버티', '기다리', '반응', '울', '위로', '보호', '도움', '지원', '가르치', '배우', '일하', '사용', '운영', '고립', '소외', '배제', '대치', '충돌', '싸우', '부상', '다친', '갇힌', '이재민')
ACTORLESS_INFRASTRUCTURE_MARKERS: 'tuple[str, ...]' = ('system', 'infrastructure', 'structure', 'layout', 'diagram', 'map', 'graph', 'chart', 'data', 'network', 'pipeline', 'facility', 'building', 'bridge', 'road', 'seawall', 'shoreline', 'coastline', 'topography', 'weather pattern', 'flow', 'mechanism', 'cross-section', '환경', '구조', '시스템', '인프라', '배치', '도면', '지도', '그래프', '차트', '데이터', '네트워크', '시설', '건물', '교량', '도로', '방파제', '해안선', '지형', '기상', '흐름', '메커니즘', '단면')
PRESENTER_FALLBACK_MARKERS: 'tuple[str, ...]' = ('presenter', 'speaker', 'briefing', 'lecture', 'meeting room', 'boardroom', 'monitor', 'screen', '발표', '브리핑', '강의', '회의실', '모니터', '화면')
_ROLE_BASED_SCENE_ACTOR_TYPES = {
    'crowd_actor',
    'group_actor',
    'background_actor',
    'relational_role_actor',
    'occupational_or_social_role_actor'}

def _normalize_text(value = None):
