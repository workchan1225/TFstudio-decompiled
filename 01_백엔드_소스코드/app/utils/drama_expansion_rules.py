# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: drama_expansion_rules.pyc (Python 3.11)

'''
Drama Expansion Rules

드라마/스토리 장르 대본 확장을 위한 규칙 시스템.
챕터별 Plot Beats, 금지어, 중복 방지 규칙을 관리합니다.

사용법:
    from app.utils.drama_expansion_rules import (
        get_chapter_plot_beat,
        build_plot_beats_prompt,
        extract_used_metaphors,
        build_forbidden_list_prompt,
        build_expansion_guidelines
    )
'''
import re
from typing import List, Set, Dict, Optional, Tuple
from dataclasses import dataclass
PlotBeat = <NODE:12>()
PLOT_BEATS: Dict[(str, PlotBeat)] = {
    '결핍': PlotBeat(stage = '결핍', name = '결핍/도입', goal = '주인공의 일상과 내면의 결핍 제시', required = [
        '일상 묘사',
        '불완전함 암시',
        '주인공 소개'], forbidden = [
        '갈등 해결',
        '카타르시스',
        '반전'], emotion_arc = '평온 → 불안감 암시'),
    '만남': PlotBeat(stage = '만남', name = '만남/변화', goal = '새로운 캐릭터나 환경 등장, 변화의 계기', required = [
        '새로운 요소 등장',
        '변화의 시작',
        '관계 형성'], forbidden = [
        '과거 회상 과다',
        '갈등 해결',
        '결핍 반복'], emotion_arc = '호기심 → 기대감'),
    '의구심': PlotBeat(stage = '의구심', name = '의구심/긴장', goal = '긴장감 고조, 장애물과 의심 등장', required = [
        '장애물 등장',
        '의심/불신',
        '갈등 암시'], forbidden = [
        '갈등 조기 해결',
        '카타르시스',
        '새 캐릭터 다수 등장'], emotion_arc = '불안 → 긴장 고조'),
    '위기_갈등': PlotBeat(stage = '위기_갈등', name = '위기/갈등', goal = '핵심 갈등 폭발, 금기 파기', required = [
        '갈등 폭발',
        '대립',
        '선택의 기로'], forbidden = [
        '쉬운 해결',
        '외부 도움으로 해결',
        '감정 평온'], emotion_arc = '갈등 → 위기감 최고조'),
    '진실_규명': PlotBeat(stage = '진실_규명', name = '진실 규명/반전', goal = '숨겨진 진실 드러남, 복선 회수', required = [
        '진실 드러남',
        '복선 회수',
        '이해/깨달음'], forbidden = [
        '새 갈등 도입',
        '새 미스터리 추가',
        '감정 평온'], emotion_arc = '충격 → 이해'),
    '카타르시스': PlotBeat(stage = '카타르시스', name = '카타르시스/해결', goal = '감정 폭발, 갈등 해결, 여운', required = [
        '감정 폭발',
        '갈등 해결',
        '여운/교훈'], forbidden = [
        '새 갈등',
        '미해결 상태',
        '급격한 반전'], emotion_arc = '감정 해소 → 평화/성장') }
CHAPTER_PLOT_MAPPING: Dict[(int, Dict[(int, str)])] = {
    3: {
        1: '결핍',
        2: '위기_갈등',
        3: '카타르시스' },
    4: {
        1: '결핍',
        2: '만남',
        3: '위기_갈등',
        4: '카타르시스' },
    5: {
        1: '결핍',
        2: '만남',
        3: '위기_갈등',
        4: '진실_규명',
        5: '카타르시스' },
    6: {
        1: '결핍',
        2: '만남',
        3: '의구심',
        4: '위기_갈등',
        5: '진실_규명',
        6: '카타르시스' },
    7: {
        1: '결핍',
        2: '만남',
        3: '의구심',
        4: '위기_갈등',
        5: '위기_갈등',
        6: '진실_규명',
        7: '카타르시스' },
    8: {
        1: '결핍',
        2: '만남',
        3: '의구심',
        4: '위기_갈등',
        5: '위기_갈등',
        6: '진실_규명',
        7: '진실_규명',
        8: '카타르시스' } }
FORBIDDEN_METAPHORS: List[str] = [
    '거미줄에 걸린 나비처럼',
    '숨 쉴 수조차 없는',
    '마치 어둠 속에서 빛을 찾는',
    '가슴에 구멍이 뚫린 듯',
    '심장이 터질 것 같은',
    '눈물이 봇물처럼',
    '마치 꿈을 꾸는 것 같은',
    '가슴이 찢어지는 것 같은',
    '온몸에 힘이 들어가는',
    '숨이 멎는 것 같은']
FORBIDDEN_EMOTIONS: List[str] = [
    '삶을 스스로 개척하려는 강한 의지',
    '자신이 잃어버린 모든 것을 되찾겠다',
    '사랑이 영원히 살아 숨 쉬고 있었다',
    '확고한 의지로 빛나는 눈빛',
    '진정한 사랑의 의미를 깨달았다',
    '모든 것을 걸고 싸우겠다는 각오',
    '운명에 맞서 싸우는']
FORBIDDEN_CHAPTER_ENDINGS: List[str] = [
    '이것이 진정한',
    '이것이야말로',
    '그것이 바로',
    '이제야 깨달았다',
    '드디어 알게 되었다',
    '결국 그것은']
FORBIDDEN_HOOKS: List[str] = [
    '충격적인 사실',
    '믿을 수 없는',
    '상상할 수 없는',
    '아무도 예상하지 못한',
    '모두가 놀란',
    '세상이 뒤집어질']
RECOMMENDED_METAPHORS: Dict[(str, List[str])] = {
    '고통': [
        '가슴을 짓누르는 돌덩이처럼',
        '살을 에는 바람처럼',
        '녹슨 못이 박히듯',
        '얼음장 같은 손길이',
        '뼈를 깎는 듯한'],
    '기쁨': [
        '봄날의 햇살처럼',
        '새벽녘의 이슬처럼',
        '날개가 돋은 듯',
        '꽃이 피어나듯',
        '바람에 실려 오는 향기처럼'],
    '슬픔': [
        '먹구름이 드리우듯',
        '가을비처럼 스며드는',
        '낙엽이 지듯',
        '해 질 녘의 노을처럼',
        '차가운 안개처럼'],
    '분노': [
        '화산이 폭발하듯',
        '파도가 휘몰아치듯',
        '불길이 타오르듯',
        '천둥이 치듯',
        '용암이 끓어오르듯'],
    '공포': [
        '어둠 속에 삼켜지듯',
        '심연으로 빠져드는',
        '칼날 위를 걷는 듯한',
        '서리가 내리듯',
        '그림자가 드리우듯'] }

def get_chapter_plot_beat(chapter_num = None, total_chapters = None):
    '''
    특정 챕터의 Plot Beat를 반환합니다.

    Args:
        chapter_num: 챕터 번호 (1부터 시작)
        total_chapters: 전체 챕터 수

    Returns:
        PlotBeat 객체 또는 None
    '''
    pass
# WARNING: Decompyle incomplete


def build_plot_beats_prompt(chapter_count = None, current_chapter = None, chapter_titles = None):
    '''
    Plot Beats 프롬프트를 생성합니다.

    Args:
        chapter_count: 전체 챕터 수
        current_chapter: 현재 확장 중인 챕터 (None이면 전체)
        chapter_titles: 챕터 제목 목록

    Returns:
        프롬프트 문자열
    '''
    lines = [
        '★★★ 챕터별 서사 구조 지침 ★★★',
        '',
        '각 챕터는 아래 지침에 따라 작성해야 합니다.',
        '이전 챕터의 내용을 반복하지 마세요!',
        '']
    for ch_num in range(1, chapter_count + 1):
        beat = get_chapter_plot_beat(ch_num, chapter_count)
        if not beat:
            continue
        if current_chapter and ch_num == current_chapter:
            lines.append(f'''>>> 챕터 {ch_num} [{beat.name}] <<< (현재 확장 중)''')
        else:
            lines.append(f'''챕터 {ch_num} [{beat.name}]:''')
        if chapter_titles and ch_num <= len(chapter_titles):
            lines.append(f'''  제목: {chapter_titles[ch_num - 1]}''')
        lines.append(f'''  목표: {beat.goal}''')
        lines.append(f'''  감정: {beat.emotion_arc}''')
        lines.append(f'''  필수: {', '.join(beat.required)}''')
        lines.append(f'''  금지: {', '.join(beat.forbidden)}''')
        lines.append('')
        return '\n'.join(lines)


def extract_used_metaphors(script = None):
    '''
    대본에서 이미 사용된 비유/은유를 추출합니다.

    Args:
        script: 현재 대본 텍스트

    Returns:
        사용된 비유 집합
    '''
    used = set()
    for metaphor in FORBIDDEN_METAPHORS:
        if metaphor[:5] in script:
            used.add(metaphor)
        patterns = [
            '마치\\s+[^.]+처럼',
            '[가-힣]+처럼',
            '[가-힣]+\\s+같은',
            '[가-힣]+듯']
        for pattern in patterns:
            matches = re.findall(pattern, script)
            for match in matches:
                if len(match) > 5:
                    used.add(match)
                return used


def extract_used_emotions(script = None):
    '''
    대본에서 이미 사용된 감정/결심 표현을 추출합니다.

    Args:
        script: 현재 대본 텍스트

    Returns:
        사용된 감정 표현 집합
    '''
    used = set()
    for emotion in FORBIDDEN_EMOTIONS:
        if emotion[:5] in script:
            used.add(emotion)
        return used


def build_forbidden_list_prompt(current_script = None):
    '''
    금지 목록 프롬프트를 생성합니다.

    Args:
        current_script: 현재 대본

    Returns:
        금지 목록 프롬프트 문자열
    '''
    used_metaphors = extract_used_metaphors(current_script)
    used_emotions = extract_used_emotions(current_script)
    lines = [
        '🚨🚨🚨 중복 표현 절대 금지 목록 🚨🚨🚨',
        '',
        '아래 표현들은 이미 사용되었거나 클리셰입니다.',
        '절대 다시 사용하지 마세요!',
        '']
    lines.append('【비유/은유 - 대본 전체에서 1회만 사용 가능】')
    for metaphor in FORBIDDEN_METAPHORS[:7]:
        status = '✗ 사용됨' if metaphor in used_metaphors else '⚠️ 1회 제한'
        lines.append(f'''  {status}: {metaphor}''')
        lines.append('')
        lines.append('【감정/결심 표현 - 반복 사용 금지】')
        for emotion in FORBIDDEN_EMOTIONS[:5]:
            status = '✗ 사용됨' if emotion in used_emotions else '⚠️ 1회 제한'
            lines.append(f'''  {status}: {emotion}''')
            lines.append('')
            lines.append('【챕터 말미 금지 패턴】')
            for ending in FORBIDDEN_CHAPTER_ENDINGS:
                lines.append(f'''  ✗ \'{ending}...\' 형태의 결말 문구''')
                lines.append('')
                lines.append('【후킹 문구 - 1회만 사용 가능】')
                for hook in FORBIDDEN_HOOKS[:4]:
                    lines.append(f'''  ⚠️ \'{hook}\' (이미 사용했다면 다른 표현 사용)''')
                    lines.append('')
                    lines.append('【대안 비유/은유 (사용 권장)】')
                    for emotion, metaphors in list(RECOMMENDED_METAPHORS.items())[:3]:
                        lines.append(f'''  [{emotion}]''')
                        for m in metaphors[:2]:
                            lines.append(f'''    ✓ {m}''')
                            lines.append('')
                            return '\n'.join(lines)


def build_expansion_guidelines(current_script = None, chapter_count = None, current_chapter = None, chapter_titles = (None, None)):
    '''
    대본 확장을 위한 전체 가이드라인을 생성합니다.

    Args:
        current_script: 현재 대본
        chapter_count: 전체 챕터 수
        current_chapter: 현재 챕터 (None이면 전체)
        chapter_titles: 챕터 제목 목록

    Returns:
        전체 가이드라인 프롬프트
    '''
    plot_beats = build_plot_beats_prompt(chapter_count, current_chapter, chapter_titles)
    forbidden_list = build_forbidden_list_prompt(current_script)
    
    try:
        build_reaction_prompt = build_reaction_prompt
        import app.utils.emotion_body_reactions
        reaction_prompt = build_reaction_prompt(current_script, [
            '분노',
            '슬픔',
            '공포',
            '기쁨',
            '긴장',
            '절망'])
    except ImportError:
        reaction_prompt = ''

    lines = [
        '============================================================',
        '대본 확장 상세 가이드라인',
        '============================================================',
        '',
        plot_beats,
        '',
        forbidden_list,
        '']
    if reaction_prompt:
        lines.extend([
            reaction_prompt,
            ''])
    lines.extend([
        '【일반 규칙】',
        '1. 동일한 문장을 다른 위치에 재사용 금지',
        '2. 같은 비유/은유 2회 이상 사용 금지',
        '3. 챕터마다 같은 결심/각오 문구 반복 금지',
        "4. '마치 ~처럼' 비유는 챕터당 최대 2개",
        '5. 이전 챕터의 감정 상태로 회귀 금지',
        '6. 해결된 갈등을 다시 등장시키지 마세요',
        '',
        '============================================================'])
    return '\n'.join(lines)


def validate_chapter_progression(previous_chapters = None, current_chapter = None, chapter_num = None, total_chapters = ('previous_chapters', List[str], 'current_chapter', str, 'chapter_num', int, 'total_chapters', int, 'return', List[str])):
    '''
    챕터 간 서사 진행을 검증합니다.

    Args:
        previous_chapters: 이전 챕터들의 내용
        current_chapter: 현재 챕터 내용
        chapter_num: 현재 챕터 번호
        total_chapters: 전체 챕터 수

    Returns:
        경고 메시지 목록
    '''
    warnings = []
    beat = get_chapter_plot_beat(chapter_num, total_chapters)
    if not beat:
        return warnings
    for forbidden in None.forbidden:
        if forbidden.lower() in current_chapter.lower():
            warnings.append(f'''챕터 {chapter_num}에서 금지된 요소 \'{forbidden}\' 감지''')
        if previous_chapters:
            prev_text = ' '.join(previous_chapters)
            words = current_chapter.split()
            for i in range(len(words) - 2):
                phrase = ' '.join(words[i:i + 3])
                if phrase in prev_text and len(phrase) > 10:
                    warnings.append(f'''이전 챕터와 중복된 구절 발견: \'{phrase[:20]}...\'''')
                
                return warnings

if __name__ == '__main__':
    test_script = '\n    유진은 거미줄에 걸린 나비처럼 꼼짝할 수 없었다.\n    그녀는 삶을 스스로 개척하려는 강한 의지를 다졌다.\n    관자놀이가 욱신거렸다.\n    '
    print('=== Plot Beats 프롬프트 (6챕터) ===')
    print(build_plot_beats_prompt(6))
    print('\n=== 금지 목록 프롬프트 ===')
    print(build_forbidden_list_prompt(test_script))
    print('\n=== 전체 가이드라인 ===')
    print(build_expansion_guidelines(test_script, 6, current_chapter = 3))
    return None
