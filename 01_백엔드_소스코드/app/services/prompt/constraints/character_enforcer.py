# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: character_enforcer.pyc (Python 3.11)

'''
CharacterEnforcer - 캐릭터 제약 강제 적용 시스템

AI가 정의된 캐릭터만 사용하고, 새로운 캐릭터를 임의로 추가하지 않도록 강제.
화자 태그 형식과 캐릭터 일관성을 유지.
'''
from typing import List, Dict, Optional
import re

try:
    from app.utils.genre_categories import get_genre_category, is_informational_category
except ImportError:
    
    def get_genre_category(genre = None):
        return 'default'

    
    def is_informational_category(genre = None):
        return False



class CharacterEnforcer:
    '''
    캐릭터 제약 강제 적용 시스템

    정의된 캐릭터만 사용하도록 강제하고,
    새로운 캐릭터 임의 생성을 방지.
    '''
    
    def __init__(self):
        pass

    
    def build_enforcement_prompt(self, characters = None, include_narrator = None, is_shorts = None, genre = (True, False, None, None), supporting_characters = ('characters', List[Dict], 'include_narrator', bool, 'is_shorts', bool, 'genre', Optional[str], 'supporting_characters', Optional[List[Dict]], 'return', str)):
        '''
        캐릭터 강제 프롬프트 생성

        Args:
            characters: 캐릭터 목록 (uniqueId, name, appearance 등)
            include_narrator: 나레이션 포함 여부
            is_shorts: 쇼츠 대본 여부 (True면 쇼츠 전용 규칙 적용)
            genre: 장르 (장르별 캐릭터 소개 스타일 분기용)
            supporting_characters: 조연 캐릭터 목록 (v1.5.0)

        Returns:
            캐릭터 강제 프롬프트
        '''
        if not characters:
            print('[CharacterEnforcer] 캐릭터 없음 - 나레이터 전용 모드')
            return self._build_narrator_only_prompt()
        char_list = None
        for char in characters:
            name = char.get('name', '이름없음')
            uid = char.get('uniqueId', 'X')
            char_list.append(f'''- **[{name}]**: 캐릭터 {uid}''')
            supporting_list = []
            if supporting_characters:
                for char in supporting_characters:
                    name = char.get('name', '')
                    if not name:
                        continue
                    appearance_count = char.get('appearanceCount', char.get('appearance_count', 0))
                    if appearance_count >= 2:
                        supporting_list.append(f'''- **[{name}]**: 조연 (반복 등장)''')
                        continue
                    supporting_list.append(f'''- **[{name}]**: 조연 (1회성)''')
                    char_names = characters()
                    supporting_names = []
                    if supporting_characters:
                        supporting_names = supporting_characters()
        all_character_names = char_names + supporting_names
        allowed_speakers = (lambda .0: [ f'''[{name}]''' for name in .0 ])(all_character_names())
        first_appearance_rules = ''
        if len(characters) >= 1:
            first_appearance_rules = self._build_first_appearance_rules(characters, is_shorts, genre)
            mode_str = '쇼츠' if is_shorts else '일반 대본'
            genre_str = f''', 장르: {genre}''' if genre else ''
            print(f'''[CharacterEnforcer] 첫 등장 소개 규칙 적용: {len(characters)}명 캐릭터 ({mode_str} 모드{genre_str})''')
        print(f'''[CharacterEnforcer] 캐릭터 제약 적용: {', '.join(char_names)}''')
        if supporting_names:
            print(f'''[CharacterEnforcer] 조연 캐릭터 허용: {', '.join(supporting_names)}''')
        supporting_section = ''
        if supporting_list:
            supporting_section = f'''\n**조연** ({len(supporting_list)}명) - AI 자동 감지됨:\n{chr(10).join(supporting_list)}\n'''
        return f'''\n## [CHARACTER LOCK] 캐릭터 제약\n\n### 허용된 화자 태그 (이것만 사용!)\n\n**나레이션**:\n- [나레이션]: 상황 설명, 묘사, 전환\n\n**등장인물** ({len(characters)}명):\n{chr(10).join(char_list)}\n{supporting_section}\n### 화자 태그 규칙\n\n1. **허용된 태그만 사용**\n   ✅ [나레이션], {allowed_speakers}\n   ❌ 그 외 모든 태그\n\n2. **정의되지 않은 새 캐릭터 추가 금지!**\n   ✅ 위에 나열된 등장인물/조연 사용 가능\n   ❌ 목록에 없는 새 캐릭터 금지\n   ❌ [지나가는 사람]: ...\n   ❌ [목소리]: ...\n   ✅ [나레이션]: 지나가던 사람이 말했다. "..."\n\n3. **목록에 없는 단역은 나레이션으로 처리**\n   ❌ [웨이터]: 주문하시겠어요?\n   ✅ [나레이션]: 웨이터가 다가와 물었다. "주문하시겠어요?"\n\n4. **태그 형식 엄수**\n   ❌ 캐릭터이름: 안녕\n   ❌ (캐릭터이름) 안녕\n   ✅ [캐릭터이름]: 안녕\n\n### 캐릭터 정보\n\n{self._build_character_info(characters)}\n{first_appearance_rules}\n\n### 검증\n\n대본 작성 후 확인:\n- [ ] 허용되지 않은 화자 태그가 없는가?\n- [ ] 목록에 없는 캐릭터가 추가되지 않았는가?\n- [ ] 미등록 단역이 나레이션으로 처리되었는가?\n- [ ] **모든 캐릭터가 첫 등장 시 나레이션으로 소개되었는가?**\n\n---\n⚠️ 허용되지 않은 화자 태그 발견 시:\n→ 해당 대사를 나레이션으로 변환하거나\n→ 기존 캐릭터 대사로 수정\n'''

    
    def _build_narrator_only_prompt(self = None):
        '''
        나레이터만 있는 경우 프롬프트 (1인칭 다큐/정보 스타일)

        정보/교양, 뉴스/분석 카테고리에서 사용.
        철학적 질문 → 경이감 → 역사적 맥락 → 심화 → 성찰 구조.
        '''
        return '\n## [CHARACTER LOCK] 1인칭 나레이터 모드 (정보/다큐 전용)\n\n### ⚠️ 필수 규칙\n\n**허용 태그**: [나레이션] 만 사용!\n**금지 태그**: [전문가], [과학자], [해설자] 등 모든 캐릭터 태그 금지!\n\n❌ **절대 금지!** (이렇게 쓰면 실패!)\n- [전문가]: 이것은 매우 중요한 발견입니다.\n- [과학자]: 연구 결과에 따르면...\n- [해설자]: 지금부터 알아보겠습니다.\n\n✅ **올바른 예** (반드시 이렇게!)\n- [나레이션]: 전문가들은 이것이 매우 중요한 발견이라고 말합니다.\n- [나레이션]: 연구 결과에 따르면...\n- [나레이션]: 지금부터 알아보겠습니다.\n\n---\n\n### 📝 1인칭 다큐 구조 (철학적 탐구 스타일)\n\n**1. 철학적 후킹 (첫 문장)**\n   - 도발적/철학적 질문으로 시작\n   - 예: "만약 시간이 멈추는 곳이 있다면, 그곳에서 당신은 영원히 존재할 수 있을까요?"\n   - 예: "우리가 당연하게 여기는 것들이 사실은 환상이라면?"\n\n**2. 경이감 도입**\n   - 주제를 신비롭고 경이로운 톤으로 소개\n   - 예: "우주에는 우리가 상상조차 하기 힘든, 시간이라는 개념 자체를 뒤흔드는 신비로운 존재가 있습니다."\n\n**3. 역사적 맥락 (연도 명시!)**\n   - 시간순으로 발전 과정 설명\n   - 예: "20세기 초, 아인슈타인은... → 1970년대에 이르러... → 2015년, 인류는 최초로..."\n\n**4. 심층 개념 설명**\n   - 핵심 개념을 쉽게 풀어서 설명\n   - 비유와 예시 활용\n\n**5. 철학적 성찰 + 시청자 참여**\n   - 단순 정보가 아닌 의미 부여\n   - 예: "당신이 생각하는 \'시간\'이란 과연 무엇인가요?"\n\n**6. 마무리 (구독 유도)**\n   - 다음 영상 예고 + 구독 요청\n\n---\n\n### 예시 (올바른 1인칭 다큐 스타일)\n\n```\n[나레이션]: 만약 빛조차 빠져나올 수 없는 곳이 있다면, 그곳에서 시간은 어떻게 흐를까요?\n\n[나레이션]: 우주에는 우리가 상상조차 하기 힘든 신비로운 존재가 있습니다. 바로 `블랙홀`입니다.\n\n[나레이션]: 20세기 초, 아인슈타인은 일반 상대성 이론을 통해 이 존재를 예측했습니다. 하지만 그것은 그저 수학적 가능성에 불과했습니다.\n\n[나레이션]: 1970년대, 스티븐 호킹은 블랙홀이 완전히 검지만은 않다는 놀라운 이론을 발표했습니다.\n\n[나레이션]: 2019년, 인류는 마침내 `블랙홀의 실제 모습`을 촬영하는 데 성공했습니다.\n\n[나레이션]: 결국 블랙홀은 단순히 우주 저편에 존재하는 천체가 아닙니다. \'시간\'이라는 우리가 당연하게 여기는 개념조차 상대적일 수 있음을 증명하는 살아있는 증거입니다.\n\n[나레이션]: 당신이 생각하는 \'시간\'이란 과연 무엇인가요? 다음 이야기에서는 그 가능성에 대해 탐구해봅니다.\n```\n\n---\n\n⚠️ **핵심 체크**:\n- [ ] 모든 화자 태그가 [나레이션]인가?\n- [ ] [전문가], [과학자] 등 캐릭터 태그가 없는가?\n- [ ] 철학적 질문 → 경이감 → 역사 → 심화 → 성찰 구조인가?\n- [ ] 연도/시대가 명시되어 있는가?\n\n---\n'

    
    def _build_character_info(self = None, characters = None):
        '''캐릭터 정보 섹션 생성'''
        if not characters:
            return '등장인물 없음'
        lines = None
        for i, char in enumerate(characters, 1):
            name = char.get('name', f'''캐릭터{i}''')
            uid = char.get('uniqueId', chr(64 + i))
            appearance = char.get('appearance', '정보 없음')
            profile = char.get('profile', '')
            lines.append(f'''**{i}. {name}** (ID: {uid})\n- 외모: {appearance}\n- 역할: {profile if profile else '미정'}''')
            return '\n\n'.join(lines)

    
    def _build_first_appearance_rules(self = None, characters = None, is_shorts = None, genre = (False, None)):
        '''
        캐릭터 첫 등장 규칙 섹션 생성

        다중 화자 대본에서 캐릭터가 처음 등장할 때
        나레이션으로 소개하도록 강제하는 규칙.

        Args:
            characters: 캐릭터 목록
            is_shorts: 쇼츠 대본 여부
            genre: 장르 (장르별 소개 스타일 분기용)

        Returns:
            첫 등장 규칙 프롬프트
        '''
        if characters or len(characters) == 0:
            return ''
        if None and is_informational_category(genre):
            return ''
        category = get_genre_category(genre) if None else 'default'
        main_char = characters[0]
        main_name = main_char.get('name', '주인공')
        main_profile = main_char.get('profile', '')
        sub_char = characters[1] if len(characters) > 1 else None
        sub_name = sub_char.get('name', '조력자') if sub_char else ''
        sub_profile = sub_char.get('profile', '') if sub_char else ''
        intro_example = self._build_connected_intro_example(characters, category)
        if is_shorts:
            return f'''\n### 🎭 캐릭터 소개 규칙 - 쇼츠 (필수!)\n\n시청자는 캐릭터 이름만으로는 누구인지 알 수 없습니다.\n반드시 나레이션으로 캐릭터의 역할/관계를 **자연스럽게 연결하여** 소개해주세요!\n\n#### 쇼츠 5턴 인트로에서 캐릭터 소개 (매우 중요!)\n\n**대화 시작 장르 (드라마, 복수, 미스터리 등):**\n- 턴1-3: 대화로 긴장감 있게 시작 (소개 없이 진행 OK)\n- **턴4 [나레이션]: ★ 여기서 모든 캐릭터 역할/관계 소개! ★**\n- 턴5: 대화로 전환\n\n**나레이션 시작 장르 (정보, 과학, 다큐 등):**\n- **턴1 [나레이션]: ★ 첫 턴에서 모든 캐릭터 역할/관계 소개! ★**\n- 턴2-5: 정보 전달\n\n#### 소개 작성 원칙 (매우 중요!)\n\n1. **관계성 중심**: 캐릭터들의 관계를 자연스럽게 연결하여 소개\n2. **기계적 나열 금지**: "~는 ~입니다. ~는 ~입니다." 형태 금지!\n3. **문학적 표현**: 캐릭터 간 역학과 감정선을 담아서 소개\n\n#### 올바른 예시\n\n**✅ 올바른 예 (쇼츠 대화 시작 장르):**\n```\n턴1 [{main_name}]: 어머니, 이 서류 보이세요?\n턴2 [{sub_name if sub_name else '나레이션'}]: 그, 그건...\n턴3 [{main_name}]: 30년간 숨기셨던 것들이에요.\n턴4 [나레이션]: {intro_example}\n턴5 [{main_name}]: 이제 모든 걸 알아버렸어요.\n```\n\n#### 주의사항\n\n- **턴4 나레이션에서 반드시 모든 캐릭터 관계 소개**\n- **소개 길이**: 1-2문장 (30-60자, 쇼츠는 짧게!)\n- **재등장 시**: 소개 불필요, 이름만 사용\n\n---\n⚠️ **핵심 (쇼츠)**: 턴1-3 대화 → **턴4 캐릭터 소개** → 턴5 전환\n턴4 나레이션에서 반드시 캐릭터 역할/관계를 소개하세요!\n'''
        return f'''{main_name}]: (강렬한 첫 대사)\n[{sub_name if sub_name else '나레이션'}]: (반응/대화)\n[{main_name}]: (갈등 고조)\n(대화 5턴 진행)\n\n[전환 문구]\n[나레이션]: 어떻게 이런 일이 일어났을까요? 모든 것은 6개월 전에 시작되었습니다.\n\n[★ 캐릭터 소개 - 전환 직후! ★]\n{intro_example}\n\n[본편 시작]\n(이제 캐릭터가 소개된 상태로 이야기 전개)\n```\n\n#### 4. 주의사항\n\n- **티저 대화에서는 소개 불필요**: 긴장감 유지가 우선!\n- **전환 직후 반드시 소개**: 본편 시작 전에 캐릭터 관계 설명\n- **소개 길이**: 캐릭터당 1-2문장 (50-100자)\n- **재등장 시**: 소개 불필요, 이름만 사용\n- **관계성 강조**: 캐릭터들 사이의 관계를 자연스럽게 표현\n\n---\n⚠️ **핵심**: 티저 대화 → 전환 → **캐릭터 소개** → 본편!\n전환 문구 이후에 반드시 캐릭터 역할/관계를 나레이션으로 **연결하여** 설명하세요!\n'''

    
    def build_speaker_tag_rules(self = None, original_speakers = None):
        '''
        화자 태그 규칙 프롬프트

        Args:
            original_speakers: 원본 대본에서 추출한 화자 목록

        Returns:
            화자 태그 규칙 프롬프트
        '''
        if not original_speakers:
            original_speakers = [
                '나레이션']
        narration_tags = original_speakers()
        character_tags = original_speakers()
        if not (lambda .0: [ f'''[{t}]''' for t in .0 ])(narration_tags()):
            narration_str = '[나레이션]'
            if not (lambda .0: [ f'''[{t}]''' for t in .0 ])(character_tags()):
                character_str = '(없음)'
        return f'''\n### 화자 구분 규칙\n\n**나레이션 태그**: {narration_str}\n**캐릭터 태그**: {character_str}\n\n### 태그 사용 예시\n\n```\n[나레이션]: 그날 아침, 햇살이 창문을 통해 들어왔다.\n[{character_tags[0] if character_tags else '인물A'}]: 오늘은 뭔가 다른 느낌이야.\n[나레이션]: 그의 목소리에는 묘한 떨림이 있었다.\n```\n\n### 금지 사항\n\n1. **새로운 태그 생성 금지**\n   - 위에 정의된 태그만 사용\n   - 임의의 [새캐릭터]: 형식 금지\n\n2. **태그 형식 변형 금지**\n   - ❌ 인물A: (콜론 앞 대괄호 누락)\n   - ❌ 【인물A】: (다른 괄호 사용)\n   - ✅ [인물A]:\n\n3. **괄호 지문 금지**\n   - ❌ [인물A]: (화가 나며) 뭐라고?!\n   - ✅ [나레이션]: 그가 화가 난 목소리로 말했다.\n   - ✅ [인물A]: 뭐라고?!\n'''

    
    def extract_speakers_from_text(self = None, text = None):
        '''
        텍스트에서 화자 태그 추출

        Args:
            text: 분석할 텍스트

        Returns:
            발견된 화자 태그 목록
        '''
        pattern = '\\[([^\\]]+)\\]:'
        matches = re.findall(pattern, text)
        seen = set()
        speakers = []
        for match in matches:
            if match not in seen:
                seen.add(match)
                speakers.append(match)
            return speakers

    
    def validate_speakers(self = None, text = None, allowed_speakers = None):
        '''
        화자 태그 검증 (생성 후 검증용)

        Args:
            text: 검증할 텍스트
            allowed_speakers: 허용된 화자 목록

        Returns:
            검증 결과 딕셔너리
        '''
        allowed = set(allowed_speakers + [
            '나레이션',
            '내레이션',
            '해설'])
        found_speakers = self.extract_speakers_from_text(text)
        violations = []
        for speaker in found_speakers:
            if speaker not in allowed:
                violations.append({
                    'speaker': speaker,
                    'type': 'unauthorized_speaker',
                    'message': f'''허용되지 않은 화자 태그: [{speaker}]''' })
            return {
                'is_valid': len(violations) == 0,
                'found_speakers': found_speakers,
                'allowed_speakers': list(allowed),
                'violations': violations }

    
    def build_parenthetical_removal_rules(self = None):
        '''괄호 지문 제거 규칙 프롬프트'''
        return '\n### 괄호 사용 완전 금지 규칙 (TTS 품질 필수!)\n\n대본에서 모든 종류의 괄호 사용을 금지합니다. TTS가 괄호 내용을 그대로 읽어버려 영상 품질이 저하됩니다.\n\n---\n\n#### 1. 동작/감정 괄호 금지\n\n❌ **금지 예시**:\n- [인물A]: (웃으며) 안녕!\n- [인물B]: (놀라며) 정말?!\n- [인물A]: (한숨을 쉬며) 그랬구나...\n\n✅ **올바른 예시**:\n- [나레이션]: 그가 미소를 지으며 말했다.\n- [인물A]: 안녕!\n\n---\n\n#### 2. 영문 표기 괄호 금지\n\n❌ **금지 예시**:\n- 시그나(Cigna)\n- 유럽우주국(ESA)\n- 나사(NASA)\n- 세계보건기구(WHO)\n\n✅ **올바른 예시**:\n- 시그나\n- 유럽우주국\n- 나사\n- 세계보건기구\n\n---\n\n#### 3. 부연설명/예시 괄호 금지\n\n❌ **금지 예시**:\n- 긍정적인 단어(파티, 사랑)\n- 부정적인 감정(거절, 고립)\n- 다양한 방법(운동, 명상, 독서 등)\n- 핵심 요소(시간, 노력, 인내)\n\n✅ **올바른 예시 (문장으로 풀어쓰기)**:\n- 파티나 사랑처럼 긍정적인 단어\n- 거절이나 고립 같은 부정적인 감정\n- 운동, 명상, 독서 등 다양한 방법\n- 시간과 노력, 그리고 인내라는 핵심 요소\n\n---\n\n#### 4. 수치/단위 괄호 금지\n\n❌ **금지 예시**:\n- 연간 매출(약 100억 원)\n- 성장률(전년 대비 15%)\n\n✅ **올바른 예시**:\n- 연간 매출이 약 100억 원에 달하며\n- 전년 대비 15%의 성장률을 기록했습니다\n\n---\n\n**핵심 원칙**:\n1. 괄호 대신 문장으로 자연스럽게 풀어쓰세요\n2. "~처럼", "~같은", "예를 들어", "~등" 표현을 활용하세요\n3. 영문 약어는 한글 표기만 사용하거나, 필요시 별도 문장으로 설명하세요\n'

    
    def _build_connected_intro_example(self = None, characters = None, category = None):
        '''
        장르 카테고리에 따른 연결형 캐릭터 소개 예시 생성

        기계적 나열("~는 ~입니다")이 아닌,
        캐릭터 간 관계를 자연스럽게 연결하는 소개 예시를 생성합니다.

        Args:
            characters: 캐릭터 목록
            category: 장르 카테고리 (\'historical\', \'dramatic\', \'revenge\', \'mystery\', \'default\')

        Returns:
            연결형 캐릭터 소개 예시 문자열
        '''
        if not characters:
            return '[나레이션]: 이 이야기의 주인공을 소개합니다.'
        main_char = None[0]
        main_name = main_char.get('name', '주인공')
        main_profile = main_char.get('profile', '')
        if len(characters) == 1:
            if category == 'historical':
                return f'''[나레이션]: {main_name}. {main_profile if main_profile else '이 이야기의 주인공입니다.'}'''
            return f'''{main_name}. {main_profile if main_profile else ''}'''
        sub_char = None[1]
        sub_name = sub_char.get('name', '조력자')
        sub_profile = sub_char.get('profile', '')
        third_char = characters[2] if len(characters) > 2 else None
        third_name = third_char.get('name', '') if third_char else ''
        third_profile = third_char.get('profile', '') if third_char else ''
        if category == 'historical':
            intro = f'''[나레이션]: {main_name}. {main_profile if main_profile else '이 이야기의 주인공입니다.'}\n[나레이션]: 그의 곁에는 {sub_name}가 있었습니다. {sub_profile if sub_profile else '그의 든든한 조력자였습니다.'}'''
            if third_char:
                intro += f'''\n[나레이션]: 그리고 {third_name}. {third_profile if third_profile else '또 다른 중요한 인물이었습니다.'}'''
            elif category == 'dramatic':
                intro = f'''[나레이션]: {main_name} 씨. {main_profile if main_profile else '평범한 일상을 살아가던 그에게 변화가 찾아옵니다.'}\n[나레이션]: 그런 그에게 {sub_name} 씨가 있었습니다. {sub_profile if sub_profile else '둘의 관계는 복잡하게 얽혀 있었습니다.'}'''
                if third_char:
                    intro += f'''\n[나레이션]: 그리고 {third_name} 씨. {third_profile if third_profile else '이야기의 또 다른 축을 이루는 인물입니다.'}'''
                elif category == 'revenge':
                    intro = f'''[나레이션]: {main_name}. {main_profile if main_profile else '그에게는 반드시 되갚아야 할 것이 있었습니다.'}\n[나레이션]: 그리고 {sub_name}. {sub_profile if sub_profile else '둘 사이에는 풀 수 없는 원한이 있었습니다.'}'''
                    if third_char:
                        intro += f'''\n[나레이션]: 그 사이에 {third_name}이 있었습니다. {third_profile if third_profile else '뜻밖의 변수가 되어줄 인물입니다.'}'''
                    elif category == 'mystery':
                        intro = f'''[나레이션]: {main_name}. {main_profile if main_profile else '모든 것은 그로부터 시작되었습니다.'}\n[나레이션]: 그리고 {sub_name}. {sub_profile if sub_profile else '그에게는 아무도 모르는 비밀이 있었습니다.'}'''
                        if third_char:
                            intro += f'''\n[나레이션]: 마지막으로 {third_name}. {third_profile if third_profile else '진실의 열쇠를 쥐고 있는 인물입니다.'}'''
                        elif category == 'heartwarming':
                            intro = f'''[나레이션]: {main_name} 씨. {main_profile if main_profile else '마음 한켠에 빈자리를 안고 살아가던 그에게'}\n[나레이션]: {sub_name} 씨가 찾아왔습니다. {sub_profile if sub_profile else '둘의 만남은 서로의 삶을 바꾸어 놓았습니다.'}'''
                            if third_char:
                                intro += f'''\n[나레이션]: 그리고 {third_name} 씨. {third_profile if third_profile else '이들의 이야기에 온기를 더해줄 인물입니다.'}'''
                            elif main_profile:
                                pass
                            
        intro = f'''{main_name}. {''}\n[나레이션]: 그리고 {sub_name}. {sub_profile if sub_profile else '둘의 관계는 이야기의 핵심이 됩니다.'}'''
        if third_char:
            intro += f'''\n[나레이션]: 마지막으로 {third_name}. {third_profile if third_profile else ''}'''
        return intro.strip()
