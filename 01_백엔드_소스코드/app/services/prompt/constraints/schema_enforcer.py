# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: schema_enforcer.pyc (Python 3.11)

'''
SchemaEnforcer - JSON 스키마 강제 적용 시스템

AI가 정해진 JSON 스키마를 반드시 준수하도록 강제하는 프롬프트 생성.
마크다운 코드블록 없이 순수 JSON만 출력하도록 강제.
'''
from typing import List, Dict, Optional
import json

class SchemaEnforcer:
    '''
    JSON 스키마 강제 적용 시스템

    AI 응답이 정해진 JSON 스키마를 준수하도록 강제.
    마크다운 코드블록, 추가 설명 등을 방지.
    '''
    
    def __init__(self):
        pass

    
    def build_enforcement_prompt(self = None, chapter_count = None, include_characters = None, include_title = (True, True)):
        '''
        스키마 강제 프롬프트 생성

        Args:
            chapter_count: 챕터 수
            include_characters: 캐릭터 정보 포함 여부
            include_title: 제목 포함 여부

        Returns:
            스키마 강제 프롬프트
        '''
        schema_parts = []
        if include_title:
            schema_parts.append('"title": "string (필수)"')
        if include_characters:
            schema_parts.append('"characters": [\n    {\n      "uniqueId": "A|B|C|...",\n      "name": "string",\n      "appearance": "string",\n      "profile": "string"\n    }\n  ]')
        schema_parts.append(f'''"chapters": [\n    // 정확히 {chapter_count}개!\n    {{\n      "title": "파트 N: 제목",\n      "content": "string (대본 내용)"\n    }}\n  ]''')
        schema_str = ',\n  '.join(schema_parts)
        return f'''\n## [SCHEMA LOCK] JSON 구조 강제\n\n### 필수 스키마 (변경 불가!)\n\n```json\n{{\n  {schema_str}\n}}\n```\n\n### 스키마 규칙 (위반 시 실패)\n\n1. **chapters 배열**: 정확히 **{chapter_count}개** 필수!\n   - {chapter_count}개 미만 또는 초과 시 → 실패\n\n2. **title 필드**: 비어있으면 안 됨\n   - 빈 문자열 "" 또는 null 금지\n\n3. **content 필드**: 대본 내용 필수\n   - 빈 content 금지\n   - 줄바꿈은 \\n으로 이스케이프\n\n### 출력 형식 (매우 중요!)\n\n1. **마크다운 코드블록 금지!**\n   ❌ ```json ... ```\n   ✅ {{ ... }} (순수 JSON만)\n\n2. **추가 텍스트 금지!**\n   ❌ "여기 결과입니다:" {{ ... }}\n   ✅ {{ ... }} (JSON만)\n\n3. **마지막에 }} 로 정확히 종료**\n   ❌ }}\\n\\n추가 설명\n   ✅ }} (종료)\n\n### JSON 이스케이프 규칙\n\n- 줄바꿈: \\n\n- 따옴표: \\"\n- 역슬래시: \\\\\n- 탭: \\t\n\n### 예시 (올바른 출력)\n\n{{\n  "title": "운명의 시작",\n  "characters": [\n    {{"uniqueId": "A", "name": "(장르에 맞는 이름)", "appearance": "30대 남성", "profile": "주인공"}}\n  ],\n  "chapters": [\n    {{"title": "파트 1: 만남", "content": "[나레이션]: 그날이었다.\\n[인물A]: 누구세요?"}},\n    {{"title": "파트 2: 갈등", "content": "[나레이션]: 시간이 흘렀다.\\n[인물A]: 왜 그랬어요?"}}\n  ]\n}}\n\n---\n⛔ JSON 구조가 맞지 않으면 파싱 실패로 전체 재생성됩니다.\n순수 JSON만 출력하세요!\n'''

    
    def build_chapter_only_prompt(self = None, chapter_count = None):
        '''
        챕터만 포함하는 간단한 스키마 프롬프트

        Args:
            chapter_count: 챕터 수

        Returns:
            간단한 스키마 프롬프트
        '''
        return f'''\n## [SCHEMA] JSON 출력 형식\n\n```json\n{{\n  "chapters": [\n    {{"title": "파트 1: 제목", "content": "대본 내용..."}},\n    {{"title": "파트 2: 제목", "content": "대본 내용..."}},\n    // ... 정확히 {chapter_count}개\n  ]\n}}\n```\n\n### 규칙\n- chapters 배열: 정확히 **{chapter_count}개**\n- 마크다운 코드블록 없이 순수 JSON만\n- content 내 줄바꿈은 \\n으로\n\n---\n'''

    
    def build_validation_checklist(self = None, chapter_count = None):
        '''
        출력 전 검증 체크리스트 프롬프트

        Args:
            chapter_count: 챕터 수

        Returns:
            검증 체크리스트 프롬프트
        '''
        return f'''\n## [VALIDATION] 출력 전 검증\n\nJSON 출력 전 다음을 확인하세요:\n\n1. [ ] chapters 배열이 정확히 **{chapter_count}개**인가?\n2. [ ] 모든 chapter에 title과 content가 있는가?\n3. [ ] content가 비어있지 않은가?\n4. [ ] 마크다운 코드블록(```)을 사용하지 않았는가?\n5. [ ] JSON 앞뒤에 추가 텍스트가 없는가?\n6. [ ] 줄바꿈이 \\n으로 이스케이프 되었는가?\n\n---\n위 항목 중 하나라도 실패하면 수정 후 출력하세요.\n'''

    
    def build_abort_conditions(self = None):
        '''
        강제 중단 조건 프롬프트

        Returns:
            중단 조건 프롬프트
        '''
        return '\n## [ABORT CONDITIONS] 강제 중단 조건\n\n다음 중 하나라도 해당되면 해당 부분을 수정하세요:\n\n1. ❌ chapters 배열이 지정된 개수와 다름\n2. ❌ title 또는 content가 비어있음\n3. ❌ 마크다운 코드블록(```) 사용\n4. ❌ JSON 앞뒤에 설명 텍스트 포함\n5. ❌ 유효하지 않은 JSON 구문\n\n---\n위 조건 발견 시 → 즉시 수정하고 계속\n'

    
    def validate_json_structure(self = None, json_str = None, expected_chapter_count = None):
        '''
        JSON 구조 검증 (생성 후 검증용)

        Args:
            json_str: 검증할 JSON 문자열
            expected_chapter_count: 예상 챕터 수

        Returns:
            검증 결과 딕셔너리
        '''
        errors = []
        if '```' in json_str:
            errors.append('마크다운 코드블록이 포함되어 있습니다')
        cleaned = json_str.strip()
        if cleaned.startswith('```'):
            lines = cleaned.split('\n')
            cleaned = '\n'.join(lines[1:-1] if lines[-1].strip() == '```' else lines[1:])
        
        try:
            data = json.loads(cleaned)
        except json.JSONDecodeError:
            e = None
            del e
            return None
            None = 
            del e

        return {
            'is_valid': None,
            'errors': len(errors) == 0,
            'data': errors if 'chapters' not in data else data if len(errors) == 0 else None }
