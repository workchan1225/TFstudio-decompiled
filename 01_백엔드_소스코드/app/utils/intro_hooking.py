# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: intro_hooking.pyc (Python 3.11)

__doc__ = '\nIntro Hooking System\n\n12가지 후킹 유형과 3단계 인트로 구조를 정의합니다.\nIn Medias Res 기법을 모든 장르에 자동 적용합니다.\n창작 모드(Strict/Balanced/Creative)에 따라 유연성을 조절합니다.\n'
from typing import Dict, List, Optional, Tuple
from dataclasses import dataclass
from enum import Enum
from genre_categories import get_genre_category, get_in_medias_res_type, get_in_medias_res_instruction, get_in_medias_res_example, get_transition_phrase, get_teaser_duration, InMediasResType
from creative_modes import build_creative_mode_instruction
TONE_INTRO_STYLES: Dict[(str, Dict[(str, str)])] = {
    '소설체': {
        'style': '문학적이고 묘사가 풍부한 인트로',
        'ending': '~했다, ~였다',
        'instruction': '감각적 묘사와 내면 심리를 섬세하게 표현하세요. 시적인 리듬감을 살리세요.',
        'example': '쓰레기 더미 사이에서 가느다란 울음 소리가 들려왔다. 한 남자가 그 소리를 따라 걸어갔다.' },
    '극적체': {
        'style': '긴장감 있고 드라마틱한 인트로',
        'ending': '~했다, ~였다',
        'instruction': '강렬한 대사나 충격적 상황으로 시작하세요. 짧은 문장으로 긴장감을 높이세요.',
        'example': '"당신이 그랬던 거죠?" 그녀의 목소리가 얼어붙었다. 남자는 대답하지 못했다.' },
    '친근체': {
        'style': '부드럽고 대화하듯 편안한 인트로',
        'ending': '~했어요, ~거든요, ~죠',
        'instruction': '마치 친구에게 이야기하듯 자연스럽게 시작하세요. 공감을 이끌어내세요.',
        'example': '쓰레기 더미 사이에서 울음소리가 들렸어요. 한 남자가 그 소리를 따라갔죠.' },
    '설명체': {
        'style': '객관적이고 정보 전달 중심의 인트로',
        'ending': '~합니다, ~입니다',
        'instruction': '명확하고 간결하게 상황을 전달하세요. 핵심 정보를 먼저 제시하세요.',
        'example': '서울역 인근에서 한 남성이 발견되었습니다. 그는 과거 IT 업계의 천재로 불렸습니다.' },
    '담담체': {
        'style': '감정 절제된 차분하고 건조한 인트로',
        'ending': '~했다, ~였다',
        'instruction': '감정을 억제하고 사실만 담담하게 전달하세요. 오히려 그 절제가 강렬함을 만듭니다.',
        'example': '남자가 쓰러져 있었다. 빈 소주병이 곁에 있었다. 그가 한때 천재였다는 것을 아는 사람은 없었다.' },
    '유머체': {
        'style': '위트 있고 가볍게 풀어가는 인트로',
        'ending': '~했다, ~했어요 (혼용)',
        'instruction': '가벼운 반전이나 위트 있는 표현으로 시작하세요. 심각한 상황도 살짝 비틀어보세요.',
        'example': '천재라고 불리던 남자가 노숙자가 됐다. 인생이란 참 예측불가다.' },
    '감성체': {
        'style': '서정적이고 감정을 섬세하게 표현하는 인트로',
        'ending': '~했다, ~였다',
        'instruction': '감정의 결을 살려 표현하세요. 분위기와 감정을 먼저 전달하세요.',
        'example': '차가운 바람이 뼈 속까지 파고들던 그날 밤이었다. 희미한 울음소리가 어둠을 뚫고 들려왔다.' },
    '다큐체': {
        'style': '사실 기반의 객관적인 다큐멘터리 인트로',
        'ending': '~했습니다, ~입니다',
        'instruction': '시간, 장소, 인물을 명확히 제시하세요. 팩트 중심으로 전개하세요.',
        'example': '2024년 1월, 서울역 인근. 한 남성이 노숙 생활을 하고 있었습니다. 그는 5년 전까지 IT 업계를 이끌던 인물이었습니다.' },
    '다채로운 문체': {
        'style': '사건의 뼈대와 감정의 여운을 분리해 전달하는 인트로',
        'ending': '~습니다(뼈대), ~지요(살)',
        'instruction': '한 줄 교대가 아니라 문장 역할로 선택하세요. 사건 진행/팩트는 ~습니다, 묘사/감정/여운은 ~지요.',
        'example': '그날 밤, 사건은 조용히 시작되었습니다. 그런데 공기에는 이미 불길한 예감이 번져 있었지요.' } }

def get_tone_intro_style(tone = None):
    '''톤에 맞는 인트로 스타일 지침 반환'''
    tone_data = TONE_INTRO_STYLES.get(tone, TONE_INTRO_STYLES['소설체'])
    return f'''\n**인트로 톤: {tone}**\n- 스타일: {tone_data['style']}\n- 문장 어미: {tone_data['ending']}\n- 적용법: {tone_data['instruction']}\n- 예시: {tone_data['example']}\n'''

HookingType = <NODE:12>()
HOOKING_TYPES: Dict[(str, HookingType)] = {
    'result_first': HookingType(id = 'result_first', name = 'Result First', korean_name = '결과 먼저 제시', principle = '스토리의 결말에서 가장 충격적인 순간을 먼저 보여주고, "어떻게 이런 일이?"라는 궁금증 유발', instruction = '가장 임팩트 있는 결과/상황을 첫 문장에 제시하세요. 그 다음 "어떻게 이런 일이 벌어졌을까요?"로 과거로 돌아가세요.', psychology = '예측 오류(Prediction Error) - 결과를 먼저 알면 과정이 더 궁금해짐', best_for = [
        'DRAMATIC',
        'REVENGE',
        'MYSTERY',
        'THRILLER'], avoid_for = [
        'ENCYCLOPEDIA',
        'LIFE_TIPS'], constraints = [
        '결과가 충분히 충격적이어야 함',
        '바로 과거로 돌아가야 함',
        '결과를 너무 자세히 보여주면 안 됨']),
    'consensus': HookingType(id = 'consensus', name = 'Consensus/Empathy', korean_name = '공감/공론', principle = '많은 사람들이 숨기거나 궁금해하는 주제를 건드려 공감대 형성', instruction = '시청자 대부분이 생각해봤지만 말하기 어려운 주제를 언급하세요. "혹시 이런 생각 해보신 적 있나요?"', psychology = '사회적 증거(Social Proof) - "나만 이런 생각 하는 게 아니구나"', best_for = [
        'CONFESSION',
        'RELATIONSHIP_EQ',
        'PSYCHOLOGY',
        'LIFE_CHOICES'], avoid_for = [
        'HISTORY',
        'SCIENCE'], constraints = [
        '보편적 공감을 이끌어낼 주제',
        '너무 개인적이거나 특수한 상황 피함']),
    'pattern_interrupt': HookingType(id = 'pattern_interrupt', name = 'Pattern Interrupt', korean_name = '상식 깨기', principle = '일반적인 상식과 반대되는 주장을 먼저 제시하여 인지적 충격 유발', instruction = '시청자가 당연하게 믿고 있던 것의 반대를 주장하세요. "○○가 사실은 해롭습니다" 또는 "○○는 쓸모없습니다"', psychology = '인지 부조화(Cognitive Dissonance) - 기존 믿음이 흔들릴 때 주의 집중', best_for = [
        'LIFE_KNOWLEDGE',
        'PSYCHOLOGY',
        'SCIENCE',
        'DOCUMENTARY'], avoid_for = [
        'HEARTWARMING',
        'TOUCHING'], constraints = [
        '뒷받침할 근거가 있어야 함',
        '단순 도발이 아닌 실제 반전',
        '지나친 과장 금지']),
    'value_proposition': HookingType(id = 'value_proposition', name = 'Value Proposition', korean_name = '가치 직접 제시', principle = '시청자가 얻을 수 있는 가치를 명확하고 직접적으로 제시', instruction = '이 영상을 보면 얻을 수 있는 구체적 이득을 첫 문장에 명시하세요. 숫자와 결과로 표현하세요.', psychology = '이득 동기(Gain Motivation) - 명확한 보상이 있을 때 행동', best_for = [
        'LIFE_TIPS',
        'LIFE_KNOWLEDGE',
        'OFFICE_SURVIVAL',
        'MONEY_SENSE'], avoid_for = [
        'DRAMATIC',
        'MYSTERY'], constraints = [
        '구체적 숫자/결과',
        '과장 금지',
        '약속한 것은 반드시 제공']),
    'data_emphasis': HookingType(id = 'data_emphasis', name = 'Data Emphasis', korean_name = '숫자/데이터 강조', principle = '콘텐츠에 투자된 시간, 비용, 연구 규모를 수치로 제시하여 신뢰성 확보', instruction = '구체적인 숫자를 제시하세요. "3년간 연구한", "1000명을 면접한", "200만원을 들인"', psychology = '구체성 효과(Concreteness Effect) - 구체적 숫자는 추상적 표현보다 신뢰받음', best_for = [
        'DOCUMENTARY',
        'TRUE_STORY',
        'REVIEW_ANALYSIS',
        'ENCYCLOPEDIA'], avoid_for = [
        'JOSEON_FOLKTALE',
        'SF_FANTASY'], constraints = [
        '검증 가능한 숫자',
        '과장된 숫자는 역효과',
        '의미 있는 숫자만']),
    'authority': HookingType(id = 'authority', name = 'Authority', korean_name = '성과/권위 활용', principle = '신뢰할 수 있는 출처, 전문가, 성공 사례를 언급하여 신뢰 확보', instruction = '전문가의 의견, 유명인의 사례, 검증된 연구 결과를 인용하세요.', psychology = '권위 효과(Authority Effect) - 전문가의 말은 더 신뢰받음', best_for = [
        'LIFE_KNOWLEDGE',
        'PSYCHOLOGY',
        'HISTORY',
        'DOCUMENTARY'], avoid_for = [
        'VARIETY',
        'CONFESSION'], constraints = [
        '실제 권위 있는 출처',
        '맹목적 권위 숭배 금지',
        '반론도 언급 가능']),
    'strong_words': HookingType(id = 'strong_words', name = 'Strong Words', korean_name = '강한 뉘앙스 단어', principle = '강렬한 감정을 유발하는 단어로 임팩트 강화', instruction = '중립적 표현 대신 강한 감정을 담은 단어를 사용하세요. "충격적인", "역대급", "반드시", "절대"', psychology = '감정 전염(Emotional Contagion) - 강한 감정 단어는 감정을 전달', best_for = [
        'DRAMATIC',
        'REVENGE',
        'THRILLER',
        'VARIETY'], avoid_for = [
        'DOCUMENTARY',
        'NEWS_REPORT'], constraints = [
        '과용 금지 (피로감)',
        '내용이 뒷받침되어야 함',
        '매번 사용하면 효과 감소']),
    'fomo': HookingType(id = 'fomo', name = 'FOMO', korean_name = '소외감 자극', principle = '"뒤처질 것 같은" 느낌으로 즉각적인 관심 유도', instruction = '"이미 많은 사람들이...", "현명한 사람들은 벌써...", "아직도 모르신다면..." 형식 사용', psychology = '손실 회피(Loss Aversion) - 놓치는 것에 대한 두려움이 얻는 것에 대한 기대보다 강함', best_for = [
        'LIFE_KNOWLEDGE',
        'MONEY_SENSE',
        'OFFICE_SURVIVAL'], avoid_for = [
        'HEARTWARMING',
        'CONFESSION'], constraints = [
        '진짜 중요한 정보일 때만',
        '과도한 불안 조장 금지',
        '해결책 반드시 제공']),
    'surprise': HookingType(id = 'surprise', name = 'Surprise/Curiosity', korean_name = '놀라운 사실', principle = '알려지지 않은 충격적 사실로 호기심 자극', instruction = '시청자가 몰랐을 법한 의외의 사실을 제시하세요. "알고 계셨나요?", "사실은..."', psychology = '호기심 간극(Curiosity Gap) - 아는 것과 모르는 것 사이의 간극이 탐구 동기 유발', best_for = [
        'ENCYCLOPEDIA',
        'HISTORY',
        'SCIENCE',
        'CONSPIRACY'], avoid_for = [
        'TOUCHING',
        'CONFESSION'], constraints = [
        '검증된 사실',
        '의외성이 있어야 함',
        '뻔한 내용 금지']),
    'urgency': HookingType(id = 'urgency', name = 'Urgency/Scarcity', korean_name = '희소성/긴급성', principle = '제한된 시간이나 수량으로 시급함 조성', instruction = '"지금 안 하면...", "이 기회는...", "시간이 얼마 남지 않았습니다" 형식 사용', psychology = '희소성 원리(Scarcity Principle) - 희귀한 것은 더 가치 있게 느껴짐', best_for = [
        'THRILLER',
        'TRUE_STORY'], avoid_for = [
        'ENCYCLOPEDIA',
        'HISTORY'], constraints = [
        '진짜 긴급한 상황일 때만',
        '거짓 긴급성 금지',
        '실제 시간제한이 있을 때']),
    'loss_aversion': HookingType(id = 'loss_aversion', name = 'Loss Aversion', korean_name = '부정/경고', principle = '하지 않으면 생길 손실을 직접 언급하여 주의 환기', instruction = '"이것을 모르면...", "절대 하지 마세요", "이 실수로 인해..." 형식으로 경고', psychology = '손실 회피(Loss Aversion) - 손실을 피하려는 동기가 이득을 얻으려는 동기보다 2배 강함', best_for = [
        'LIFE_KNOWLEDGE',
        'LIFE_TIPS',
        'MONEY_SENSE'], avoid_for = [
        'HEARTWARMING',
        'VARIETY'], constraints = [
        '공포심만 유발하고 끝내면 안 됨',
        '반드시 해결책 제시',
        '과도한 불안 조장 금지']),
    'curiosity_gap': HookingType(id = 'curiosity_gap', name = 'Curiosity Gap', korean_name = '질문형', principle = '질문으로 시청자의 뇌가 자동으로 답을 찾게 만들기', instruction = '시청자가 답을 알고 싶어하는 질문으로 시작하세요. "왜 ~일까요?", "어떻게 ~했을까요?"', psychology = '질문 효과(Question Effect) - 질문을 받으면 뇌가 자동으로 답을 찾기 시작', best_for = [
        'MYSTERY',
        'ENCYCLOPEDIA',
        'PSYCHOLOGY',
        'DOCUMENTARY'], avoid_for = [
        'VARIETY'], constraints = [
        '답이 있는 질문',
        '너무 쉬운 질문 금지',
        '영상에서 답을 반드시 제공']) }
INTRO_STRUCTURE = {
    'attention': {
        'name': '어텐션 (Attention)',
        'duration': '0-3초',
        'goal': '스크롤 멈추게 하기',
        'instruction': '"나와 관련이 있을까?"라는 시청자의 질문에 즉답해야 합니다.',
        'effective': [
            '시각적 임팩트',
            '음향 자극',
            '핵심 한 문장',
            '감정 자극'],
        'prohibited': [
            '"안녕하세요"',
            '"오늘은 이런 걸 해볼게요"',
            '긴 설명',
            '로고만 표시'] },
    'anchor': {
        'name': '앵커 (Anchor)',
        'duration': '3-8초',
        'goal': '시청자가 이 콘텐츠를 어떻게 해석할지 기준점 설정',
        'instruction': '명확한 메시지를 던지지 않으면 시청자는 혼란스러워합니다.',
        'effective': [
            '명확한 주제 제시',
            '구체적 숫자/시간',
            '문제 → 해결 구도',
            '핵심 약속'],
        'prohibited': [
            '애매한 표현',
            '여러 주제 혼합',
            '배경 설명'] },
    'promise': {
        'name': '프로미스 (Promise)',
        'duration': '8-15초',
        'goal': '"끝까지 봐야겠다"고 느끼게 하기',
        'instruction': '본론에서 얻을 구체적 가치를 미리 암시합니다.',
        'effective': [
            '결과 일부 미리 보여주기',
            '"마지막이 가장 강력합니다"',
            '구체적 베네핏',
            '시간 약속'],
        'prohibited': [
            '모든 내용 요약',
            '지루한 개요',
            '약속 없이 본론 진입'] } }
# WARNING: Decompyle incomplete
