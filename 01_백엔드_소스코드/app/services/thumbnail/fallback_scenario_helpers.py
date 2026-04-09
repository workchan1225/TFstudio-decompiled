# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: fallback_scenario_helpers.pyc (Python 3.11)

'''
Fallback Scenario Helpers
Gemini API 실패 시 대본 기반 고품질 폴백 시나리오 생성 헬퍼

핵심 개선:
- 대본 심층 분석 (갈등/감정/숫자/대화 추출)
- 패턴 기반 훅 생성 (20+종 템플릿)
- 3가지 관점별 situation 생성 (clean_title 접두어 제거)
'''
import re
import logging
from typing import List, Dict, Any, Optional
logger = logging.getLogger(__name__)
SENTENCE_SPLIT_PATTERN = re.compile('(?<!\\d)[.?!。]\\s*(?!\\d)|\\n+')
GREETING_SKIP_PATTERNS = [
    '여러분',
    '안녕하세요',
    '오늘은',
    '지금부터',
    '반갑습니다',
    '구독',
    '좋아요',
    '알림',
    '채널',
    '영상을 시작']
CHAPTER_PATTERN = re.compile('^\\s*[\\[【\\(]\\s*(챕터|chapter|파트|part)\\s*\\d', re.IGNORECASE)
CONFLICT_KEYWORDS = [
    '하지만',
    '그런데',
    '그러나',
    '에도 불구하고',
    '반면',
    '오히려',
    '충돌',
    '갈등',
    '위기',
    '위험',
    '폭발',
    '붕괴',
    '파괴',
    '무너',
    '사라',
    '잃',
    '망',
    '죽',
    '살해',
    '배신',
    '사기',
    '거짓']
EMOTION_KEYWORDS = [
    '눈물',
    '울',
    '슬픔',
    '고통',
    '절망',
    '두려',
    '공포',
    '무서',
    '분노',
    '화가',
    '억울',
    '충격',
    '놀라',
    '경악',
    '소름',
    '감동',
    '희망',
    '기쁨',
    '행복']
TRANSITION_PATTERNS = re.compile('(?:하지만|그런데|그러나|그래서|결국|알고\\s*보니|사실은|놀랍게도|충격적으로)')
NUMBER_PATTERN = re.compile('\\d+[조억만천백]\\s*[원명개]?|\\d[\\d,]*%|\\d[\\d,]+\\s*(?:원|명|개|건|채|톤|kg|km)|\\d+[.]\\d+\\s*(?:배|도|%)')
AGE_RANK_PATTERN = re.compile('^\\d+대$|^\\d+등$|^\\d+위$|^\\d+번째$')
DIALOGUE_PATTERN = re.compile('["""\\\']([^"""\\\']{4,40})["""\\\']')
HOOK_PATTERNS_SHORT: Dict[(str, List[str])] = {
    'curiosity': [
        '{keyword} 숨겨진 비밀',
        '아무도 모르는 {keyword}',
        '{keyword}의 진짜 정체',
        '이걸 왜 숨겼나?!',
        '{keyword} 알고 보니...'],
    'emotional': [
        '{person} 무너졌다',
        '차마 말 못한 비밀',
        '{person} 오열했다',
        '마지막이었다...',
        '{keyword}에 눈물 쏟았다'],
    'shocking': [
        '{number} 사라졌다',
        '이거 실화입니다',
        '전부 거짓이었다',
        '{keyword} 충격 반전',
        '{number} 날아갔다'],
    'question': [
        '대체 왜 그랬을까?',
        '이래도 괜찮다고?!',
        '{person}한테 무슨 일이',
        '누가 이렇게 만들었나',
        '{keyword} 어떻게?!'],
    'urgency': [
        '경고 무시한 결과',
        '{keyword} 시작됐다',
        '진작 알았으면...',
        '지금 당장 확인해',
        '이미 늦었다'],
    'reversal': [
        '알고 보니 {keyword}',
        '안전한 줄 알았는데',
        '결국 이렇게 됐다',
        '{keyword}인 줄 알았더니',
        '소름 돋는 반전'] }
HOOK_PATTERNS_DESCRIPTIVE: Dict[(str, List[str])] = {
    'curiosity': [
        '가장 믿었던 {person}이... {keyword} 숨기고 있었다',
        '{keyword}의 진실이 밝혀졌다... 전부 뒤집혔다',
        '아무도 몰랐던 {keyword}... 진짜 이유가 따로 있었다',
        '{person}만 알고 있던 비밀... 결국 들통났다',
        '10년간 숨겨왔던 {keyword}... 드디어 드러났다'],
    'emotional': [
        '{person}이 떠난 줄 알았는데... 끝까지 지키고 있었다',
        '세상에서 가장 믿었던 {person}이... 날 버리고 떠났다',
        '{person}이 마지막으로 남긴 말... 눈물이 멈추지 않았다',
        '평생 숨겨온 비밀을 {person}이 털어놓았다... 가족 모두 울었다',
        '{keyword} 앞에서 {person}이 무릎 꿇었다... 차마 볼 수 없었다'],
    'shocking': [
        '{number}이 하루 만에 증발했다... 아무도 몰랐다',
        '{keyword} 무시하다 {number} 날렸다... 되돌릴 수 없다',
        '{person} 무시하다 전부 날려먹었다... 실화입니다',
        '감히 {keyword}?! {person} 결국 이렇게 당했다',
        '매일 하던 {keyword}이 이렇게 위험했다... 소름 돋는다'],
    'question': [
        '{person}한테 무슨 일이 있었던 거야... 아무도 말 안 했다',
        '왜 아무도 {keyword}에 대해 말 안 했나... 이유가 있었다',
        '{keyword} 대체 왜 이런 일이... 진짜 원인을 추적했다',
        '다들 알면서 왜 숨겼을까... {keyword}의 불편한 진실',
        '{person}이 왜 그랬는지... 이유를 듣고 할 말을 잃었다'],
    'urgency': [
        '{keyword} 지금 시작됐다... 모르면 큰일 난다',
        '전문가들이 경고한 {keyword}... 현실이 됐다',
        '{keyword} 바꾸는 유일한 방법... 진작 알았으면 좋았을 텐데',
        '지금 당장 {keyword} 확인해... 시간이 없다',
        '이미 늦었다... {keyword} 되돌릴 수 없는 상황이 됐다'],
    'reversal': [
        '떠난 줄 알았던 {person}이... 다시 나타났다',
        '{keyword}인 줄 알았는데... 정반대였다',
        '결국 {keyword} 이렇게 끝났다... 아무도 예상 못한 결말',
        '{person}이 마지막에 한 선택... 모든 걸 뒤집었다',
        '안전하다고 믿었던 {keyword}... 반전이 시작됐다'] }
DOMAIN_PATTERN_WEIGHTS: Dict[(str, Dict[(str, float)])] = {
    '경제': {
        'shocking': 2,
        'urgency': 1.5,
        'curiosity': 1.3 },
    '건강': {
        'emotional': 2,
        'shocking': 1.5,
        'question': 1.3 },
    '범죄': {
        'shocking': 2,
        'curiosity': 1.5,
        'reversal': 1.3 },
    '가족': {
        'emotional': 2,
        'question': 1.5,
        'reversal': 1.3 },
    '재난': {
        'urgency': 2,
        'shocking': 1.5,
        'emotional': 1.3 },
    '정치': {
        'shocking': 2,
        'curiosity': 1.5,
        'urgency': 1.3 },
    '기술': {
        'curiosity': 2,
        'shocking': 1.5,
        'urgency': 1.3 },
    '직장': {
        'emotional': 2,
        'shocking': 1.5,
        'question': 1.3 },
    '교육': {
        'question': 2,
        'emotional': 1.5,
        'shocking': 1.3 },
    '역사': {
        'curiosity': 2,
        'reversal': 1.5,
        'shocking': 1.3 } }
SCENARIO_CATEGORY_PREFERENCE = [
    [
        'curiosity',
        'shocking'],
    [
        'emotional',
        'question'],
    [
        'urgency',
        'reversal']]

def extract_script_insights(script_content = None, clean_title = None):
    '''대본에서 시나리오 생성에 유용한 구체적 정보를 추출

    Returns:
        key_sentences: 갈등/감정 키워드가 많은 상위 5문장
        key_numbers: 숫자/통계 추출
        conflict_phrases: 전환어 주변 문장
        dialogue_lines: 대화문 추출
        topic_keywords: 빈도 기반 주요 명사
    '''
    if not script_content:
        return _empty_insights()
    sentences = None(script_content)
    filtered = _filter_noise_sentences(sentences)
    if not filtered:
        filtered = sentences[:20] if sentences else []
    scored = _score_sentences(filtered)
    scored.sort(key = (lambda x: x[1]), reverse = True)
    key_sentences = scored[:5]()
    key_numbers = _extract_numbers(script_content)
    conflict_phrases = _extract_conflict_phrases(filtered)
    dialogue_lines = _extract_dialogues(script_content)
    topic_keywords = _extract_topic_keywords(script_content, clean_title)
    return {
        'key_sentences': key_sentences,
        'key_numbers': key_numbers,
        'conflict_phrases': conflict_phrases,
        'dialogue_lines': dialogue_lines,
        'topic_keywords': topic_keywords }


def generate_pattern_hooks(insights = None, domain = None, count = None, hook_style = (9, 'descriptive')):
    """대본 내용 기반으로 다양한 패턴의 훅 텍스트 생성

    Args:
        hook_style: 'short' (단답형 6-14자) 또는 'descriptive' (설명형 15-35자)

    시나리오별 다른 카테고리 훅 배정:
    - 위치 0,3,6: curiosity/shocking 카테고리 우선
    - 위치 1,4,7: emotional/question 카테고리 우선
    - 위치 2,5,8: urgency/reversal 카테고리 우선
    """
    pass
# WARNING: Decompyle incomplete


def build_angle_situations(insights = None, topic_context = None, clean_title = None):
    '''3가지 다른 관점의 시나리오 situation 생성

    관점:
    1. 갈등 관점 (Conflict): 무슨 일이 벌어졌는가
    2. 인물 관점 (Personal): 누가 어떤 영향을 받았는가
    3. 결과 관점 (Consequence): 어떤 결과/반전이 있는가
    '''
    domain = topic_context.get('domain', '일반')
    main_person = topic_context.get('main_person', '주인공')
    key_sentences = insights.get('key_sentences', [])
    conflict_phrases = insights.get('conflict_phrases', [])
    dialogue_lines = insights.get('dialogue_lines', [])
    key_numbers = insights.get('key_numbers', [])
    topic_keywords = insights.get('topic_keywords', [])
    primary_kw = topic_keywords[0] if topic_keywords else clean_title[:10]
    secondary_kw = topic_keywords[1] if len(topic_keywords) > 1 else ''
    angles = []
    conflict_situation = _build_conflict_situation(conflict_phrases, key_sentences, domain, primary_kw, clean_title, key_numbers)
    if conflict_phrases:
        pass
    elif key_sentences:
        pass
    
    conflict_quote = ''
    angles.append({
        'situation': conflict_situation,
        'emotion': _pick_emotion_for_angle('conflict', domain),
        'scene_type': 'conflict',
        'key_person': main_person,
        'composition_hint': '인물 클로즈업 + 텍스트 상단',
        'script_quote': _truncate(conflict_quote, 200),
        'scene_ko': f'''{primary_kw} - 핵심 갈등의 순간''' })
    personal_situation = _build_personal_situation(dialogue_lines, key_sentences, main_person, domain, primary_kw)
    if dialogue_lines:
        pass
    elif len(key_sentences) > 1:
        pass
    
    personal_quote = ''
    angles.append({
        'situation': personal_situation,
        'emotion': _pick_emotion_for_angle('personal', domain),
        'scene_type': 'discovery',
        'key_person': main_person,
        'composition_hint': '얼굴 클로즈업 + 어두운 배경',
        'script_quote': _truncate(personal_quote, 200),
        'scene_ko': f'''{main_person}의 결정적 순간''' })
    consequence_situation = _build_consequence_situation(key_numbers, key_sentences, domain, primary_kw, secondary_kw)
    consequence_quote = ''
    for s in key_sentences:
        if NUMBER_PATTERN.search(s):
            consequence_quote = s
            key_sentences[1]
        
        if consequence_quote and len(key_sentences) > 2:
            consequence_quote = key_sentences[2]
    angles.append({
        'situation': consequence_situation,
        'emotion': _pick_emotion_for_angle('consequence', domain),
        'scene_type': 'crisis',
        'key_person': topic_context.get('secondary_person', '관련 인물'),
        'composition_hint': '중앙 인물 + 텍스트 하단',
        'script_quote': _truncate(consequence_quote, 200),
        'scene_ko': f'''{primary_kw} - 반전의 결과''' })
    return angles


def select_scenario_hooks(hooks = None, scenario_index = None):
    '''시나리오 인덱스에 맞는 훅 선택'''
    if not hooks:
        return '이거 진짜 실화야?!'
    idx = None(scenario_index, len(hooks) - 1)
    return hooks[idx]


def _empty_insights():
    return {
        'key_sentences': [],
        'key_numbers': [],
        'conflict_phrases': [],
        'dialogue_lines': [],
        'topic_keywords': [] }


def _split_sentences(text = None):
    '''텍스트를 문장 단위로 분리'''
    raw_parts = SENTENCE_SPLIT_PATTERN.split(text)
    sentences = []
    for part in raw_parts:
        part = part.strip()
        if len(part) >= 8:
            sentences.append(part)
        return sentences


def _filter_noise_sentences(sentences = None):
    '''인사말, 챕터 제목 등 노이즈 문장 필터링'''
    pass
# WARNING: Decompyle incomplete


def _score_sentences(sentences = None):
    '''각 문장에 점수 부여 (갈등어+2, 감정어+2, 숫자+1, 느낌표/물음표+1)'''
    scored = []
    for s in sentences:
        score = 0
        lowered = s.lower()
        for kw in CONFLICT_KEYWORDS:
            if kw in lowered:
                score += 2
            for kw in EMOTION_KEYWORDS:
                if kw in lowered:
                    score += 2
                if NUMBER_PATTERN.search(s):
                    score += 1
        if DIALOGUE_PATTERN.search(s):
            score += 1
        if '!' in s or '?' in s:
            score += 1
        scored.append((s, score))
        return scored


def _extract_numbers(text = None):
    '''대본에서 숫자/통계 추출 (금액/규모 우선)'''
    matches = NUMBER_PATTERN.findall(text)
    seen = set()
    monetary = []
    others = []
    monetary_markers = re.compile('[조억만천백]\\s*원|원|명|건|채|%')
    for m in matches:
        m = m.strip()
        if m in seen and len(m) < 2 or AGE_RANK_PATTERN.match(m):
            continue
        seen.add(m)
        if monetary_markers.search(m):
            monetary.append(m)
            continue
        others.append(m)
        return monetary + others[:6]


def _extract_conflict_phrases(sentences = None):
    """전환어('하지만', '그런데' 등) 주변 문장 추출"""
    result = []
    seen = set()
    for i, s in enumerate(sentences):
        if TRANSITION_PATTERNS.search(s):
            if s not in seen:
                seen.add(s)
                result.append(s)
            if i + 1 < len(sentences) and sentences[i + 1] not in seen:
                seen.add(sentences[i + 1])
                result.append(sentences[i + 1])
        if len(result) >= 6:
            pass
        
        return result


def _extract_dialogues(text = None):
    '''따옴표로 감싼 대화문 추출'''
    matches = DIALOGUE_PATTERN.findall(text)
    seen = set()
    result = []
    for m in matches:
        m = m.strip()
        if m not in seen:
            if  <= 4, len(m) or 4, len(m) <= 40:
                pass
            
        else:
            seen.add(m)
            result.append(m)
        if len(result) >= 5:
            pass
        
        return result


def _extract_topic_keywords(script_content = None, clean_title = None):
    '''빈도 기반 주요 키워드 추출 (kiwipiepy 사용 가능 시 활용)'''
    noise_nouns = {
        '영상',
        '오늘',
        '지금',
        '구독',
        '소개',
        '시작',
        '안녕',
        '알림',
        '위협',
        '이번',
        '채널',
        '챕터',
        '파트',
        '여러분',
        '이야기',
        '좋아요'}
    
    try:
        extract_nouns = extract_nouns
        KIWI_AVAILABLE = KIWI_AVAILABLE
        import app.utils.korean_pos_analyzer
        if KIWI_AVAILABLE:
            combined = clean_title + ' ' + script_content[:3000]
            nouns = extract_nouns(combined)
            freq = { }
            for n in nouns:
                if len(n) >= 2 and n not in noise_nouns:
                    freq[n] = freq.get(n, 0) + 1
                sorted_nouns = sorted(freq.items(), key = (lambda x: x[1]), reverse = True)
                return sorted_nouns[:8]()
            except Exception:
                pass
            words = re.findall('[가-힣]{2,6}', script_content[:3000])
            freq = { }
            stopwords = {
                '어떤',
                '최근',
                '그것은',
                '그것을',
                '그것이',
                '그동안',
                '그래도',
                '그래서',
                '그리고',
                '되었다',
                '때문에',
                '무엇을',
                '사실이',
                '없었다',
                '여기서',
                '우리는',
                '이것은',
                '이것을',
                '이것이',
                '이렇게',
                '입니다',
                '있었다',
                '저것은',
                '한다는',
                '합니다',
                '것입니다',
                '다가오는',
                '있습니다',
                '했습니다',
                '소개',
                '시작',
                '안녕',
                '위협',
                '이번',
                '챕터',
                '파트',
                '그런데',
                '여러분',
                '오늘은',
                '이야기',
                '하지만',
                '지금부터',
                '안녕하세요'}
            title_words = set(re.findall('[가-힣]{2,6}', clean_title))
            for w in words:
                if w not in stopwords:
                    freq[w] = freq.get(w, 0) + 1
                for tw in title_words:
                    if tw in freq:
                        freq[tw] = freq[tw] + 3
                    sorted_words = sorted(freq.items(), key = (lambda x: x[1]), reverse = True)
                    result = []
                    particle_re = re.compile('(?:의|은|는|이|가|을|를|에|로|와|과|도)$')
                    for w, _ in sorted_words:
                        cleaned = particle_re.sub('', w)
                        if len(cleaned) >= 2 and (lambda .0: [ r for r in .0 ]) not in result():
                            result.append(cleaned)
                        if len(result) >= 8:
                            cleaned
                        
                        return result



def _extract_person_candidates(insights = None, domain = None):
    '''대본에서 인물 후보 추출'''
    dialogue_lines = insights.get('dialogue_lines', [])
    keywords = insights.get('topic_keywords', [])
    person_words = []
    person_markers = [
        '아버지',
        '어머니',
        '엄마',
        '아빠',
        '아들',
        '딸',
        '형',
        '누나',
        '동생',
        '할아버지',
        '할머니',
        '남편',
        '아내',
        '사장',
        '직원',
        '의사',
        '환자',
        '선생',
        '학생',
        '경찰',
        '피해자',
        '가해자',
        '주민',
        '시민',
        '전문가']
    for kw in keywords:
        if kw in person_markers:
            person_words.append(kw)
        domain_persons = {
            '가족': [
                '아버지',
                '어머니',
                '아들'],
            '건강': [
                '환자',
                '의사'],
            '범죄': [
                '피해자',
                '범인'],
            '경제': [
                '투자자',
                '전문가'],
            '직장': [
                '직원',
                '사장'],
            '교육': [
                '학생',
                '선생'],
            '재난': [
                '주민',
                '생존자'] }
        if not person_words:
            person_words = domain_persons.get(domain, [
                '그 사람'])
    return person_words[:4]


def _fill_pattern(pattern = None, kw_candidates = None, num_candidates = None, person_candidates = (None, None), dialogue_candidates = ('pattern', str, 'kw_candidates', List[str], 'num_candidates', List[str], 'person_candidates', Optional[List[str]], 'dialogue_candidates', Optional[List[str]], 'return', List[str])):
    '''패턴 템플릿에 keyword/number/person/dialogue 대입하여 훅 후보 생성'''
    pass
# WARNING: Decompyle incomplete


def _build_conflict_situation(conflict_phrases, key_sentences = None, domain = None, primary_kw = None, clean_title = (None,), key_numbers = ('conflict_phrases', List[str], 'key_sentences', List[str], 'domain', str, 'primary_kw', str, 'clean_title', str, 'key_numbers', Optional[List[str]], 'return', str)):
    '''갈등 관점 situation 생성 — 대본 문장 가공하여 드라마틱하게'''
    if conflict_phrases and len(conflict_phrases) >= 2:
        base = conflict_phrases[0]
        follow = conflict_phrases[1]
        if len(base) < 25 and len(follow) < 40:
            combined = f'''{base} — {follow}'''
            if len(combined) > 65:
                combined = combined[:62] + '...'
            return combined
        if None(follow) > len(base) and len(follow) <= 60:
            return follow
        if None(base) > 60:
            base = base[:57] + '...'
        return base
    if None:
        base = conflict_phrases[0]
        if key_numbers and len(base) < 35:
            base = f'''{base} — {key_numbers[0]}의 피해가 시작됐다'''
            if len(base) > 65:
                base = base[:62] + '...'
            return base
        if None(base) > 60:
            base = base[:57] + '...'
        return base
    domain_conflict_templates = {
        '경제': f'''{None}이(가) 한순간에 증발했다 — 전문가도 예측 못한 결과''',
        '건강': f'''{primary_kw} 진단 결과가 나왔다 — 아무도 예상 못한 수치''',
        '범죄': f'''{primary_kw}의 증거가 드러났다 — 모든 것이 뒤집히는 순간''',
        '가족': f'''{primary_kw} 비밀이 폭로됐다 — 가족 관계가 무너지는 순간''',
        '재난': f'''{primary_kw} 경보가 현실이 됐다 — 전문가의 경고가 맞았다''',
        '정치': f'''{primary_kw} 기밀이 유출됐다 — 파장이 시작되는 순간''',
        '기술': f'''{primary_kw}이(가) 통제를 벗어났다 — 인간의 예상을 뒤엎는 순간''',
        '직장': f'''{primary_kw} 통보를 받았다 — 예고 없이 닥친 현실''',
        '교육': f'''{primary_kw} 결과가 나왔다 — 인생을 바꾸는 순간''' }
    if domain in domain_conflict_templates:
        return domain_conflict_templates[domain]
    if None:
        base = key_sentences[0]
        if len(base) > 60:
            base = base[:57] + '...'
        return base
    return f'''{None} — 핵심 갈등이 폭발하는 순간'''


def _build_personal_situation(dialogue_lines, key_sentences = None, main_person = None, domain = None, primary_kw = ('dialogue_lines', List[str], 'key_sentences', List[str], 'main_person', str, 'domain', str, 'primary_kw', str, 'return', str)):
    '''인물 관점 situation 생성'''
    pass
# WARNING: Decompyle incomplete


def _build_consequence_situation(key_numbers, key_sentences = None, domain = None, primary_kw = None, secondary_kw = ('key_numbers', List[str], 'key_sentences', List[str], 'domain', str, 'primary_kw', str, 'secondary_kw', str, 'return', str)):
    '''결과 관점 situation 생성'''
    if key_numbers:
        num = key_numbers[0]
        return f'''피해 규모 {num} — 숨겨졌던 데이터가 공개되자 모든 게 뒤집혔다'''
    domain_consequence_templates = {
        '경제': f'''{None} 이후 모든 것이 바뀌었다 — 되돌릴 수 없는 결과''',
        '건강': f'''{primary_kw} 치료 후 예상치 못한 결과가 나왔다''',
        '범죄': f'''{primary_kw} 사건의 진범이 밝혀지자 모든 게 뒤집혔다''',
        '가족': f'''{primary_kw} 이후 가족은 다시 예전으로 돌아갈 수 없었다''',
        '재난': f'''{primary_kw} 피해가 집계되자 전문가들도 입을 다물지 못했다''',
        '정치': f'''{primary_kw} 결정의 파장이 걷잡을 수 없이 커졌다''',
        '기술': f'''{primary_kw} 결과가 공개되자 세상이 뒤집혔다''',
        '직장': f'''{primary_kw} 이후 회사는 돌이킬 수 없는 위기에 빠졌다''',
        '교육': f'''{primary_kw} 결과가 공개되자 학부모들이 분노했다''' }
    if domain in domain_consequence_templates:
        return domain_consequence_templates[domain]
    if None(key_sentences) > 2:
        base = key_sentences[2]
        if len(base) > 60:
            base = base[:57] + '...'
        return base
    kw_part = f'''{secondary_kw}과(와) {primary_kw}''' if None else primary_kw
    return f'''{kw_part} — 결국 이렇게 끝났다'''


def _pick_emotion_for_angle(angle = None, domain = None):
    '''관점과 도메인에 맞는 감정 선택'''
    angle_emotions = {
        'conflict': {
            '경제': '긴장',
            '건강': '공포',
            '범죄': '긴장',
            '가족': '분노',
            '재난': '공포',
            '정치': '충격' },
        'personal': {
            '경제': '절망',
            '건강': '슬픔',
            '범죄': '충격',
            '가족': '슬픔',
            '재난': '슬픔',
            '정치': '분노' },
        'consequence': {
            '경제': '충격',
            '건강': '놀라움',
            '범죄': '경악',
            '가족': '감동',
            '재난': '충격',
            '정치': '경악' } }
    emotions = angle_emotions.get(angle, { })
    return emotions.get(domain, {
        'conflict': '긴장',
        'personal': '슬픔',
        'consequence': '충격' }.get(angle, '긴장'))


def _truncate(text = None, max_len = None):
    '''텍스트 길이 제한'''
    if not text:
        return ''
    if None(text) <= max_len:
        return text
    return None[:max_len - 3] + '...'
