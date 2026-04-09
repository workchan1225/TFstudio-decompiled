# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: tone_dampening_config.pyc (Python 3.11)

__doc__ = "\n톤 완화(Dampening) 설정\n\nAI 대본의 과장/형용사 완화를 위한 장르별 설정.\n장르에 따라 적절한 완화 레벨을 자동 매핑.\n\n사용법:\n    from app.utils.tone_dampening_config import (\n        get_dampening_level,\n        get_level_config,\n        get_temperature_for_genre,\n    )\n\n    level = get_dampening_level('LIFE_KNOWLEDGE')  # DampeningLevel.STRONG\n    config = get_level_config(level)\n    temp = get_temperature_for_genre('LIFE_KNOWLEDGE', 0.9)  # 0.7\n"
from typing import Dict, List
from dataclasses import dataclass
from enum import Enum

class DampeningLevel(Enum):
    '''완화 레벨'''
    NONE = 'none'
    MINIMAL = 'minimal'
    MODERATE = 'moderate'
    STRONG = 'strong'

DampeningLevelConfig = <NODE:12>()
LEVEL_CONFIGS: Dict[(DampeningLevel, DampeningLevelConfig)] = {
    DampeningLevel.STRONG: DampeningLevelConfig(name = '강한 완화', temperature_delta = -0.2, adjective_reduction = 'heavy', superlative_policy = 'forbid', exclamation_policy = 'forbid', forbidden_patterns = [
        '완전 미쳤',
        '역대급',
        '전설의',
        '충격적인',
        '믿을 수 없는',
        '경악',
        '전율',
        '소름 돋는',
        '최강의',
        '최고의',
        '압도적인',
        '놀라운',
        '엄청난',
        '대단한',
        '끝내주는',
        '미친',
        '헐'], replacement_rules = {
        '엄청나게': '',
        '굉장히': '',
        '완전히': '',
        '절대로': '',
        '무려': '',
        '자그마치': '',
        '정말': '',
        '진짜': '' }, prompt_instruction = '\n### 문체 조정 (강함 - 절대 위반 금지)\n\n**금지 표현:**\n- 과장 형용사: "충격적인", "놀라운", "엄청난", "대단한", "압도적인"\n- 과장 부사: "엄청나게", "굉장히", "완전히", "무려", "자그마치"\n- 감탄 표현: "헐", "미친", "끝내주는", "역대급"\n- 최상급: "최고의", "최강의", "가장 ~한"\n- 나레이션에서 느낌표 사용 금지\n\n**대체 방법:**\n- (X) "엄청나게 충격적인 사건이 발생했다!"\n- (O) "예상치 못한 사건이 발생했다."\n\n- (X) "그녀의 반응은 정말 놀라웠다."\n- (O) "그녀는 잠시 말을 잃었다."\n\n- (X) "무려 10년간의 비밀이 드러났다!"\n- (O) "10년간의 비밀이 드러났다."\n\n**원칙:**\n1. 사실과 상황을 구체적으로 묘사\n2. 감정은 행동/반응으로 표현\n3. 숫자/데이터는 그 자체로 충분\n4. 독자가 스스로 판단하게 유도\n'),
    DampeningLevel.MODERATE: DampeningLevelConfig(name = '중간 완화', temperature_delta = -0.1, adjective_reduction = 'moderate', superlative_policy = 'reduce', exclamation_policy = 'reduce', forbidden_patterns = [
        '완전 미쳤',
        '역대급',
        '전설의',
        '충격적인',
        '믿을 수 없는',
        '경악',
        '전율',
        '소름 돋는',
        '최강의',
        '최고의'], replacement_rules = {
        '엄청나게': '상당히',
        '굉장히': '꽤',
        '완전히': '전적으로',
        '절대로': '결코',
        '무려': '',
        '자그마치': '' }, prompt_instruction = '\n### 문체 조정 (중간 - 반드시 준수)\n- 과장된 형용사/부사 사용을 줄이세요\n- "충격적인", "믿을 수 없는", "소름 돋는" 대신 구체적 상황 묘사로 대체\n- 느낌표는 정말 필요한 대사에서만 사용 (나레이션에서 최소화)\n- "무려", "자그마치" 같은 강조 부사 대신 숫자/사실만 제시\n- 최상급 표현("최고의", "최강의") 대신 비교/맥락 제공\n\n예시:\n- (X) "충격적이게도 무려 10년이나 숨겨온 비밀!"\n- (O) "10년간 숨겨온 비밀이 드러났다."\n'),
    DampeningLevel.MINIMAL: DampeningLevelConfig(name = '최소 완화', temperature_delta = 0, adjective_reduction = 'light', superlative_policy = 'allow', exclamation_policy = 'reduce', forbidden_patterns = [
        '완전 미쳤',
        '역대급',
        '전설의'], replacement_rules = {
        '엄청나게': '상당히',
        '굉장히': '꽤' }, prompt_instruction = '\n### 문체 조정 (최소)\n- 과도한 느낌표(!!!) 사용을 자제하세요 (문장당 최대 1개)\n- "완전 미쳤", "역대급" 같은 과장 표현을 피하세요\n- 장르 특유의 긴장감/공포감은 유지하되, 과장 없이 묘사로 전달하세요\n'),
    DampeningLevel.NONE: DampeningLevelConfig(name = '완화 없음', temperature_delta = 0, adjective_reduction = 'none', superlative_policy = 'allow', exclamation_policy = 'allow', forbidden_patterns = [], replacement_rules = { }, prompt_instruction = '') }
# WARNING: Decompyle incomplete
