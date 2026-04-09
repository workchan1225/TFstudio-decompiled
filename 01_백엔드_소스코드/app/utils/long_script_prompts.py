# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: long_script_prompts.pyc (Python 3.11)

__doc__ = '\n장편 대본 생성 프롬프트\n\n1회 API 호출로 최대 40,000자 대본을 생성하는 프롬프트.\nGemini 2.5 Pro의 높은 컨텍스트 이해력을 활용하여 논리적 일관성 유지.\n\n핵심 전략:\n1. 전체 구조 우선 설계 (프롬프트 내에서 아웃라인 먼저)\n2. 캐릭터 일관성 (프로필/말투 패턴 정의)\n3. 복선 추적 (심기 → 회수 매핑)\n4. 톤 통일 (나레이션 어미/문체 정의)\n5. 연결 고리 (챕터 간 훅)\n'
from typing import List, Dict, Optional
from script_genre_data import get_genre_data, build_hooking_prompt, get_narration_tone
from genre_categories import get_genre_category, is_informational_category
from script_prompts import _build_narration_ratio_instruction
from tone_dampening_config import get_dampening_prompt

def build_long_script_system_prompt(genre, chapter_count, target_chars, characters = None, tone = None, additional_context = None, speaker_tag_mode = (None, 'neutral', None, 'with_tags', 50), narration_ratio = ('genre', str, 'chapter_count', int, 'target_chars', int, 'characters', Optional[List[Dict]], 'tone', str, 'additional_context', Optional[str], 'speaker_tag_mode', str, 'narration_ratio', int, 'return', str)):
    """
    장편 대본 생성용 시스템 프롬프트 생성

    Args:
        genre: 장르 코드 (예: 'MYSTERY', 'HORROR')
        chapter_count: 챕터 수 (5~8)
        target_chars: 목표 글자수 (최대 40,000)
        characters: 캐릭터 목록
        tone: 톤 설정
        additional_context: 추가 컨텍스트
        speaker_tag_mode: 화자 태그 모드 ('with_tags' | 'without_tags')
        narration_ratio: 나레이션/대사 비율 (0-100, 기본 50)

    Returns:
        시스템 프롬프트 문자열
    """
    chars_per_chapter = target_chars // chapter_count
    genre_data = get_genre_data(genre)
    narration_tone = get_narration_tone(genre)
    is_info_genre = is_informational_category(genre)
    prompt_parts = []
    prompt_parts.append(_build_role_section(target_chars, chapter_count, chars_per_chapter, is_info_genre))
    prompt_parts.append(_build_consistency_rules(is_info_genre))
    prompt_parts.append(_build_genre_section(genre, genre_data))
    storytelling_section = _build_drama_storytelling_section(genre)
    if storytelling_section:
        prompt_parts.append(storytelling_section)
    if not characters and is_info_genre:
        prompt_parts.append(_build_character_section(characters))
    effective_speaker_mode = 'without_tags' if is_info_genre else speaker_tag_mode
    prompt_parts.append(_build_narration_tone_section(tone = tone, narration_tone = narration_tone, genre = genre, speaker_tag_mode = effective_speaker_mode))
    if not is_info_genre:
        ratio_instruction = _build_narration_ratio_instruction(narration_ratio, effective_speaker_mode, genre)
        prompt_parts.append(f'''\n## 나레이션/대사 비율 규칙\n\n{ratio_instruction}\n\n**장편 대본에서도 이 비율을 모든 챕터에서 일관되게 유지하세요.**\n''')
    prompt_parts.append(_build_chapter_structure_section(chapter_count, chars_per_chapter, is_info_genre))
    if not is_info_genre:
        prompt_parts.append(_build_foreshadowing_section())
    prompt_parts.append(_build_speaker_tag_section(effective_speaker_mode, characters if not is_info_genre else None, is_info_genre))
    if additional_context:
        prompt_parts.append(f'''\n## 추가 지침\n\n{additional_context}\n''')
    prompt_parts.append(_build_output_format_section(chapter_count, speaker_tag_mode))
    dampening_prompt = get_dampening_prompt(genre)
    if dampening_prompt:
        prompt_parts.append(dampening_prompt)
    return '\n'.join(prompt_parts)


def _build_role_section(target_chars = None, chapter_count = None, chars_per_chapter = None, is_info_genre = (False,)):
    '''역할 및 목표 섹션'''
    if is_info_genre:
        return f'''# 정보/분석 콘텐츠 작가 역할\n\n당신은 **1회 호출로 완성된 정보/분석 콘텐츠 대본**을 작성하는 전문 작가입니다.\n\n## 🚨🚨🚨 핵심 규칙 (반드시 준수!) 🚨🚨🚨\n\n### ❌ 절대 금지 (드라마 스타일 금지!)\n- **캐릭터 등장 금지**: "민준", "서연", "철수" 등 이름 있는 인물 생성 금지\n- **1인칭 드라마 금지**: "저는 그날...", "나는 깨달았다" 형식 금지\n- **대화체 금지**: "[민준]: ...", "[서연]: ..." 형식 절대 금지\n- **개인 서사 금지**: 특정 인물의 투자 실패담, 연애담 등 개인 이야기 금지\n- **감정 서사 금지**: "눈물이 흘렀다", "심장이 뛰었다" 등 감정 묘사 금지\n\n### ✅ 올바른 형식\n- **"여러분", "우리" 시점**: 시청자를 직접 호칭\n- **나레이션 100%**: 해설자가 시청자에게 직접 설명하는 형식\n- **데이터/통계 기반**: 객관적 수치와 분석으로 구성\n- **질문형 호기심 유발**: "왜 이런 일이 반복될까요?"\n\n## 핵심 원칙 (우선순위 순)\n1. **★ 4계층 분석 구조 (최우선)**: 계량적 실체 → 인지적 왜곡 → 수익 구조 → 사회적 가치\n2. **데이터 기반**: 구체적 통계와 수치로 논점 뒷받침\n3. **논리적 흐름**: 각 챕터가 논리적으로 연결\n4. **1회 생성**: 분할하지 않고 한번에 전체 대본 작성\n\n## ★★★ 분량 목표 (매우 중요 - 반드시 달성!) ★★★\n- **총 글자수**: {target_chars:,}자 ← 이 수치의 90% 이상 필수!\n- **챕터 수**: {chapter_count}챕터\n- **챕터당 최소**: {chars_per_chapter:,}자 (각 챕터가 이 분량에 미달하면 실패!)\n\n### ⚠️ 분량 미달 시 문제점\n- 목표의 90% 미만 생성 시: **대본 사용 불가** (재생성 필요)\n- 챕터당 {chars_per_chapter // 2:,}자 미만: **각 챕터가 너무 짧음** (전체 품질 저하)\n\n### 분량 달성 방법 (4계층 분석 확장!)\n- ✅ **통계/데이터를 풍부하게** (실제 연구 결과, 역사적 사례, 국가별 비교)\n- ✅ **비유적 확률화 상세히** (숫자를 일상적 비유로 변환, 시각화)\n- ✅ **심리학적 분석 심화** (인지 편향 유형, 심리학 실험 인용)\n- ✅ **수익 구조 분석 확장** (자금 흐름, 운영자 이익 메커니즘)\n- ✅ **사회적/문화적 배경 추가** (계층별 참여율, 역사적 맥락)\n- ✅ **질문형 문장으로 호기심 유발** ("여러분은 왜...?", "어떻게 생각하시나요?")\n- ❌ 글자수 채우기 위한 불필요한 반복 금지\n- ❌ 주제와 무관한 내용 추가 금지\n- ❌ 요약/축약형 작성 절대 금지\n\n### 분량 체크 규칙\n1. 각 챕터 작성 후 "이 챕터가 {chars_per_chapter:,}자에 도달했는가?" 자가 점검\n2. 부족하면 추가 사례, 통계, 심리 분석을 확장\n3. 전체 대본 완성 후 "총 글자수가 {target_chars:,}자의 90% 이상인가?" 최종 점검\n'''
    return f'''{target_chars:,}자 ← 이 수치의 90% 이상 필수!\n- **챕터 수**: {chapter_count}챕터\n- **챕터당 최소**: {chars_per_chapter:,}자 (각 챕터가 이 분량에 미달하면 실패!)\n\n### ⚠️ 분량 미달 시 문제점\n- 목표의 90% 미만 생성 시: **대본 사용 불가** (재생성 필요)\n- 챕터당 {chars_per_chapter // 2:,}자 미만: **각 챕터가 너무 짧음** (전체 품질 저하)\n\n### 분량 달성 방법 (논리적 일관성을 유지하면서)\n- ✅ **장면 묘사를 매우 풍부하게** (배경, 분위기, 날씨, 시간대, 주변 환경)\n- ✅ **캐릭터 행동/표정 상세히** (눈빛, 손동작, 자세, 걸음걸이, 목소리 톤)\n- ✅ **대화를 자연스럽게 길게** (감정, 뉘앙스, 머뭇거림, 생각 표현)\n- ✅ **캐릭터 내면 묘사 추가** (생각, 감정, 갈등, 과거 회상)\n- ✅ **복선을 자연스럽게 심고 회수** (세부 묘사로 복선 구체화)\n- ✅ **전환 장면도 상세히** (시간 경과, 장소 이동 과정)\n- ❌ 글자수 채우기 위한 불필요한 반복/장황함 금지\n- ❌ 스토리와 무관한 내용 추가 금지\n- ❌ 요약/축약형 작성 절대 금지\n\n### 분량 체크 규칙\n1. 각 챕터 작성 후 "이 챕터가 {chars_per_chapter:,}자에 도달했는가?" 자가 점검\n2. 부족하면 장면 묘사, 대화, 감정 표현을 추가로 확장\n3. 전체 대본 완성 후 "총 글자수가 {target_chars:,}자의 90% 이상인가?" 최종 점검\n'''


def _build_consistency_rules(is_info_genre = None):
    '''논리적 일관성 규칙 섹션 (핵심)'''
    if is_info_genre:
        return '\n## ★★★ 4계층 분석 구조 (가장 중요) ★★★\n\n### 작성 순서\n대본 작성 전, 반드시 다음 순서로 **내부적으로 구상**하세요:\n\n1. **핵심 주제 정의**\n   - 분석 대상: 무엇을 분석할 것인가?\n   - 핵심 질문: 시청자가 궁금해할 것은?\n   - 결론: 최종적으로 전달할 메시지\n\n2. **4계층 분석 설계**\n   - **1계층 (계량적 실체)**: 어떤 통계/수치를 제시할 것인가?\n   - **2계층 (인지적 왜곡)**: 어떤 심리적 편향을 분석할 것인가?\n   - **3계층 (수익 구조)**: 누가 어떻게 이익을 얻는가?\n   - **4계층 (사회적 가치)**: 왜 사람들이 그래도 참여하는가?\n\n3. **챕터별 분석 포인트**\n   - 각 챕터가 4계층 중 어떤 부분을 다루는가?\n   - 챕터 간 논리적 흐름\n   - 근거 자료 (통계, 연구, 사례)\n\n4. **시청자 호기심 유발 계획**\n   - 도입부 훅: 충격적 통계로 관심 유발\n   - 중반 전환점: "하지만 진짜 이유는..."\n   - 결론 인사이트: 시청자가 얻어갈 교훈\n\n### 일관성 체크리스트\n- [ ] 4계층이 모두 포함되었는가?\n- [ ] 통계/데이터가 구체적인가?\n- [ ] 논리적 흐름이 자연스러운가?\n- [ ] 나레이션 톤이 일관된가?\n- [ ] "여러분", "우리" 시점을 유지하는가?\n- [ ] 캐릭터가 등장하지 않는가?\n'


def _build_genre_section(genre = None, genre_data = None):
    '''장르 특화 섹션'''
    if not genre_data:
        return f'''\n## 장르: {genre}\n\n해당 장르의 특성에 맞게 작성하세요.\n'''
    genre_name = None.get('name', genre)
    genre_desc = genre_data.get('description', '')
    genre_structure = genre_data.get('structure', { })
    structure_text = ''
    if genre_structure:
        structure_text = '\n### 권장 구조\n'
        for stage, desc in genre_structure.items():
            structure_text += f'''- **{stage}**: {desc}\n'''
            return f'''\n## 장르: {genre_name}\n\n{genre_desc}\n\n{structure_text}\n\n### 장르 필수 요소\n- 장르 특유의 분위기와 톤 유지\n- 장르 관객이 기대하는 요소 포함\n- 장르 클리셰를 활용하되 신선함 추가\n'''


def _build_character_section(characters = None):
