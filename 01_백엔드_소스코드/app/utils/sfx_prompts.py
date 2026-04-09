# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: sfx_prompts.pyc (Python 3.11)

'''
SFX (Sound Effects) 카테고리 및 스타일 정의 모듈

효과음 카테고리 정보와 장르별 스타일 가이드를 제공합니다.
'''
from typing import Dict, List
SFX_CATEGORIES: Dict[(str, Dict)] = {
    'action': {
        'name': '동작/액션',
        'description': '발소리, 문 열림/닫힘, 충돌음, 타격음 등',
        'examples': [
            'footsteps',
            'door_open',
            'door_close',
            'punch',
            'crash',
            'fall',
            'break'],
        'default_volume': 0.7,
        'typical_duration': (0.5, 3) },
    'ambient': {
        'name': '환경음',
        'description': '바람, 빗소리, 새소리, 도시 소음, 기계음 등',
        'examples': [
            'wind',
            'rain',
            'birds',
            'city_traffic',
            'machinery',
            'crowd'],
        'default_volume': 0.4,
        'typical_duration': (5, 30) },
    'voice': {
        'name': '음성 효과',
        'description': '한숨, 웃음, 울음, 놀람, 비명 등',
        'examples': [
            'sigh',
            'laugh',
            'cry',
            'gasp',
            'scream',
            'whisper'],
        'default_volume': 0.6,
        'typical_duration': (0.5, 2) },
    'music': {
        'name': '음악적 효과',
        'description': '드럼롤, 팡파레, 긴장 스팅어, 전환음 등',
        'examples': [
            'drumroll',
            'fanfare',
            'tension_sting',
            'transition',
            'whoosh'],
        'default_volume': 0.5,
        'typical_duration': (1, 5) },
    'ui': {
        'name': 'UI/알림',
        'description': '클릭, 알림음, 성공/실패음 등',
        'examples': [
            'click',
            'notification',
            'success',
            'error',
            'pop'],
        'default_volume': 0.5,
        'typical_duration': (0.2, 1) },
    'nature': {
        'name': '자연음',
        'description': '물소리, 천둥, 파도, 폭포 등',
        'examples': [
            'water_flow',
            'thunder',
            'waves',
            'waterfall',
            'fire_crackling'],
        'default_volume': 0.5,
        'typical_duration': (3, 30) } }
GENRE_SFX_STYLES: Dict[(str, Dict)] = {
    'DRAMATIC': {
        'preferred_categories': [
            'action',
            'voice',
            'music'],
        'intensity_multiplier': 1.2,
        'ambient_usage': 'moderate',
        'style_notes': '극적인 순간에 임팩트 있는 효과음, 전환 시 드라마틱한 스팅어' },
    'THRILLER': {
        'preferred_categories': [
            'ambient',
            'music',
            'action'],
        'intensity_multiplier': 1.3,
        'ambient_usage': 'heavy',
        'style_notes': '긴장감 조성을 위한 저음 앰비언스, 갑작스러운 충격음' },
    'HORROR': {
        'preferred_categories': [
            'ambient',
            'voice',
            'music'],
        'intensity_multiplier': 1.4,
        'ambient_usage': 'heavy',
        'style_notes': '으스스한 배경음, 갑작스러운 비명, 불안한 음향 효과' },
    'COMEDY': {
        'preferred_categories': [
            'ui',
            'voice',
            'music'],
        'intensity_multiplier': 0.8,
        'ambient_usage': 'light',
        'style_notes': '코믹한 효과음, 과장된 동작음, 밝은 전환음' },
    'DOCUMENTARY': {
        'preferred_categories': [
            'ambient',
            'nature'],
        'intensity_multiplier': 0.6,
        'ambient_usage': 'moderate',
        'style_notes': '자연스러운 환경음, 절제된 효과음' },
    'HEARTWARMING': {
        'preferred_categories': [
            'ambient',
            'music',
            'nature'],
        'intensity_multiplier': 0.7,
        'ambient_usage': 'light',
        'style_notes': '따뜻한 분위기의 효과음, 부드러운 전환음' },
    'MYSTERY': {
        'preferred_categories': [
            'ambient',
            'music',
            'action'],
        'intensity_multiplier': 1.1,
        'ambient_usage': 'moderate',
        'style_notes': '미스터리한 분위기의 효과음, 단서 발견 시 강조음' } }
DEFAULT_SFX_STYLE = {
    'preferred_categories': [
        'action',
        'ambient',
        'music'],
    'intensity_multiplier': 1,
    'ambient_usage': 'moderate',
    'style_notes': '균형 잡힌 효과음 사용' }

def get_sfx_category(category_id = None):
    '''카테고리 정보 반환'''
    return SFX_CATEGORIES.get(category_id, SFX_CATEGORIES['action'])


def get_genre_sfx_style(genre = None):
    '''장르별 SFX 스타일 반환'''
    return GENRE_SFX_STYLES.get(genre, DEFAULT_SFX_STYLE)


def get_all_sfx_categories():
    '''모든 SFX 카테고리 반환'''
    return SFX_CATEGORIES.copy()


def get_category_examples(category_id = None):
    '''카테고리별 예시 반환'''
    category = SFX_CATEGORIES.get(category_id, { })
    return category.get('examples', [])
