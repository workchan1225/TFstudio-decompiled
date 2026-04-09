# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: narration_style_guide.pyc (Python 3.11)

'''
한국 드라마 대본 스타일 가이드 - 주어 반복 제거 + 문장 흐름

AI가 생성하는 대본에서 "그는", "그녀는", 캐릭터 이름을 문장마다 반복하는 것을 방지.
한국어 특성상 주어를 생략해도 자연스럽게 읽히므로, 드라마 대본 스타일로 작성.

핵심 원칙:
- 새로운 장면/인물 등장 시에만 주어 사용
- 같은 주체의 연속 행동은 주어 생략
- 톤/문체에 맞는 어미와 표현 사용
- 문장 연결어와 어미를 다양하게 사용하여 자연스러운 흐름 유지
'''
SENTENCE_FLOW_GUIDE = '\n## 🌊 문장 흐름 가이드 (매우 중요!)\n\n### ❌ 절대 금지: 단순 나열식 문장\n```\n그는 집에 갔다. 문을 열었다. 방에 들어갔다. 불을 켰다. 앉았다.\n```\n→ "~했다. ~했다. ~했다." 반복은 AI 티가 100% 나는 최악의 패턴입니다!\n\n### ✅ 올바른 문장 흐름\n\n**1. 어미 다양화 (필수!)**\n같은 어미를 3번 이상 연속 사용 금지! 다양한 어미를 섞어서 사용하세요:\n\n| 기본형 | 변형 (돌려쓰기) |\n|--------|----------------|\n| ~했다 | ~했죠, ~한 것이다, ~했던 것이다, ~하고 있었다 |\n| ~였다 | ~이었죠, ~인 셈이었다, ~일 뿐이었다 |\n| ~했습니다 | ~했어요, ~했던 거예요, ~한 거죠, ~하게 됩니다 |\n\n**2. 연결어 활용 (흐름 유지)**\n문장 사이에 적절한 연결어를 넣어 흐름을 만드세요:\n\n- 순접: 그리고, 그래서, 그러자, 그러더니, 그렇게\n- 역접: 그런데, 하지만, 그러나, 그럼에도\n- 시간: 그때, 그 순간, 잠시 후, 얼마 지나지 않아, 그러던 중\n- 강조: 결국, 마침내, 드디어, 사실은, 정말로\n- 전환: 한편, 그 무렵, 다른 한편으로, 한편으로는\n\n**3. 중문 구조 활용 (~는데, ~고, ~며)**\n짧은 문장만 나열하지 말고, 중문으로 연결하세요:\n\n❌ 문을 열었다. 방이 어두웠다. 불을 켰다.\n✅ 문을 여는데, 방 안이 어두웠다. 불을 켜자 먼지가 피어올랐다.\n\n❌ 전화가 왔다. 받았다. 목소리가 들렸다.\n✅ 전화가 울리더니, 받자마자 익숙한 목소리가 들려왔다.\n\n**4. 리듬감 (긴 문장 + 짧은 문장)**\n긴 문장 다음에 짧은 문장을 배치하면 임팩트가 생깁니다:\n\n```\n오랜 시간 동안 그 자리를 지켜온 노인은, 마침내 무거운 입을 열었다.\n"그건 사실이야."\n단 한 마디.\n그러나 그 말 한마디가 모든 것을 뒤흔들었다.\n```\n\n**5. 감각적 표현 삽입**\n행동만 나열하지 말고, 감각을 섞으세요:\n\n❌ 문을 열었다. 들어갔다. 앉았다.\n✅ 문이 삐걱거리며 열렸다. 퀴퀴한 냄새가 코를 찔렀다. 먼지 쌓인 의자에 털썩 주저앉았다.\n\n### 📝 체크리스트\n\n대본 작성 후 확인하세요:\n- [ ] "~했다. ~했다. ~했다." 3연속 이상 있으면 → 어미 변경!\n- [ ] 5문장 이상 연결어 없이 나열되어 있으면 → 연결어 추가!\n- [ ] 모든 문장이 비슷한 길이면 → 리듬감 추가!\n- [ ] 행동만 나열되어 있으면 → 감각 표현 추가!\n'
TONE_SENTENCE_PATTERNS = {
    '소설체': {
        'connectors': [
            '그러던 중',
            '그때였다',
            '이윽고',
            '마침내',
            '그렇게'],
        'endings': [
            '~했다',
            '~였다',
            '~했던 것이다',
            '~하고 있었다',
            '~인 것이다'],
        'rhythm': '긴 묘사 문장 후 짧은 감정 문장' },
    '극적체': {
        'connectors': [
            '그 순간!',
            '바로 그때!',
            '그러자!',
            '드디어!',
            '결국!'],
        'endings': [
            '~했다!',
            '~이다!',
            '~할 줄이야!',
            '~였던 것이다!'],
        'rhythm': '짧고 강렬한 문장 연속 후 여운' },
    '친근체': {
        'connectors': [
            '그랬는데요',
            '그런데 말이에요',
            '있잖아요',
            '그래서요',
            '근데'],
        'endings': [
            '~했어요',
            '~했죠',
            '~한 거예요',
            '~했다니까요'],
        'rhythm': '대화하듯 자연스러운 흐름' },
    '설명체': {
        'connectors': [
            '이때',
            '이 과정에서',
            '그 결과',
            '따라서',
            '결론적으로'],
        'endings': [
            '~했습니다',
            '~합니다',
            '~한 것입니다',
            '~하게 됩니다'],
        'rhythm': '정보 전달 후 정리 문장' },
    '담담체': {
        'connectors': [
            '그리고',
            '그랬다',
            '그뿐이었다',
            '그것뿐이었다'],
        'endings': [
            '~했다',
            '~였다',
            '~이다'],
        'rhythm': '짧고 건조한 문장 연속' },
    '유머체': {
        'connectors': [
            '그런데',
            '아니 근데',
            '웃긴 건',
            '참고로',
            '솔직히'],
        'endings': [
            '~했다',
            '~했어요',
            '~했죠',
            '~한 거다'],
        'rhythm': '예상 깨기, 반전, 자조' },
    '감성체': {
        'connectors': [
            '그 순간',
            '문득',
            '어느새',
            '그렇게',
            '마치'],
        'endings': [
            '~했다',
            '~였다',
            '~하고 있었다',
            '~인 것만 같았다'],
        'rhythm': '감정선 따라 흐르는 묘사' },
    '다큐체': {
        'connectors': [
            '이때',
            '당시',
            '그 결과',
            '이로 인해',
            '한편'],
        'endings': [
            '~했습니다',
            '~합니다',
            '~된 것입니다',
            '~하게 됩니다'],
        'rhythm': '사실 전달 후 의미 부여' },
    '다채로운 문체': {
        'connectors': [
            '그때였지요',
            '그런데요',
            '사실은요',
            '그렇게',
            '그 순간'],
        'endings': [
            '~습니다',
            '~했습니다',
            '~지요',
            '~죠',
            '~었지요'],
        'rhythm': '뼈대(진행/동작/팩트)는 ~습니다, 살(묘사/감정/여운)은 ~지요' } }
TONE_FORBIDDEN_ENDINGS = {
    '소설체': [
        '했어요',
        '해요',
        '예요',
        '이에요',
        '합니다',
        '입니다',
        '하오',
        '했소'],
    '극적체': [
        '했어요',
        '해요',
        '네요',
        '합니다',
        '입니다',
        '하오',
        '했소'],
    '친근체': [
        '했다',
        '였다',
        '이다',
        '있다',
        '없다',
        '하오',
        '했소',
        '합니다',
        '입니다'],
    '설명체': [
        '했다',
        '였다',
        '이다',
        '했어요',
        '해요',
        '예요',
        '하오',
        '했소'],
    '담담체': [
        '했어요',
        '해요',
        '예요',
        '합니다',
        '네요',
        '하오',
        '했소'],
    '유머체': [
        '하오',
        '했소',
        '하였다',
        '되었다'],
    '감성체': [
        '합니다',
        '입니다',
        '하오',
        '했소',
        '하였다'],
    '다큐체': [
        '했다',
        '였다',
        '이다',
        '했어요',
        '해요',
        '예요',
        '하오',
        '했소'],
    '다채로운 문체': [
        '했다',
        '였다',
        '이다',
        '이었다',
        '있었다',
        '없었다',
        '같았다',
        '됐다',
        '한다',
        '있다',
        '없다',
        '했어요',
        '해요',
        '예요',
        '이에요',
        '하오',
        '했소'] }
TONE_REQUIRED_ENDINGS = {
    '소설체': [
        '했다',
        '였다',
        '이었다',
        '있었다',
        '없었다'],
    '극적체': [
        '했다',
        '였다',
        '이다',
        '있다'],
    '친근체': [
        '했어요',
        '했죠',
        '예요',
        '이에요',
        '거예요',
        '했거든요'],
    '설명체': [
        '합니다',
        '했습니다',
        '입니다',
        '됩니다',
        '있습니다'],
    '담담체': [
        '했다',
        '였다',
        '이다',
        '그뿐이었다'],
    '유머체': [
        '했다',
        '했어요',
        '했죠',
        '한 거다',
        '한 거예요'],
    '감성체': [
        '했다',
        '였다',
        '있었다',
        '같았다',
        '흘렀다'],
    '다큐체': [
        '합니다',
        '했습니다',
        '입니다',
        '됩니다',
        '되었습니다'],
    '다채로운 문체': [
        '습니다',
        '했습니다',
        '입니다',
        '됩니다',
        '지요',
        '죠',
        '었지요',
        '였지요'] }

def get_tone_ending_rules(tone = None):
    '''
    톤별 어미 규칙 프롬프트 생성

    Args:
        tone: 톤/문체 (소설체, 극적체, 친근체 등)

    Returns:
        어미 규칙 프롬프트 문자열
    '''
    if not tone:
        return ''
    required = None.get(tone, TONE_REQUIRED_ENDINGS['소설체'])
    forbidden = TONE_FORBIDDEN_ENDINGS.get(tone, [])
    required_str = (lambda .0: [ f'''~{e}''' for e in .0 ])(required())
    forbidden_str = (lambda .0: [ f'''~{e}''' for e in .0 ])(forbidden()) if forbidden else '없음'
    if tone == '다채로운 문체':
        return f'''\n### ⚠️ {tone} 어미 규칙 (필수 준수!)\n\n✅ **필수 어미** (나레이션에서 반드시 사용):\n{required_str}\n\n❌ **금지 어미** (절대 사용 금지!):\n{forbidden_str}\n\n⚠️ **중요**: 한 줄씩 번갈아 쓰는 규칙이 아닙니다.\n- 사건의 뼈대(진행/동작/팩트/수치/결론)는 `~습니다`\n- 사건의 살(묘사/감정/여운/공감)은 `~지요`\n- 문장 역할에 따라 선택하세요. 기계적 교대 금지!\n\n📌 **{tone} 나레이션 예시**:\n- "사건은 새벽 다섯 시에 시작되었습니다. 골목 끝 가로등이 유난히 흔들리고 있었지요. 신고 접수는 3분 뒤 완료되었습니다. 그 짧은 틈이 오래 남지요."\n'''
    if tone in ('설명체', '다큐체'):
        pass
    elif tone == '친근체':
        pass
    
    return f''' 어미 규칙 (필수 준수!)\n\n✅ **필수 어미** (나레이션에서 반드시 사용):\n{required_str}\n\n❌ **금지 어미** (절대 사용 금지!):\n{forbidden_str}\n\n⚠️ **중요**: 한 문단 내에서 어미를 섞지 마세요!\n- 잘못된 예: "그는 문을 열었다. 안에는 아무도 없었어요." (혼용!)\n- 올바른 예 ({tone}): 모든 나레이션이 ~{required[0]} 어미로 통일\n\n📌 **{tone} 나레이션 예시**:\n- "그때, 철수가 문을 열었습니다. 안에는 아무도 없었습니다."- "그때, 철수가 문을 열었어요. 안에는 아무도 없었죠."{'- "그때, 철수가 문을 열었다. 안에는 아무도 없었다."'}\n'''

TONE_DRAMA_STYLES = {
    '소설체': {
        'ending': '~했다, ~였다 (과거형)',
        'style': '서사적이고 묘사가 풍부한 문체',
        'example_bad': '그는 문을 열었다. 그는 방 안을 둘러봤다. 그는 한숨을 쉬었다.',
        'example_good': '철수가 문을 열었다.\n방 안을 천천히 둘러본다.\n텅 빈 공간. 적막만이 가득했다.\n깊은 한숨이 새어 나왔다.' },
    '극적체': {
        'ending': '~했다! ~이다! (강렬한 표현)',
        'style': '짧고 강렬한 문장, 긴장감 있는 전개',
        'example_bad': '그는 뛰어들었다. 그는 소리쳤다. 그는 주먹을 휘둘렀다.',
        'example_good': '철수가 뛰어든다!\n소리친다!\n주먹이 허공을 가른다!\n피할 새도 없었다!' },
    '친근체': {
        'ending': '~했어요, ~예요 (부드러운 어조)',
        'style': '독자에게 말하듯 친근한 문체',
        'example_bad': '그는 문을 열었어요. 그는 들어갔어요. 그는 앉았어요.',
        'example_good': '철수가 문을 열었어요.\n조심스럽게 안으로 들어가요.\n빈 의자에 털썩 앉았죠.\n뭔가 이상한 느낌이 들었어요.' },
    '설명체': {
        'ending': '~했습니다, ~입니다 (격식체)',
        'style': '객관적이고 정보 전달 중심',
        'example_bad': '그는 출근했습니다. 그는 업무를 시작했습니다. 그는 회의에 참석했습니다.',
        'example_good': '철수가 출근했습니다.\n9시 정각, 업무를 시작합니다.\n10시에 예정된 회의에 참석했습니다.\n중요한 안건이 논의되었습니다.' },
    '담담체': {
        'ending': '~했다 (짧고 건조한)',
        'style': '감정 절제, 최소한의 묘사',
        'example_bad': '그는 왔다. 그는 봤다. 그는 갔다.',
        'example_good': '철수가 왔다.\n봤다.\n그리고 갔다.\n그것뿐이었다.' },
    '유머체': {
        'ending': '~했다/~했어요 (가벼운 어조)',
        'style': '위트 있고 재미있는 표현',
        'example_bad': '그는 넘어졌다. 그는 당황했다. 그는 일어났다.',
        'example_good': '철수가 화려하게 넘어졌다.\n아, 이건 좀 창피하다.\n주변 시선이 따갑다.\n아무렇지 않은 척 일어났다. 실패.' },
    '감성체': {
        'ending': '~했다 (서정적 표현)',
        'style': '감정과 분위기 중심의 묘사',
        'example_bad': '그녀는 창밖을 봤다. 그녀는 슬펐다. 그녀는 눈물을 흘렸다.',
        'example_good': '영희가 창밖을 바라본다.\n빗방울이 유리를 타고 흐른다.\n마음 한구석이 아려온다.\n눈가에 맺힌 물기. 빗물인지 눈물인지.' },
    '다큐체': {
        'ending': '~했습니다, ~합니다 (객관적)',
        'style': '사실 기반, 시간/장소 명시',
        'example_bad': '그는 현장에 도착했습니다. 그는 조사를 시작했습니다. 그는 증거를 발견했습니다.',
        'example_good': '2024년 1월 15일 오후 3시.\n철수 형사가 현장에 도착했습니다.\n조사가 시작됩니다.\n결정적 증거가 발견되었습니다.' },
    '다채로운 문체': {
        'ending': '~습니다(뼈대), ~지요(살)',
        'style': '나레이션 전용. 문장 역할에 따라 어미 선택',
        'example_bad': '그날 바람이 차가웠다. 낙엽이 바스락거렸어요. 그녀는 고개를 떨구었다.',
        'example_good': '그날따라 유독 바람이 차가웠지요.\n낙엽이 발밑에서 바스락거렸습니다.\n그녀는 고개를 떨구었습니다.\n어깨가 잔뜩 움츠러들어 있었지요.\n한참을 그렇게 서 있었습니다.' } }

def build_korean_drama_style_prompt(character_names = None, tone = None):
    '''
    한국 드라마 대본 스타일 프롬프트 생성 (간소화 버전)

    Args:
        character_names: 등장인물 이름 목록
        tone: 톤/문체 (소설체, 극적체, 친근체 등)

    Returns:
        프롬프트에 추가할 가이드라인 문자열
    '''
    tone_style = TONE_DRAMA_STYLES.get(tone, TONE_DRAMA_STYLES['소설체'])
    tone_name = tone if tone else '소설체'
    return f'''\n## 🎬 주어 반복 금지 ({tone_name} 스타일)\n\n**"그는", "그녀는"을 문장마다 반복하지 마세요!** 한국어는 주어 생략이 자연스럽습니다.\n\n- **어미**: {tone_style['ending']}\n- **새 장면/인물 전환 시만** 주어 사용\n- **같은 주체 연속 행동**은 주어 생략: "책상에 앉는다. 서류를 펼친다."\n- **3문장 이상 같은 주어 시작 금지**\n'''


def build_expansion_drama_style_prompt(character_names = None, tone = None):
    '''
    대본 확장용 한국 드라마 스타일 프롬프트 (간결 버전)

    Args:
        character_names: 등장인물 이름 목록
        tone: 톤/문체

    Returns:
        프롬프트 문자열
    '''
    first_char = character_names[0] if character_names else '주인공'
    tone_style = TONE_DRAMA_STYLES.get(tone, TONE_DRAMA_STYLES['소설체'])
    tone_name = tone if tone else '소설체'
    return f'''\n## 🎬 주어 반복 금지 (한국 드라마 스타일 - {tone_name})\n\n⚠️ "그는", "그녀는", 캐릭터 이름을 문장마다 반복하지 마세요!\n\n**{tone_name} 어미**: {tone_style['ending']}\n\n❌ 금지:\n{tone_style['example_bad']}\n\n✅ 올바름:\n{tone_style['example_good']}\n\n### 규칙\n1. 장면/인물 전환 시에만 주어 사용\n2. 같은 주체의 연속 행동 = 주어 생략\n3. 3문장 이상 같은 주어 시작 금지\n4. **{tone_name} 어미({tone_style['ending']}) 유지!**\n'''


def build_pronoun_reduction_prompt(narration_ratio = None, tone = None, character_names = None):
    '''이전 버전과의 호환성을 위한 래퍼 함수.'''
    return build_korean_drama_style_prompt(character_names, tone)


def get_action_beat_examples(character_names = None):
    '''액션 비트 예시 - 주어 생략 중심'''
    return '\n### 주어 생략 예시\n\n❌ 그는 화가 났다. 그는 주먹을 쥐었다. 그는 소리쳤다.\n✅ 주먹이 불끈 쥐어진다. "이건 아니야!"\n\n❌ 그녀는 슬펐다. 그녀는 눈물을 흘렸다. 그녀는 고개를 숙였다.\n✅ 눈물이 볼을 타고 흐른다. 고개가 떨군다.\n'


def get_tone_specific_guide(tone = None):
    '''톤별 가이드 반환'''
    if tone in TONE_DRAMA_STYLES:
        style = TONE_DRAMA_STYLES[tone]
        return f'''**{tone}**: {style['style']} (어미: {style['ending']})'''


def build_sentence_flow_prompt(tone = None):
    '''
    문장 흐름 가이드 프롬프트 생성 (톤별 적용)

    Args:
        tone: 톤/문체 (소설체, 극적체, 친근체 등)

    Returns:
        문장 흐름 가이드 프롬프트 문자열
    '''
    lines = [
        SENTENCE_FLOW_GUIDE]
    if tone and tone in TONE_SENTENCE_PATTERNS:
        pattern = TONE_SENTENCE_PATTERNS[tone]
        lines.extend([
            f'''\n### 🎭 {tone} 전용 문장 패턴\n''',
            f'''**권장 연결어**: {', '.join(pattern['connectors'])}''',
            f'''**권장 어미**: {', '.join(pattern['endings'])}''',
            f'''**리듬**: {pattern['rhythm']}''',
            ''])
    return '\n'.join(lines)


def build_complete_style_prompt(character_names = None, tone = None, include_flow_guide = None):
    '''
    완전한 스타일 프롬프트 생성 (주어 생략 + 문장 흐름)

    Args:
        character_names: 등장인물 이름 목록
        tone: 톤/문체
        include_flow_guide: 문장 흐름 가이드 포함 여부

    Returns:
        완전한 스타일 가이드 프롬프트
    '''
    parts = []
    parts.append(build_korean_drama_style_prompt(character_names, tone))
    if include_flow_guide:
        parts.append(build_sentence_flow_prompt(tone))
    return '\n\n'.join(parts)


def build_expansion_complete_style_prompt(character_names = None, tone = None, exclude_endings = None):
    '''
    대본 확장용 완전한 스타일 프롬프트 (간결 버전)

    Args:
        character_names: 등장인물 이름 목록
        tone: 톤/문체
        exclude_endings: True면 어미 규칙 제외 (중복 방지용)

    Returns:
        확장용 스타일 가이드 프롬프트
    '''
    first_char = character_names[0] if character_names else '주인공'
    tone_name = tone if tone else '소설체'
    tone_style = TONE_DRAMA_STYLES.get(tone, TONE_DRAMA_STYLES['소설체'])
    tone_pattern = TONE_SENTENCE_PATTERNS.get(tone, TONE_SENTENCE_PATTERNS.get('소설체', { }))
    endings_section = ''
    if not exclude_endings:
        endings_section = f'''\n**{tone_name} 권장 어미**: {', '.join(tone_pattern.get('endings', [
            '~했다',
            '~였다']))}'''
    return f'''\n## 🎬 대본 스타일 가이드 - {tone_name} (필수!)\n\n### 1. 주어 반복 금지\n⚠️ "그는", "그녀는", 캐릭터 이름을 문장마다 반복하지 마세요!\n\n❌ 금지: {tone_style['example_bad']}\n✅ 올바름: {tone_style['example_good']}\n\n### 2. 문장 흐름 (가장 중요!)\n\n⚠️ "~했다. ~했다. ~했다." 단순 나열 절대 금지!\n{endings_section}\n**권장 연결어**: {', '.join(tone_pattern.get('connectors', [
        '그런데',
        '그래서',
        '그때']))}\n**리듬**: {tone_pattern.get('rhythm', '긴 문장 + 짧은 문장 교차')}\n\n❌ 금지 패턴:\n```\n집에 갔다. 문을 열었다. 들어갔다. 앉았다. 한숨을 쉬었다.\n```\n\n✅ 올바른 패턴:\n```\n집에 도착하자, 낡은 문이 삐걱거리며 열렸다.\n텅 빈 방. 어둠만이 가득했다.\n먼지 쌓인 의자에 털썩 주저앉자, 깊은 한숨이 새어나왔다.\n```\n\n### 3. 체크리스트\n- [ ] 같은 어미 3번 연속 금지 → 어미 다양화!\n- [ ] 5문장 이상 연결어 없음 → 연결어 추가!\n- [ ] "그는", "그녀는" 연속 → 주어 생략!\n'''
