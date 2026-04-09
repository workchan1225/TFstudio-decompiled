# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: intro_hook_generator.pyc (Python 3.11)

'''
Intro Hook Generator - AI 기반 후킹 텍스트 생성

하이라이트 장면을 기반으로 시청자를 후킹할 텍스트/질문을 생성합니다.
'''
import json
import logging
from typing import Optional
logger = logging.getLogger(__name__)

class IntroHookGenerator:
    '''AI 기반 후킹 텍스트 생성'''
    HOOK_PROMPT = '당신은 YouTube 바이럴 영상의 인트로 후킹 카피라이터입니다.\n아래 장면 내용을 바탕으로 시청자가 스크롤을 멈추고 영상을 클릭하게 만드는 **후킹 텍스트**를 생성하세요.\n\n인트로 유형: {intro_type}\n장면 내용: {narration_text}\n\n{type_instruction}\n\n## 핵심 원칙\n- **호기심 갭(Curiosity Gap)**: 핵심 정보를 암시하되 완전히 공개하지 않아 답을 알고 싶게 만들 것\n- **오픈 루프(Open Loop)**: 질문이나 미완결 상황을 던져 시청자의 뇌가 답을 찾으려 하게 만들 것\n- **구체적 숫자/디테일**: 막연한 표현 대신 구체적인 숫자나 상황을 사용할 것\n- **감정 자극**: 놀라움, 분노, 공감, 불안 중 하나 이상의 감정을 자극할 것\n- "안녕하세요", "오늘은" 같은 평범한 시작은 절대 금지\n- 과장 없이도 극적인 문장을 만들 것\n\n반드시 아래 JSON 형식으로 응답하세요:\n```json\n{{\n  "hookText": "후킹 텍스트 (한국어, 20자 이내, 강렬하고 극적)",\n  "variants": ["대안 1 (다른 기법 적용)", "대안 2 (또 다른 기법 적용)"]\n}}\n```'
    TYPE_INSTRUCTIONS = {
        'highlight_question': '**질문형 (Irresistible Question)** — 답을 안 들을 수 없는 질문을 던지세요.\n시청자의 뇌는 질문을 들으면 자동으로 답을 찾으려는 심리적 루프가 생깁니다.\n좋은 예: "왜 아무도 이 방법을 알려주지 않았을까?", "이 남자가 모든 걸 버린 진짜 이유는?"\n나쁜 예: "오늘의 주제가 뭘까요?", "궁금하지 않으세요?" (너무 막연함)',
        'highlight_teaser': '**티저형 (Curiosity Gap / Before-After)** — 결과를 살짝 보여주되 과정은 숨기세요.\n가장 극적인 결과나 반전을 암시하여 "어떻게 그렇게 된 거지?" 하는 반응을 유도하세요.\n좋은 예: "모두가 불가능하다고 했다. 그런데 결과는 정반대였다.", "이 한마디가 모든 것을 뒤바꿨다"\n나쁜 예: "놀라운 결말이 기다립니다" (구체성 없이 막연한 약속)',
        'hook_text_only': '**임팩트형 (Pattern Interrupt / High-Stakes)** — 한 문장으로 시청자의 스크롤을 멈추세요.\n상식을 뒤집거나, 긴급한 경고를 하거나, 강렬한 반전을 제시하세요.\n검증된 패턴:\n- 반전형: "[상식] — 사실 완전히 틀렸습니다"\n- 경고형: "이거 모르면 전부 잃습니다"\n- 고백형: "3번 망하고 나서야 깨달았습니다"\n- 숫자형: "딱 하나만 바꿨을 뿐인데"',
        'custom': '**자유형** — 아래 7가지 검증된 바이럴 패턴 중 가장 적합한 것을 선택하세요:\n1. 반전/역설 (Unexpected Contradiction): 상식의 반대를 주장\n2. 구체적 숫자 약속 (Specific Number Promise): 기대치를 구체적으로 설정\n3. 개인 고백 (Personal Confession): 실패/실수를 솔직하게 고백\n4. 저항 불가 질문 (Irresistible Question): 답을 안 들을 수 없는 질문\n5. 결과 미리보기 (Before-After Snapshot): 변화의 결과를 먼저 제시\n6. 직관 반전 (Counterintuitive How-to): 직관에 반하는 방법론\n7. 긴급 경고 (High-Stakes Warning): 손해 회피 심리 자극' }
    
    def generate_hook_text(self = None, narration_text = None, intro_type = None, api_key = ('highlight_question', None)):
        """
        후킹 텍스트 생성

        Args:
            narration_text: 장면 나레이션 텍스트
            intro_type: 인트로 유형
            api_key: Google API 키

        Returns:
            {'hookText': '...', 'variants': ['...', '...']}
        """
        type_instruction = self.TYPE_INSTRUCTIONS.get(intro_type, self.TYPE_INSTRUCTIONS['custom'])
        prompt = self.HOOK_PROMPT.format(intro_type = intro_type, narration_text = narration_text[:500], type_instruction = type_instruction)
        
        try:
            GoogleProvider = GoogleProvider
            import app.services.ai.google_provider
            provider = GoogleProvider(api_key = api_key)
            response = provider.model.generate_content(prompt)
            text = response.text.strip()
            return self._parse_response(text)
        except Exception:
            e = None
            logger.error(f'''[IntroHookGenerator] 후킹 텍스트 생성 실패: {e}''')
            del e
            return None
            None = 
            del e


    HOOK_SCRIPT_PROMPT = '당신은 유튜브 조회수 100만 이상의 바이럴 영상 인트로를 전문으로 쓰는 카피라이터입니다.\n아래 영상의 핵심 장면들을 바탕으로 시청자가 처음 5초 안에 "이건 꼭 봐야 해"라고 느끼는 **후킹 인트로 대본**을 작성하세요.\n\n영상 하이라이트:\n{highlights_text}\n\n## 반드시 지켜야 할 핵심 원칙\n\n### 심리 기법 (최소 2가지 이상 적용)\n- **호기심 갭**: 핵심 정보를 암시만 하고 공개하지 않아 답을 듣기 전까지 이탈 불가능하게 만들기\n- **오픈 루프**: 미완결 상황이나 질문을 던져 시청자의 뇌가 자동으로 답을 찾게 만들기\n- **감정 자극**: 놀라움, 공감, 긴장감, 분노 중 하나 이상을 자극하기\n- **구체적 디테일**: 막연한 표현("놀라운", "대단한") 대신 구체적 상황/숫자 사용\n\n### 구조 (3-Beat 구조 권장)\n1. **첫 문장 (0~3초)**: 즉시 주의를 끄는 강렬한 한 마디 — 반전, 질문, 경고, 또는 충격적 사실\n2. **중간 (3~10초)**: 상황을 확장하고 긴장감을 높이는 문장 — "그런데", "하지만", "문제는" 등으로 전개\n3. **마지막 (10~15초)**: 영상을 봐야 하는 이유를 암시하는 문장 — 답을 알려줄 것을 약속하되 스포일러는 금지\n\n### 절대 하지 말 것\n- "안녕하세요", "여러분", "오늘은" 으로 시작하지 않기\n- "놀라운 사실을 알려드립니다" 같은 빈 약속 금지\n- 스포일러 금지 — 결과를 암시하되 직접 공개하면 안 됨\n- 설명조 금지 — "이 영상에서는 X를 다룰 건데요" 식의 메타 설명 금지\n\n### 검증된 바이럴 후킹 패턴 (적합한 것 선택)\n- 반전형: "모두가 [X]라고 믿었다. 하지만 진실은 정반대였다."\n- 질문형: "[구체적 상황]에서 [예상 밖 결과]가 나온 이유, 알고 있나요?"\n- 경고형: "[X]를 계속하면 [구체적 손해]를 피할 수 없습니다."\n- 고백형: "[실패/실수]를 겪고 나서야 깨달은 것이 있습니다."\n- 숫자형: "딱 [N]가지만 바꿨을 뿐인데 [극적 결과]가 일어났습니다."\n- 대비형: "[평범한 상황]. 그런데 [반전 상황]."\n\n## 출력 형식\n- 30초 이내 나레이션 분량 (약 80~120자)\n- 3~5줄로 나누어 자연스러운 나레이션 흐름\n- 각 줄은 완결된 문장\n- 한국어, 구어체, 나레이션에 적합한 톤\n\n반드시 아래 JSON 형식으로 응답하세요:\n```json\n{{\n  "hookScript": "전체 대본 (한 문장으로 합친 것)",\n  "hookScriptLines": ["줄1", "줄2", "줄3"],\n  "estimatedDuration": 15\n}}\n```'
    
    def generate_hook_script(self = None, highlights = None, api_key = None):
        """
        30초 미만 후킹 인트로 대본 생성

        Args:
            highlights: 하이라이트 장면 목록
            api_key: Google API 키

        Returns:
            {'hookScript': '...', 'hookScriptLines': ['...', '...'], 'estimatedDuration': 15}
        """
        highlights_text = (lambda .0: pass# WARNING: Decompyle incomplete
)(highlights[:5]())
        prompt = self.HOOK_SCRIPT_PROMPT.format(highlights_text = highlights_text)
        
        try:
            GoogleProvider = GoogleProvider
            import app.services.ai.google_provider
            provider = GoogleProvider(api_key = api_key)
            response = provider.model.generate_content(prompt)
            text = response.text.strip()
            return self._parse_script_response(text)
        except Exception:
            e = None
            logger.error(f'''[IntroHookGenerator] 후킹 대본 생성 실패: {e}''')
            del e
            return None
            None = 
            del e


    
    def _parse_script_response(self = None, text = None):
        cleaned = self._extract_json(text)
        
        try:
            data = json.loads(cleaned)
            return {
                'hookScript': data.get('hookScript', ''),
                'hookScriptLines': data.get('hookScriptLines', []),
                'estimatedDuration': data.get('estimatedDuration', 0) }
        except json.JSONDecodeError:
            logger.warning(f'''[IntroHookGenerator] 대본 JSON 파싱 실패: {text[:200]}''')
            return 


    _extract_json = (lambda text = None: if '```json' in text:
text.split('```json')[1].split('```')[0].strip()if None in text:
text.split('```')[1].split('```')[0].strip())()
    
    def _parse_response(self = None, text = None):
        cleaned = self._extract_json(text)
        
        try:
            data = json.loads(cleaned)
            return {
                'hookText': data.get('hookText', ''),
                'variants': data.get('variants', []) }
        except json.JSONDecodeError:
            logger.warning(f'''[IntroHookGenerator] JSON 파싱 실패: {text[:200]}''')
            return
