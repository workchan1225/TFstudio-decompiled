# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: story_circle.pyc (Python 3.11)

"""
Story Circle (Dan Harmon's 8-Step Story Structure)

댄 하먼의 스토리 서클 8단계를 동적으로 적용하여 서사 구조를 생성합니다.
하드코딩된 예시 없이 AI가 시놉시스에 맞게 창의적으로 생성하도록 지침만 제공합니다.
"""
from typing import Dict, List, Optional, Tuple
STORY_CIRCLE_STEPS = {
    1: {
        'name': 'YOU',
        'korean': '편안함의 영역',
        'role': '현상 유지 (Status Quo)',
        'description': '주인공이 익숙한 환경에 존재하는 "이전(before)" 상태',
        'instruction': '주인공의 일상, 현재 상태, 편안함의 영역을 보여주세요. 완벽하거나 행복하지 않아도 되지만, 적어도 적응된 상태입니다.',
        'psychology': '시청자가 주인공과 동일시할 수 있는 공감대 형성',
        'key_question': '주인공은 어떤 일상을 살고 있는가?',
        'position': 'top' },
    2: {
        'name': 'NEED',
        'korean': '욕구/결핍',
        'role': '결핍 발생 (The Problem)',
        'description': '현상 유지를 깨뜨리는 내면의 결핍이나 외부 사건',
        'instruction': '주인공이 얻고 싶은 것 또는 사라지기를 바라는 문제를 제시하세요. 이것이 서사의 엔진을 점화합니다.',
        'psychology': '시청자에게 "왜 이 이야기를 봐야 하는가?"에 대한 답을 제공',
        'key_question': '주인공은 무엇을 원하는가? 또는 어떤 문제에 직면했는가?',
        'position': 'top' },
    3: {
        'name': 'GO',
        'korean': '경계 횡단',
        'role': '문턱을 넘다 (Crossing the Threshold)',
        'description': '주인공이 욕구를 충족시키기 위해 익숙하지 않은 상황으로 첫발을 내딛는 순간',
        'instruction': '주인공이 의식적인 결정을 내리고 편안함의 영역을 떠나는 순간을 보여주세요. 이것은 돌이킬 수 없는 선택입니다.',
        'psychology': '서사적 긴장감 시작, 시청자의 기대감 상승',
        'key_question': '주인공은 어떤 결정을 내렸는가?',
        'position': 'threshold' },
    4: {
        'name': 'SEARCH',
        'korean': '시련과 적응',
        'role': '시련의 길 (Road of Trials)',
        'description': '혼돈의 세계에서 새로운 환경에 적응하고 시련을 극복하려 애쓰는 단계',
        'instruction': '주인공이 장애물과 시련을 겪으며 성장하는 과정을 보여주세요. 되돌아가는 길은 막혀 있습니다.',
        'psychology': '시청자가 주인공과 함께 고군분투하며 감정적 투자 증가',
        'key_question': '주인공은 어떤 시련을 겪는가? 어떻게 적응하는가?',
        'position': 'bottom' },
    5: {
        'name': 'FIND',
        'korean': '발견',
        'role': '욕구 획득 (Getting What They Wanted)',
        'description': '주인공이 마침내 원하던 것을 획득하는 순간 (또는 그것의 원형)',
        'instruction': '주인공이 목표에 도달하거나 핵심적인 깨달음을 얻는 순간을 보여주세요. 하지만 이것은 종종 "거짓된 승리"일 수 있습니다.',
        'psychology': '감정적 정점, 하지만 대가를 치르지 않았으므로 불완전한 승리',
        'key_question': '주인공이 발견한 것은 무엇인가?',
        'position': 'bottom' },
    6: {
        'name': 'TAKE',
        'korean': '대가',
        'role': '가장 큰 대가 (The Price)',
        'description': '발견의 대가로 가장 큰 희생이나 상실을 겪는 단계',
        'instruction': '주인공이 가장 큰 감정적/물리적 대가를 치르는 순간을 보여주세요. 이것이 이야기의 진정한 감정적 최저점입니다.',
        'psychology': '"영혼의 어두운 밤" - 시청자가 가장 강한 감정적 반응을 보이는 순간',
        'key_question': '주인공이 치른 대가는 무엇인가?',
        'position': 'bottom' },
    7: {
        'name': 'RETURN',
        'korean': '복귀',
        'role': '익숙한 세계로 돌아오다 (Return)',
        'description': '대가를 치르고 진정한 깨달음을 얻은 주인공이 출발점으로 돌아오는 단계',
        'instruction': '주인공이 변화된 모습으로 일상으로 돌아오는 과정을 보여주세요. 이 복귀도 또 다른 시련을 수반할 수 있습니다.',
        'psychology': '서사적 완결감 시작, 카타르시스 준비',
        'key_question': '주인공은 어떻게 돌아오는가?',
        'position': 'threshold' },
    8: {
        'name': 'CHANGE',
        'korean': '변화',
        'role': '새로운 질서 (New Order)',
        'description': '여정을 마친 주인공이 근본적으로 변화하여 새로운 질서에 도달',
        'instruction': '주인공이 어떻게 변했는지 보여주세요. 더 현명해지는 긍정적 변화일 수도, 모든 것을 잃는 비극적 변화일 수도 있습니다.',
        'psychology': '완전한 서사적 만족감, 시청자에게 여운과 교훈 제공',
        'key_question': '주인공은 어떻게 변화했는가?',
        'position': 'top' } }
CHAPTER_TO_CIRCLE_MAPPING = {
    4: {
        1: [
            1,
            2],
        2: [
            3,
            4],
        3: [
            5,
            6],
        4: [
            7,
            8] },
    5: {
        1: [
            1,
            2],
        2: [
            3,
            4],
        3: [
            5],
        4: [
            6,
            7],
        5: [
            8] },
    6: {
        1: [
            1],
        2: [
            2,
            3],
        3: [
            4],
        4: [
            5,
            6],
        5: [
            7],
        6: [
            8] },
    7: {
        1: [
            1],
        2: [
            2],
        3: [
            3,
            4],
        4: [
            5],
        5: [
            6],
        6: [
            7],
        7: [
            8] },
    8: {
        1: [
            1],
        2: [
            2],
        3: [
            3],
        4: [
            4],
        5: [
            5],
        6: [
            6],
        7: [
            7],
        8: [
            8] } }
GENRE_CIRCLE_VARIATIONS = {
    'drama': {
        'focus_steps': [
            2,
            6,
            8],
        'emotional_arc': '안타까움 → 분노 → 통쾌함 → 교훈',
        'step_emphasis': {
            1: '시청자가 공감할 수 있는 평범한 일상',
            2: '불합리한 상황 또는 억울한 피해',
            6: '가장 큰 시련과 감정적 폭발',
            8: '정의 실현 또는 깨달음' } },
    'info': {
        'focus_steps': [
            2,
            5,
            8],
        'emotional_arc': '문제 인식 → 해결책 발견 → 실천과 변화',
        'step_emphasis': {
            1: '시청자가 현재 겪고 있는 불편함/오해',
            2: '시청자가 해결하고 싶은 문제 (지식의 격차)',
            5: '핵심 솔루션, "아하!" 순간',
            6: '솔루션을 얻기 위해 치러야 할 대가 (노력, 변화)',
            8: '변화된 미래, 새로운 질서' } },
    'mystery': {
        'focus_steps': [
            4,
            5,
            8],
        'emotional_arc': '의문 → 추리 → 진실 발견 → 해결',
        'step_emphasis': {
            4: '단서 수집과 추리 과정',
            5: '결정적 단서 발견, 반전의 실마리',
            8: '진실 규명, 예상치 못한 결말' } },
    'revenge': {
        'focus_steps': [
            2,
            4,
            6,
            8],
        'emotional_arc': '억울함 → 인내 → 반격 → 통쾌한 승리',
        'step_emphasis': {
            2: '극단적 피해, 분노의 씨앗',
            4: '복수 준비, 숨겨진 능력 연마',
            6: '가해자에게 치르게 하는 대가',
            8: '정의 실현, 담담한 승리' } },
    'heartwarming': {
        'focus_steps': [
            1,
            5,
            6,
            8],
        'emotional_arc': '오해 → 갈등 → 진심 발견 → 화해',
        'step_emphasis': {
            1: '차가워 보이는 관계, 서로를 이해하지 못하는 상태',
            5: '숨겨진 진심 발견, 오해가 풀리는 순간',
            6: '용서하기 위해 버려야 할 것 (자존심, 분노)',
            8: '따뜻한 화해, 관계 회복' } },
    'thriller': {
        'focus_steps': [
            3,
            4,
            6,
            7],
        'emotional_arc': '위기 감지 → 긴장 고조 → 절체절명 → 탈출',
        'step_emphasis': {
            3: '위험 속으로 들어가는 순간 (돌이킬 수 없음)',
            4: '점점 조여오는 위협, 탈출 시도',
            6: '절체절명의 순간, 모든 희망 상실',
            7: '극적 탈출 또는 반전' } } }

def get_genre_category(genre = None):
    '''장르 코드에서 카테고리 추출'''
    drama_genres = [
        'DRAMATIC',
        'CONFESSION',
        'TOUCHING',
        'LIFE_LESSONS',
        'LIFE_CHALLENGE']
    info_genres = [
        'ENCYCLOPEDIA',
        'LIFE_TIPS',
        'LIFE_KNOWLEDGE',
        'OFFICE_SURVIVAL',
        'MONEY_SENSE',
        'RELATIONSHIP_EQ',
        'PSYCHOLOGY',
        'LIFE_CHOICES',
        'KNOWLEDGE_BITE']
    mystery_genres = [
        'MYSTERY',
        'CONSPIRACY']
    revenge_genres = [
        'REVENGE']
    heartwarming_genres = [
        'HEARTWARMING',
        'FAMILY']
    thriller_genres = [
        'THRILLER',
        'HORROR']
    if genre in drama_genres:
        return 'drama'
    if None in info_genres:
        return 'info'
    if None in mystery_genres:
        return 'mystery'
    if None in revenge_genres:
        return 'revenge'
    if None in heartwarming_genres:
        return 'heartwarming'
    if None in thriller_genres:
        return 'thriller'


def get_chapter_circle_steps(chapter_num = None, total_chapters = None):
    '''특정 챕터에 해당하는 스토리 서클 단계 반환'''
    if total_chapters not in CHAPTER_TO_CIRCLE_MAPPING:
        if total_chapters < 4:
            total_chapters = 4
        elif total_chapters > 8:
            total_chapters = 8
    mapping = CHAPTER_TO_CIRCLE_MAPPING.get(total_chapters, CHAPTER_TO_CIRCLE_MAPPING[6])
    return mapping.get(chapter_num, [])


def build_story_circle_prompt(genre = None, chapter_count = None, synopsis = None, include_psychology = (6, None, True)):
    '''
    스토리 서클 기반 대본 구조 프롬프트 생성

    Args:
        genre: 장르 코드
        chapter_count: 챕터 수
        synopsis: 시놉시스 (선택)
        include_psychology: 심리학적 원리 포함 여부

    Returns:
        스토리 서클 구조 프롬프트
    '''
    category = get_genre_category(genre)
    variation = GENRE_CIRCLE_VARIATIONS.get(category, GENRE_CIRCLE_VARIATIONS['drama'])
    lines = [
        "## 스토리 서클 8단계 구조 (Dan Harmon's Story Circle)",
        '',
        f'''**감정 곡선**: {variation['emotional_arc']}''',
        '',
        '각 챕터는 다음 스토리 서클 단계를 따라야 합니다:',
        '']
    for chapter_num in range(1, chapter_count + 1):
        steps = get_chapter_circle_steps(chapter_num, chapter_count)
        step_names = []
        step_instructions = []
        for step_num in steps:
            step = STORY_CIRCLE_STEPS[step_num]
            step_names.append(f'''{step['name']}({step['korean']})''')
            if step_num in variation.get('step_emphasis', { }):
                instruction = variation['step_emphasis'][step_num]
            else:
                instruction = step['instruction']
            step_instructions.append(f'''  - {step['key_question']}''')
            step_instructions.append(f'''  - {instruction}''')
            if include_psychology and step_num in variation.get('focus_steps', []):
                step_instructions.append(f'''  - [심리] {step['psychology']}''')
            lines.append(f'''### 챕터 {chapter_num}: {' + '.join(step_names)}''')
            lines.extend(step_instructions)
            lines.append('')
            lines.extend([
                '## 스토리 서클 핵심 원칙',
                '',
                "1. **하강과 복귀**: 주인공은 반드시 '질서의 세계'에서 '혼돈의 세계'로 내려갔다가 다시 올라와야 합니다.",
                '2. **변화 필수**: 마지막에 주인공은 처음과 달라져야 합니다. 같은 사람으로 끝나면 안 됩니다.',
                '3. **대가 지불**: 5단계(발견) 후 반드시 6단계(대가)가 있어야 합니다. 공짜 승리는 없습니다.',
                '4. **감정 곡선**: 시청자의 감정이 롤러코스터를 타듯 오르내려야 합니다.',
                ''])
            return '\n'.join(lines)


def build_chapter_structure_with_circle(genre = None, chapter_count = None):
    '''
    스토리 서클을 적용한 챕터 구조 반환

    Returns:
        {챕터번호: {steps: [], instruction: str, focus: str}}
    '''
    pass
# WARNING: Decompyle incomplete


def get_story_circle_summary():
    '''스토리 서클 8단계 요약 반환 (간단한 버전)'''
    return '스토리 서클 8단계:\n1. YOU (편안함) - 주인공의 일상\n2. NEED (욕구) - 문제/욕구 발생\n3. GO (이동) - 새로운 상황으로 진입\n4. SEARCH (시련) - 적응과 시련\n5. FIND (발견) - 원하던 것 획득\n6. TAKE (대가) - 가장 큰 대가 지불\n7. RETURN (복귀) - 일상으로 돌아옴\n8. CHANGE (변화) - 변화된 새로운 질서'


def build_story_circle_expansion_prompt(genre = None, chapter_count = None):
    '''
    대본 확장 시 스토리 서클 기반 지침 생성

    기존 대본 구조를 유지하면서 각 챕터의 스토리 서클 단계에 맞게
    세부 묘사를 추가하도록 안내합니다.

    Args:
        genre: 장르 코드
        chapter_count: 챕터 수

    Returns:
        확장용 스토리 서클 프롬프트
    '''
    category = get_genre_category(genre)
    variation = GENRE_CIRCLE_VARIATIONS.get(category, GENRE_CIRCLE_VARIATIONS['drama'])
    lines = [
        '## 스토리 서클 단계별 확장 지침',
        '',
        '각 챕터를 확장할 때, 해당 챕터의 스토리 서클 단계에 맞는 요소를 강화하세요:',
        '']
    for chapter_num in range(1, chapter_count + 1):
        steps = get_chapter_circle_steps(chapter_num, chapter_count)
        if not steps:
            continue
        step_names = []
        expansion_tips = []
        for step_num in steps:
            step = STORY_CIRCLE_STEPS[step_num]
            step_names.append(f'''{step['name']}''')
            if step_num == 1:
                expansion_tips.append('주인공의 일상 세부 묘사 추가 (환경, 습관, 감정 상태)')
                continue
            if step_num == 2:
                expansion_tips.append('결핍이나 욕구가 생기는 과정을 더 구체적으로 묘사')
                continue
            if step_num == 3:
                expansion_tips.append('결정을 내리는 심리 묘사, 갈등하는 내면 추가')
                continue
            if step_num == 4:
                expansion_tips.append('시련과 고군분투를 생생하게 묘사, 긴장감 추가')
                continue
            if step_num == 5:
                expansion_tips.append('발견의 순간을 극적으로 강조, 감정적 정점 묘사')
                continue
            if step_num == 6:
                expansion_tips.append('대가를 치르는 고통과 상실감을 깊이 있게 묘사')
                continue
            if step_num == 7:
                expansion_tips.append('복귀 과정의 심경 변화, 성찰하는 내면 묘사')
                continue
            if step_num == 8:
                expansion_tips.append('변화된 모습을 구체적으로, 여운 있게 마무리')
            lines.append(f'''**챕터 {chapter_num}** ({' + '.join(step_names)} 단계)''')
            for tip in expansion_tips:
                lines.append(f'''  - {tip}''')
                for step_num in steps:
                    if step_num in variation.get('step_emphasis', { }):
                        emphasis = variation['step_emphasis'][step_num]
                        lines.append(f'''  - [장르 강조] {emphasis}''')
                    lines.append('')
                    lines.extend([
                        '## 확장 시 스토리 서클 핵심 원칙',
                        '',
                        '1. **기존 구조 유지**: 스토리 서클 단계 순서를 절대 바꾸지 마세요',
                        '2. **단계 특성 강화**: 각 단계의 핵심 요소(위 팁)를 세부 묘사로 강화하세요',
                        '3. **감정 곡선 유지**: 확장해도 감정 흐름이 자연스럽게 유지되어야 합니다',
                        f'''4. **장르 감정선**: {variation['emotional_arc']}''',
                        ''])
                    return '\n'.join(lines)
