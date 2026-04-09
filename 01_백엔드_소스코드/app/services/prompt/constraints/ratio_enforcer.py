# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: ratio_enforcer.pyc (Python 3.11)

'''
RatioEnforcer - 나레이션/대사 비율 강제 적용 시스템

AI가 선택된 나레이션/대사 비율을 반드시 준수하도록 강제하는 프롬프트 생성.
비율에 따라 챕터 구조 템플릿을 제공하여 준수율 향상.
'''
from typing import List, Tuple
from dataclasses import dataclass
RatioConfig = <NODE:12>()

class RatioEnforcer:
    '''
    나레이션/대사 비율 강제 적용 시스템

    선택된 비율에 따라 챕터 구조 템플릿을 제공하고,
    AI가 해당 구조를 준수하도록 강제.
    '''
    RATIO_THRESHOLDS = [
        (0, 20, 'dialogue_heavy'),
        (21, 40, 'dialogue_focus'),
        (41, 60, 'balanced'),
        (61, 80, 'narration_focus'),
        (81, 100, 'narration_heavy')]
    
    def __init__(self):
        pass

    
    def get_ratio_type(self = None, narration_ratio = None):
        '''비율에 따른 타입 반환'''
        for low, high, ratio_type in self.RATIO_THRESHOLDS:
            if  <= low, narration_ratio or low, narration_ratio <= high:
                pass
            
            
            return None, ratio_type
            return 'balanced'

    
    def calculate_line_distribution(self = None, narration_ratio = None, chapter_count = None, target_length = (4000,)):
        '''
        챕터당 라인 수 계산

        Args:
            narration_ratio: 나레이션 비율 (0-100)
            chapter_count: 챕터 수
            target_length: 총 목표 글자수

        Returns:
            (나레이션 라인 수, 대사 라인 수)
        '''
        avg_line_length = 50
        total_lines = target_length // avg_line_length
        lines_per_chapter = total_lines // chapter_count
        narration_lines = int(lines_per_chapter * narration_ratio / 100)
        dialogue_lines = lines_per_chapter - narration_lines
        return (max(narration_lines, 1), max(dialogue_lines, 1))

    
    def build_enforcement_prompt(self = None, narration_ratio = None, chapter_count = None, speaker_tag_mode = ('with_tags', 4000), target_length = ('narration_ratio', int, 'chapter_count', int, 'speaker_tag_mode', str, 'target_length', int, 'return', str)):
        '''
        강제 적용 프롬프트 생성

        Args:
            narration_ratio: 나레이션 비율 (0-100)
            chapter_count: 챕터 수
            speaker_tag_mode: 화자 태그 모드
            target_length: 목표 글자수

        Returns:
            비율 강제 프롬프트
        '''
        dialogue_ratio = 100 - narration_ratio
        (narr_lines, dial_lines) = self.calculate_line_distribution(narration_ratio, chapter_count, target_length)
        ratio_type = self.get_ratio_type(narration_ratio)
        structure_template = self._get_structure_template(ratio_type, narr_lines, dial_lines)
        if speaker_tag_mode == 'without_tags':
            return self._build_first_person_prompt(narration_ratio, chapter_count)
        return f'''{narration_ratio}% / {dialogue_ratio}%\n\n### 비율 계산 (각 챕터에서 준수!)\n\n- **나레이션** [나레이션]: → 약 **{narr_lines}줄** (챕터당)\n- **캐릭터 대사** [캐릭터명]: → 약 **{dial_lines}줄** (챕터당)\n\n### 구조 템플릿 ({self._get_ratio_description(ratio_type)})\n\n각 챕터는 다음 패턴을 따르세요:\n\n```\n{structure_template}\n```\n\n### 비율 검증 방법\n\n각 챕터 작성 후:\n1. [나레이션]: 태그 개수를 세기 → 약 {narr_lines}개\n2. [캐릭터이름]: 태그 개수를 세기 → 약 {dial_lines}개\n3. 비율이 ±15% 이상 벗어나면 수정\n\n### 비율별 특성\n\n{self._get_ratio_characteristics(ratio_type)}\n\n---\n⚠️ 비율이 크게 벗어나면 대본의 균형이 무너집니다.\n각 챕터에서 위 템플릿을 참고하여 비율을 유지하세요.\n'''

    
    def _get_structure_template(self = None, ratio_type = None, narr_lines = None, dial_lines = ('ratio_type', str, 'narr_lines', int, 'dial_lines', int, 'return', str)):
        '''비율 타입별 구조 템플릿 반환'''
        if ratio_type == 'dialogue_heavy':
            return '[나레이션]: 상황 설명 (1줄)\n[캐릭터A]: 대사\n[캐릭터B]: 대사\n[캐릭터A]: 대사\n[캐릭터B]: 대사\n[캐릭터A]: 대사\n[나레이션]: 전환 (1줄)\n[캐릭터B]: 대사\n[캐릭터A]: 대사\n... (대사 위주로 계속)'
        if None == 'dialogue_focus':
            return '[나레이션]: 상황 설명 (2줄)\n[캐릭터A]: 대사\n[캐릭터B]: 대사\n[캐릭터A]: 대사\n[나레이션]: 감정/상황 묘사 (1줄)\n[캐릭터B]: 대사\n[캐릭터A]: 대사\n[나레이션]: 전환 (1줄)\n... (대사:나레이션 = 3:1 비율)'
        if None == 'balanced':
            return '[나레이션]: 상황 설명 (2-3줄)\n[캐릭터A]: 대사\n[캐릭터B]: 대사\n[나레이션]: 감정/반응 묘사 (1-2줄)\n[캐릭터A]: 대사\n[나레이션]: 행동/상황 (1-2줄)\n[캐릭터B]: 대사\n[나레이션]: 전환/정리 (1-2줄)\n... (나레이션과 대사가 균형있게)'
        if None == 'narration_focus':
            return '[나레이션]: 상황 설명 (3-4줄)\n[캐릭터A]: 대사 (1줄)\n[나레이션]: 반응/감정 묘사 (2-3줄)\n[캐릭터B]: 대사 (1줄)\n[나레이션]: 행동/전개 (3-4줄)\n[캐릭터A]: 대사 (1줄)\n[나레이션]: 정리/전환 (2-3줄)\n... (나레이션 중심, 대사는 핵심만)'

    
    def _get_ratio_description(self = None, ratio_type = None):
        '''비율 타입 설명'''
        descriptions = {
            'dialogue_heavy': '대사 중심형',
            'dialogue_focus': '대사 위주형',
            'balanced': '균형형',
            'narration_focus': '나레이션 위주형',
            'narration_heavy': '나레이션 중심형' }
        return descriptions.get(ratio_type, '균형형')

    
    def _get_ratio_characteristics(self = None, ratio_type = None):
        '''비율 타입별 특성'''
        characteristics = {
            'dialogue_heavy': '- 대화 중심의 빠른 전개\n- 나레이션은 최소한의 상황 설명만\n- 캐릭터 대사로 스토리 진행\n- 예: 토크쇼, 대화극, 시트콤',
            'dialogue_focus': '- 대화가 주도하되 나레이션으로 보완\n- 감정/상황은 나레이션으로 부가 설명\n- 대사 연속 후 짧은 나레이션\n- 예: 드라마, 막장 사연, 복수극',
            'balanced': '- 나레이션과 대사가 조화\n- 상황 설명 후 대화, 다시 나레이션\n- 스토리와 캐릭터 균형\n- 예: 일반 드라마, 가족 이야기',
            'narration_focus': '- 나레이션이 주도하고 대사로 포인트\n- 묘사와 설명이 풍부\n- 대사는 핵심 대목에서만\n- 예: 다큐드라마, 역사극, 서사극',
            'narration_heavy': '- 거의 나레이션으로만 진행\n- 대사는 극히 제한적\n- 묘사와 해설 중심\n- 예: 다큐멘터리, 교육 콘텐츠, 정보 영상' }
        return characteristics.get(ratio_type, characteristics['balanced'])

    
    def _build_first_person_prompt(self = None, narration_ratio = None, chapter_count = None):
        '''1인칭 모드 프롬프트 (화자 태그 없음)'''
        return '\n## [MANDATORY] 1인칭 나레이터 모드\n\n### 형식\n- 화자 태그 [캐릭터명]: 사용하지 않음\n- 전체가 1인칭 나레이션으로 진행\n- 대사는 큰따옴표("")로 표현\n\n### 예시\n```\n그날, 나는 그 문을 열었다.\n방 안은 어두웠고, 묘한 냄새가 났다.\n"누구세요?" 뒤에서 목소리가 들렸다.\n나는 천천히 뒤를 돌아봤다.\n```\n\n### 특성\n- 몰입감 있는 1인칭 시점\n- 화자의 내면 심리 직접 표현 가능\n- 대사는 큰따옴표로 구분\n\n---\n1인칭 모드에서는 비율 개념이 다르게 적용됩니다.\n전체적으로 자연스러운 흐름을 유지하세요.\n'

    
    def validate_ratio(self = None, text = None, target_ratio = None):
        '''
        텍스트의 비율 검증 (생성 후 검증용)

        Args:
            text: 검증할 텍스트
            target_ratio: 목표 나레이션 비율

        Returns:
            검증 결과 딕셔너리
        '''
        import re
        narration_pattern = '\\[나레이션\\]:'
        dialogue_pattern = '\\[[^\\]]+\\]:'
        narration_count = len(re.findall(narration_pattern, text))
        all_speaker_count = len(re.findall(dialogue_pattern, text))
        dialogue_count = all_speaker_count - narration_count
        total = narration_count + dialogue_count
        if total == 0:
            return {
                'is_valid': False,
                'actual_ratio': 0,
                'target_ratio': target_ratio,
                'deviation': target_ratio,
                'narration_count': 0,
                'dialogue_count': 0 }
        actual_ratio = None((narration_count / total) * 100)
        deviation = abs(actual_ratio - target_ratio)
        return {
            'is_valid': deviation <= 15,
            'actual_ratio': actual_ratio,
            'target_ratio': target_ratio,
            'deviation': deviation,
            'narration_count': narration_count,
            'dialogue_count': dialogue_count }
