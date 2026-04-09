# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: creative_title_enhancer.pyc (Python 3.11)

'''
창의적 제목 강화 프롬프트 시스템

기존 제목들을 분석하여 더 자극적이고 창의적인 변형 제목 생성
'''
from typing import Optional
from app.utils.title_pattern_profile import build_title_style_instruction, normalize_title_style_profile
CREATIVE_STRATEGIES = {
    'provocative': {
        'name': '도발적 변형',
        'instruction': '\n**도발적 변형 전략:**\n- "~하다" → "~해도 되는 걸까?" (의문 유발)\n- 금기어 암시: "아무도 말 안 하는", "함부로 말 못하는", "숨겨진"\n- 대비 강화: "부자들만 아는 vs 서민들은 모르는", "전문가 vs 일반인"\n- 반전 암시: "그런데 진짜 문제는...", "하지만 아무도 몰랐다"\n',
        'examples': [
            '원본: "재테크 성공 비결 5가지" → 변형: "은행원도 함부로 말 못하는 재테크의 진짜 비밀"',
            '원본: "다이어트 방법" → 변형: "의사들이 환자한테 절대 안 알려주는 다이어트 진실"'] },
    'emotional': {
        'name': '감정 극대화',
        'instruction': '\n**감정 극대화 전략:**\n- 분노 유발: "당신도 당하고 있다", "속고 있었다", "배신당한"\n- 공감 유발: "나만 이런 줄 알았는데", "다들 겪는 일", "왜 아무도 안 알려줬지"\n- 충격 유발: "경악", "오열", "무릎 꿇다", "소름끼치는"\n- 호기심 유발: "결국...", "알고보니", "반전은"\n',
        'examples': [
            '원본: "주식 투자 실패 사례" → 변형: "3억 날리고 오열한 40대...결국 그가 깨달은 것"',
            '원본: "직장인 현실" → 변형: "당신도 매일 당하고 있다...회사가 숨기는 불편한 진실"'] },
    'curiosity': {
        'name': '호기심 극대화',
        'instruction': '\n**호기심 극대화 전략:**\n- 수수께끼형: "왜 ~일까?", "어떻게 ~했을까?", "도대체 무슨 일이"\n- 반전 암시: "그런데 진짜 이유는...", "알고 보니 전혀 달랐다"\n- 숫자 강조: "단 3초", "99%가 모르는", "1%만 아는", "단 1가지"\n- 비밀 암시: "비밀리에", "극비", "공개 불가였던"\n',
        'examples': [
            '원본: "성공한 CEO 특징" → 변형: "왜 억만장자들은 새벽 4시에 일어날까? 99%가 모르는 이유"',
            '원본: "건강 관리 팁" → 변형: "의사가 절대 공개 안 하던 건강 비법...단 1가지"'] },
    'urgency': {
        'name': '긴급성 부여',
        'instruction': '\n**긴급성 부여 전략:**\n- 시간 한정: "지금 당장", "늦기 전에", "당장 확인하세요", "오늘 안에"\n- 손실 회피: "놓치면 후회할", "모르면 손해보는", "안 하면 망하는"\n- 트렌드 연결: "요즘 난리난", "핫한", "화제의", "터진"\n- 위기감: "시간이 없다", "이미 늦었다", "마지막 기회"\n',
        'examples': [
            '원본: "투자 정보" → 변형: "지금 당장 확인 안 하면 후회할 투자 정보...시간 없다"',
            '원본: "건강 검진" → 변형: "이 증상 무시하면 진짜 큰일 난다...늦기 전에 확인하세요"'] },
    'authority': {
        'name': '권위 활용',
        'instruction': '\n**권위 활용 전략:**\n- 전문가 인용: "하버드 교수가 밝힌", "서울대 연구팀 발표", "의사 출신 유튜버"\n- 내부자 정보: "업계 관계자 폭로", "현직 직원이 밝힌", "전 직원 증언"\n- 데이터 기반: "100만명 조사 결과", "10년 추적 연구", "통계로 증명된"\n- 경험 기반: "20년 경력", "1000명 상담", "직접 경험한"\n',
        'examples': [
            '원본: "수면의 중요성" → 변형: "하버드 수면연구소가 밝힌 충격적 진실...매일 이렇게 자면 수명 단축"',
            '원본: "회사 생활 팁" → 변형: "대기업 인사팀장 출신이 폭로한 승진의 진짜 비밀"'] } }

def build_creative_title_prompt(existing_titles, genre, content_type = None, language = None, count = None, title_style_profile = ('', '', '한국어', 10, 'hybrid', 50), title_style_mix = ('existing_titles', list, 'genre', str, 'content_type', str, 'language', str, 'count', int, 'title_style_profile', str, 'title_style_mix', int, 'return', str)):
    """
    기존 제목 기반 창의적 제목 생성 프롬프트 빌드

    Args:
        existing_titles: 기존 생성된 제목 리스트 [{'title': str, 'description': str}, ...]
        genre: 장르
        content_type: 콘텐츠 타입
        language: 언어
        count: 생성할 제목 수

    Returns:
        str: AI에게 전달할 프롬프트
    """
    (normalized_profile, normalized_mix) = normalize_title_style_profile(title_style_profile, title_style_mix)
    style_instruction = build_title_style_instruction(normalized_profile, normalized_mix, context = 'script_titles', genre = genre)
    titles_text = (lambda .0: for t in .0:
passcontinue'- '[f'''{t}'''])(existing_titles[:10]())
    strategies_text = ''
    for key, strategy in CREATIVE_STRATEGIES.items():
        strategies_text += f'''\n### {strategy['name']}\n'''
        strategies_text += strategy['instruction']
        strategies_text += '\n**예시:**\n'
        for example in strategy['examples']:
            strategies_text += f'''  {example}\n'''
    prompt = f'''당신은 유튜브 바이럴 콘텐츠 전문가입니다.\n주어진 기존 제목들을 분석하고, 더 자극적이고 클릭을 유도하는 새로운 제목 {count}개를 생성해주세요.\n\n## 기존 제목 (분석 대상)\n{titles_text}\n\n## 장르 정보\n- 장르: {genre if genre else '일반'}\n- 콘텐츠 타입: {content_type if content_type else '일반'}\n- 언어: {language}\n\n## 제목 스타일 프로필\n{style_instruction}\n\n## 창의적 변형 전략\n다음 5가지 전략을 골고루 활용하여 각각 다른 스타일의 제목을 만드세요:\n{strategies_text}\n\n## 생성 지침\n\n1. **기존 제목 분석**: 주제, 키워드, 타겟 독자를 파악하세요\n2. **전략 혼합**: 5가지 전략을 조합하여 각 제목마다 다른 접근법 사용\n3. **구체성 유지**: 추상적 표현 대신 구체적 숫자, 대상, 상황 명시\n4. **감정 자극**: 분노, 호기심, 공포, 기대 등 감정을 자극하는 표현 사용\n5. **클릭베이트 but 신뢰**: 자극적이지만 허위 정보 암시 금지\n\n## 금지 사항\n- 기존 제목과 동일한 구조 반복 ❌\n- 지나친 추상적 표현 ("놀라운", "대박") ❌\n- 허위 정보 암시 ❌\n- 같은 패턴 3개 이상 반복 ❌\n\n## 출력 형식\n각 제목은 다음 형식으로 출력하세요:\n1. [자극적인 제목] | [50자 이내 설명 - 왜 이 제목이 효과적인지]\n2. [자극적인 제목] | [50자 이내 설명]\n...\n\n{count}개의 창의적이고 자극적인 제목을 생성해주세요.'''
    return prompt


def get_diversity_instruction():
    '''
    기본 제목 생성 시 다양성 확보를 위한 추가 지시사항

    Returns:
        str: 다양성 지침 프롬프트
    '''
    return '\n=== 제목 다양성 지침 (필수) ===\n\n**각 제목은 반드시 다른 접근 방식을 사용하세요:**\n\n1. **질문형 제목** (2개)\n   - "왜 ~일까?", "~하면 어떨까?", "도대체 ~?"\n   - 시청자의 궁금증을 직접 자극\n\n2. **반전형 제목** (2개)\n   - "~인 줄 알았는데", "사실은 ~", "알고 보니"\n   - 기존 상식을 뒤집는 구조\n\n3. **감정형 제목** (2개)\n   - 분노: "참을 수 없는", "당하고만 있을 건가"\n   - 공감: "나만 그런 줄 알았는데", "다들 겪는"\n   - 감동: "눈물 없이 못 보는", "울컥"\n\n4. **정보형 제목** (2개)\n   - "~하는 방법 완벽 정리", "~가지", "A to Z"\n   - 실용적 가치 강조\n\n5. **트렌드형 제목** (2개)\n   - 시사 연결, "요즘 화제인", "난리난"\n   - 현재 이슈와 연결\n\n**반드시 지켜야 할 금지 사항:**\n- 10개 제목이 비슷한 구조/패턴 반복 ❌\n- 같은 키워드 3회 이상 반복 ❌\n- 같은 감정 유형만 사용 ❌\n- "~합니다", "~입니다" 등 설명체 반복 ❌\n\n**다양성 체크리스트:**\n□ 질문형 2개 포함?\n□ 반전형 2개 포함?\n□ 감정형 2개 포함?\n□ 정보형 2개 포함?\n□ 트렌드형 2개 포함?\n□ 각 제목의 첫 단어가 모두 다른가?\n'
