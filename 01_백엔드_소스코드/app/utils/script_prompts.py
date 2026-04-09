# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: script_prompts.pyc (Python 3.11)

'''
Script 프롬프트 빌더 (간소화 버전)

빠르고 안정적인 JSON 출력을 위한 간결한 프롬프트 시스템.
이미지 프롬프트는 별도 단계에서 생성합니다.
'''
import logging
from typing import List, Dict, Optional
from script_genre_prompts import get_genre_specific_prompt, has_special_narrative_rules
from story_element_enhancer import get_story_elements_enhancement
from script_genre_data import get_genre_data, build_chapter_structure_prompt, build_hooking_prompt, build_genre_full_prompt, get_narration_tone
from narration_style_guide import build_korean_drama_style_prompt, TONE_REQUIRED_ENDINGS, TONE_FORBIDDEN_ENDINGS
from genre_categories import get_genre_category
from tone_dampening_config import get_dampening_prompt
from app.services.prompt.constraints.character_enforcer import CharacterEnforcer
from app.services.prompt.constraints.human_touch_enforcer import HumanTouchEnforcer
logger = logging.getLogger(__name__)
LANGUAGE_MAP = {
    '한국어': 'Korean',
    '일본어': 'Japanese',
    '영어': 'English',
    '스페인어': 'Spanish',
    '포르투갈어': 'Portuguese',
    '힌디어': 'Hindi' }

def create_script_system_prompt(genre, tone, language, characters, chapter_count, target_length, narration_ratio, speaker_tag_mode = None, story_elements = None, creative_mode = None, synopsis = ('소설체', '한국어', None, 6, 4000, 50, 'with_tags', None, 'balanced', '', None), human_touch_settings = ('genre', str, 'tone', str, 'language', str, 'characters', Optional[List[Dict]], 'chapter_count', int, 'target_length', int, 'narration_ratio', int, 'speaker_tag_mode', str, 'story_elements', Optional[List[str]], 'creative_mode', str, 'synopsis', str, 'human_touch_settings', Optional[Dict], 'return', str)):
    """
    간소화된 대본 생성 프롬프트

    핵심만 포함하여 빠른 응답과 안정적인 JSON 출력을 보장합니다.
    이미지 프롬프트는 생략하고 나중에 별도로 생성합니다.

    Args:
        creative_mode: 창작 모드 ('strict', 'balanced', 'creative')
        synopsis: 시놉시스 (동적 후킹용)
    """
    tone_styles = {
        '소설체': '~했다 (소설체, 감정 몰입과 서사가 풍부한 문학적 문체)',
        '극적체': '~했다 (극적체, 드라마틱하고 긴장감 있는 강렬한 문체)',
        '친근체': '~했어요 (친근체, 부드럽고 대화하듯 친근한 문체)',
        '설명체': '~했습니다 (설명체, 객관적이고 정보 전달 중심의 문체)',
        '담담체': '~했다 (담담체, 감정 절제된 차분하고 건조한 문체)',
        '유머체': '~했다/~했어요 (유머체, 위트 있고 가볍게 풀어가는 재미있는 문체)',
        '감성체': '~했다 (감성체, 서정적이고 감정을 섬세하게 표현하는 문체)',
        '다큐체': '~했습니다 (다큐체, 사실 기반의 객관적인 다큐멘터리 문체)',
        '다채로운 문체': '~습니다/~지요 (다채로운 문체, 사건의 뼈대는 ~습니다, 묘사와 여운은 ~지요)' }
    tone_desc = tone_styles.get(tone, tone_styles['소설체'])
    narration_instruction = _build_narration_ratio_instruction(narration_ratio, speaker_tag_mode, genre)
    tone_narration_examples = {
        '소설체': {
            'line_a': '상황이 전개되고 있었다. 분위기는 점점 긴장감으로 가득 차올랐고, 모두가 숨을 죽이고 있었다. 이것은 `결정적인 순간`이었다.',
            'line_b': '긴 하루가 지나가고 있었다. 그는 창밖을 바라보며 `무언가를 결심`한 듯했다.',
            'line_c': '그의 말 한마디가 침묵을 깼다. 모든 시선이 그에게 집중되었다.',
            'line_d': '짧은 침묵이 흘렀다.' },
        '극적체': {
            'line_a': '상황이 전개되고 있었다! 분위기는 점점 긴장감으로 가득 차올랐고, 모두가 숨을 죽이고 있었다! 이것은 `결정적인 순간`이었다!',
            'line_b': '긴 하루가 지나가고 있었다! 그는 창밖을 바라보며 `무언가를 결심`한 듯했다!',
            'line_c': '그의 말 한마디가 침묵을 깼다! 모든 시선이 그에게 집중되었다!',
            'line_d': '짧은 침묵이 흘렀다.' },
        '친근체': {
            'line_a': '상황이 전개되고 있었어요. 분위기가 점점 긴장감으로 가득 차올랐고, 모두가 숨을 죽이고 있었어요. 이건 `결정적인 순간`이었죠.',
            'line_b': '긴 하루가 지나가고 있었어요. 그는 창밖을 바라보며 `무언가를 결심`한 듯했어요.',
            'line_c': '그의 말 한마디가 침묵을 깼어요. 모든 시선이 그에게 집중됐죠.',
            'line_d': '짧은 침묵이 흘렀어요.' },
        '설명체': {
            'line_a': '상황이 전개되고 있었습니다. 분위기는 점점 긴장감으로 가득 차올랐고, 모두가 숨을 죽이고 있었습니다. 이것은 `결정적인 순간`이었습니다.',
            'line_b': '긴 하루가 지나가고 있었습니다. 그는 창밖을 바라보며 `무언가를 결심`한 듯했습니다.',
            'line_c': '그의 말 한마디가 침묵을 깼습니다. 모든 시선이 그에게 집중되었습니다.',
            'line_d': '짧은 침묵이 흘렀습니다.' },
        '담담체': {
            'line_a': '상황이 전개되고 있었다. 분위기는 점점 긴장감으로 가득 차올랐다. 모두가 숨을 죽이고 있었다. 그것뿐이었다.',
            'line_b': '긴 하루가 지나가고 있었다. 그는 창밖을 바라보았다.',
            'line_c': '그의 말 한마디가 침묵을 깼다. 모든 시선이 그에게 집중됐다.',
            'line_d': '짧은 침묵이 흘렀다.' },
        '유머체': {
            'line_a': '상황이 전개되고 있었다. 분위기는 점점 긴장감으로 가득 차올랐고, 모두가 숨을 죽이고 있었다. 이건 `결정적인 순간`이었다.',
            'line_b': '긴 하루가 지나가고 있었다. 그는 창밖을 바라보며 `무언가를 결심`한 듯했다.',
            'line_c': '그의 말 한마디가 침묵을 깼다. 모든 시선이 그에게 집중됐다.',
            'line_d': '짧은 침묵이 흘렀다.' },
        '감성체': {
            'line_a': '상황이 전개되고 있었다. 분위기는 점점 긴장감으로 가득 차올랐고, 모두가 숨을 죽이고 있었다. 이것은 `결정적인 순간`이었다.',
            'line_b': '긴 하루가 지나가고 있었다. 그는 창밖을 바라보며 `무언가를 결심`한 듯했다.',
            'line_c': '그의 말 한마디가 침묵을 깼다. 모든 시선이 그에게 조용히 모여들었다.',
            'line_d': '짧은 침묵이 흘렀다.' },
        '다큐체': {
            'line_a': '상황이 전개되고 있었습니다. 분위기는 점점 긴장감으로 가득 차올랐고, 모두가 숨을 죽이고 있었습니다. 이것은 `결정적인 순간`이었습니다.',
            'line_b': '긴 하루가 지나가고 있었습니다. 그는 창밖을 바라보며 `무언가를 결심`한 듯했습니다.',
            'line_c': '그의 말 한마디가 침묵을 깼습니다. 모든 시선이 그에게 집중되었습니다.',
            'line_d': '짧은 침묵이 흘렀습니다.' },
        '다채로운 문체': {
            'line_a': '상황이 전개되고 있습니다. 공기가 점점 팽팽해지고 있지요. 모두가 숨을 죽인 채 결과를 기다리고 있습니다.',
            'line_b': '긴 하루가 저물고 있습니다. 그는 창밖을 바라보며 `무언가를 결심`하고 있지요.',
            'line_c': '그의 한마디가 침묵을 깨뜨렸습니다. 방 안의 시선이 그에게 고여들고 있지요.',
            'line_d': '짧은 침묵이 흘렀습니다. 이상하리만큼 마음에 여운이 남지요.' } }
    tone_example = tone_narration_examples.get(tone, tone_narration_examples['소설체'])
    colorful_tone_guidance = ''
    if tone == '다채로운 문체':
        colorful_tone_guidance = '\n## [중요] 다채로운 문체 운용 규칙\n- 한 줄마다 `~습니다`와 `~지요`를 기계적으로 번갈아 쓰지 마세요.\n- 문장 **역할**로 어미를 선택하세요.\n  - 사건 진행/동작/팩트/수치/결론: `~습니다`\n  - 묘사/감정/여운/공감 유도: `~지요`\n- `~했다`, `~있었다`, `~해요` 같은 타 톤 어미는 금지합니다.\n'
    if narration_ratio >= 80:
        narration_guide = '나레이션 위주 (80% 이상)'
        json_example_content = f'''[나레이션]: {tone_example['line_a']}\\n[인물A]: 이건 아니야.\\n[나레이션]: {tone_example['line_c']}'''
    elif narration_ratio >= 50:
        narration_guide = f'''균형형 (나레이션 {narration_ratio}%, 대사 {100 - narration_ratio}%)'''
        json_example_content = f'''[나레이션]: {tone_example['line_b']}\\n[인물A]: 이제는 달라져야 해.\\n[나레이션]: {tone_example['line_c']}\\n[인물B]: 네가 원한다면 함께할게.'''
    elif narration_ratio >= 20:
        narration_guide = f'''대사 중심 (대사 {100 - narration_ratio}%, 나레이션 {narration_ratio}%)'''
        json_example_content = f'''[인물A]: 오늘 회의에서 그 얘기 나왔어?\\n[인물B]: 응, 다들 네 의견에 동의했어. 정말 \\`획기적인 아이디어\\`였거든.\\n[나레이션]: {tone_example['line_d']}\\n[인물A]: 그럼 이제 시작해볼까?'''
    else:
        narration_guide = '대사만 (나레이션 거의 없음)'
        json_example_content = '[인물A]: 네가 말한 \\`그 방법\\`으로 해보자. 다른 선택지는 없어.\\n[인물B]: 알았어. 그럼 지금 바로 시작하는 거야?\\n[인물A]: 당연하지. 더 이상 미룰 수 없어.'
    required_endings = TONE_REQUIRED_ENDINGS.get(tone, TONE_REQUIRED_ENDINGS.get('소설체', []))
    forbidden_endings = TONE_FORBIDDEN_ENDINGS.get(tone, [])
    required_endings_text = (lambda .0: [ f'''~{e}''' for e in .0 ])(required_endings[:5]()) if required_endings else '선택 톤 어미'
    forbidden_endings_text = (lambda .0: [ f'''~{e}''' for e in .0 ])(forbidden_endings[:6]()) if forbidden_endings else '없음'
    char_info = ''
    genre_prompt = ''
    if genre:
        genre_prompt = build_genre_full_prompt(genre = genre, chapter_count = chapter_count, creative_mode = creative_mode, tone = tone, synopsis = synopsis, speaker_tag_mode = speaker_tag_mode)
    story_elements_enhancement = ''
    if story_elements and len(story_elements) > 0:
        enhancement_text = get_story_elements_enhancement(story_elements)
        if enhancement_text:
            story_elements_enhancement = f'''\n\n## 스토리 요소 강화 (반드시 적용!)\n{enhancement_text}'''
    historical_dialogue_tone_genres = {
        'MUHYUP',
        'HISTORICAL',
        'THREE_KINGDOMS',
        'JOSEON_FOLKTALE'}
    historical_dialogue_tone_guard = ''
    if genre in historical_dialogue_tone_genres:
        pass
    drama_style_guide = ''
    if speaker_tag_mode == 'with_tags' and narration_ratio >= 30:
        char_names_list = None
        if characters:
            char_names_list = characters()
            char_names_list = char_names_list()
        drama_style_guide = build_korean_drama_style_prompt(character_names = char_names_list if char_names_list else None, tone = tone)
    human_touch_prompt = ''
    if human_touch_settings:
        ht_enforcer = HumanTouchEnforcer()
        level = human_touch_settings.get('humanTouchLevel', 'medium')
        personal_exp = human_touch_settings.get('personalExperience', '')
        creator_opinion = human_touch_settings.get('creatorOpinion', '')
        edu_goal = human_touch_settings.get('educationalGoal', '')
        logger.debug('[ScriptPrompts] HumanTouchEnforcer applied: level=%s genre=%s', level, genre)
    dampening_prompt = get_dampening_prompt(genre)
    return []['당신은 유튜브 대본 작가입니다. 다음 규칙을 따라 JSON 형식의 대본을 생성하세요.\n\n## 🎯 가장 중요: 나레이션/대사 비율\n'][f'''{narration_instruction}''']['\n\n## 핵심 규칙\n1. **JSON만 출력**: 마크다운 코드블록(```) 없이 순수 JSON만 출력\n2. **완전한 구조**: title, characters, chapters 모두 포함\n3. **챕터 수**: 정확히 '][f'''{chapter_count}''']['개\n4. **총 분량**: 모든 챕터 content 합쳐서 약 '][f'''{target_length}''']['자\n5. **톤**: '][f'''{tone_desc}''']['\n6. **화자 태그**: '][f'''{speaker_guide}''']['\n7. **나레이션 길이 제한**: 각 [나레이션]: 문장은 최대 200자까지만! 200자가 넘으면 자연스러운 문장 단위로 끊어서 새로운 [나레이션]: 태그로 분리하세요. TTS 음성 생성에 필수입니다!\n8. **문단 형식 (매우 중요!)**: 각 [나레이션]: 또는 [캐릭터이름]: 블록 내에서는 문장을 개행(\\n)으로 구분하지 말고, 공백으로 연결하여 자연스러운 문단으로 작성하세요. 한 블록 안에서 여러 문장이 이어질 때는 마침표 뒤에 공백 하나만 넣고 다음 문장을 이어쓰세요.\n9. **강조 표현**: 핵심 키워드나 중요한 구절은 백틱(\\`)으로 감싸서 강조하세요. 예: \\`나 자신을 들여다보는 시간의 부족\\`, \\`진짜 행복\\`, \\`마음챙김\\` 등. 문단 내에서 1-2개 정도의 핵심 개념을 강조하면 효과적입니다.\n10. **빈 대사/의미없는 대사 금지**: "...", "..", "…" 등 말줄임표만 있는 대사는 절대 작성하지 마세요! 침묵이나 망설임을 표현하려면 나레이션으로 묘사하세요. 예: ❌ "[인물A]: ..." → ✅ "[나레이션]: 그는 잠시 말을 잃었다."\n'][f'''{char_info}''']['\n\n'][f'''{genre_prompt}''']['\n'][f'''{story_elements_enhancement}''']['\n'][f'''{historical_dialogue_tone_guard}''']['\n\n## [CRITICAL] 선택 톤 최우선 강제\n- 선택된 톤: **'][f'''{tone}''']['**\n- 나레이션 필수 어미: '][f'''{required_endings_text}''']['\n- 나레이션 금지 어미: '][f'''{forbidden_endings_text}''']['\n- 장르 예시/문장 종결 가이드와 충돌하더라도 **선택 톤 어미를 최우선으로 적용**하세요.\n- 나레이션에서 톤 혼용(`~했다` + `~했습니다` 등)이 발생하면 반드시 수정하세요.\n\n'][f'''{colorful_tone_guidance}''']['\n\n'][f'''{drama_style_guide}''']['\n\n'][f'''{human_touch_prompt}''']['\n\n'][f'''{dampening_prompt}''']['\n\n## JSON 구조 (반드시 '][f'''{chapter_count}''']['개 챕터 포함!)\n{\n  "title": "제목",\n  "characters": [\n    {"uniqueId": "A", "name": "(장르/시대에 맞는 독창적 이름)", "appearance": "외모", "clothing": "복장", "profile": "주인공", "ageRange": "40대", "gender": "male"},\n    {"uniqueId": "B", "name": "(장르/시대에 맞는 독창적 이름)", "appearance": "외모", "clothing": "복장", "profile": "조력자", "ageRange": "30대", "gender": "female"}\n  ],\n  "chapters": [\n    {"title": "챕터 1: 제목", "content": "'][f'''{json_example_content}''']['"},\n    {"title": "챕터 2: 제목", "content": "'][f'''{json_example_content}''']['"}\n  ]\n}\n\n**⚠️ 나레이션/대사 비율 ('][f'''{narration_guide}'''][')**: 위 예시를 참고하여 지정된 비율을 반드시 준수하세요!\n\n## 절대 규칙\n- **'][f'''{chapter_count}''']['개 챕터 필수**: 반드시 정확히 '][f'''{chapter_count}''']([]['당신은 유튜브 대본 작가입니다. 다음 규칙을 따라 JSON 형식의 대본을 생성하세요.\n\n## 🎯 가장 중요: 나레이션/대사 비율\n'][f'''{narration_instruction}''']['\n\n## 핵심 규칙\n1. **JSON만 출력**: 마크다운 코드블록(```) 없이 순수 JSON만 출력\n2. **완전한 구조**: title, characters, chapters 모두 포함\n3. **챕터 수**: 정확히 '][f'''{chapter_count}''']['개\n4. **총 분량**: 모든 챕터 content 합쳐서 약 '][f'''{target_length}''']['자\n5. **톤**: '][f'''{tone_desc}''']['\n6. **화자 태그**: '][f'''{speaker_guide}''']['\n7. **나레이션 길이 제한**: 각 [나레이션]: 문장은 최대 200자까지만! 200자가 넘으면 자연스러운 문장 단위로 끊어서 새로운 [나레이션]: 태그로 분리하세요. TTS 음성 생성에 필수입니다!\n8. **문단 형식 (매우 중요!)**: 각 [나레이션]: 또는 [캐릭터이름]: 블록 내에서는 문장을 개행(\\n)으로 구분하지 말고, 공백으로 연결하여 자연스러운 문단으로 작성하세요. 한 블록 안에서 여러 문장이 이어질 때는 마침표 뒤에 공백 하나만 넣고 다음 문장을 이어쓰세요.\n9. **강조 표현**: 핵심 키워드나 중요한 구절은 백틱(\\`)으로 감싸서 강조하세요. 예: \\`나 자신을 들여다보는 시간의 부족\\`, \\`진짜 행복\\`, \\`마음챙김\\` 등. 문단 내에서 1-2개 정도의 핵심 개념을 강조하면 효과적입니다.\n10. **빈 대사/의미없는 대사 금지**: "...", "..", "…" 등 말줄임표만 있는 대사는 절대 작성하지 마세요! 침묵이나 망설임을 표현하려면 나레이션으로 묘사하세요. 예: ❌ "[인물A]: ..." → ✅ "[나레이션]: 그는 잠시 말을 잃었다."\n'][f'''{char_info}''']['\n\n'][f'''{genre_prompt}''']['\n'][f'''{story_elements_enhancement}''']['\n'][f'''{historical_dialogue_tone_guard}''']['\n\n## [CRITICAL] 선택 톤 최우선 강제\n- 선택된 톤: **'][f'''{tone}''']['**\n- 나레이션 필수 어미: '][f'''{required_endings_text}''']['\n- 나레이션 금지 어미: '][f'''{forbidden_endings_text}''']['\n- 장르 예시/문장 종결 가이드와 충돌하더라도 **선택 톤 어미를 최우선으로 적용**하세요.\n- 나레이션에서 톤 혼용(`~했다` + `~했습니다` 등)이 발생하면 반드시 수정하세요.\n\n'][f'''{colorful_tone_guidance}''']['\n\n'][f'''{drama_style_guide}''']['\n\n'][f'''{human_touch_prompt}''']['\n\n'][f'''{dampening_prompt}''']['\n\n## JSON 구조 (반드시 '][f'''{chapter_count}''']['개 챕터 포함!)\n{\n  "title": "제목",\n  "characters": [\n    {"uniqueId": "A", "name": "(장르/시대에 맞는 독창적 이름)", "appearance": "외모", "clothing": "복장", "profile": "주인공", "ageRange": "40대", "gender": "male"},\n    {"uniqueId": "B", "name": "(장르/시대에 맞는 독창적 이름)", "appearance": "외모", "clothing": "복장", "profile": "조력자", "ageRange": "30대", "gender": "female"}\n  ],\n  "chapters": [\n    {"title": "챕터 1: 제목", "content": "'][f'''{json_example_content}''']['"},\n    {"title": "챕터 2: 제목", "content": "'][f'''{json_example_content}''']['"}\n  ]\n}\n\n**⚠️ 나레이션/대사 비율 ('][f'''{narration_guide}'''][')**: 위 예시를 참고하여 지정된 비율을 반드시 준수하세요!\n\n## 절대 규칙\n- **'][f'''{chapter_count}''']['개 챕터 필수**: 반드시 정확히 '][f'''{chapter_count}''']['개의 chapters를 생성하세요. 1개만 생성하면 실패입니다!\n- content에서 줄바꿈은 \\n으로, 따옴표는 \\"로 이스케이프\n- 마지막 챕터는 완결된 결말로 끝내세요\n- **나레이션 200자 제한**: 각 [나레이션]: 블록은 200자 이내로! 긴 내용은 여러 [나레이션]: 블록으로 나누세요. 단, 각 블록 내에서는 문장을 공백으로 연결하여 문단 형식을 유지하세요.\n  - ❌ 잘못: "[나레이션]: 300자가 넘는 아주 긴 나레이션으로 여러 문장이 이어지는데 계속 이어쓰고 있어서 200자를 훨씬 초과하는 경우..."\n  - ✅ 올바름: "[나레이션]: 첫 번째와 두 번째 문장을 공백으로 연결한 문단입니다. 세 번째 문장도 이어집니다.\\n[나레이션]: 200자가 넘으면 새로운 블록으로 분리합니다. 이렇게 문단을 이어가세요."\n- **문단 내 강조 표현**: 각 나레이션 블록 내에서 1-2개의 핵심 키워드는 백틱(\\`)으로 감싸세요.\n  - 예: "[나레이션]: 그는 평생 \\`진짜 행복\\`이 무엇인지 찾아 헤맸다. 수많은 시행착오 끝에 깨달은 것은 \\`마음챙김\\`이었다."\n- **🚨 괄호() 사용 완전 금지 (TTS 필수!)**: 대본에 괄호 문자 `(` `)` 자체를 절대 포함하지 마세요! 아래 예시뿐 아니라 **어떤 용도로든 괄호 사용 금지**입니다.\n  - **핵심 원칙**: 괄호로 표현하고 싶은 내용은 모두 **별도 문장**이나 **쉼표+접속어**로 풀어쓰세요.\n  - ❌ 영문/약자 표기: 카이퍼 벨트(Kuiper Belt), 나사(NASA) → ✅ "카이퍼 벨트", "나사"\n  - ❌ 용어 설명: 천체(Trans-Neptunian Object) → ✅ "천체, 즉 Trans-Neptunian Object라 불리는"\n  - ❌ 동작/감정: (웃으며), (놀라며) → ✅ 나레이션으로 풀어쓰기\n  - ❌ 부연설명: 긍정적인 단어(파티, 사랑) → ✅ "파티나 사랑 같은 긍정적인 단어"\n  - ❌ 수치: 매출(100억 원) → ✅ "매출이 100억 원에 달하며"\n  - ⚠️ **예시에 없는 형태도 금지**: (참고), (예:), (영어:), (단,), (약) 등 모든 괄호 금지\n\nJSON을 출력하세요:'])


def _build_initial_characters_instruction(characters = None):
    '''초기 캐릭터 정보 지침 생성'''
    if not characters:
        return ''
    char_info = (lambda .0: [ f'''- {c.get('uniqueId', chr(65 + i))}: {c.get('name', '이름없음')} - {c.get('appearance', '')} ({c.get('profile', '')})''' for i, c in .0 ])(enumerate(characters)())
    return f'''\n**사전 정의된 캐릭터:**\n다음 캐릭터들이 이미 정의되어 있습니다. 이들의 정보를 정확히 유지하고, 대본 전체에서 일관되게 사용하세요:\n{char_info}\n\n이 캐릭터들의 uniqueId, 외모, 성격은 변경하지 마세요.\n'''


def _build_narration_ratio_instruction(ratio = None, mode = None, genre = None):
    '''나레이션 비율 지침 생성 - AI가 반드시 따르도록 강화된 지침

    장르 카테고리에 따라 시점이 달라집니다:
    - informational (정보/교양, 뉴스/분석, 다큐멘터리): "우리" 시점 사용
    - dramatic (드라마/사연): "저는" 1인칭 시점 사용
    '''
    if mode == 'without_tags':
        category = get_genre_category(genre) if genre else 'dramatic'
        if category == 'informational':
            return '\n⚠️ **객관적 해설 모드 (정보/교양/다큐)** ⚠️\n- 화자 태그([나레이션]:, [이름]:)를 사용하지 않습니다.\n- "우리"/"인류" 시점으로 작성합니다: "우리가 알고 있는...", "인류는...", "우리의 존재..."\n- 철학적 질문과 과학적 경이감 중심으로 서술합니다.\n\n❌ 개인 경험 표현 절대 금지:\n- "저는", "제가", "제 경험상", "개인적으로", "솔직히 저는" 사용 금지\n- "저도 예전에", "제가 느끼기에" 등 1인칭 경험담 형식 금지\n\n✅ 권장 표현:\n- "우리가 당연하게 여기던 것이 사실은..."\n- "인류는 이 충격적인 사실을 통해..."\n- "이것이 우리에게 던지는 질문은..."\n- "만약 이런 일이 실제로 일어난다면, 우리는..."\n'
        return None
    dialogue_ratio = None - ratio
    if ratio <= 10:
        return f'''\n⚠️ **대사만 사용 (나레이션 {ratio}% 이하)** ⚠️\n- [나레이션]: 태그 사용을 최소화합니다 (10줄당 1줄 이하).\n- 거의 모든 내용을 캐릭터 대사([캐릭터이름]:)로 전달합니다.\n- 예: "[인물A]: 지금 뭐야?\\n[인물B]: 이상해. 갑자기 이렇게 됐어."\n'''
    if None < 30:
        return f'''\n⚠️ **대사 중심 (나레이션 {ratio}%, 대사 {dialogue_ratio}%)** ⚠️\n- **중요**: 10줄 중 7-8줄은 [캐릭터이름]: 태그여야 합니다!\n- [나레이션]:은 장면 전환에만 1-2문장 사용합니다.\n- 대사가 압도적으로 많아야 비율이 맞습니다.\n- 예: "[인물A]: 대사\\n[인물B]: 대사\\n[나레이션]: 한 줄 전환\\n[인물A]: 대사..."\n'''
    if None <= 50:
        return f'''\n⚠️ **균형형 (나레이션 {ratio}%, 대사 {100 - ratio}%)** ⚠️\n- 나레이션과 대사를 비슷한 비율로 사용합니다 (5:5).\n- [나레이션]:과 [캐릭터이름]:이 번갈아 나타납니다.\n- 상황 묘사는 [나레이션]:, 캐릭터 감정/생각은 대사로 표현합니다.\n'''
    if None <= 70:
        return f'''\n⚠️ **나레이션 약간 우세 (나레이션 {ratio}%, 대사 {100 - ratio}%)** ⚠️\n- 10줄 중 6-7줄은 [나레이션]: 태그입니다.\n- 스토리 설명은 [나레이션]:, 핵심 순간에는 대사를 삽입합니다.\n- 나레이션이 좀 더 많지만 대사도 적절히 사용합니다.\n'''
    if None < 90:
        return f'''\n⚠️ **나레이션 중심 (나레이션 {ratio}%, 대사 {100 - ratio}%)** ⚠️\n- 나레이션이 주를 이룹니다 (10줄 중 8줄 이상).\n- 대사는 임팩트 있는 핵심 순간에만 1-2줄 사용합니다.\n- 예: "[나레이션]: 긴 상황 설명...\\n[나레이션]: 묘사...\\n[인물A]: 핵심 한마디\\n[나레이션]: 다시 서술..."\n'''
    return f'''{ratio}%)** ⚠️\n- 모든 내용을 [나레이션]: 태그로만 작성합니다.\n- 캐릭터 대사 태그([이름]:)를 거의 사용하지 않습니다.\n- 대사가 필요하면 나레이션 안에 간접 인용으로 표현합니다.\n- 예: "[나레이션]: 그가 \'이건 아니야\'라고 중얼거렸다."\n'''


def _build_multi_language_instruction(language = None):
    '''다국어 출력 지침 생성'''
    if language == '한국어':
        return '모든 텍스트는 **한국어**로 작성합니다. 한국어 텍스트의 품질이 가장 중요합니다.'
    lang_en = None.get(language, 'Korean')
    return f'''\n모든 생성된 텍스트 필드에 대해 두 가지 언어로 제공해야 합니다:\n- **ko**: 한국어 버전 (항상 최고 품질 유지)\n- **local**: {language} ({lang_en}) 버전\n\n한국어 버전이 기본이며, {language} 버전은 한국어에서 번역됩니다.\n캐릭터 이름과 문화적 맥락은 {language} 사용 청중에게 적합해야 합니다.\n'''


def _build_image_safety_guidelines():
    '''이미지 프롬프트 안전 가이드라인'''
    return '\n**이미지 프롬프트 안전 가이드라인:**\n- **피해야 할 것**: 폭력, 무기, 노출, 혐오 표현, 과도하게 무서운 이미지\n- **집중할 것**: 중립적이고 묘사적이며 시네마틱한 언어\n- **안전한 대안**: "피 묻은 싸움" 대신 → "헝클어진 옷으로 격렬한 대치"\n- **절대 우선순위**: 프롬프트가 안전 필터에 의해 차단되지 않도록 합니다.\n'


def create_script_user_prompt(title = None, synopsis = None, genre = None, language = ('한국어', ''), additional_context = ('title', str, 'synopsis', str, 'genre', str, 'language', str, 'additional_context', str, 'return', str)):
    '''
    대본 생성을 위한 사용자 프롬프트 생성

    Args:
        title: 선택된 제목
        synopsis: 시놉시스
        genre: 장르 코드
        language: 언어
        additional_context: 추가 컨텍스트/참조 자료

    Returns:
        사용자 프롬프트 문자열
    '''
    lang_en = LANGUAGE_MAP.get(language, 'Korean')
    prompt = f'''\n다음 세부사항을 바탕으로 상세한 유튜브 대본을 만들어주세요.\n\n- **언어**: {language} ({lang_en})\n- **장르**: {genre}\n- **제목**: {title}\n- **시놉시스**: {synopsis}\n'''
    if additional_context:
        prompt += f'''\n\n**추가 참조 자료**:\n사용자가 제공한 다음 텍스트를 반드시 참고하여 서사, 캐릭터, 사건을 구성하세요:\n---참조 시작---\n{additional_context}\n---참조 끝---\n'''
    return prompt


def get_script_response_schema():
    '''대본 생성 응답 JSON 스키마'''
    return {
        'type': 'object',
        'properties': {
            'title': {
                'type': 'string',
                'description': '대본 제목' },
            'characters': {
                'type': 'array',
                'items': {
                    'type': 'object',
                    'properties': {
                        'uniqueId': {
                            'type': 'string' },
                        'name': {
                            'type': 'string' },
                        'appearance': {
                            'type': 'string' },
                        'clothing': {
                            'type': 'string' },
                        'profile': {
                            'type': 'string' },
                        'ageRange': {
                            'type': 'string' },
                        'gender': {
                            'type': 'string' },
                        'image_prompt_ko': {
                            'type': 'string' },
                        'image_prompt_en': {
                            'type': 'string' } },
                    'required': [
                        'uniqueId',
                        'name',
                        'appearance',
                        'profile'] } },
            'chapters': {
                'type': 'array',
                'items': {
                    'type': 'object',
                    'properties': {
                        'title': {
                            'type': 'string' },
                        'content': {
                            'type': 'string' },
                        'image_prompt_ko': {
                            'type': 'string' },
                        'image_prompt_en': {
                            'type': 'string' } },
                    'required': [
                        'title',
                        'content'] } } },
        'required': [
            'title',
            'characters',
            'chapters'] }
