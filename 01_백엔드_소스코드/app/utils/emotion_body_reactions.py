# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: emotion_body_reactions.pyc (Python 3.11)

'''
Emotion Body Reactions Library

감정별 신체 반응 라이브러리.
대본 확장 시 다양한 묘사를 제공하여 중복을 방지합니다.

사용법:
    from app.utils.emotion_body_reactions import (
        get_available_reactions,
        build_reaction_prompt,
        extract_used_reactions
    )
'''
import re
from typing import List, Set, Dict, Optional
EMOTION_BODY_REACTIONS: Dict[(str, List[str])] = {
    '분노': [
        '주먹을 꽉 쥐었다',
        '턱에 힘이 들어갔다',
        '손끝이 부들부들 떨렸다',
        '이를 악물었다',
        '미간이 찌푸려졌다',
        '목덜미가 뜨거워졌다',
        '어금니를 깨물었다',
        '손톱이 손바닥에 파고들었다',
        '관자놀이가 욱신거렸다',
        '눈에 핏발이 섰다',
        '숨이 거칠어졌다',
        '입술이 바르르 떨렸다',
        '목소리가 떨렸다',
        '온몸에 힘이 들어갔다',
        '얼굴이 붉게 달아올랐다'],
    '슬픔': [
        '눈시울이 붉어졌다',
        '목이 메어왔다',
        '어깨가 축 처졌다',
        '코끝이 시큰해졌다',
        '손바닥으로 얼굴을 가렸다',
        '호흡이 불규칙해졌다',
        '눈물이 볼을 타고 흘러내렸다',
        '입술을 깨물었다',
        '고개가 저절로 떨궈졌다',
        '가슴이 먹먹해졌다',
        '손이 힘없이 늘어졌다',
        '목울대가 떨렸다',
        '숨을 삼키며 참았다',
        '눈가가 촉촉해졌다',
        '한숨이 새어 나왔다'],
    '공포': [
        '등골이 서늘해졌다',
        '목덜미가 뻣뻣해졌다',
        '손에 땀이 배었다',
        '심장이 쿵쾅거렸다',
        '다리에 힘이 풀렸다',
        '동공이 확장되었다',
        '온몸에 소름이 돋았다',
        '숨이 멎는 것 같았다',
        '등줄기에 식은땀이 흘렀다',
        '입이 바싹 말랐다',
        '목소리가 떨려 나왔다',
        '무릎이 후들거렸다',
        '손끝이 차가워졌다',
        '심장이 조여오는 듯했다',
        '온몸이 굳어버렸다'],
    '기쁨': [
        '입가에 미소가 번졌다',
        '눈이 반짝였다',
        '가슴이 벅차올랐다',
        '얼굴이 환하게 빛났다',
        '심장이 두근거렸다',
        '온몸에 전율이 흘렀다',
        '어깨가 가벼워졌다',
        '발걸음이 가벼워졌다',
        '눈가에 잔주름이 생겼다',
        '입꼬리가 올라갔다',
        '볼이 발그레해졌다',
        '손뼉을 마주쳤다',
        '웃음이 터져 나왔다',
        '숨이 가빠졌다',
        '눈물이 글썽였다'],
    '긴장': [
        '손에 땀이 났다',
        '심장이 빠르게 뛰었다',
        '목이 바짝 말랐다',
        '어깨에 힘이 들어갔다',
        '호흡이 얕아졌다',
        '손가락이 무의식적으로 움직였다',
        '입술을 핥았다',
        '눈을 질끈 감았다',
        '몸이 경직되었다',
        '침을 삼켰다',
        '손이 미세하게 떨렸다',
        '이마에 땀이 맺혔다',
        '목소리가 떨렸다',
        '다리를 떨었다',
        '손톱으로 손바닥을 긁었다'],
    '절망': [
        '무릎에서 힘이 빠져 주저앉았다',
        '모든 것이 무너지는 듯했다',
        '눈앞이 아득해졌다',
        '숨 쉬는 것조차 힘겨웠다',
        '온몸의 힘이 빠졌다',
        '머리가 텅 비어버렸다',
        '입술이 파르르 떨렸다',
        '눈물조차 나오지 않았다',
        '가슴에 구멍이 뚫린 것 같았다',
        '다리가 휘청거렸다',
        '손이 허공을 헤맸다',
        '목소리가 나오지 않았다',
        '온몸이 무거워졌다',
        '고개를 떨궜다',
        '어깨가 축 처졌다'],
    '놀람': [
        '눈이 휘둥그레졌다',
        '입이 떡 벌어졌다',
        '심장이 덜컥 내려앉았다',
        '숨이 멎는 듯했다',
        '몸이 굳어버렸다',
        '한 발짝 뒤로 물러섰다',
        '손으로 입을 막았다',
        '눈을 껌뻑였다',
        '말문이 막혔다',
        '온몸에 전율이 흘렀다',
        '귀를 의심했다',
        '눈을 비볐다',
        '고개를 갸웃거렸다',
        '숨을 들이켰다',
        '얼굴이 하얗게 질렸다'],
    '그리움': [
        '가슴 한 구석이 시려왔다',
        '눈가가 촉촉해졌다',
        '한숨이 새어 나왔다',
        '마음 한 켠이 텅 빈 것 같았다',
        '목이 메어왔다',
        '손이 무의식적으로 가슴을 짚었다',
        '눈을 지그시 감았다',
        '코끝이 시큰해졌다',
        '입술을 깨물었다',
        '손끝으로 무언가를 어루만졌다',
        '발걸음이 느려졌다',
        '멀리 하늘을 바라보았다',
        '미소가 애잔하게 번졌다',
        '추억이 밀려와 눈물이 고였다',
        '가슴이 먹먹해졌다'],
    '결심': [
        '눈빛이 단단해졌다',
        '주먹을 불끈 쥐었다',
        '어깨를 꼿꼿이 폈다',
        '고개를 끄덕였다',
        '입술을 굳게 다물었다',
        '턱을 치켜들었다',
        '눈을 질끈 감았다가 떴다',
        '깊은 숨을 내쉬었다',
        '목소리에 힘이 실렸다',
        '발을 굳게 디뎠다',
        '시선이 흔들리지 않았다',
        '손을 가슴에 얹었다',
        '입꼬리가 단호하게 올라갔다',
        '미간에 주름이 잡혔다',
        '눈에 불꽃이 일었다'] }
CLICHE_REACTIONS: List[str] = [
    '관자놀이가 욱신거렸다',
    '눈물이 봇물처럼 터져 나왔다',
    '손으로 눈물을 닦아냈지만 멈추지 않았다',
    '가슴이 찢어지는 것 같았다',
    '온몸에 힘이 들어갔다',
    '심장이 터질 것 같았다',
    '숨을 참았다']

def extract_used_reactions(script = None):
    '''
    대본에서 이미 사용된 신체 반응 표현을 추출합니다.

    Args:
        script: 현재 대본 텍스트

    Returns:
        사용된 신체 반응 표현 집합
    '''
    used = set()
    for emotion, reactions in EMOTION_BODY_REACTIONS.items():
        for reaction in reactions:
            base_pattern = reaction.replace('다', '').replace('었', '').replace('았', '')
            if base_pattern[:5] in script:
                used.add(reaction)
            return used


def get_available_reactions(emotion = None, already_used = None, exclude_cliches = None, limit = (None, True, 5)):
    '''
    사용 가능한 신체 반응 표현 목록을 반환합니다.

    Args:
        emotion: 감정 유형 (분노, 슬픔, 공포 등)
        already_used: 이미 사용된 표현 집합
        exclude_cliches: 클리셰 표현 제외 여부
        limit: 반환할 최대 개수

    Returns:
        사용 가능한 신체 반응 표현 목록
    '''
    pass
# WARNING: Decompyle incomplete


def build_reaction_prompt(current_script = None, target_emotions = None):
    '''
    프롬프트에 포함할 신체 반응 가이드를 생성합니다.

    Args:
        current_script: 현재 대본 (이미 사용된 표현 추출용)
        target_emotions: 대상 감정 목록 (없으면 모든 감정)

    Returns:
        프롬프트에 포함할 신체 반응 가이드 문자열
    '''
    pass
# WARNING: Decompyle incomplete


def get_emotion_from_context(context = None):
    '''
    문맥에서 감정을 추론합니다.

    Args:
        context: 문맥 텍스트

    Returns:
        추론된 감정 또는 None
    '''
    emotion_keywords = {
        '분노': [
            '화가',
            '분노',
            '열받',
            '빡치',
            '짜증',
            '격분',
            '울분'],
        '슬픔': [
            '슬픔',
            '슬퍼',
            '우울',
            '비통',
            '애도',
            '눈물'],
        '공포': [
            '무서',
            '두려',
            '공포',
            '겁',
            '무섭',
            '떨리'],
        '기쁨': [
            '기쁨',
            '행복',
            '좋아',
            '기뻐',
            '환희',
            '감동'],
        '긴장': [
            '긴장',
            '불안',
            '초조',
            '걱정',
            '두근'],
        '절망': [
            '절망',
            '좌절',
            '포기',
            '실망',
            '무력'],
        '놀람': [
            '놀라',
            '충격',
            '경악',
            '깜짝',
            '어리둥절'],
        '그리움': [
            '그리',
            '그립',
            '향수',
            '회상',
            '추억'],
        '결심': [
            '결심',
            '각오',
            '다짐',
            '마음먹',
            '결의'] }
    context_lower = context.lower()
    for emotion, keywords in emotion_keywords.items():
        for keyword in keywords:
            if keyword in context_lower:
                
                
                return None, None, emotion
            return None

if __name__ == '__main__':
    test_script = '\n    유진은 관자놀이가 욱신거렸다. 눈물이 볼을 타고 흘러내렸다.\n    그녀는 주먹을 꽉 쥐었다.\n    '
    print('=== 이미 사용된 표현 ===')
    used = extract_used_reactions(test_script)
    for r in used:
        print(f'''  - {r}''')
        print('\n=== 분노 감정 사용 가능한 표현 ===')
        available = get_available_reactions('분노', used)
        for r in available:
            print(f'''  ✓ {r}''')
            print('\n=== 전체 프롬프트 ===')
            prompt = build_reaction_prompt(test_script, [
                '분노',
                '슬픔',
                '공포'])
            print(prompt)
            return None
            return None
