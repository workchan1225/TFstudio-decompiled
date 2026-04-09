# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: logical_coherence_enforcer.pyc (Python 3.11)

__doc__ = '\nLogical Coherence Enforcer - 논리적 개연성 강제 모듈\n\n나이/성별에 따른 시각적 특징을 Python 코드에서 자동 추가:\n- 할머니/할아버지 → 주름진 얼굴, 흰머리, 늙은 피부\n- 아이/소년/소녀 → 어린 얼굴, 작은 체구, 순수한 눈빛\n- 중년 → 성숙한 인상, 약간의 주름\n'
import re
from typing import Dict, List, Optional, Tuple
AGE_VISUAL_FEATURES: Dict[(str, Dict)] = {
    'elderly': {
        'age_range': (70, 100),
        'keywords_ko': [
            '할머니',
            '할아버지',
            '노인',
            '노부부',
            '늙은',
            '노파',
            '노옹',
            '백발'],
        'keywords_en': [
            'elderly',
            'old',
            'aged',
            'senior',
            'grandmother',
            'grandfather'],
        'features_en': 'wrinkled face, gray/white hair, aged weathered skin, gentle tired eyes, thin frame',
        'features_ko': '주름진 얼굴, 흰머리/백발, 늙은 피부, 온화한 눈빛, 마른 체형' },
    'mature': {
        'age_range': (55, 69),
        'keywords_ko': [
            '노년',
            '은퇴'],
        'keywords_en': [
            'mature',
            'retired'],
        'features_en': 'graying hair, some wrinkles, mature dignified features',
        'features_ko': '희끗한 머리카락, 약간의 주름, 성숙하고 위엄있는 인상' },
    'middle_aged': {
        'age_range': (40, 54),
        'keywords_ko': [
            '아저씨',
            '아줌마',
            '중년',
            '사십대',
            '오십대'],
        'keywords_en': [
            'middle-aged',
            'forties',
            'fifties'],
        'features_en': 'mature features, some wrinkles, distinguished professional look',
        'features_ko': '중년의 외모, 약간의 주름, 성숙한 인상' },
    'adult': {
        'age_range': (30, 39),
        'keywords_ko': [
            '삼십대',
            '서른'],
        'keywords_en': [
            'thirties',
            'adult'],
        'features_en': 'mature adult features, confident appearance',
        'features_ko': '성인의 외모, 자신감 있는 인상' },
    'young_adult': {
        'age_range': (20, 29),
        'keywords_ko': [
            '청년',
            '젊은',
            '이십대',
            '스무살',
            '대학생'],
        'keywords_en': [
            'young adult',
            'twenties',
            'youth'],
        'features_en': 'youthful face, smooth skin, energetic vibrant appearance',
        'features_ko': '젊은 얼굴, 매끄러운 피부, 활기찬 인상' },
    'teenager': {
        'age_range': (13, 19),
        'keywords_ko': [
            '청소년',
            '고등학생',
            '중학생',
            '십대'],
        'keywords_en': [
            'teenager',
            'teen',
            'adolescent',
            'high school'],
        'features_en': 'youthful teenage features, fresh face, slim build',
        'features_ko': '청소년의 외모, 싱그러운 얼굴, 날씬한 체형' },
    'child': {
        'age_range': (6, 12),
        'keywords_ko': [
            '아이',
            '소년',
            '소녀',
            '어린',
            '초등학생',
            '아동'],
        'keywords_en': [
            'child',
            'kid',
            'boy',
            'girl',
            'young'],
        'features_en': 'childlike round face, small stature, innocent bright eyes, small frame',
        'features_ko': '어린 얼굴, 작은 체구, 순수한 눈빛, 동글동글한 볼' },
    'toddler': {
        'age_range': (2, 5),
        'keywords_ko': [
            '유아',
            '꼬마',
            '유치원생'],
        'keywords_en': [
            'toddler',
            'preschooler',
            'little'],
        'features_en': 'very small child features, chubby cheeks, tiny stature, baby-like face',
        'features_ko': '아주 어린 얼굴, 통통한 볼, 아주 작은 체구, 아기 같은 얼굴' },
    'infant': {
        'age_range': (0, 1),
        'keywords_ko': [
            '아기',
            '갓난아기',
            '신생아',
            '영아'],
        'keywords_en': [
            'infant',
            'baby',
            'newborn'],
        'features_en': 'baby face, very chubby cheeks, tiny body, soft features',
        'features_ko': '아기 얼굴, 통통한 볼, 아주 작은 몸, 부드러운 이목구비' } }
# WARNING: Decompyle incomplete
