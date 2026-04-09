# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: info_content_system.pyc (Python 3.11)

'''
정보/교양 장르를 위한 고급 콘텐츠 시스템

이 모듈은 지식 전달형 유튜브 대본을 위한 페르소나, 어조 원칙,
금지 표현, 리텐션 훅, 알고리즘 전략을 정의합니다.

적용 장르 (10개):
- LIFE_KNOWLEDGE, OFFICE_SURVIVAL, MONEY_SENSE, RELATIONSHIP_EQ
- PSYCHOLOGY, LIFE_CHOICES, KNOWLEDGE_BITE
- NEWS_REPORT, REVIEW_ANALYSIS, COMEDY
'''
from typing import Dict, List, Optional, Tuple
import random
INFO_PERSONA = {
    'identity': '100만 구독자를 보유한 지식·이슈 분석 유튜브 채널의 메인 호스트',
    'mindset': {
        'wrong': '설명하는 사람',
        'right': '이미 결론을 알고 있고, 시청자를 그 결론까지 끌고 가는 사람' },
    'goal': "시청자가 '어? 이거... 내 얘기잖아?'라고 느끼게 만드는 것",
    'tone_reference': {
        'wrong': [
            '뉴스 앵커',
            '교수',
            '유튜브 강사'],
        'right': '옆집 사는 똑똑한 형/누나가 술자리에서 진지하게 썰 풀어주는 느낌' },
    'attitude': "설득하지 마세요. '이게 현실이다'라는 태도로 말하세요." }
WRITING_PRINCIPLES = {
    '1_no_abstract': {
        'name': '추상적 비유 금지',
        'description': "'위험한 설계', '보이지 않는 위협' 같은 표현 금지. 시청자의 실제 하루를 가져오세요.",
        'bad_example': '구조적 위험이 커지고 있습니다',
        'good_example': '내일 아침 출근길에, 여러분 차가 미끄러질 수 있는 상황입니다',
        'bad_example_2': '경제적 불확실성이 증가하고 있습니다',
        'good_example_2': '이번 달 월급, 10만원이 사라질 수 있습니다' },
    '2_sentence_rhythm': {
        'name': '문장 호흡 조절',
        'description': '긴 문장 → 아주 짧은 문장 → 다시 긴 문장. 리듬이 느껴져야 합니다.',
        'example': '이건 단순한 문제가 아닙니다. 진짜 큰일이에요. 남 일이 아닙니다.',
        'pattern': '긴 → 짧 → 긴 → 짧' },
    '3_tone_balance': {
        'name': '반말과 존댓말의 경계 유지',
        'description': '완전 반말도, 완전 존댓말도 아닌 친근하지만 권위 있는 중간 지점 유지',
        'wrong': [
            '완전 반말',
            '완전 존댓말'],
        'right': '친근하지만 권위 있는 중간 지점' },
    '4_interjections': {
        'name': '추임새 적극 삽입',
        'description': '실제 말하는 사람처럼 끊어가세요.',
        'examples': [
            '솔직히 말해서',
            '자, 잘 들어보세요',
            '이게 왜 문제냐면요',
            '여기서 대부분 착각합니다',
            '근데 말이죠',
            '아, 이게 중요해요',
            '잠깐, 여기서'] },
    '5_fact_first_then_question': {
        'name': '팩트 먼저, 질문은 1개만',
        'description': '★★★ 인트로에서 질문만 나열하지 마세요! 반드시 구체적 데이터/사례로 시작하고, 질문은 챕터당 최대 1-2개만 사용하세요.',
        'wrong_pattern': '질문 → 질문 → 질문 → 질문 (❌ 질문 폭탄 금지)',
        'right_pattern': '충격적 팩트/데이터 → 시청자 일상 연결 → 질문 1개 → 예시/사례 → 심층 정보',
        'example_wrong': '왜 이럴까요? 어떻게 될까요? 무슨 의미일까요? 과연 우리는 뭘 해야 할까요?',
        'example_right': '매일 커피 3잔을 마시면 심장병 위험이 23% 낮아집니다. 하버드 의대 12만명 추적 연구 결과입니다. 그런데 여러분, 이상하지 않으세요? 지금부터 그 비밀을 파헤쳐보겠습니다.',
        'rules': [
            '인트로 첫 문장 = 무조건 구체적 숫자/데이터/사례',
            '질문은 챕터당 최대 2개 (연속 질문 금지)',
            '질문 뒤에는 반드시 구체적 답변/예시 따라와야 함',
            "추상적 질문 금지 ('과연 무엇일까요?', '어떤 의미일까요?' 등)"] },
    '6_no_over_explain': {
        'name': '설명 과잉 금지',
        'description': '정의 → 예시 → 재정의, 이 3단계를 절대 모두 쓰지 마세요. 정의는 생략하고 바로 예시부터 시작하세요.',
        'wrong_pattern': '정의 → 예시 → 재정의',
        'right_pattern': '예시부터 시작 (이해는 시청자가 하게 두세요)' } }
FORBIDDEN_EXPRESSIONS = [
    '정리하자면',
    '쉽게 말해',
    '결론적으로',
    '중요한 점은',
    '~라고 볼 수 있습니다',
    '요약하면',
    '다시 말해',
    '간단히 말해서']
ALTERNATIVE_EXPRESSIONS = {
    '정리하자면': '그래서 어떤 일이 벌어지냐면요',
    '쉽게 말해': '(삭제하고 예시로 시작)',
    '결론적으로': '결국 남는 건 이거예요',
    '중요한 점은': '이건 꼭 알고 가세요',
    '~라고 볼 수 있습니다': '~인 거죠',
    '요약하면': '그래서 뭐가 남냐면요',
    '다시 말해': '(삭제하고 다른 예시로)',
    '간단히 말해서': '핵심만 말씀드리면요' }
RECOMMENDED_ENDINGS = [
    '~인 거죠',
    '~거든요',
    '~일 수밖에 없습니다',
    '이게 말이 되나요?',
    '~잖아요',
    '~하는 거예요']
INFO_STRUCTURE = {
    '1_fact_based_hook': {
        'name': '도입부 (The Fact-Based Hook)',
        'duration': '초반 30초',
        'description': '★★★ 질문이 아닌 구체적 데이터/사례로 시작하세요! 시청자의 스크롤을 멈추게 하는 충격적 팩트가 먼저입니다.',
        'goal': "시청자가 '이건 알아두면 좋겠다'라고 느끼게",
        'formula': [
            '1️⃣ 충격적 데이터/사례 (첫 문장 = 무조건 구체적 숫자/사실)',
            '2️⃣ 시청자 일상 연결 (이게 왜 당신 문제인지)',
            '3️⃣ 질문 1개 (선택적, 연속 질문 금지)',
            '4️⃣ 영상 가치 미리보기 (끝까지 봐야 하는 이유)'],
        'intro_template': {
            'step1_fact_shock': "[구체적 숫자/연구 결과/사례] - 예: '매일 커피 3잔을 마시면 심장병 위험이 23% 낮아집니다.'",
            'step2_relevance': "[시청자 일상 연결] - 예: '여러분도 매일 아침 커피 한 잔으로 하루를 시작하시죠?'",
            'step3_single_question': "[질문 1개만, 선택적] - 예: '그런데 왜 커피가 건강에 좋다는 사실이 이제서야 밝혀졌을까요?'",
            'step4_value_preview': "[영상 가치] - 예: '오늘 영상에서 그 비밀을 파헤쳐보겠습니다.'" },
        'important_rules': [
            '★ 첫 문장은 무조건 구체적 숫자/데이터/사례 (질문으로 시작 금지)',
            '★ 연속 질문 절대 금지 (질문 → 질문 → 질문 패턴 차단)',
            '★ 질문 뒤에는 반드시 구체적 답변/예시 필수',
            "추상적 표현 금지 ('경이로운', '놀라운', '비밀스러운' 등)",
            '검증되지 않은 정보나 과장된 주장 금지'],
        'bad_examples': [
            "❌ '왜 인류는 가장 깊은 고통 속에서도 다시 일어설 수 있을까요?' (질문으로 시작)",
            "❌ '우리가 매일 마주하는 상실과 절망의 순간들 속에서, 우리 몸은 과연 어떤 비밀스러운 기적을 품고 있는 것일까요?' (추상적 + 질문)",
            "❌ '이 질문은 과학과 철학의 경계를 넘나들며...' (추상적 설명)"],
        'good_examples': [
            "✅ '2023년 네이처지에 발표된 연구에 따르면, 극심한 트라우마를 겪은 사람의 67%가 5년 내 완전히 회복했습니다.'",
            "✅ '지난 10년간 노벨 생리의학상 수상 연구의 40%가 바로 이 주제를 다뤘습니다.'",
            "✅ '매일 아침 일어나서 하는 이 습관, 당신의 수명을 10년 줄이고 있을 수 있습니다.'"],
        'closing_teaser': '이 영상 끝까지 보시면, 이 주제에 대해 더 잘 이해하실 수 있을 겁니다.' },
    '2_curiosity_gap': {
        'name': '중간 브릿지 (Curiosity Gap)',
        'description': '정보를 다 주지 마세요. 반드시 멈추세요.',
        'rule': '정보 과부하 방지, 호기심 유지' },
    '3_deep_analysis': {
        'name': '본론 (The Deep Analysis)',
        'subtitle': "'남의 일 → 내 문제'",
        'connections': {
            '국가 통계': '내 지갑',
            '정책 이야기': '이번 달 카드값',
            '경제 구조': '내일 점심값' },
        'preemptive_rebuttal': {
            'trigger': '이렇게 반박하는 분들 분명히 나옵니다',
            'action': '그리고 그 반박을 즉시 깨부수세요' } },
    '4_grand_insight': {
        'name': '결론 (The Grand Insight)',
        'rules': [
            '요약하지 마세요',
            '교훈으로 끝내지 마세요'],
        'composition': [
            '시청자의 가치관을 흔드는 질문',
            '불편한 통찰',
            '다음 영상이 궁금해지는 여지'],
        'final_question_rule': "의견이 아니라 '선택'을 강요해야 합니다",
        'examples': [
            '여러분이라면 들어가시겠습니까, 피하시겠습니까?',
            '지금 버티시겠습니까, 정리하시겠습니까?',
            '이 상황에서 여러분은 어떤 선택을 하시겠습니까?'] } }
RETENTION_HOOKS = {
    'fear_transition': {
        'name': "'지금부터 진짜다' 계열 (전환용)",
        'hooks': [
            '자, 여기서부터 얘기가 완전히 달라집니다',
            '지금까지는 예고편이었고요',
            '이 부분이 정말 핵심이에요',
            '지금부터가 핵심이에요',
            '이제 진짜 문제로 들어갑니다',
            '여기서부터 집중해서 보시면 좋겠습니다',
            '여기서 한 번 더 생각해볼 부분이 있어요'] },
    'cognitive_dissonance': {
        'name': "'인지적 부조화' 유도 질문형",
        'hooks': [
            '여기까지 들으셨으면 이런 생각 들죠?',
            '이쯤 되면 한 가지 의문이 생깁니다',
            '이게 과연 정상적인 구조일까요?',
            '여러분이라면 이 상황, 납득되세요?',
            '이게 정말 우연이라고 보이세요?',
            '개인의 문제처럼 보이지만, 더 큰 맥락이 있습니다'] },
    'structure_reveal': {
        'name': "'구조 분석' 계열",
        'hooks': [
            '이건 운이 나빠서 생긴 일이 아닙니다',
            '여기에는 분명한 패턴이 있습니다',
            '사람 몇 명의 실수가 아니에요',
            '데이터를 보면 이런 경향이 보입니다',
            '이 구조를 이해하면 대응할 수 있습니다',
            '통계를 보면 이런 패턴이 반복됩니다'] },
    'break_illusion': {
        'name': "'새로운 관점 제시' 계열",
        'hooks': [
            '많은 분들이 이렇게 생각하시는데, 다른 관점도 있습니다',
            '이 판단, 정말 많은 분들이 하시죠',
            '이게 합리적인 선택처럼 보이죠?',
            '지금 이 말에 고개 끄덕이셨다면, 한 가지 더 생각해보세요',
            '이 논리, 한 번 더 검토해볼 필요가 있어요',
            '숫자를 하나만 바꾸면, 얘기가 완전히 달라집니다'] },
    'real_answer': {
        'name': "'핵심 원인 분석' 계열 (전환용)",
        'hooks': [
            '문제는 우리가 보는 그게 아닙니다',
            '진짜 원인은 전혀 다른 데 있습니다',
            '표면적인 현상 뒤에 더 중요한 요소가 있습니다',
            '본질은 따로 있습니다',
            '다들 결과만 보지, 원인은 안 봅니다',
            '시선 하나만 바꾸면 구조가 보입니다'] },
    'algorithm_pressure': {
        'name': '자연스러운 리텐션 유도 문구',
        'hooks': [
            '이 부분이 가장 핵심입니다',
            '이 다음 얘기가 더 중요합니다',
            '이건 꼭 알고 가셔야 합니다',
            '잠깐만 더 보시면 전체 그림이 보입니다',
            '여기서 핵심 포인트가 나옵니다'] },
    'hook_transition': {
        'name': "한 문장으로 '훅+전환' 동시에 쓰는 문구",
        'hooks': [
            '이제 전체 구조가 보이기 시작할 거예요',
            '여기까지 들으셨다면, 이미 절반은 오셨습니다',
            '이제 그림이 조금씩 보이기 시작하죠',
            '지금부터 숫자가 말을 하기 시작합니다',
            '감정 빼고, 구조만 보겠습니다'] },
    'cta_watch_complete': {
        'name': '시청 완료 유도형 (CTA)',
        'description': '영상을 끝까지 보도록 유도하는 문구. 도입부나 중반에 사용',
        'hooks': [
            '이 정보가 필요하시다면, 이 영상을 끝까지 봐주셔야 합니다',
            '영상 마지막에 가장 중요한 포인트가 나옵니다',
            '끝까지 보시면 핵심 솔루션을 알려드립니다',
            '이 내용을 놓치면 정말 손해입니다. 끝까지 집중해주세요',
            '마지막 파트가 가장 중요하니 꼭 끝까지 시청해주세요',
            '여기서 멈추면 안 됩니다. 진짜 중요한 건 다음입니다',
            '이 다음에 나오는 내용이 핵심입니다',
            '끝까지 보시면 전체 그림이 보입니다'],
        'placement': {
            'intro': '도입부에서 기대감 형성',
            'middle': '중반 전환점에서 리마인드',
            'before_climax': '클라이맥스 직전 긴장감 조성' } },
    'cta_engagement': {
        'name': '참여 유도형 (CTA)',
        'description': '좋아요, 구독, 댓글 등 시청자 참여를 유도하는 문구. 마무리에 사용',
        'hooks': [
            '오늘 영상이 도움되셨다면 좋아요 부탁드립니다',
            '더 많은 정보가 궁금하시다면 구독 눌러주세요',
            '알림 설정하시면 새로운 영상을 가장 먼저 받아보실 수 있습니다',
            '댓글로 여러분의 생각을 나눠주세요',
            '이런 정보가 필요하셨다면 좋아요로 알려주세요',
            '다음에 다뤘으면 하는 주제가 있다면 댓글로 남겨주세요'],
        'placement': '마무리 챕터에서 자연스럽게 삽입' } }
ALGORITHM_RULES = {
    'retention_mentions': {
        'rule': '영상 중 최소 3번 리텐션 멘트 삽입',
        'examples': [
            '이 부분이 핵심입니다',
            '이건 꼭 알고 가세요'],
        'placement': '자연스럽게 삽입' },
    'viewer_treatment': {
        'wrong': '시청자를 가르치려 하지 마세요',
        'right': '시청자와 함께 탐구하는 동반자로 대하세요' },
    'ending_style': {
        'rule': '생각할 거리를 남기고 끝내세요',
        'effect': '다음 영상에서 더 깊이 다룰 내용을 자연스럽게 언급하세요' },
    'cta_strategy': {
        'rule': 'CTA(시청 유도)는 자연스럽게, 최소 2회 삽입',
        'placement': {
            'intro': "도입부에서 '끝까지 봐야 하는 이유' 제시",
            'middle': "중반 전환점에서 '다음 내용이 핵심' 리마인드",
            'outro': '마무리에서 참여 유도 (좋아요/구독/댓글)' },
        'principles': [
            '콘텐츠 맥락에 맞게 자연스럽게 삽입',
            "과도한 압박 금지 ('반드시', '꼭' 남발 자제)",
            "가치 제시형 ('도움되셨다면', '궁금하시다면')"],
        'intro_cta_examples': [
            '이 정보가 필요하시다면, 이 영상을 끝까지 봐주셔야 합니다',
            '영상 마지막에 가장 중요한 포인트가 나옵니다',
            '끝까지 보시면 핵심 솔루션을 알려드립니다'],
        'outro_cta_examples': [
            '오늘 영상이 도움되셨다면 좋아요 부탁드립니다',
            '더 많은 정보가 궁금하시다면 구독 눌러주세요'] } }
ANALYSIS_GUIDELINES = {
    'numbers': '수치는 단정하지 말고 범위로 말하세요',
    'mechanism': '메커니즘은 반드시 설명하세요 (예: 왜 매년 오르는지, 언제 비용이 터지는지)',
    'data_presentation': '데이터는 나열하지 말고 인과관계로 설명하세요',
    'example': 'A가 벌어진 이유는 사실 B라는 구조 때문이었습니다.' }
GENRE_SPECIFIC_GUIDES = {
    'LIFE_KNOWLEDGE': {
        'focus': "생활 꿀팁 - '미리 알았으면 손해 안 봤을' 정보",
        'hook_type': 'break_illusion',
        'emphasis': [
            '실용적 액션 포인트',
            '즉시 적용 가능한 팁'],
        'tip': "정보+사례 스토리 조합, '이것만 알면' 패턴 활용" },
    'OFFICE_SURVIVAL': {
        'focus': '직장 노하우 - 회사에서 바로 써먹는 생존법',
        'hook_type': 'cognitive_dissonance',
        'emphasis': [
            '경험담+팁',
            '공감 포인트'],
        'tip': '직장인의 일상 속 구체적 상황 제시' },
    'MONEY_SENSE': {
        'focus': '돈 이야기 - 돈 지키는 법 (돈 버는 법 아님)',
        'hook_type': 'structure_reveal',
        'emphasis': [
            '반감 없는 신뢰감',
            '수치 기반 설명'],
        'tip': "'돈 버는 법' 대신 '돈 지키는 법'으로 접근" },
    'ECONOMICS': {
        'focus': '경제학 - 경제 현상의 구조와 메커니즘 이해',
        'hook_type': 'structure_reveal',
        'emphasis': [
            '거시경제 개념',
            '데이터 기반 분석',
            '정책과 일상의 연결'],
        'tip': "거시경제 개념을 개인의 일상 경험에 연결. 예: '전기요금 인상' → '기준금리 인상' → '왜 인상했는가'" },
    'RELATIONSHIP_EQ': {
        'focus': '관계의 기술 - 관계 스트레스 줄이는 방법',
        'hook_type': 'cognitive_dissonance',
        'emphasis': [
            '생각 전환',
            '상대방 심리 분석'],
        'tip': '공감 먼저, 해결책 나중' },
    'PSYCHOLOGY': {
        'focus': '심리 이야기 - 과학 기반의 행동 심리',
        'hook_type': 'break_illusion',
        'emphasis': [
            '과학적 근거',
            '쉬운 설명',
            '실천법'],
        'tip': '어려운 심리학 용어 대신 일상 언어 사용' },
    'LIFE_CHOICES': {
        'focus': '인생 가이드 - 선택의 기준 제시',
        'hook_type': 'real_answer',
        'emphasis': [
            '정답 제시 X',
            '판단 기준 제시 O'],
        'tip': '결론 강요 대신 프레임워크 제공' },
    'KNOWLEDGE_BITE': {
        'focus': '상식 플러스 - 역사/과학/기술의 교양',
        'hook_type': 'hook_transition',
        'emphasis': [
            '짧고 임팩트',
            '호기심 자극'],
        'tip': '놀라운 사실로 시작, 일상 연결로 마무리' },
    'NEWS_REPORT': {
        'focus': '뉴스/리포트 - 객관적 보도 형식',
        'hook_type': 'fear_transition',
        'emphasis': [
            '역피라미드',
            '5W1H',
            '출처 명시'],
        'tip': '팩트 기반이되 리텐션 훅 유지' },
    'REVIEW_ANALYSIS': {
        'focus': '리뷰/분석 - 평가와 비평',
        'hook_type': 'structure_reveal',
        'emphasis': [
            '평가 기준 제시',
            '장단점 균형'],
        'tip': '주관적 의견에 객관적 근거 덧붙이기' },
    'COMEDY': {
        'focus': '코미디 - 웃음과 유머 중심',
        'hook_type': 'hook_transition',
        'emphasis': [
            '건전한 가족 유머',
            '비속어 금지'],
        'tip': '정보성 콘텐츠에 유머 터치 추가' } }

def get_info_prompt_enhancement(genre = None, language = None, persuasion_mode = None):
    """
    장르에 맞는 정보 콘텐츠 강화 프롬프트를 반환합니다.

    Args:
        genre: 장르 코드 (예: 'LIFE_KNOWLEDGE', 'PSYCHOLOGY')
        language: 언어 코드 (기본값: 'ko')
        persuasion_mode: 6단계 설득형 구조 적용 여부 (기본값: True)

    Returns:
        장르별 강화 프롬프트 문자열
    """
    genre_upper = genre.upper()
    genre_guide = GENRE_SPECIFIC_GUIDES.get(genre_upper, GENRE_SPECIFIC_GUIDES.get('LIFE_KNOWLEDGE'))
    hook_type = genre_guide.get('hook_type', 'break_illusion')
    sample_hooks = get_retention_hooks(hook_type, count = 3)
    prompt = chr(10).join[f'''{(lambda .0: [ f'''- "{h}"''' for h in .0 ])(sample_hooks())}''']['\n\n### 장르 특화 팁\n'][f'''{genre_guide.get('tip', '시청자의 일상과 연결하라')}'''](chr(10).join[f'''{(lambda .0: [ f'''- "{h}"''' for h in .0 ])(sample_hooks())}''']['\n\n### 장르 특화 팁\n'][f'''{genre_guide.get('tip', '시청자의 일상과 연결하라')}''']['\n\n### 알고리즘 생존\n- 최소 3번 리텐션 멘트 삽입\n- 시청자와 함께 탐구하는 동반자로 대하세요\n- 생각할 거리를 남기고 끝내세요\n\n### ⚠️ 인트로(챕터1) 작성 규칙 (매우 중요!)\n\n**★ 첫 문장 = 무조건 구체적 데이터/사례 (질문으로 시작 금지!)**\n\n❌ 절대 금지 패턴 (질문 폭탄):\n- "왜 인류는 ~할까요? 과연 우리는 ~? 무슨 의미일까요? 어떤 비밀이 숨겨져 있을까요?"\n- 연속 질문 (질문 → 질문 → 질문)\n- 추상적 질문 ("과연 무엇일까요?", "어떤 의미일까요?")\n\n✅ 올바른 인트로 패턴:\n```\n[Step 1] 충격적 팩트: "2023년 네이처지 발표에 따르면, 트라우마 환자의 67%가 5년 내 완전 회복했습니다."\n[Step 2] 시청자 연결: "여러분도 한 번쯤 힘든 시기를 겪어보셨죠?"\n[Step 3] 질문 1개: "그런데 왜 어떤 사람은 빨리 회복하고, 어떤 사람은 오래 걸릴까요?"\n[Step 4] 가치 미리보기: "오늘 영상에서 그 비밀을 파헤쳐보겠습니다."\n```\n\n**인트로 체크리스트**:\n- [ ] 첫 문장이 구체적 숫자/데이터/사례로 시작하는가?\n- [ ] 연속 질문이 없는가? (질문은 챕터당 최대 1-2개)\n- [ ] 질문 뒤에 반드시 구체적 답변/예시가 따라오는가?\n- [ ] 추상적 표현("경이로운", "놀라운", "비밀스러운") 없는가?\n\n### 🔍 논리적 일관성 검증 (필수)\n**주어와 시간 표현 일관성 확인**:\n- ❌ "인류는 수십 년간" → ✅ "과학자들은 수십 년간" 또는 "인류는 약 한 세기 동안"\n- ❌ "인간은 최근 몇 년간" → ✅ "현대인은 최근 몇 년간"\n- 구체적 연도 언급 시 계산 검증 (예: 1930년대~현재 = 약 90년, "수십 년" 아닌 "약 한 세기")\n'])
    if persuasion_mode and genre_upper in PERSUASION_APPLICABLE_GENRES:
        persuasion_config = PERSUASION_APPLICABLE_GENRES[genre_upper]
        persuasion_prompt = _build_persuasion_structure_prompt(genre_upper, persuasion_config)
        prompt += f'''\n{persuasion_prompt}'''
    return prompt.strip()


def _build_persuasion_structure_prompt(genre = None, config = None):
    '''
    6단계 설득형 구조 프롬프트를 생성합니다.

    Args:
        genre: 장르 코드
        config: PERSUASION_APPLICABLE_GENRES의 장르별 설정

    Returns:
        설득형 구조 프롬프트 문자열
    '''
    identity_target = config.get('identity_shift_target', '깨어있는 사람')
    sanctuary_focus = config.get('sanctuary_focus', '')
    techniques = config.get('primary_techniques', [])
    prompt = '\n## 🎯 6단계 설득형 서사 구조 (고몰입·고전환)\n\n**핵심 원칙**: "정보 전달자가 아닌, 시대를 앞서가는 가이드"로 포지셔닝\n\n### 1단계: Metaphor Hook (비유 충격) - 첫 15초\n- **목적**: 극단적 비유로 호기심+긴장감 동시 자극\n- **심리학**: 인지 충격으로 즉각적 주의 집중\n- **예시**: "지금 여러분은 3만km 열차를 타고 절벽으로 달리고 있습니다"\n- **금지**: 추상적 비유, 평범한 시작, 팩트 나열\n\n### 2단계: Value Attack (가치 전면 부정) - 15-45초\n- **목적**: 시청자의 \'성역\'(당연한 믿음)을 흔들어 인지 부조화 유발\n- **심리학**: 믿음이 흔들리면 답을 찾으려 집중\n'
    if sanctuary_focus:
        prompt += f'''- **이 장르 성역**: {sanctuary_focus}\n'''
    prompt += '- **패턴**: "여러분은 지금 [당연한 행동]을 하고 계신가요? 죄송하지만 그건 [망해가는 과거의 방식]입니다."\n\n### 3단계: Logic Bridge (논리적 다리) - 45초-2분\n- **목적**: 기술적 근거로 부정의 이유 설명, 논리적 타당성 확보\n- **심리학**: 감정적 반응 후 논리적 뒷받침 필요\n- **기법**:\n  - 앵커링: 큰 숫자 → 작은 숫자 극적 대비 ("연봉 3억 의사 vs 유지비 2천만 로봇")\n  - 권위 후광: 권위자 인용 + 쉬운 비유 ("일론 머스크가 예측한 AGI... 쉽게 말하면 다이아몬드가 돌멩이 되는 겁니다")\n  - 사회적 증거: 통계적 표현 ("이미 99%가 파산했습니다")\n\n### 4단계: Visual Scenario (철수 vs 영수) - 2-3분\n- **목적**: 추상적 개념을 구체적 미래 시뮬레이션으로 변환\n- **심리학**: 구체적 시나리오가 추상보다 설득력 강함\n- **필수**: 두 인물 대비 (따르는 자 vs 무시하는 자)\n- **템플릿**: "철수는 [새 방식]을 선택했습니다. 5년 후 [긍정적 결과]. 반면 영수는 [기존 방식]을 고수했죠. 5년 후 [부정적 결과]."\n- **핵심**: 시청자가 "나는 무조건 철수가 되어야겠다"고 느끼게\n\n### 5단계: The Only Ark (유일한 방주) - 3-4분\n- **목적**: 단 하나의 대안 제시, 의사결정 피로도 감소\n- **심리학**: 선택 역설 - 선택지 많으면 결정 못함\n- **패턴**: 여러 대안 언급 → 대부분 기각 → 단 하나만 집중 조명\n- **예시**: "주식? 부동산? 코인? 다 불확실합니다. 하지만 딱 하나, 확실한 게 있어요."\n\n### 6단계: Identity Shift (정체성 변환) - 마지막 30초\n- **목적**: 시청자를 새 정체성으로 정의, 소속감 및 행동 유도\n- **심리학**: 새 집단에 소속되면 그 집단처럼 행동하려 함\n'
    prompt += f'''- **이 장르 목표 정체성**: {identity_target}\n'''
    prompt += '- **패턴**: "여러분은 더 이상 [기존 정체성]이 아닙니다. 오늘부터 여러분은 [새 정체성]입니다."\n- **CTA**: "\'나는 오늘부터 OO이다\'라고 댓글 쓰기" / 구체적 행동 지시\n\n---\n\n### 💡 권장 수사학 기법\n'
    for tech_key in techniques:
        tech = MICRO_PERSUASION_TECHNIQUES.get(tech_key, { })
        if tech:
            prompt += f'''- **{tech.get('name', tech_key)}**: {tech.get('description', '')}\n'''
            if 'formula' in tech:
                prompt += f'''  - 공식: {tech.get('formula')}\n'''
        prompt += '\n### 📝 핵심 문장 패턴\n\n**가치 공격 패턴**:\n"여러분은 지금 [당연한 행동]을 하고 계신가요? 죄송하지만 그건 [망해가는 과거의 방식]입니다. 진짜 [성공한 사람들]은 지금 [새로운 방식]에 올라타고 있습니다. 제가 그 증거를 보여드리죠."\n\n**공포-기회 패턴**:\n"[무서운 사실]. 하지만 뒤집어 보면, [엄청난 기회]가 열립니다."\n\n**철수/영수 패턴**:\n"철수는 [새 방식]을 선택했습니다. [시간] 후, [긍정적 결과]. 영수는 [기존 방식]을 고수했죠. [시간] 후, [부정적 결과]. 여러분은 누가 되고 싶으세요?"\n\n**정체성 변환 패턴**:\n"여러분은 더 이상 [기존 정체성]이 아닙니다. 오늘부터 여러분은 [새 정체성]입니다."\n\n---\n\n### ⚠️ 중요 주의사항\n1. 허위/과장 정보 금지 - 검증 가능한 데이터 사용\n2. 시청자 비하 금지 - 공감과 동반자 관점 유지\n3. 완전한 거짓 부정 금지 - 논리적 근거 필수\n4. 여러 대안 동시 추천 금지 - "유일한 방주" 원칙 준수\n\n### 🔍 논리적 일관성 검증 (CRITICAL)\n\n**주어와 시간 표현의 일관성** - 반드시 확인하세요:\n\n| 주어 | ❌ 부적절한 시간 표현 | ✅ 적절한 시간 표현 |\n|------|---------------------|-------------------|\n| 인류, 인간 | 수십 년, 몇 년, 최근 | 수천 년, 수만 년, 역사 이래 |\n| 현대인, 우리 세대 | 수천 년, 태초부터 | 수십 년, 최근 몇 년 |\n| 과학자들, 연구자들 | 수만 년, 인류 역사 | 수십 년, 최근 연구 |\n| 현대 물리학, 현대 의학 | 수천 년 전부터 | 약 100년간, 20세기 이후 |\n\n**잘못된 예시와 수정**:\n- ❌ "인류는 수십 년간 이 미스터리를 마주했습니다"\n- ✅ "과학자들은 수십 년간 이 미스터리를 연구해왔습니다"\n- ✅ "인류는 약 한 세기 동안 이 미스터리를 마주했습니다"\n\n**검증 체크리스트**:\n- [ ] "인류"가 주어일 때 "수십 년", "몇 년" 사용하지 않았는가?\n- [ ] 시간 표현이 문맥상 역사적 사실과 일치하는가?\n- [ ] 구체적 연도를 언급했다면 계산이 맞는가? (예: 1930년대~현재 = 약 90년)\n'
        return prompt


def get_retention_hooks(hook_type = None, count = None):
    """
    특정 유형의 리텐션 훅을 반환합니다.

    Args:
        hook_type: 훅 유형 ('fear_transition', 'cognitive_dissonance', 등)
        count: 반환할 훅 수

    Returns:
        훅 리스트
    """
    hooks_data = RETENTION_HOOKS.get(hook_type, RETENTION_HOOKS.get('fear_transition'))
    hooks = hooks_data.get('hooks', [])
    return hooks[:count]


def get_random_retention_hooks(count = None, exclude_types = None):
    '''
    랜덤하게 리텐션 훅을 선택합니다 (유형 다양화).

    Args:
        count: 반환할 훅 수
        exclude_types: 제외할 훅 유형

    Returns:
        (훅 텍스트, 훅 유형) 튜플 리스트
    '''
    pass
# WARNING: Decompyle incomplete


def check_forbidden_expressions(text = None):
    '''
    텍스트에서 금지 표현을 검출합니다.

    Args:
        text: 검사할 텍스트

    Returns:
        검출된 금지 표현과 대체 표현 리스트
    '''
    found = []
    for expr in FORBIDDEN_EXPRESSIONS:
        if expr in text:
            found.append({
                'forbidden': expr,
                'alternative': ALTERNATIVE_EXPRESSIONS.get(expr, '(삭제 권장)'),
                'count': text.count(expr) })
        return found


def get_alternative_expression(forbidden = None):
    '''
    금지 표현의 대체 표현을 반환합니다.

    Args:
        forbidden: 금지 표현

    Returns:
        대체 표현
    '''
    return ALTERNATIVE_EXPRESSIONS.get(forbidden, '(삭제 권장)')


def is_info_genre(genre = None):
    '''
    해당 장르가 정보 콘텐츠 시스템 적용 대상인지 확인합니다.

    Args:
        genre: 장르 코드

    Returns:
        정보 장르 여부
    '''
    info_genres = {
        'TECH',
        'SPACE',
        'COMEDY',
        'HEALTH',
        'NATURE',
        'FINANCE',
        'SCIENCE',
        'POLITICS',
        'BIOGRAPHY',
        'ECONOMICS',
        'LIFE_TIPS',
        'PSYCHOLOGY',
        'DOCUMENTARY',
        'MONEY_SENSE',
        'NEWS_REPORT',
        'ENCYCLOPEDIA',
        'LIFE_CHOICES',
        'INFORMATIONAL',
        'SOCIAL_ISSUES',
        'KNOWLEDGE_BITE',
        'LIFE_KNOWLEDGE',
        'OFFICE_SURVIVAL',
        'RELATIONSHIP_EQ',
        'REVIEW_ANALYSIS',
        'NATURAL_DISASTER'}
    return genre.upper() in info_genres


def get_info_expansion_rules(genre = None):
    '''
    정보 장르의 대본 확장 규칙을 반환합니다.

    Args:
        genre: 장르 코드

    Returns:
        확장 규칙 프롬프트
    '''
    genre_guide = GENRE_SPECIFIC_GUIDES.get(genre, { })
    hook_type = genre_guide.get('hook_type', 'break_illusion')
    return f'''\n## 정보 대본 확장 규칙 ({genre})\n\n### 리텐션 강화\n- 매 2분(약 500자)마다 리텐션 훅 삽입\n- 7개 유형 순환 사용: {', '.join(RETENTION_HOOKS.keys())}\n- 이 장르 권장 훅 유형: {hook_type}\n\n### 추상적 표현 구체화\n- "위험이 커지고 있다" → "여러분 월급에서 10만원이 사라질 수 있습니다"\n- "경제 상황이 좋지 않다" → "이번 달 카드값, 예상보다 많이 나올 겁니다"\n- 모든 통계/정책은 시청자 일상과 연결\n\n### 금지 표현 대체\n- "정리하자면" → "그래서 어떤 일이 벌어지냐면요"\n- "쉽게 말해" → (삭제하고 예시로 시작)\n- "중요한 점은" → "이건 꼭 알고 가세요"\n\n### 문장 리듬 조절\n- 긴 문장 → 짧은 임팩트 문장 → 긴 문장\n- 추임새 추가: "솔직히 말해서", "자, 잘 들어보세요", "이게 왜 문제냐면요"\n\n### 반박 선제 차단\n- "이렇게 반박하는 분들 분명히 나옵니다" 섹션 포함\n- 예상 반박 제시 후 즉시 논파\n\n### 결론 강화\n- 요약하지 마세요\n- 선택을 강요하는 질문으로 마무리\n- "여러분이라면 어떤 선택을 하시겠습니까?"\n'''


def get_info_analysis_criteria(genre = None):
    '''
    정보 장르의 대본 분석 기준을 반환합니다.

    Args:
        genre: 장르 코드

    Returns:
        분석 기준 프롬프트
    '''
    return f'''\n## 정보 대본 분석 기준 ({genre})\n\n### 1. 사실 기반 훅 효과\n- [ ] 첫 30초가 검증된 데이터로 시작하는가?\n- [ ] 호기심과 관심이 유발되는가?\n- [ ] 균형 잡힌 시각이 제시되는가?\n\n### 2. 리텐션 구조\n- [ ] 최소 3회 리텐션 멘트가 포함되었는가?\n- [ ] 리텐션 훅이 다양한 유형으로 배치되었는가?\n- [ ] 호기심 갭(Curiosity Gap)이 적절히 형성되는가?\n\n### 3. 금지 표현 검출\n- [ ] "정리하자면", "쉽게 말해" 등 금지 표현이 없는가?\n- [ ] 문어체/보고서 말투가 없는가?\n- [ ] 권장 종결어미(~인 거죠, ~거든요)가 사용되었는가?\n\n### 4. 문장 리듬\n- [ ] 긴-짧-긴 호흡 패턴이 유지되는가?\n- [ ] 추임새가 자연스럽게 삽입되었는가?\n- [ ] 질문 → 정보 순서가 지켜지는가?\n\n### 5. 추상적 표현\n- [ ] 통계/정책이 시청자 일상과 연결되었는가?\n- [ ] "구조적 위험" 같은 추상적 표현 대신 구체적 상황이 제시되었는가?\n\n### 6. 반박 선제 차단\n- [ ] 예상 반박에 대한 대응이 포함되었는가?\n- [ ] 반박 논파가 설득력 있는가?\n\n### 7. 결론 구조\n- [ ] 요약으로 끝나지 않았는가?\n- [ ] 선택 강요형 질문이 있는가?\n- [ ] 찝찝함/여운이 남는가?\n\n### 8. 알고리즘 생존\n- [ ] 시청자와 함께 탐구하는 동반자 관점으로 작성되었는가?\n- [ ] 다음 콘텐츠 암시가 있는가?\n'''


def get_info_fix_rules(genre = None):
    '''
    정보 장르의 대본 수정 규칙을 반환합니다.

    Args:
        genre: 장르 코드

    Returns:
        수정 규칙 프롬프트
    '''
    return f'''\n## 정보 대본 수정 규칙 ({genre})\n\n### 1. 금지 표현 대체\n- "정리하자면" → "그래서 어떤 일이 벌어지냐면요"\n- "쉽게 말해" → (삭제 또는 예시로 시작)\n- "결론적으로" → "결국 남는 건 이거예요"\n- "중요한 점은" → "이건 꼭 알고 가세요"\n- "~라고 볼 수 있습니다" → "~인 거죠"\n\n### 2. 추상적 표현 구체화\n- "위험이 커지고 있다" → "여러분 월급에서 10만원이 사라질 수 있습니다"\n- "경제 불확실성" → "이번 달 카드값 예상보다 많이 나올 겁니다"\n- "구조적 문제" → "당장 다음 달부터 적용되는 변화"\n\n### 3. 리텐션 훅 삽입\n- 2분(500자)마다 적절한 훅 추가\n- 추천 훅 배치:\n  - 시작 1분: fear_transition 유형\n  - 중간: cognitive_dissonance 또는 break_illusion 유형\n  - 후반: algorithm_pressure 유형\n\n### 4. 문장 리듬 조정\n- 3문장 이상 긴 문장 연속 시 짧은 임팩트 문장 삽입\n- 예: "진짜 큰일이에요." "남 일이 아닙니다."\n\n### 5. 추임새 추가\n- 정보 전달 전: "솔직히 말해서", "자, 잘 들어보세요"\n- 전환점: "이게 왜 문제냐면요", "여기서 대부분 착각합니다"\n\n### 6. 질문-정보 순서 재배치\n- 정보 먼저 나온 경우 → 질문으로 시작하도록 재배치\n- "X입니다" → "여러분은 X 알고 계셨나요? 사실 X인 거죠"\n\n### 7. 결론 재구성\n- 요약 형태로 끝난 경우 → 선택 강요 질문으로 변경\n- "정리하면 A, B, C입니다" → "여러분이라면 어떤 선택을 하시겠습니까?"\n\n### 8. 반박 선제 차단 추가\n- 논란이 될 수 있는 주장 뒤에 추가\n- "이렇게 반박하는 분들 분명히 나옵니다. 하지만..."\n'''


def get_fact_based_hook_template(topic = None):
    '''
    사실 기반 훅 템플릿을 반환합니다.

    Args:
        topic: 주제 (선택)

    Returns:
        사실 기반 훅 템플릿
    '''
    template = '\n[검증된 데이터/사실로 시작]\n\n여러분, 이거 아세요?\n[흥미로운 사실 또는 통계]\n\n이건 많은 분들이 잘 모르시는 부분인데요.\n\n[시청자 일상과의 연결]\n\n이 영상 끝까지 보시면, 이 주제에 대해 더 잘 이해하실 수 있을 겁니다.\n'
    return template.strip()


def get_interjections(count = None):
    '''
    추임새 리스트를 반환합니다.

    Args:
        count: 반환할 추임새 수

    Returns:
        추임새 리스트
    '''
    return WRITING_PRINCIPLES['4_interjections']['examples'][:count]


def get_recommended_endings(count = None):
    '''
    권장 종결어미 리스트를 반환합니다.

    Args:
        count: 반환할 종결어미 수

    Returns:
        종결어미 리스트
    '''
    return RECOMMENDED_ENDINGS[:count]


def get_final_question_examples(count = None):
    '''
    결론부 선택 강요 질문 예시를 반환합니다.

    Args:
        count: 반환할 예시 수

    Returns:
        질문 예시 리스트
    '''
    return INFO_STRUCTURE['4_grand_insight']['examples'][:count]

PERSUASION_STRUCTURE = {
    '1_metaphor_hook': {
        'name': 'Metaphor Hook (비유 충격)',
        'duration': '첫 15초',
        'description': '일상적이지만 극단적인 비유로 시작하여 호기심과 공포를 동시에 자극',
        'psychology': '인지 충격 + 감정 활성화',
        'formula': [
            "극단적 비유로 시작 (예: '지금 여러분은 3만km 열차를 타고 절벽으로 달리고 있습니다')",
            '시청자 현실과 즉시 연결',
            '감정 활성화 (호기심, 긴장감, 몰입)'],
        'examples': [
            '여러분이 매일 마시는 커피, 사실은 뇌에 시한폭탄을 심는 행위입니다.',
            '지금 여러분은 3만 킬로미터짜리 열차를 타고 절벽으로 달리고 있습니다.',
            '여러분의 통장에서 매달 100만 원이 증발하고 있습니다. 눈에 안 보일 뿐이죠.'],
        'prohibited': [
            '추상적 비유',
            '너무 평범한 시작',
            '호기심 없는 팩트 나열'] },
    '2_value_attack': {
        'name': 'Value Attack (가치 전면 부정)',
        'duration': '15-45초',
        'description': '시청자가 신성시하는 가치/상식을 전면 부정하여 인지 부조화 유발',
        'psychology': '인지 부조화(Cognitive Dissonance) - 믿음이 흔들리면 답을 찾으려 집중',
        'formula': [
            "시청자의 '성역'(당연하다고 믿는 것) 찾기",
            "'유통기한이 지났다'고 선언",
            '기존 믿음이 왜 위험한지 암시'],
        'examples': [
            '의대 가면 성공? 죄송하지만 그건 20년 전 공식입니다.',
            '열심히 저축하면 부자 된다? 그건 할머니 세대 얘기예요.',
            '집 사야 안정적이다? 지금 집 사면 30년 동안 노예입니다.'],
        'sanctuary_examples': [
            '공부 열심히 하면 성공한다',
            '집은 반드시 사야 한다',
            '안정적인 직장이 답이다',
            '저축이 미덕이다',
            '경험보다 스펙이 중요하다'],
        'prohibited': [
            '완전한 거짓말',
            '근거 없는 부정',
            '시청자 비하'] },
    '3_logic_bridge': {
        'name': 'Logic Bridge (논리적 다리)',
        'duration': '45초-2분',
        'description': '기술적 근거를 통해 부정의 이유를 설명, 논리적 타당성 확보',
        'psychology': '이성적 합리화 - 감정적 반응 후 논리적 뒷받침 필요',
        'formula': [
            '구체적 데이터/연구 인용',
            '권위자 활용 (전문가, 연구기관)',
            '복잡한 개념은 쉬운 비유로 치환'],
        'examples': [
            'AGI가 뭔지 쉽게 설명하면요. 지금까지 다이아몬드였던 게 돌멩이가 되는 겁니다.',
            '연봉 3억 의사 vs 유지비 2,000만 원 로봇. 병원장이라면 뭘 선택하겠습니까?',
            '삼성전자 10년 치 데이터를 보면요. 패턴이 보입니다.'],
        'techniques': {
            'anchoring': '큰 숫자 → 작은 숫자 극적 대비',
            'authority_halo': '권위자 인용 + 쉬운 비유',
            'social_proof': '통계적 표현으로 확증 편향 활용' } },
    '4_visual_scenario': {
        'name': 'Visual Scenario (철수 vs 영수)',
        'duration': '2-3분',
        'description': '추상적 개념을 구체적 미래 시뮬레이션으로 변환, 두 인물 대비',
        'psychology': '심상화(Visualization) - 구체적 시나리오가 추상보다 설득력 강함',
        'formula': [
            '두 인물 설정 (따르는 자 vs 무시하는 자)',
            '각각의 미래 구체적으로 시뮬레이션',
            "시청자가 '나는 무조건 A가 되어야겠다' 느끼게"],
        'template': '철수는 [새로운 방식]을 선택했습니다. 5년 후 [긍정적 결과]. 반면 영수는 [기존 방식]을 고수했죠. 5년 후 [부정적 결과].',
        'examples': [
            "철수는 2020년에 월급의 30%를 미국 주식에 넣었습니다. 지금 자산 5배. 영수는 '위험하다'며 적금만 했죠. 지금 물가 상승분도 못 따라갑니다.",
            'A씨는 이 방법을 실천했습니다. 1년 후 연봉이 2배가 됐어요. B씨는 무시했죠. 아직도 같은 자리에 있습니다.'],
        'prohibited': [
            '추상적 비교',
            '두 선택이 비슷해 보이는 결과',
            '결과가 모호한 시나리오'] },
    '5_the_only_ark': {
        'name': 'The Only Ark (유일한 방주)',
        'duration': '3-4분',
        'description': '수많은 선택지 중 가장 안전한 단 하나의 대안 제시, 의사결정 피로도 감소',
        'psychology': '선택 역설(Paradox of Choice) - 선택지 많으면 결정 못함, 하나만 제시하면 따름',
        'formula': [
            '여러 대안 언급 후 대부분 기각',
            '단 하나의 대안만 집중 조명',
            '그 대안의 구체적 실행법 제시'],
        'examples': [
            '주식? 부동산? 코인? 다 불확실합니다. 하지만 딱 하나, 확실한 게 있어요.',
            '이것저것 다 해봤자 실패합니다. 오직 하나에 집중하세요.',
            '선택지가 많아 보이지만, 실제로 되는 건 이것 하나뿐입니다.'],
        'prohibited': [
            '여러 대안 동시 추천',
            '선택을 시청자에게 떠넘김',
            '모호한 결론'] },
    '6_identity_shift': {
        'name': 'Identity Shift (정체성 변환)',
        'duration': '마지막 30초',
        'description': '시청자를 새로운 계급/정체성으로 정의, 소속감 및 행동 유도',
        'psychology': '사회적 정체성 이론 - 새 집단에 소속되면 그 집단처럼 행동하려 함',
        'formula': [
            "시청자를 새로운 정체성으로 정의 (예: '자본가', '깨어있는 1%')",
            '행동 유도 (지금 당장 할 것 제시)',
            "소속감 부여 ('우리'로 묶기)"],
        'identity_examples': [
            '자본가',
            '깨어있는 1%',
            '현명한 투자자',
            '시스템을 이해한 사람',
            '미래를 준비하는 사람',
            '남들과 다른 선택을 한 사람'],
        'cta_patterns': [
            "'나는 오늘부터 OO이다'라고 댓글 쓰기",
            '특정 행동 지시 (계좌 확인, 자료 다운로드 등)',
            '구독하고 알림 설정하기'],
        'examples': [
            "여러분은 더 이상 월급쟁이가 아닙니다. 오늘부터 '자본가'입니다.",
            '이 영상을 끝까지 본 여러분은 이미 상위 1%입니다.',
            '우리는 다릅니다. 우리는 준비된 사람들입니다.'] } }
MICRO_PERSUASION_TECHNIQUES = {
    'fear_to_opportunity': {
        'name': '공포→기회 프레이밍 (Fear-to-Opportunity)',
        'description': '공포(Fear)를 보여준 뒤 즉시 기회(Opportunity)로 치환',
        'psychology': '공포로 주의를 끈 뒤, 기회로 희망을 주어 행동 유도',
        'formula': "[Pain Point] + '그런데 뒤집어 보면' + [Reward]",
        'examples': [
            {
                'pain': 'AI가 일자리를 뺏습니다.',
                'transition': '그런데 뒤집어 보면요,',
                'reward': '물가가 0원인 천국이 올 수도 있습니다.' },
            {
                'pain': '전세 사기가 넘쳐납니다.',
                'transition': '하지만 이건 반대로 보면,',
                'reward': '진짜 싸게 집 살 기회이기도 합니다.' }],
        'transition_phrases': [
            '그런데 뒤집어 보면요,',
            '하지만 이건 반대로 보면,',
            '그런데 여기서 기회가 보입니다.',
            '근데 말이죠, 이게 오히려...'] },
    'anchoring_contrast': {
        'name': '앵커링 극적 대비 (Anchoring & Contrast)',
        'description': '큰 숫자와 작은 숫자를 극적으로 대비시켜 계산 전 결론 도달',
        'psychology': '첫 번째 숫자가 기준점(앵커)이 되어 두 번째 숫자를 극단적으로 느끼게 함',
        'formula': "[큰 숫자] + 'vs' + [작은 숫자]",
        'examples': [
            '연봉 3억 의사 vs 유지비 2,000만 원 로봇',
            '10년 적금 이자 500만 원 vs 주식 1년 수익 5,000만 원',
            '월세 100만 원 × 30년 = 3.6억 vs 대출 이자 1.5억'],
        'application': '비교하려는 대상 중 더 큰 숫자를 먼저 제시하여 기준점 설정' },
    'authority_plus_analogy': {
        'name': '권위 후광 + 대중화 (Authority & Jargon)',
        'description': '권위자 인용 + 어려운 개념을 쉬운 비유로 치환',
        'psychology': "권위자의 후광 효과 + 쉬운 이해로 '지적 우월감' 선사",
        'formula': "[권위자]가 말했습니다 + [전문용어] + '쉽게 말하면' + [쉬운 비유]",
        'examples': [
            '일론 머스크가 예측한 AGI... 쉽게 말하면, 다이아몬드가 돌멩이가 되는 겁니다.',
            '워렌 버핏이 말한 복리의 마법... 눈덩이를 굴리는 거예요. 처음엔 작지만 점점 커집니다.',
            '레이 달리오가 경고한 디레버리징... 쉽게 말하면, 빚잔치 끝나고 청구서 날아오는 겁니다.'],
        'authority_figures': [
            '일론 머스크',
            '워렌 버핏',
            '레이 달리오',
            '피터 틸',
            '하버드 연구팀',
            'MIT 교수',
            '골드만삭스 분석가'] },
    'statistical_social_proof': {
        'name': '통계적 사회적 증거 (Statistical Social Proof)',
        'description': '통계적(또는 통계처럼 들리는) 표현으로 확증 편향 활용',
        'psychology': '숫자는 객관적으로 느껴짐 + 다수가 그렇다면 나도 그래야 함',
        'formula': '[숫자]%가 [행동/결과]',
        'examples': [
            '이미 99%가 파산했습니다.',
            'AI 오진율은 의사보다 낮습니다.',
            '상위 1%는 이 방법을 씁니다.',
            '10명 중 9명이 이 실수를 합니다.'],
        'caution': '과장/허위 통계 금지, 출처 있으면 반드시 명시',
        'patterns': [
            '[X]% 가 [결과]',
            '[X]명 중 [Y]명이 [행동]',
            '상위 [X]%는 [특징]',
            '[연구기관] 조사 결과 [통계]'] } }
UNIVERSAL_3STEP_PROCESS = {
    'step_1_find_sanctuary': {
        'name': "시청자의 '성역' 찾기",
        'description': "시청자가 당연히 맞다고 믿는 상식을 찾고, '유통기한이 지났다'고 선언하며 시작",
        'questions_to_ask': [
            '이 주제에서 시청자가 당연시하는 믿음은?',
            '그 믿음이 틀렸다면 어떤 증거가 있는가?',
            '이 부정이 시청자에게 어떤 감정을 유발하는가?'],
        'sanctuary_examples': {
            'MONEY_SENSE': [
                '저축이 최고다',
                '집은 사야 한다',
                '보험은 필수다'],
            'LIFE_CHOICES': [
                '학력이 중요하다',
                '대기업이 안정적이다',
                '결혼해야 행복하다'],
            'OFFICE_SURVIVAL': [
                '열심히 하면 인정받는다',
                '회사에 충성하면 보상받는다'],
            'PSYCHOLOGY': [
                '의지력으로 해결된다',
                '긍정적으로 생각하면 된다'],
            'LIFE_KNOWLEDGE': [
                '아는 게 힘이다',
                '경험이 최고의 스승이다'],
            'RELATIONSHIP_EQ': [
                '솔직하게 말하면 된다',
                '참으면 해결된다'],
            'KNOWLEDGE_BITE': [
                '상식은 다 맞다',
                '전문가 말은 믿어야 한다'] },
        'attack_templates': [
            "'{성역}'? 죄송하지만 그건 {시대} 전 공식입니다.",
            "'{성역}'라고 생각하시나요? 완전히 틀렸습니다.",
            "여러분이 믿는 '{성역}', 유통기한이 지났습니다."] },
    'step_2_dual_scenario': {
        'name': "'철수와 영수' 시나리오 설정",
        'description': '제안을 따랐을 때 vs 거부했을 때의 미래를 극명하게 대비하는 두 인물 설정',
        'template': {
            'follower': '철수는 [새 방식]을 따랐습니다. [시간] 후, [긍정적 구체적 결과]',
            'denier': '영수는 [기존 방식]을 고수했습니다. [시간] 후, [부정적 구체적 결과]' },
        'key_rule': "시청자가 '나는 무조건 철수가 되어야겠다'고 느끼게 시각적 묘사",
        'name_pairs': [
            ('철수', '영수'),
            ('A씨', 'B씨'),
            ('민수', '지훈'),
            ('현명한 투자자', '일반인')],
        'time_frames': [
            '1년 후',
            '3년 후',
            '5년 후',
            '10년 후'] },
    'step_3_immediate_action': {
        'name': "'지금 당장' 행동 지시",
        'description': '영상이 끝나고 무엇을 해야 할지 모르면 시청자는 이탈. 아주 구체적이고 쉬운 첫 번째 행동 지시',
        'action_patterns': [
            "'나는 오늘부터 {정체성}이다'라고 댓글에 쓰세요.",
            '지금 바로 {구체적 행동}을 확인해보세요.',
            '이 영상 저장하고, 내일 다시 보세요.',
            '구독 누르고 알림 설정하세요. 다음 영상이 더 중요합니다.'],
        'action_examples': {
            'MONEY_SENSE': [
                '내 연금 계좌 확인하기',
                '지출 내역 검토하기',
                '투자 앱 설치하기'],
            'LIFE_CHOICES': [
                '버킷리스트 3개 쓰기',
                '5년 후 목표 적기',
                '메모장에 결심 쓰기'],
            'OFFICE_SURVIVAL': [
                '이력서 업데이트하기',
                '링크드인 접속하기',
                '스킬업 계획 세우기'],
            'PSYCHOLOGY': [
                '오늘 감정 기록하기',
                '명상 앱 설치하기',
                '수면 시간 체크하기'],
            'LIFE_KNOWLEDGE': [
                '관련 책 검색하기',
                '전문가 채널 구독하기',
                '메모하기'],
            'RELATIONSHIP_EQ': [
                '중요한 사람에게 연락하기',
                '감사 표현하기',
                '경청 연습하기'],
            'KNOWLEDGE_BITE': [
                '더 찾아보기',
                '관련 영상 보기',
                '친구에게 공유하기'] } } }
CORE_SENTENCE_PATTERNS = {
    'value_attack_pattern': {
        'name': '가치 공격 패턴',
        'template': '여러분은 지금 [당연한 행동]을 하고 계신가요? 죄송하지만 그건 [망해가는 과거의 방식]입니다. 진짜 [성공한 사람들]은 지금 [새로운 방식]에 올라타고 있습니다. 제가 그 증거를 보여드리죠.',
        'variables': {
            '당연한 행동': [
                '예금',
                '보험',
                '부동산 투자',
                '의대 준비',
                '적금',
                '연금 납입'],
            '망해가는 과거의 방식': [
                '20년 전 공식',
                '이미 망한 전략',
                '구시대적 방법',
                '유통기한 지난 조언'],
            '성공한 사람들': [
                '진짜 부자들',
                '상위 1%',
                '깨어있는 사람들',
                '미래를 준비하는 사람들'],
            '새로운 방식': [
                'AI 투자',
                '글로벌 주식',
                '새로운 기술',
                '디지털 자산',
                '지식 투자'] },
        'examples': [
            '여러분은 지금 열심히 적금을 붓고 계신가요? 죄송하지만 그건 20년 전 공식입니다. 진짜 부자들은 지금 미국 주식에 올라타고 있습니다. 제가 그 증거를 보여드리죠.',
            '여러분은 지금 안정적인 직장만 찾고 계신가요? 죄송하지만 그건 이미 끝난 게임입니다. 상위 1%는 지금 부업에 올라타고 있습니다. 제가 그 증거를 보여드리죠.'] },
    'fear_opportunity_pattern': {
        'name': '공포-기회 패턴',
        'template': '[무서운 사실]. 하지만 뒤집어 보면, [엄청난 기회]가 열립니다.',
        'examples': [
            'AI가 일자리를 뺏습니다. 하지만 뒤집어 보면, 물가 0원 시대가 열릴 수 있습니다.',
            '부동산 거품이 터집니다. 하지만 뒤집어 보면, 10년 만의 매수 기회가 옵니다.',
            '금리가 계속 오릅니다. 하지만 뒤집어 보면, 예금 이자로 월급 버는 시대가 옵니다.'] },
    'identity_shift_pattern': {
        'name': '정체성 변환 패턴',
        'template': '여러분은 더 이상 [기존 정체성]이 아닙니다. 오늘부터 여러분은 [새로운 정체성]입니다.',
        'identity_pairs': [
            ('월급쟁이', '자본가'),
            ('소비자', '투자자'),
            ('직장인', '사업가 마인드를 가진 직장인'),
            ('일반인', '상위 1%'),
            ('두려워하는 사람', '준비된 사람')],
        'examples': [
            "여러분은 더 이상 월급쟁이가 아닙니다. 오늘부터 여러분은 '자본가'입니다.",
            "여러분은 더 이상 소비자가 아닙니다. 오늘부터 여러분은 '투자자'입니다.",
            "여러분은 더 이상 두려워하는 사람이 아닙니다. 오늘부터 여러분은 '준비된 사람'입니다."] },
    'anchoring_pattern': {
        'name': '앵커링 대비 패턴',
        'template': '[큰 숫자]. vs [작은 숫자]. 여러분이라면 뭘 선택하시겠습니까?',
        'examples': [
            '연봉 3억 의사. vs 유지비 2,000만 원 로봇. 병원장이라면 뭘 선택하겠습니까?',
            '30년 적금 이자 3,000만 원. vs 주식 10년 수익 3억. 뭐가 더 나아 보이세요?',
            '월세 30년 = 3.6억. vs 대출 이자 1억. 어느 쪽이 손해일까요?'] },
    'dual_scenario_pattern': {
        'name': '철수/영수 대비 패턴',
        'template': '[A]는 [새 방식]을 선택했습니다. [시간] 후, [A의 결과]. [B]는 [기존 방식]을 고수했습니다. [시간] 후, [B의 결과]. 여러분은 누가 되고 싶으세요?',
        'examples': [
            "철수는 2020년에 월급의 30%를 미국 주식에 넣었습니다. 지금 자산 5배. 영수는 '위험하다'며 적금만 했죠. 물가 상승분도 못 따라갑니다. 여러분은 누가 되고 싶으세요?",
            "민수는 퇴근 후 2시간씩 부업에 투자했습니다. 1년 후 월 수입이 2배. 지훈은 '피곤하다'며 넷플릭스만 봤죠. 아직도 월급만 기다립니다. 여러분은요?"] } }
PERSUASION_APPLICABLE_GENRES = {
    'LIFE_KNOWLEDGE': {
        'persuasion_level': 'HIGH',
        'primary_techniques': [
            'statistical_social_proof',
            'fear_to_opportunity'],
        'identity_shift_target': '현명한 생활인, 정보력 있는 사람',
        'sanctuary_focus': '아는 게 힘이다, 경험이 중요하다' },
    'OFFICE_SURVIVAL': {
        'persuasion_level': 'HIGH',
        'primary_techniques': [
            'fear_to_opportunity',
            'authority_plus_analogy'],
        'identity_shift_target': '회사에서 살아남는 전략가, 커리어 관리자',
        'sanctuary_focus': '열심히 하면 인정받는다, 충성하면 보상받는다' },
    'MONEY_SENSE': {
        'persuasion_level': 'HIGH',
        'primary_techniques': [
            'anchoring_contrast',
            'fear_to_opportunity'],
        'identity_shift_target': '자본가, 현명한 투자자, 돈을 이해하는 사람',
        'sanctuary_focus': '저축이 최고다, 안전이 우선이다' },
    'RELATIONSHIP_EQ': {
        'persuasion_level': 'HIGH',
        'primary_techniques': [
            'fear_to_opportunity',
            'statistical_social_proof'],
        'identity_shift_target': '관계 전문가, 소통 달인',
        'sanctuary_focus': '솔직하면 된다, 참으면 해결된다' },
    'PSYCHOLOGY': {
        'persuasion_level': 'HIGH',
        'primary_techniques': [
            'authority_plus_analogy',
            'statistical_social_proof'],
        'identity_shift_target': '자기 이해자, 마음을 아는 사람',
        'sanctuary_focus': '의지력으로 된다, 긍정이 답이다' },
    'LIFE_CHOICES': {
        'persuasion_level': 'HIGH',
        'primary_techniques': [
            'authority_plus_analogy',
            'anchoring_contrast'],
        'identity_shift_target': '깨어있는 1%, 주도적 선택자',
        'sanctuary_focus': '정해진 길이 있다, 남들 따라하면 된다' },
    'KNOWLEDGE_BITE': {
        'persuasion_level': 'HIGH',
        'primary_techniques': [
            'statistical_social_proof',
            'authority_plus_analogy'],
        'identity_shift_target': '지식인, 교양인',
        'sanctuary_focus': '상식은 다 맞다, 전문가만 안다' },
    'SOCIAL_ISSUES': {
        'persuasion_level': 'HIGH',
        'primary_techniques': [
            'fear_to_opportunity',
            'statistical_social_proof'],
        'identity_shift_target': '깨어있는 시민, 변화를 이끄는 사람',
        'sanctuary_focus': '나 하나 바뀐다고 달라지나, 정부가 해결해야지' },
    'SOCIAL_ISSUE': {
        'persuasion_level': 'HIGH',
        'primary_techniques': [
            'fear_to_opportunity',
            'statistical_social_proof'],
        'identity_shift_target': '깨어있는 시민, 변화를 이끄는 사람',
        'sanctuary_focus': '나 하나 바뀐다고 달라지나, 정부가 해결해야지' } }
