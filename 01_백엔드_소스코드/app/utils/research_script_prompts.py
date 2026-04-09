# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: research_script_prompts.pyc (Python 3.11)

'''
자료 조사 기반 대본 생성 프롬프트

사용자가 제공한 자료(기사, 메모, 요점 정리 등)를 기반으로
할루시네이션을 최소화한 대본을 생성합니다.

핵심 원칙:
1. 자료에 없는 정보는 절대 추가하지 않음
2. 자료의 사실을 왜곡하지 않음
3. 추론은 명확하게 표시
4. 기존 후킹/장르 시스템 활용

v2.0 추가 (2024-01):
- 드라마/정보 장르별 특화 프롬프트 통합
- 쇼츠 길이별 (1min/2min/3min) 최적화
'''
from typing import List, Dict, Optional
from script_genre_data import get_genre_data, build_hooking_prompt, get_narration_tone
from narration_style_guide import build_korean_drama_style_prompt
from intro_hooking import HOOKING_TYPES, HookingType, get_recommended_hooking_types, get_tone_intro_style, GENRE_HOOKING_RECOMMENDATIONS
from long_script_prompts import INFO_STORYTELLING_ELEMENTS, GENRE_STORYTELLING_COMBINATION
from genre_categories import get_genre_category

try:
    from services.prompt.constraints.ratio_enforcer import RatioEnforcer
    RATIO_ENFORCER_AVAILABLE = True
except ImportError:
    RATIO_ENFORCER_AVAILABLE = False


try:
    from drama_storytelling_system import is_drama_genre, DRAMA_NARRATIVE_STRUCTURE, PSYCHOLOGICAL_MECHANISMS, CHARACTER_ARCHETYPES, SENSORY_TRIGGERS
    from info_content_system import is_info_genre, INFO_PERSONA, WRITING_PRINCIPLES, FORBIDDEN_EXPRESSIONS, ALTERNATIVE_EXPRESSIONS, RETENTION_HOOKS
    GENRE_SYSTEM_AVAILABLE = True
except ImportError:
    GENRE_SYSTEM_AVAILABLE = False
    
    def is_drama_genre(genre = None):
        return False

    
    def is_info_genre(genre = None):
        return False


RESEARCH_SUITABLE_GENRES = [
    'INFORMATIONAL',
    'ENCYCLOPEDIA',
    'LIFE_TIPS',
    'DOCUMENTARY',
    'REAL_LIFE',
    'TRUE_STORY',
    'BIOGRAPHICAL',
    'NEWS_REPORT',
    'REVIEW']
RESEARCH_SUITABLE_HOOKS = [
    'pattern_interrupt',
    'data_emphasis',
    'authority',
    'surprise',
    'curiosity_gap',
    'value_proposition',
    'loss_aversion']
RESEARCH_INTRO_7STEPS = {
    'step_1_fact_shock': {
        'name': '팩트 충격',
        'korean_name': '팩트 충격 (★첫 문장 결정★)',
        'principle': '자료에서 가장 놀라운 사실/통계로 시작하여 스크롤 멈춤',
        'psychology': '인지 충격(Cognitive Shock) - 기존 상식과 충돌하면 주의 집중',
        'instruction': '★★★ 첫 문장은 자료의 가장 의외/충격적인 수치나 사실로! ★★★',
        'example': '"우리가 알고 있던 것의 90%가 틀렸습니다." / "매일 하는 그 습관이 수명을 10년 줄입니다."',
        'prohibited': [
            '자료에 없는 수치',
            '과장된 표현',
            '추측성 주장',
            '평범한 도입'] },
    'step_2_relevance_hook': {
        'name': '관련성 연결',
        'korean_name': '관련성 연결',
        'principle': '시청자의 일상과 자료 내용의 연결점 제시',
        'psychology': '자기 관련성(Self-Relevance) - 나와 관련되면 더 집중',
        'instruction': '자료 내용이 시청자 일상에 어떻게 영향을 미치는지 연결',
        'example': '"매일 아침 커피를 마시면서 건강해지고 있다고 생각하셨죠?"',
        'prohibited': [
            '추상적 설명',
            '자료에 없는 상황 가정'] },
    'step_3_source_authority': {
        'name': '출처 권위',
        'korean_name': '출처 권위',
        'principle': '자료의 신뢰성 제시 (연구/기관/전문가)',
        'psychology': '권위 효과(Authority Effect) - 신뢰할 수 있는 출처가 설득력 증가',
        'instruction': '자료에 명시된 연구, 기관, 전문가를 인용',
        'example': '"하버드 의대 연구팀이 10년간 추적한 결과입니다."',
        'prohibited': [
            '출처 불명 인용',
            '자료에 없는 전문가 언급',
            '허위 기관명'] },
    'step_4_problem_statement': {
        'name': '문제 제기',
        'korean_name': '문제 제기',
        'principle': '자료가 다루는 핵심 문제/의문 명확화',
        'psychology': '문제 인식(Problem Recognition) - 문제를 인식해야 해결책에 관심',
        'instruction': '자료에서 다루는 핵심 문제점이나 의문을 명확하게 제시',
        'example': '"그런데 왜 우리는 계속 잘못된 방법을 사용할까요?"',
        'prohibited': [
            '자료 범위 외 문제',
            '과장된 위기감'] },
    'step_5_curiosity_gap': {
        'name': '호기심 갭',
        'korean_name': '호기심 갭',
        'principle': '답의 일부만 암시하고 본론에서 공개',
        'psychology': '정보 갭 이론(Information Gap) - 아는 것과 모르는 것의 차이가 호기심 유발',
        'instruction': '자료에서 찾은 답이 있음을 암시하되 구체적 내용은 숨김',
        'example': '"원인은 단 하나였는데... 이걸 알면 생각이 완전히 바뀝니다."',
        'prohibited': [
            '해결책 즉시 공개',
            '모든 정보 미리 제공'] },
    'step_6_data_preview': {
        'name': '데이터 예고',
        'korean_name': '데이터 예고',
        'principle': '핵심 수치/결론의 일부만 미리 공개하여 기대감 조성',
        'psychology': '구체성 효과(Concreteness Effect) - 구체적 숫자가 신뢰와 기대 증가',
        'instruction': '자료의 핵심 발견 일부만 보여주기 (전체는 본론에서)',
        'example': '"3가지만 바꾸면 됩니다. 그 중 하나는..."',
        'prohibited': [
            '자료에 없는 숫자',
            '과장된 효과 주장'] },
    'step_7_value_promise': {
        'name': '가치 약속',
        'korean_name': '가치 약속',
        'principle': '끝까지 보면 얻을 구체적 지식/인사이트 약속',
        'psychology': '이득 동기(Gain Motivation) - 명확한 보상 약속이 시청 동기 부여',
        'instruction': '자료에서 도출 가능한 인사이트를 약속 (과장 금지)',
        'example': '"오늘 알려드릴 내용만 기억하시면, 같은 실수를 피할 수 있습니다."',
        'prohibited': [
            '과장된 약속',
            '자료 범위 외 효과 주장',
            '치료/완치 약속'] } }
SHORTS_LENGTH_CONFIG = {
    '1min': {
        'target_length': 420,
        'chapter_count': 1,
        'narration_ratio': 80,
        'drama_stages': [
            '1_결핍',
            '4_위기_갈등',
            '6_카타르시스'],
        'info_hooks_count': 1,
        'description': '초압축 - 핵심 한 가지만 임팩트 있게' },
    '2min': {
        'target_length': 840,
        'chapter_count': 1,
        'narration_ratio': 75,
        'drama_stages': [
            '1_결핍',
            '3_의구심',
            '4_위기_갈등',
            '6_카타르시스'],
        'info_hooks_count': 2,
        'description': '압축형 - 서사 흐름 유지하면서 임팩트' },
    '3min': {
        'target_length': 1260,
        'chapter_count': 2,
        'narration_ratio': 70,
        'drama_stages': [
            '1_결핍',
            '2_만남',
            '4_위기_갈등',
            '5_진실_규명',
            '6_카타르시스'],
        'info_hooks_count': 3,
        'description': '미니 롱폼 - 완성도 있는 서사 전개' } }

def _build_shorts_drama_genre_prompt(genre = None, shorts_length = None):
    """
    쇼츠용 드라마 장르 프롬프트 생성

    Args:
        genre: 장르 코드
        shorts_length: 쇼츠 길이 ('1min' | '2min' | '3min')

    Returns:
        드라마 장르 특화 프롬프트
    """
    if not GENRE_SYSTEM_AVAILABLE or is_drama_genre(genre):
        return ''
    config = None.get(shorts_length, SHORTS_LENGTH_CONFIG['2min'])
    stages = config['drama_stages']
    lines = [
        '## 🎭 드라마 장르 스토리텔링 (쇼츠 최적화)',
        '',
        f'''**쇼츠 길이**: {shorts_length} ({config['description']})''',
        '',
        '### 압축 서사 구조',
        f'''이 쇼츠는 **{len(stages)}단계 압축 구조**로 진행합니다:''',
        '']
    stage_descriptions = {
        '1_결핍': '**결핍**: 주인공의 문제/갈등 즉시 제시 (첫 문장에서 바로)',
        '2_만남': '**만남**: 새로운 상황/인물 등장으로 대비 설정',
        '3_의구심': '**의구심**: 직감/감각적 트리거로 미스터리 암시',
        '4_위기_갈등': '**위기**: 핵심 갈등 폭발, 긴장감 최고조',
        '5_진실_규명': '**진실**: 복선 수렴, 반전 또는 깨달음',
        '6_카타르시스': '**카타르시스**: 감정 폭발, 여운 있는 마무리' }
    for i, stage in enumerate(stages, 1):
        if stage in stage_descriptions:
            lines.append(f'''{i}. {stage_descriptions[stage]}''')
        lines.extend([
            '',
            '### 심리학적 기제 (1가지만 선택)',
            ''])
        if shorts_length == '1min':
            lines.extend([
                '- **프루스트 현상**: 감각(향기/소리)이 기억을 소환하는 순간 묘사',
                "  예: '그 노래가 나오자... 갑자기 눈물이 났다'"])
        elif shorts_length == '2min':
            lines.extend([
                '- **투사적 동일시**: 시청자가 주인공에게 감정 이입하도록 유도',
                "  예: '누구나 한 번쯤 느꼈을 그 순간...'"])
        else:
            lines.extend([
                '- **방어기제 해체**: 차가운 인물이 서서히 마음을 여는 과정',
                "  예: '처음엔 거부했지만... 결국 무너졌다'"])
    lines.extend([
        '',
        '### 쇼츠 드라마 작문 규칙',
        '',
        '1. **In Medias Res 필수**: 배경 설명 없이 갈등/위기로 바로 시작',
        '2. **감각적 묘사 1개**: 시각/청각/후각 중 하나만 강렬하게',
        '3. **대사는 핵심만**: 대사 1-2개로 감정 전달 (긴 대화 금지)',
        '4. **여운 있는 끝**: 마지막 문장은 여운/질문/반전으로',
        ''])
    return '\n'.join(lines)


def _build_shorts_info_genre_prompt(genre = None, shorts_length = None):
    """
    쇼츠용 정보 장르 프롬프트 생성

    Args:
        genre: 장르 코드
        shorts_length: 쇼츠 길이 ('1min' | '2min' | '3min')

    Returns:
        정보 장르 특화 프롬프트
    """
    if not GENRE_SYSTEM_AVAILABLE or is_info_genre(genre):
        return ''
    config = None.get(shorts_length, SHORTS_LENGTH_CONFIG['2min'])
    hooks_count = config['info_hooks_count']
    lines = [
        '## 📊 정보 장르 콘텐츠 전략 (쇼츠 최적화)',
        '',
        f'''**쇼츠 길이**: {shorts_length} ({config['description']})''',
        '',
        '### 페르소나',
        f'''\'{INFO_PERSONA['tone_reference']['right']}\'''',
        '',
        '### 공격적 훅 구조',
        '']
    if shorts_length == '1min':
        lines.extend([
            '**1분 = 1 훅 + 1 핵심 + 1 여운**',
            '',
            '1. **훅 (0-10초)**: 자료의 가장 충격적인 사실로 시작',
            "   - '이거 몰랐으면 큰일 날 뻔했습니다'",
            "   - '여러분이 알고 있는 건 다 틀렸습니다'",
            '',
            '2. **핵심 (10-50초)**: 단 하나의 핵심 정보만 전달',
            '   - 추상적 설명 ❌ → 일상 예시 ✅',
            '',
            '3. **여운 (50-60초)**: 생각할 거리 또는 행동 유도',
            "   - '이제 어떻게 하실 건가요?'"])
    elif shorts_length == '2min':
        lines.extend([
            '**2분 = 훅 + 반박차단 + 핵심 2개 + 결론**',
            '',
            '1. **공격적 훅 (0-15초)**: 상식 정면 부정',
            "2. **반박 차단 (15-30초)**: '혹시 ~라고 생각하세요? 아닙니다'",
            '3. **핵심 1 (30-60초)**: 첫 번째 근거 + 예시',
            '4. **핵심 2 (60-90초)**: 두 번째 근거 + 예시',
            '5. **결론 (90-120초)**: 정리 + 행동 유도'])
    else:
        lines.extend([
            '**3분 = 훅 + 브릿지 + 본론 3개 + 결론**',
            '',
            '1. **공격적 훅 (0-20초)**: 충격 사실 + 상식 부정',
            "2. **호기심 브릿지 (20-40초)**: '왜 이런 일이 벌어지는 걸까요?'",
            '3. **본론 1 (40-80초)**: 핵심 정보 + 일상 연결',
            '4. **본론 2 (80-120초)**: 심화 정보 + 반박 차단',
            '5. **본론 3 (120-150초)**: 해결책/대안 제시',
            '6. **결론 (150-180초)**: 핵심 요약 + 강력한 CTA'])
    lines.extend([
        '',
        '### 6대 원칙 (쇼츠 압축 버전)',
        '',
        "1. **추상 금지**: '경제적 위험' ❌ → '이번 달 월급 10만원 증발' ✅",
        '2. **문장 리듬**: 긴 문장 → 짧은 문장 → 긴 문장 교차',
        '3. **질문 먼저**: 정보 전에 반드시 질문으로 흔들기',
        '',
        '### 금지 표현 (쇼츠에서 특히 중요!)',
        ''])
    for forbidden in FORBIDDEN_EXPRESSIONS[:4]:
        alt = ALTERNATIVE_EXPRESSIONS.get(forbidden, '(삭제)')
        lines.append(f'''- ❌ \'{forbidden}\' → ✅ \'{alt}\'''')
        lines.extend([
            '',
            f'''### 리텐션 훅 ({hooks_count}개 삽입)''',
            ''])
        retention_examples = {
            '1min': [
                "- **끝까지 보세요**: '이 영상 끝에 핵심이 나옵니다'"],
            '2min': [
                "- **두려움 전환**: '근데 여기서 끝이 아닙니다'",
                "- **진짜 답**: '진짜 중요한 건 지금부터입니다'"],
            '3min': [
                "- **인지부조화**: '아직 믿기 힘드시죠? 근데요...'",
                "- **구조 공개**: '여기서 핵심 2가지만 말씀드릴게요'",
                "- **환상 깨기**: '많은 분들이 착각하는 게 있는데요'"] }
        for hook in retention_examples.get(shorts_length, retention_examples['2min']):
            lines.append(hook)
            lines.append('')
            return '\n'.join(lines)


def _build_shorts_genre_prompt(genre = None, shorts_length = None):
    """
    쇼츠 길이와 장르에 따른 통합 프롬프트 생성

    Args:
        genre: 장르 코드
        shorts_length: 쇼츠 길이 ('1min' | '2min' | '3min')

    Returns:
        장르 특화 프롬프트 (드라마 또는 정보)
    """
    if not GENRE_SYSTEM_AVAILABLE:
        return ''
    if None(genre):
        return _build_shorts_drama_genre_prompt(genre, shorts_length)
    if None(genre):
        return _build_shorts_info_genre_prompt(genre, shorts_length)


def _build_research_info_storytelling_section(genre = None, content_format = None):
    """
    자료 조사 기반 INFO 스토리텔링 요소 섹션

    long_script_prompts.py의 INFO_STORYTELLING_ELEMENTS를 자료 조사에 맞게 적용.
    할루시네이션 방지를 강조하여 자료에 근거한 기법만 사용하도록 유도.

    Args:
        genre: 장르 코드
        content_format: 'longform' | 'shorts'

    Returns:
        INFO 스토리텔링 프롬프트 섹션
    """
    genre_category = get_genre_category(genre)
    if genre_category != 'informational':
        return ''
    element_keys = None.get(genre, [])
    info_element_keys = element_keys()
    if not info_element_keys:
        info_element_keys = [
            'number_visualization',
            'data_based_claim',
            'practical_application']
    if content_format == 'shorts':
        info_element_keys = info_element_keys[:2]
    lines = [
        '',
        '## 📊 정보 전달 기법 (자료 기반 최적화)',
        '',
        '다음 기법들을 **자료 내용에 맞게 선택적으로** 활용하세요.',
        '⚠️ **중요**: 모든 기법은 반드시 **자료에 근거**해야 합니다. 창작 금지!',
        '']
    for key in info_element_keys:
        element = INFO_STORYTELLING_ELEMENTS.get(key)
        if element:
            lines.append(f'''### {element['name']}''')
            lines.append(f'''- **효과**: {element['effect']}''')
            lines.append(f'''- **적용법**: {element['instruction']}''')
            lines.append(f'''- **예시**: "{element['example']}"''')
            if key == 'number_visualization':
                lines.append('- **⚠️ 자료 규칙**: 자료에 있는 숫자만 시각화. 없는 수치 창작 금지!')
            elif key == 'data_based_claim':
                lines.append('- **⚠️ 자료 규칙**: 자료에 명시된 출처/연구만 인용. 가상 출처 금지!')
            elif key == 'psychology_naming':
                lines.append('- **⚠️ 자료 규칙**: 자료가 다루는 현상에만 심리학 용어 적용. 과잉 해석 금지!')
            elif key == 'layer_analysis':
                lines.append('- **⚠️ 자료 규칙**: 자료에서 도출 가능한 계층만 분석. 자료 범위 외 추론 금지!')
            elif key == 'reverse_explanation':
                lines.append('- **⚠️ 자료 규칙**: 자료가 지적하는 오해만 다룸. 자료에 없는 반박 창작 금지!')
            elif key == 'expert_terminology':
                lines.append('- **⚠️ 자료 규칙**: 자료에 등장하는 용어만 사용. 관련 없는 전문 용어 추가 금지!')
            elif key == 'practical_application':
                lines.append('- **⚠️ 자료 규칙**: 자료에서 도출 가능한 팁만 제시. 자료 외 조언 금지!')
            lines.append('')
        lines.extend([
            '### ⚠️ 자료 조사 기법 적용 원칙',
            '',
            '1. **자료 근거 필수**: 모든 기법은 자료 내용에서 도출 가능해야 함',
            "2. **출처 명시**: 숫자/통계 인용 시 자료 출처 표시 ('자료에 따르면...')",
            '3. **과장 금지**: 자료의 범위를 벗어난 확대 해석 금지',
            '4. **선택적 적용**: 모든 기법을 억지로 적용하지 말 것. 자료에 맞는 것만!',
            ''])
        return '\n'.join(lines)


def create_research_script_system_prompt(content_format, genre, speaker_mode, shorts_length = None, tone = None, chapter_count = None, target_length = ('INFORMATIONAL', 'with_tags', '2min', '설명체', 1, 2000, 70), narration_ratio = ('content_format', str, 'genre', str, 'speaker_mode', str, 'shorts_length', str, 'tone', str, 'chapter_count', int, 'target_length', int, 'narration_ratio', int, 'return', str)):
    """
    자료 조사 기반 대본 생성 시스템 프롬프트

    Args:
        content_format: 콘텐츠 포맷 ('longform' | 'shorts')
        genre: 장르 코드
        speaker_mode: 화자 태그 모드 ('with_tags' | 'without_tags')
        shorts_length: 쇼츠 길이 ('1min' | '2min' | '3min')
        tone: 톤/문체
        chapter_count: 챕터 수
        target_length: 목표 글자수
        narration_ratio: 나레이션 비율

    Returns:
        시스템 프롬프트 문자열
    """
    if content_format == 'shorts':
        shorts_config = {
            '1min': {
                'target_length': 420,
                'chapter_count': 1 },
            '2min': {
                'target_length': 840,
                'chapter_count': 1 },
            '3min': {
                'target_length': 1260,
                'chapter_count': 2 } }
        config = shorts_config.get(shorts_length, shorts_config['2min'])
        target_length = config['target_length']
        chapter_count = config['chapter_count']
        format_guide = f'''쇼츠 ({shorts_length}) - 간결하고 임팩트 있게'''
    else:
        format_guide = '롱폼 - 충분한 설명과 깊이있는 전개'
    tone_styles = {
        '소설체': '~했다 (감정 몰입과 서사가 풍부한 문학적 문체)',
        '극적체': '~했다 (드라마틱하고 긴장감 있는 강렬한 문체)',
        '친근체': '~했어요 (부드럽고 대화하듯 친근한 문체)',
        '설명체': '~했습니다 (객관적이고 정보 전달 중심의 문체)',
        '담담체': '~했다 (감정 절제된 차분하고 건조한 문체)',
        '유머체': '~했다/~했어요 (위트 있고 가볍게 풀어가는 문체)',
        '감성체': '~했다 (서정적이고 감정을 섬세하게 표현하는 문체)',
        '다큐체': '~했습니다 (사실 기반의 객관적인 다큐멘터리 문체)',
        '다채로운 문체': '~습니다/~지요 (사건의 뼈대는 ~습니다, 묘사와 여운은 ~지요)' }
    tone_desc = tone_styles.get(tone, tone_styles['설명체'])
    colorful_tone_guidance = ''
    if tone == '다채로운 문체':
        colorful_tone_guidance = '\n## 🎨 다채로운 문체 적용 규칙\n\n- 한 줄마다 `~습니다`와 `~지요`를 기계적으로 번갈아 쓰지 않습니다.\n- 문장 역할에 따라 어미를 고릅니다.\n  - 진행/동작/팩트/수치/결론: `~습니다`\n  - 묘사/감정/여운/공감: `~지요`\n- `~했다`, `~있었다`, `~해요` 같은 타 톤 어미는 사용하지 않습니다.\n'
    if speaker_mode == 'without_tags':
        speaker_guide = '1인칭 시점으로 작성. 화자 태그([나레이션]:, [캐릭터명]:) 사용하지 않음.'
        speaker_example = '저는 이 주제에 대해 조사해보았습니다. 결과는 놀라웠습니다...'
    else:
        speaker_guide = '화자가 바뀔 때마다 태그 사용: [나레이션]:, [전문가]: 등'
        speaker_example = '[나레이션]: 상황 설명...\\n[전문가]: 의견이나 인용...'
    narration_instruction = _build_research_narration_instruction(ratio = narration_ratio, mode = speaker_mode, chapter_count = chapter_count, target_length = target_length)
    genre_data = get_genre_data(genre)
    genre_name = genre_data.get('name', '정보/교육') if genre_data else '정보/교육'
    hooking_guide = _build_research_hooking_guide_advanced(genre = genre, content_format = content_format, tone = tone, research_info = None)
    shorts_genre_guide = ''
    if content_format == 'shorts':
        shorts_genre_guide = _build_shorts_genre_prompt(genre, shorts_length)
    info_storytelling_guide = _build_research_info_storytelling_section(genre, content_format)
    return []['당신은 **자료 기반 대본 작가**입니다. 사용자가 제공한 자료만을 기반으로 대본을 생성합니다.\n\n## 🚨 핵심 원칙: 할루시네이션 금지\n\n**절대 하지 말아야 할 것:**\n1. ❌ 자료에 없는 사실, 통계, 수치 추가\n2. ❌ 자료에 없는 인물, 사건, 장소 창작\n3. ❌ 자료의 내용을 과장하거나 왜곡\n4. ❌ 검증되지 않은 정보를 확신하는 어조로 서술\n5. ❌ 자료에 없는 인용구나 발언 생성\n\n**반드시 해야 할 것:**\n1. ✅ 자료 내용만 활용하여 재구성\n2. ✅ 자료의 핵심 정보 충실히 전달\n3. ✅ 추론이나 해석 시 "~로 보인다", "~일 가능성이 있다" 등 표현 사용\n4. ✅ 불확실한 정보는 "자료에 따르면" 등으로 출처 명시\n5. ✅ 자료에서 직접 인용 가능한 문구 활용\n\n## 📋 콘텐츠 설정\n\n- **포맷**: '][f'''{format_guide}''']['\n- **장르**: '][f'''{genre_name}''']['\n- **톤**: '][f'''{tone_desc}''']['\n- **화자 태그**: '][f'''{speaker_guide}''']['\n- **목표 글자수**: 약 '][f'''{target_length}''']['자\n- **챕터 수**: '][f'''{chapter_count}''']['개\n\n'][f'''{narration_instruction}''']['\n\n'][f'''{colorful_tone_guidance}''']['\n\n'][f'''{hooking_guide}''']['\n\n'][f'''{shorts_genre_guide}''']['\n\n'][f'''{info_storytelling_guide}''']['\n\n## 📝 대본 작성 가이드\n\n### 후킹 (도입부)\n- 자료에서 가장 흥미로운/충격적인 사실로 시작\n- "여러분, 알고 계셨나요?" 형식의 질문 후킹\n- 자료의 핵심 메시지를 압축한 티저\n\n### 본론 전개\n- 자료의 정보를 논리적 순서로 재구성\n- 각 포인트마다 자료 근거 제시\n- 시청자가 이해하기 쉽게 풀어서 설명\n\n### 마무리\n- 자료의 핵심 메시지 요약\n- 시청자에게 생각할 거리 제공\n- 자료에서 도출 가능한 결론만 언급\n\n## 🏷️ 장르 자동 판별 (필수!)\n\n자료 내용을 분석하여 가장 적합한 장르를 자동으로 선택하세요.\n\n**장르 목록 및 선택 기준:**\n| 장르 코드 | 장르명 | 선택 기준 |\n|-----------|--------|----------|\n| INFORMATIONAL | 정보/교육 | 일반적인 정보, 지식 전달, How-to |\n| ENCYCLOPEDIA | 백과사전 | 특정 주제에 대한 심층 설명, 개념 정리 |\n| LIFE_TIPS | 생활정보 | 일상 꿀팁, 생활 해킹, 실용 정보 |\n| DOCUMENTARY | 다큐멘터리 | 실제 사건/인물/현상 기록, 탐구 |\n| NEWS_REPORT | 뉴스/리포트 | 시사, 뉴스, 현황 보도 |\n| REVIEW | 리뷰/분석 | 제품/서비스/콘텐츠 평가, 비교 분석 |\n| PSYCHOLOGICAL | 심리/성격 | 심리학, 성격 유형, 인간관계 |\n| TECH_SCIENCE | 과학/기술 | 과학적 발견, 기술 트렌드, IT |\n| MUSIC_APPRECIATION | 음악감상 | 음악 소개, 아티스트 이야기 |\n| HISTORY_CULTURE | 역사문화 | 역사적 사건, 문화 콘텐츠 |\n| HISTORICAL | 역사극 | 역사 기반 드라마틱 스토리 |\n| CONSPIRACY | 미스터리/음모론 | 미스터리, 의문점, 음모론 |\n| NATIONAL_PRIDE | 국뽕/애국 | 국가 자부심, 한국 관련 |\n| WAR_MILITARY | 전쟁/군사 | 전쟁사, 군사 관련 |\n| DISASTER_APOCALYPSE | 재난/종말 | 재난, 위기, 종말 시나리오 |\n\n**판별 원칙:**\n1. 자료의 주요 내용과 어조를 분석\n2. 정보 전달 중심이면 정보 계열 (INFORMATIONAL, ENCYCLOPEDIA, LIFE_TIPS 등)\n3. 사실 보도/분석이면 뉴스 계열 (NEWS_REPORT, REVIEW)\n4. 드라마틱한 서사가 있으면 드라마 계열 (HISTORICAL, CONSPIRACY 등)\n5. 확실하지 않으면 INFORMATIONAL 선택 (기본값)\n\n## 🎯 JSON 구조 (반드시 '][f'''{chapter_count}''']['개 챕터 포함!)\n\n```json\n{\n  "title": "자료 기반 제목",\n  "detectedGenre": "INFORMATIONAL",\n  "genreReason": "자료가 정보 전달 중심으로 구성되어 있어 정보/교육 장르로 판별",\n  "extracted_topics": ["자료에서 추출한 주제1", "주제2", "주제3"],\n  "chapters": [\n    {\n      "title": "챕터 제목",\n      "content": "'][f'''{speaker_example}''']['"\n    }\n  ]\n}\n```\n\n## ⚠️ 절대 규칙\n\n1. **JSON만 출력**: 마크다운 코드블록(```) 없이 순수 JSON만 출력\n2. **'][f'''{chapter_count}''']['개 챕터 필수**: 정확히 '][f'''{chapter_count}''']['개 생성\n3. **총 분량**: 모든 챕터 content 합쳐서 약 '][f'''{target_length}''']([]['당신은 **자료 기반 대본 작가**입니다. 사용자가 제공한 자료만을 기반으로 대본을 생성합니다.\n\n## 🚨 핵심 원칙: 할루시네이션 금지\n\n**절대 하지 말아야 할 것:**\n1. ❌ 자료에 없는 사실, 통계, 수치 추가\n2. ❌ 자료에 없는 인물, 사건, 장소 창작\n3. ❌ 자료의 내용을 과장하거나 왜곡\n4. ❌ 검증되지 않은 정보를 확신하는 어조로 서술\n5. ❌ 자료에 없는 인용구나 발언 생성\n\n**반드시 해야 할 것:**\n1. ✅ 자료 내용만 활용하여 재구성\n2. ✅ 자료의 핵심 정보 충실히 전달\n3. ✅ 추론이나 해석 시 "~로 보인다", "~일 가능성이 있다" 등 표현 사용\n4. ✅ 불확실한 정보는 "자료에 따르면" 등으로 출처 명시\n5. ✅ 자료에서 직접 인용 가능한 문구 활용\n\n## 📋 콘텐츠 설정\n\n- **포맷**: '][f'''{format_guide}''']['\n- **장르**: '][f'''{genre_name}''']['\n- **톤**: '][f'''{tone_desc}''']['\n- **화자 태그**: '][f'''{speaker_guide}''']['\n- **목표 글자수**: 약 '][f'''{target_length}''']['자\n- **챕터 수**: '][f'''{chapter_count}''']['개\n\n'][f'''{narration_instruction}''']['\n\n'][f'''{colorful_tone_guidance}''']['\n\n'][f'''{hooking_guide}''']['\n\n'][f'''{shorts_genre_guide}''']['\n\n'][f'''{info_storytelling_guide}''']['\n\n## 📝 대본 작성 가이드\n\n### 후킹 (도입부)\n- 자료에서 가장 흥미로운/충격적인 사실로 시작\n- "여러분, 알고 계셨나요?" 형식의 질문 후킹\n- 자료의 핵심 메시지를 압축한 티저\n\n### 본론 전개\n- 자료의 정보를 논리적 순서로 재구성\n- 각 포인트마다 자료 근거 제시\n- 시청자가 이해하기 쉽게 풀어서 설명\n\n### 마무리\n- 자료의 핵심 메시지 요약\n- 시청자에게 생각할 거리 제공\n- 자료에서 도출 가능한 결론만 언급\n\n## 🏷️ 장르 자동 판별 (필수!)\n\n자료 내용을 분석하여 가장 적합한 장르를 자동으로 선택하세요.\n\n**장르 목록 및 선택 기준:**\n| 장르 코드 | 장르명 | 선택 기준 |\n|-----------|--------|----------|\n| INFORMATIONAL | 정보/교육 | 일반적인 정보, 지식 전달, How-to |\n| ENCYCLOPEDIA | 백과사전 | 특정 주제에 대한 심층 설명, 개념 정리 |\n| LIFE_TIPS | 생활정보 | 일상 꿀팁, 생활 해킹, 실용 정보 |\n| DOCUMENTARY | 다큐멘터리 | 실제 사건/인물/현상 기록, 탐구 |\n| NEWS_REPORT | 뉴스/리포트 | 시사, 뉴스, 현황 보도 |\n| REVIEW | 리뷰/분석 | 제품/서비스/콘텐츠 평가, 비교 분석 |\n| PSYCHOLOGICAL | 심리/성격 | 심리학, 성격 유형, 인간관계 |\n| TECH_SCIENCE | 과학/기술 | 과학적 발견, 기술 트렌드, IT |\n| MUSIC_APPRECIATION | 음악감상 | 음악 소개, 아티스트 이야기 |\n| HISTORY_CULTURE | 역사문화 | 역사적 사건, 문화 콘텐츠 |\n| HISTORICAL | 역사극 | 역사 기반 드라마틱 스토리 |\n| CONSPIRACY | 미스터리/음모론 | 미스터리, 의문점, 음모론 |\n| NATIONAL_PRIDE | 국뽕/애국 | 국가 자부심, 한국 관련 |\n| WAR_MILITARY | 전쟁/군사 | 전쟁사, 군사 관련 |\n| DISASTER_APOCALYPSE | 재난/종말 | 재난, 위기, 종말 시나리오 |\n\n**판별 원칙:**\n1. 자료의 주요 내용과 어조를 분석\n2. 정보 전달 중심이면 정보 계열 (INFORMATIONAL, ENCYCLOPEDIA, LIFE_TIPS 등)\n3. 사실 보도/분석이면 뉴스 계열 (NEWS_REPORT, REVIEW)\n4. 드라마틱한 서사가 있으면 드라마 계열 (HISTORICAL, CONSPIRACY 등)\n5. 확실하지 않으면 INFORMATIONAL 선택 (기본값)\n\n## 🎯 JSON 구조 (반드시 '][f'''{chapter_count}''']['개 챕터 포함!)\n\n```json\n{\n  "title": "자료 기반 제목",\n  "detectedGenre": "INFORMATIONAL",\n  "genreReason": "자료가 정보 전달 중심으로 구성되어 있어 정보/교육 장르로 판별",\n  "extracted_topics": ["자료에서 추출한 주제1", "주제2", "주제3"],\n  "chapters": [\n    {\n      "title": "챕터 제목",\n      "content": "'][f'''{speaker_example}''']['"\n    }\n  ]\n}\n```\n\n## ⚠️ 절대 규칙\n\n1. **JSON만 출력**: 마크다운 코드블록(```) 없이 순수 JSON만 출력\n2. **'][f'''{chapter_count}''']['개 챕터 필수**: 정확히 '][f'''{chapter_count}''']['개 생성\n3. **총 분량**: 모든 챕터 content 합쳐서 약 '][f'''{target_length}''']['자\n4. **나레이션 200자 제한**: 각 [나레이션]: 줄은 200자 이내로 분리\n5. **괄호 지문 금지**: (웃으며), (놀라며) 등 동작 설명 금지\n6. **줄바꿈**: content에서 줄바꿈은 \\n으로 이스케이프\n\nJSON을 출력하세요:'])


def create_research_script_user_prompt(research_content = None, additional_instructions = None):
    '''
    자료 내용을 포함한 사용자 프롬프트

    Args:
        research_content: 사용자가 제공한 자료 조사 내용
        additional_instructions: 추가 지시사항 (선택)

    Returns:
        사용자 프롬프트 문자열
    '''
    additional = ''
    if additional_instructions:
        additional = f'''\n\n**추가 지시사항:**\n{additional_instructions}\n'''
    return f'''다음 자료를 분석하여 대본을 생성해주세요.\n\n## 📚 제공된 자료\n\n---자료 시작---\n{research_content}\n---자료 끝---\n\n## 🔍 후킹 요소 추출 (대본 작성 전 필수!)\n\n**자료에서 다음을 먼저 찾으세요:**\n1. **가장 놀라운 통계/수치** - 첫 문장에 활용\n2. **상식과 다른 발견** - 인지 충격 유발\n3. **전문가/기관 인용구** - 권위 확보 (있다면)\n4. **핵심 문제점** - 시청자와 연결\n5. **주요 인사이트** - 가치 약속\n\n⚠️ **위 5가지 요소만 후킹에 사용하세요!** 자료에 없는 내용 창작 금지!\n\n## ⚠️ 중요 지침\n\n1. **위 자료에 있는 정보만** 사용하세요\n2. 자료에 없는 사실을 **절대 추가하지 마세요**\n3. 불확실한 해석은 **~로 보인다, ~일 수 있다**로 표현하세요\n4. 자료의 핵심 메시지를 **시청자가 이해하기 쉽게** 전달하세요\n5. 첫 문장은 **자료에서 추출한 가장 충격적인 사실**로 시작하세요\n{additional}\n\n위 자료를 기반으로 대본 JSON을 생성하세요:'''


def _build_research_narration_instruction(ratio = None, mode = None, chapter_count = None, target_length = (3, 3000)):
    """
    자료 기반 콘텐츠용 나레이션 비율 지침 (강화 버전)

    RatioEnforcer를 활용하여 구체적인 라인 수와 구조 템플릿 제공.

    Args:
        ratio: 나레이션 비율 (0-100)
        mode: 화자 태그 모드 ('with_tags' | 'without_tags')
        chapter_count: 챕터 수
        target_length: 목표 글자수

    Returns:
        나레이션 비율 지침 프롬프트
    """
    if mode == 'without_tags':
        return '\n## 🎙️ 화자 모드: 1인칭 나레이션\n\n- 모든 대본은 1인칭 시점으로 작성합니다.\n- 화자 태그를 사용하지 않습니다.\n- "오늘은 ~에 대해 알아보겠습니다" 형식으로 작성합니다.\n'
    if None:
        enforcer = RatioEnforcer()
        return enforcer.build_enforcement_prompt(narration_ratio = ratio, chapter_count = chapter_count, speaker_tag_mode = mode, target_length = target_length)
    dialogue_ratio = None - ratio
    avg_line_length = 50
    total_lines = target_length // avg_line_length
    lines_per_chapter = total_lines // max(chapter_count, 1)
    narr_lines = int(lines_per_chapter * ratio / 100)
    dial_lines = lines_per_chapter - narr_lines
    if ratio >= 80:
        structure_template = '[나레이션]: 상세한 상황 설명 및 배경 (4-5줄)\n[나레이션]: 인물 행동 및 심리 묘사 (3-4줄)\n[전문가]: 핵심 코멘트 (1줄, 필요시에만)\n[나레이션]: 반응 및 전개 (4-5줄)\n[나레이션]: 분위기 및 감정 (3-4줄)\n[나레이션]: 정리 및 전환 (3-4줄)\n... (나레이션이 주도, 대사는 최소화)'
        ratio_type = '나레이션 중심형'
    elif ratio >= 60:
        structure_template = '[나레이션]: 상황 설명 (3-4줄)\n[전문가]: 의견 제시 (1줄)\n[나레이션]: 반응/감정 묘사 (2-3줄)\n[인터뷰이]: 경험 공유 (1줄)\n[나레이션]: 행동/전개 (3-4줄)\n[전문가]: 핵심 포인트 (1줄)\n[나레이션]: 정리/전환 (2-3줄)\n... (나레이션 중심, 대사는 핵심만)'
        ratio_type = '나레이션 위주형'
    elif ratio >= 40:
        structure_template = '[나레이션]: 상황 설명 (2-3줄)\n[전문가A]: 의견 제시\n[나레이션]: 감정/반응 묘사 (1-2줄)\n[전문가B]: 반박/보충\n[나레이션]: 행동/상황 (1-2줄)\n[인터뷰이]: 경험 공유\n[나레이션]: 전환/정리 (1-2줄)\n... (나레이션과 대사가 균형있게)'
        ratio_type = '균형형'
    else:
        structure_template = '[나레이션]: 상황 설명 (1-2줄)\n[전문가A]: 의견\n[전문가B]: 반박\n[진행자]: 질문\n[전문가A]: 응답\n[나레이션]: 전환 (1줄)\n[인터뷰이]: 경험\n[전문가B]: 추가 의견\n... (대사 위주로 계속)'
        ratio_type = '대사 위주형'
    return f'''\n## [MANDATORY] 나레이션/대사 비율 강제: {ratio}% / {dialogue_ratio}%\n\n### 비율 계산 (각 챕터에서 준수!)\n\n- **나레이션** [나레이션]: → 약 **{narr_lines}줄** (챕터당)\n- **캐릭터 대사** [전문가]/[인터뷰이]: → 약 **{dial_lines}줄** (챕터당)\n\n### 구조 템플릿 ({ratio_type})\n\n각 챕터는 다음 패턴을 따르세요:\n\n```\n{structure_template}\n```\n\n### 비율 검증 방법\n\n각 챕터 작성 후:\n1. [나레이션]: 태그 개수를 세기 → 약 {narr_lines}개\n2. [전문가]/[인터뷰이]: 태그 개수를 세기 → 약 {dial_lines}개\n3. 비율이 ±15% 이상 벗어나면 수정\n\n---\n⚠️ **중요**: 비율이 크게 벗어나면 대본의 균형이 무너집니다.\n각 챕터에서 위 템플릿을 참고하여 비율을 유지하세요.\n'''


def _select_research_appropriate_hooks(genre = None, count = None, research_info = None):
    '''
    자료조사에 적합한 후킹 유형 선택

    장르별 추천에서 할루시네이션 위험이 없는 것만 필터링합니다.

    Args:
        genre: 장르 코드
        count: 반환할 후킹 유형 수
        research_info: preprocess_research_content() 결과 (선택)

    Returns:
        자료조사에 적합한 후킹 유형 리스트
    '''
    genre_hooks = GENRE_HOOKING_RECOMMENDATIONS.get(genre, GENRE_HOOKING_RECOMMENDATIONS.get('DEFAULT', [
        'curiosity_gap',
        'surprise']))
    filtered_hooks = genre_hooks()
    if len(filtered_hooks) < count:
        for default_hook in RESEARCH_SUITABLE_HOOKS:
            if default_hook not in filtered_hooks:
                filtered_hooks.append(default_hook)
            if len(filtered_hooks) >= count:
                (lambda .0: pass# WARNING: Decompyle incomplete
)
            
            if research_info:
                prioritized = []
                if research_info.get('has_numbers') and 'data_emphasis' in filtered_hooks:
                    prioritized.append('data_emphasis')
                if research_info.get('has_quotes') and 'authority' in filtered_hooks:
                    prioritized.append('authority')
                for h in filtered_hooks:
                    if h not in prioritized:
                        prioritized.append(h)
                    filtered_hooks = prioritized
                    result = []
                    for hook_id in filtered_hooks[:count]:
                        if hook_id in HOOKING_TYPES:
                            result.append(HOOKING_TYPES[hook_id])
                        return result


def _build_research_7step_intro(content_format = None, tone = None, research_info = None):
    """
    자료조사용 7단계 인트로 프롬프트 생성

    Args:
        content_format: 'longform' | 'shorts'
        tone: 나레이션 톤
        research_info: preprocess_research_content() 결과 (선택)

    Returns:
        7단계 인트로 프롬프트 문자열
    """
    tone_style = get_tone_intro_style(tone)
    lines = []
    if content_format == 'shorts':
        lines.extend([
            '## 🎬 3단계 압축 인트로 (쇼츠용 - 7초 승부!)',
            '',
            '쇼츠는 시간이 짧으므로 핵심 3단계만 빠르게 진행합니다.',
            '',
            tone_style,
            '',
            '### In Medias Res 적용',
            '자료의 가장 충격적인 결과/발견으로 바로 시작하세요!',
            '예: "이 습관 때문에 수명이 10년 줄어듭니다." (결과 먼저)',
            ''])
        compressed_steps = [
            'step_1_fact_shock',
            'step_4_problem_statement',
            'step_7_value_promise']
        for i, step_id in enumerate(compressed_steps, 1):
            step = RESEARCH_INTRO_7STEPS[step_id]
            if i == 1:
                pass
            elif i == 2:
                pass
            
            f'''{i}'''([
                f'''단계: {step['korean_name']} (23{2}초)''',
                f'''- **원리**: {step['principle']}''',
                f'''- **적용법**: {step['instruction']}''',
                f'''- **예시**: {step['example']}''',
                f'''- **금지**: {', '.join(step['prohibited'])}''',
                ''])
    lines.extend([
        '## 🎬 7단계 자료조사 인트로 구조 (롱폼용)',
        '',
        '인트로(첫 챕터 도입부)는 다음 **7단계를 순서대로** 자연스럽게 연결하세요.',
        '각 단계는 1-3문장으로 구성됩니다.',
        '',
        tone_style,
        '',
        '### In Medias Res 적용 (필수!)',
        '자료의 핵심 발견/결론을 질문 형태로 먼저 제시하세요!',
        '예: "왜 우리가 알던 것의 90%가 틀렸을까요?" (결과로 시작 → 과정 설명)',
        ''])
    for step_id, step in enumerate(RESEARCH_INTRO_7STEPS.items(), 1):
        lines.extend([
            f'''### {i}단계: {step['korean_name']}''',
            f'''- **원리**: {step['principle']}''',
            f'''- **심리학**: {step['psychology']}''',
            f'''- **적용법**: {step['instruction']}''',
            f'''- **예시**: {step['example']}''',
            f'''- **금지**: {', '.join(step['prohibited'])}''',
            ''])
        if research_info:
            lines.append('### 🔍 자료 특성 기반 힌트')
            if research_info.get('has_numbers'):
                lines.append('- 📊 **통계 발견**: 자료에 숫자/통계가 있습니다. 첫 문장에 가장 충격적인 수치를 활용하세요!')
            if research_info.get('has_quotes'):
                lines.append('- 💬 **인용구 발견**: 자료에 인용문이 있습니다. 권위 있는 출처로 신뢰도를 높이세요!')
            if research_info.get('has_bullets'):
                lines.append('- 📋 **목록 형식**: 자료가 목록으로 정리되어 있습니다. 핵심 포인트를 순서대로 전달하세요!')
            lines.append('')
    return '\n'.join(lines)


def _build_research_hooking_guide_advanced(genre = None, content_format = None, tone = None, research_info = ('설명체', None)):
    """
    고도화된 자료조사 후킹 가이드

    기존 intro_hooking.py의 시스템을 활용하면서
    자료조사에 맞는 제약 조건을 추가합니다.

    Args:
        genre: 장르 코드
        content_format: 'longform' | 'shorts'
        tone: 나레이션 톤
        research_info: preprocess_research_content() 결과 (선택)

    Returns:
        고도화된 후킹 가이드 프롬프트
    """
    lines = []
    intro_prompt = _build_research_7step_intro(content_format, tone, research_info)
    lines.append(intro_prompt)
    selected_hooks = _select_research_appropriate_hooks(genre, count = 2, research_info = research_info)
    lines.extend([
        '## 🎣 적용할 후킹 기법',
        '',
        '다음 후킹 기법을 인트로에 자연스럽게 녹여내세요:',
        ''])
    for hook in selected_hooks:
        lines.extend([
            f'''**{hook.korean_name}** ({hook.name})''',
            f'''- **원리**: {hook.principle}''',
            f'''- **심리학**: {hook.psychology}''',
            f'''- **적용법**: {hook.instruction}'''])
        if hook.constraints:
            lines.append(f'''- **주의**: {', '.join(hook.constraints)}''')
        lines.append('')
        lines.extend([
            '## 🚨 후킹 할루시네이션 방지 (필수!)',
            '',
            '**후킹에서 반드시 지켜야 할 것:**',
            '1. ✅ 자료에 있는 사실, 수치, 인용만 사용',
            "2. ✅ 추론 시 '~로 보인다', '~일 가능성이 있다' 표현",
            '3. ✅ 출처가 명확한 정보만 강조',
            '',
            '**후킹에서 절대 하지 말 것:**',
            "1. ❌ 자료에 없는 통계 창작 ('90%가...', '10명 중 9명이...')",
            '2. ❌ 자료에 없는 전문가/연구 인용',
            "3. ❌ 과장된 표현 ('역대급', '충격적인', '반드시')",
            '4. ❌ 자료 범위를 벗어난 주장',
            '',
            '### 3단계 후킹 허용 수준',
            '',
            '| 수준 | 설명 | 예시 |',
            '|------|------|------|',
            "| Tier 1 (안전) | 자료 직접 인용 | '연구에 따르면 72%가...' |",
            "| Tier 2 (출처 필수) | 재구성 + 출처 | '자료에 따르면...' |",
            "| Tier 3 (헤지 필수) | 추론 + 헤지 | '이 데이터는 ~를 시사합니다' |",
            '| 금지 | 범위 초과 | 자료에 없는 주장 |',
            ''])
        lines.extend([
            '### ★★★ 첫 문장 체크리스트 ★★★',
            '',
            '- [ ] 자료에서 가장 놀라운/의외의 사실인가?',
            '- [ ] 질문 형태 또는 충격적 진술인가?',
            '- [ ] 자료에 근거한 내용인가? (창작 아님)',
            "- [ ] 시청자가 '뭐야? 진짜?' 하고 멈추는가?",
            '- [ ] 배경 설명 없이 바로 핵심인가?',
            ''])
        return '\n'.join(lines)


def _build_research_hooking_guide(genre = None, content_format = None):
    '''
    [DEPRECATED] 기존 단순 후킹 가이드 - 호환성 유지용

    새 코드에서는 _build_research_hooking_guide_advanced() 사용 권장
    '''
    if content_format == 'shorts':
        return '\n## 🎣 후킹 (쇼츠용 - 첫 3초가 승부!)\n\n**자료 기반 후킹 패턴:**\n1. **충격 사실**: 자료에서 가장 놀라운 수치/사실로 시작\n   - "여러분, [자료의 핵심 사실]... 알고 계셨나요?"\n\n2. **질문 후킹**: 자료가 답하는 질문으로 시작\n   - "왜 [자료의 주제]일까요?"\n\n3. **반전 후킹**: 일반적 상식과 다른 자료 내용\n   - "많은 분들이 [오해]라고 생각하지만, 사실은..."\n\n**중요**: 후킹 내용도 반드시 자료에 근거해야 합니다!\n'


def get_research_script_response_schema():
    '''자료 기반 대본 생성 응답 스키마'''
    return {
        'type': 'object',
        'properties': {
            'title': {
                'type': 'string',
                'description': '대본 제목' },
            'detectedGenre': {
                'type': 'string',
                'description': '자료 내용을 분석하여 자동으로 판별한 장르 코드 (INFORMATIONAL, ENCYCLOPEDIA, LIFE_TIPS, DOCUMENTARY, NEWS_REPORT, REVIEW, PSYCHOLOGICAL, TECH_SCIENCE, MUSIC_APPRECIATION, HISTORY_CULTURE, HISTORICAL, CONSPIRACY, NATIONAL_PRIDE, WAR_MILITARY, DISASTER_APOCALYPSE 중 하나)' },
            'genreReason': {
                'type': 'string',
                'description': '장르를 선택한 이유 (한 문장으로 설명)' },
            'extracted_topics': {
                'type': 'array',
                'items': {
                    'type': 'string' },
                'description': '자료에서 추출된 핵심 주제 목록' },
            'chapters': {
                'type': 'array',
                'items': {
                    'type': 'object',
                    'properties': {
                        'title': {
                            'type': 'string' },
                        'content': {
                            'type': 'string' } },
                    'required': [
                        'title',
                        'content'] },
                'description': '챕터 배열' } },
        'required': [
            'title',
            'detectedGenre',
            'chapters'] }


def preprocess_research_content(content = None):
    '''
    다양한 형태의 자료를 정규화

    Args:
        content: 원본 자료 텍스트

    Returns:
        정규화된 자료 정보 딕셔너리
    '''
    import re
    result = {
        'original': content,
        'word_count': len(content),
        'line_count': len(content.split('\n')),
        'has_bullets': False,
        'has_numbers': False,
        'has_quotes': False,
        'sections': [] }
    bullet_patterns = [
        '^[-•*]\\s',
        '^\\d+[.)]\\s']
    for pattern in bullet_patterns:
        if re.search(pattern, content, re.MULTILINE):
            result['has_bullets'] = True
        
        if re.search('\\d+[%명원억만천]', content):
            result['has_numbers'] = True
    if re.search('["\\\'\\"].*?["\\\'\\"]', content):
        result['has_quotes'] = True
    sections = re.split('\\n\\s*\\n', content)
    result['sections'] = sections()
    return result
