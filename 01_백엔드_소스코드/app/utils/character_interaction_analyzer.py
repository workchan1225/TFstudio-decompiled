# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: character_interaction_analyzer.pyc (Python 3.11)

'''
Character Interaction Analyzer - 캐릭터 상호작용 분석기

2인 이상 등장 장면에서 캐릭터 간 관계/상호작용 분석:
- 상호작용 유형: 대면, 대치, 포옹, 도주 등
- 위치 관계: 가까움/멀음, 마주봄/같은 방향
- 관계 역학: 우위/열위, 친밀/적대
- v1.7.2: 시선 대상(gaze target) 추출 추가
'''
import hashlib
import re
from typing import Dict, List, Optional, TypedDict, Tuple

def InteractionAnalysisResult():
    '''InteractionAnalysisResult'''
    gaze_instruction: Optional[str] = '상호작용 분석 결과'

InteractionAnalysisResult = <NODE:27>(InteractionAnalysisResult, 'InteractionAnalysisResult', TypedDict, total = False)
INTERACTION_KEYWORDS: Dict[(str, Dict)] = {
    'confrontation': {
        'keywords_ko': [
            '대치',
            '노려보',
            '으르렁',
            '맞서',
            '적대',
            '싸움',
            '갈등',
            '쏘아보',
            '마주섰다',
            '대립',
            '충돌',
            '위협',
            '노려봤다',
            '험악',
            '싸우'],
        'keywords_en': [
            'confront',
            'face off',
            'standoff',
            'hostile',
            'stare down',
            'clash',
            'threaten',
            'oppose',
            'fight'],
        'positioning': 'facing each other tensely with invaded personal space, one pressing forward while the other holds ground or retreats',
        'prompt': 'tense confrontation with invaded personal space, aggressor leaning nose-to-nose into opponent space, asymmetric reaction: one explosive with clenched fists while the other freezes cold or retreats behind furniture barrier',
        'distance': 'medium' },
    'embrace': {
        'keywords_ko': [
            '포옹',
            '안았다',
            '껴안',
            '안아주',
            '끌어안',
            '품에',
            '와락',
            '부둥켜',
            '껴안았다',
            '감싸안',
            '안겨'],
        'keywords_en': [
            'hug',
            'embrace',
            'hold',
            'arms around',
            'wrapped',
            'cuddle'],
        'positioning': 'holding each other tightly with full body contact, one person initiating while other receives',
        'prompt': 'tight emotional embrace with asymmetric body language, initiator wrapping arms around tightly while receiver melts into hug or stands stiff with shock, visible emotional weight in shoulder tension and head position',
        'distance': 'very close' },
    'conversation': {
        'keywords_ko': [
            '대화',
            '말했다',
            '물었다',
            '대답',
            '얘기',
            '이야기',
            '속삭',
            '말을',
            '대화를'],
        'keywords_en': [
            'talk',
            'said',
            'asked',
            'conversation',
            'discuss',
            'whisper',
            'chat'],
        'positioning': 'facing each other with natural conversation distance, body angles slightly offset',
        'prompt': 'engaged conversation with prop-mediated interaction, one gesturing toward shared document or screen while the other reacts, unequal body language: active speaker leaning forward while listener crosses arms or fidgets with object',
        'distance': 'comfortable' },
    'chase': {
        'keywords_ko': [
            '쫓았다',
            '추격',
            '도망',
            '달렸다',
            '뒤따라',
            '쫓기',
            '도주',
            '추적',
            '뒤쫓',
            '달아났다',
            '도망쳤다'],
        'keywords_en': [
            'chase',
            'pursuit',
            'running after',
            'flee',
            'escape',
            'follow',
            'hunt'],
        'positioning': 'one behind the other in running motion',
        'prompt': 'chase scene, pursuer and pursued, running motion, dynamic movement',
        'distance': 'separated' },
    'protection': {
        'keywords_ko': [
            '가렸다',
            '막아서',
            '보호',
            '지켰다',
            '감싸',
            '방어',
            '지키려',
            '앞에 섰다',
            '가로막',
            '보호하려'],
        'keywords_en': [
            'protect',
            'shield',
            'guard',
            'defend',
            'cover',
            'stand in front'],
        'positioning': 'protector standing firmly between threat and protected person, arms spread wide as barrier',
        'prompt': 'protective stance with clear body barrier, protector facing threat with squared shoulders and spread arms, protected person cowering or clutching protector from behind with fear expression',
        'distance': 'close' },
    'romantic': {
        'keywords_ko': [
            '손을 잡',
            '마주보',
            '눈을 맞',
            '키스',
            '다가갔다',
            '손잡',
            '끌어당겼다',
            '입술',
            '이마',
            '뺨',
            '포옹하며',
            '사랑'],
        'keywords_en': [
            'holding hands',
            'gazing',
            'kiss',
            'intimate',
            'romantic',
            'love',
            'tender',
            'caress',
            'affection'],
        'positioning': 'facing each other intimately with loving gazes',
        'prompt': 'romantic gaze, intimate proximity, tender moment, loving expression',
        'distance': 'very close' },
    'separation': {
        'keywords_ko': [
            '떠났다',
            '돌아섰다',
            '이별',
            '멀어져',
            '등을 돌렸다',
            '걸어갔다',
            '떠나',
            '사라졌다',
            '떨어져'],
        'keywords_en': [
            'leaving',
            'turning away',
            'farewell',
            'walking away',
            'departure',
            'goodbye',
            'parting'],
        'positioning': 'one turning away with deliberate distance, the other reaching out or frozen in place',
        'prompt': 'emotional separation with asymmetric departure, leaver walking away with stiff back and clenched hands, remaining person reaching out with desperate expression or frozen mid-step in disbelief',
        'distance': 'increasing' },
    'helping': {
        'keywords_ko': [
            '도와',
            '부축',
            '일으켜',
            '손을 내밀',
            '잡아당겨',
            '끌어올려',
            '구해'],
        'keywords_en': [
            'help',
            'support',
            'lift',
            'reach out',
            'pull up',
            'rescue',
            'assist'],
        'positioning': 'one helping or supporting the other',
        'prompt': 'helping gesture, supportive pose, one assisting the other, reaching out',
        'distance': 'close' },
    'observing': {
        'keywords_ko': [
            '바라보',
            '지켜보',
            '관찰',
            '숨어서',
            '몰래',
            '훔쳐보'],
        'keywords_en': [
            'watching',
            'observing',
            'looking at',
            'spying',
            'secretly'],
        'positioning': 'one observing the other from a distance',
        'prompt': 'observing from distance, watchful gaze, separated positions',
        'distance': 'far' },
    'intimidation': {
        'keywords_ko': [
            '압박',
            '위압',
            '으름장',
            '으스댐',
            '내려다',
            '굴복',
            '눌려',
            '기죽'],
        'keywords_en': [
            'intimidate',
            'pressure',
            'dominate',
            'tower over',
            'overpower',
            'bully'],
        'positioning': 'dominant figure looming over the cowering other, height and angle difference maximized',
        'prompt': 'intimidation with extreme power asymmetry, dominant figure standing tall with aggressive downward gaze and expansive posture, subordinate shrinking with hunched shoulders and averted eyes, furniture or objects between them used as psychological barrier by the weaker party',
        'distance': 'close' } }
POSITIONING_KEYWORDS: Dict[(str, Dict)] = {
    'facing': {
        'keywords_ko': [
            '마주',
            '앞에',
            '바라보',
            '눈을 맞'],
        'keywords_en': [
            'facing',
            'in front of',
            'looking at',
            'eye contact'],
        'prompt': 'characters facing each other' },
    'side_by_side': {
        'keywords_ko': [
            '나란히',
            '옆에',
            '함께',
            '같이'],
        'keywords_en': [
            'side by side',
            'beside',
            'together',
            'next to'],
        'prompt': 'characters standing side by side' },
    'behind': {
        'keywords_ko': [
            '뒤에',
            '등 뒤',
            '따라',
            '뒤따라'],
        'keywords_en': [
            'behind',
            'following',
            'at the back',
            'trailing'],
        'prompt': 'one character positioned behind the other' },
    'above': {
        'keywords_ko': [
            '위에',
            '내려다',
            '올려다'],
        'keywords_en': [
            'above',
            'looking down',
            'over'],
        'prompt': 'one character positioned above, looking down' },
    'below': {
        'keywords_ko': [
            '아래',
            '바닥에',
            '무릎',
            '엎드려'],
        'keywords_en': [
            'below',
            'on the ground',
            'kneeling',
            'lying'],
        'prompt': 'one character positioned lower, looking up' } }
RELATIONSHIP_KEYWORDS: Dict[(str, Dict)] = {
    'dominant': {
        'keywords_ko': [
            '명령',
            '지시',
            '꾸짖',
            '호통',
            '위협',
            '다그'],
        'keywords_en': [
            'command',
            'order',
            'scold',
            'threaten',
            'demand'],
        'dynamic': 'dominant-submissive' },
    'submissive': {
        'keywords_ko': [
            '복종',
            '고개를 숙',
            '무릎',
            '사죄',
            '빌었다'],
        'keywords_en': [
            'obey',
            'bow',
            'kneel',
            'apologize',
            'beg'],
        'dynamic': 'submissive' },
    'protective': {
        'keywords_ko': [
            '보호',
            '지켜',
            '돌봐',
            '걱정',
            '안전'],
        'keywords_en': [
            'protect',
            'guard',
            'care',
            'worry',
            'safe'],
        'dynamic': 'protective' },
    'equal': {
        'keywords_ko': [
            '함께',
            '같이',
            '협력',
            '동료'],
        'keywords_en': [
            'together',
            'cooperate',
            'partner',
            'equal'],
        'dynamic': 'equal' } }
GAZE_PATTERNS_KO = [
    ('([가-힣A-Za-z]+)(?:를|을)\\s*(?:바라보|쳐다보|노려보|지켜보|보고|보며|본다|봤다|봅니다)', 'look_at'),
    ('([가-힣A-Za-z]+)에게\\s*(?:시선|눈길)', 'look_at'),
    ('([가-힣A-Za-z]+)(?:를|을)\\s*향(?:해|하여|한)', 'toward'),
    ('([가-힣A-Za-z]+)\\s*(?:앞에|곁에|옆에)\\s*(?:서서|앉아|모여)', 'near'),
    ('([가-힣A-Za-z]+)(?:이|가)\\s*(?:누워|쓰러져|넘어져|엎드려)', 'lying_subject')]
GAZE_PATTERNS_EN = [
    ('(?:look(?:ing)?|stare?|gaze?|watch(?:ing)?)\\s+(?:at|toward)\\s+(?:the\\s+)?([a-zA-Z\\s]+?)(?:\\.|,|$|\\s+(?:with|and|who))', 'look_at'),
    ('turn(?:s|ed|ing)?\\s+(?:to|toward)\\s+(?:the\\s+)?([a-zA-Z\\s]+?)(?:\\.|,|$)', 'toward'),
    ('facing\\s+(?:the\\s+)?([a-zA-Z\\s]+?)(?:\\.|,|$)', 'facing'),
    ('(?:gather|crowd|surround)(?:s|ed|ing)?\\s+(?:around|near)\\s+(?:the\\s+)?([a-zA-Z\\s]+?)(?:\\.|,|$)', 'around')]
INVALID_GAZE_TARGETS_KO = {
    '말',
    '눈빛',
    '마음',
    '말투',
    '모습',
    '상황',
    '시선',
    '장면',
    '타인',
    '표정',
    '행동',
    '넘어져',
    '넘어짐',
    '뒷모습',
    '사람들',
    '앞모습',
    '타다'}
INTERACTION_PROMPT_VARIANTS: Dict[(str, List[str])] = {
    'confrontation': [
        'tense confrontation, hostile stare, aggressive body language, facing off',
        'high-stakes standoff, rigid shoulders, sharp eye contact, verbal clash posture',
        'psychological face-off, defensive spacing, hard expressions, escalating tension',
        'conflict-driven exchange, forceful stance, pressured eye-line, adversarial energy'],
    'embrace': [
        'tight embrace, emotional hug, arms wrapped around, intimate proximity',
        'protective hold, close body contact, comforting posture, emotional closeness',
        'mutual embrace, softened shoulders, grounded connection, reassuring touch',
        'relief-filled hug, secure body contact, vulnerable closeness, gentle support'],
    'conversation': [
        'engaged conversation, eye contact, natural dialogue pose, attentive listening',
        'active dialogue exchange, responsive eye movement, turn-taking posture, grounded interaction',
        'focused verbal interaction, conversational rhythm, subtle hand emphasis, mutual attention',
        'natural discussion flow, dynamic listening cues, expressive but controlled dialogue posture'],
    'chase': [
        'chase scene, pursuer and pursued, running motion, dynamic movement',
        'high-urgency pursuit, distance compressing, directional movement tension, rapid momentum',
        'escape-and-pursuit dynamic, staggered spacing, breathless motion, kinetic framing',
        'desperate chase progression, evasive pathing, pressure from behind, unstable pace'],
    'protection': [
        'protective stance, shielding gesture, defensive positioning, guarding',
        'body-blocking protection, guarded eye-line, protective reach, defensive alignment',
        'cover-and-shield posture, alert protective focus, barrier-like positioning, protective urgency',
        'guardian dynamic, threat-facing orientation, immediate shielding movement, defense-first posture'],
    'romantic': [
        'romantic gaze, intimate proximity, tender moment, loving expression',
        'soft romantic tension, gentle eye contact, subtle closeness, affectionate body language',
        'intimate emotional connection, softened posture, warm expressions, tender interaction',
        'quiet romantic focus, close interpersonal distance, affectionate gestures, emotionally open stance'],
    'separation': [
        'emotional separation, one walking away, distance growing, farewell moment',
        'parting tension, diverging movement paths, unresolved emotion, widening distance',
        'farewell dynamic, backward glance and retreat, emotional disconnection, increasing gap',
        'turning-away moment, broken proximity, restrained sadness, gradual emotional distance'],
    'helping': [
        'helping gesture, supportive pose, one assisting the other, reaching out',
        'supportive intervention, stabilizing contact, cooperative posture, practical assistance',
        'care-focused assistance, one character guiding the other, protective support dynamics',
        'active aid interaction, grounded helping stance, reassuring support, coordinated movement'],
    'observing': [
        'observing from distance, watchful gaze, separated positions',
        'cautious observation, visual focus from afar, restrained movement, monitoring posture',
        'quiet surveillance dynamic, measured distance, intent gaze, low-profile stance',
        'attentive watching posture, detached spacing, silent evaluation, controlled body language'],
    'intimidation': [
        'intimidation with extreme power asymmetry, dominant figure standing tall with aggressive downward gaze and expansive posture, subordinate shrinking with hunched shoulders and averted eyes',
        'psychological dominance display, towering stance with hands on hips or leaning over desk, smaller figure pressed back against wall or furniture',
        'power imbalance confrontation, aggressor invading space from above, victim curling inward with defensive arm positioning',
        'threatening authority dynamic, dominant figure blocking exit path with wide stance, intimidated person clutching object for comfort with downcast eyes'] }

def _pick_prompt_variant(seed_text = None, variants = None):
    if not variants:
        return ''
    digest = None.sha256(seed_text.encode('utf-8')).hexdigest()
    index = int(digest[:8], 16) % len(variants)
    return variants[index]


def _build_interaction_prompt(interaction_type, narration, character_count = None, positioning = None, relationship_dynamic = None, default_prompt = ('interaction_type', str, 'narration', str, 'character_count', int, 'positioning', str, 'relationship_dynamic', str, 'default_prompt', str, 'return', str)):
    variants = INTERACTION_PROMPT_VARIANTS.get(interaction_type, [])
    if default_prompt:
        variants = variants + [
            default_prompt]
    base_prompt = _pick_prompt_variant(f'''{interaction_type}|{character_count}|{relationship_dynamic}|{narration}''', variants)
    dynamic_clause_map = {
        'dominant-submissive': 'clear power imbalance and psychological pressure',
        'submissive': 'hesitant and defensive body language',
        'protective': 'protective intent with shielding orientation',
        'equal': 'balanced stance and reciprocal awareness' }
    prompt_parts = [
        base_prompt,
        positioning,
        dynamic_clause_map.get(relationship_dynamic, ''),
        f'''{character_count} characters interacting''']
    return ', '.join(filter(None, prompt_parts))

INVALID_GAZE_TARGETS_EN = {
    'back',
    'gaze',
    'look',
    'scene',
    'action',
    'backside',
    'behavior',
    'expression'}
EXPLICIT_ROMANTIC_CUES_KO = ('키스', '입맞춤', '포옹', '껴안', '손을 잡', '연인', '사랑 고백', '입술')
EXPLICIT_ROMANTIC_CUES_EN = ('kiss', 'kissing', 'embrace', 'hugging', 'holding hands', 'lover', 'romantic date', 'love confession')

def _is_valid_gaze_target(target = None, lang = None):
    if not target:
        cleaned = ''.strip().lower()
        if not cleaned:
            return False
        if None(cleaned) <= 1:
            return False
        if None == 'ko':
            if cleaned in INVALID_GAZE_TARGETS_KO:
                return False
            if None.endswith(('하다', '되다', '타다', '보다', '오다', '가다', '서다', '앉다', '눕다', '있다')):
                return False
    if cleaned in INVALID_GAZE_TARGETS_EN:
        return False


def _match_target_to_candidates(target = None, candidates = None):
    if not target:
        normalized_target = ''.strip().lower()
        if not normalized_target:
            return None
        for candidate in None:
            if not candidate:
                normalized_candidate = ''.strip().lower()
                if not normalized_candidate:
                    continue
            if normalized_target == normalized_candidate and normalized_target in normalized_candidate or normalized_candidate in normalized_target:
                
                return None, candidate
            return None


def _has_explicit_romantic_intent(narration = None):
    pass
# WARNING: Decompyle incomplete


def extract_gaze_target(narration = None, candidate_targets = None):
    '''
    v1.7.2: 나레이션에서 시선 대상 추출

    여러 캐릭터가 한 대상을 바라보는 상황 감지:
    - "마을 사람들이 아이를 보고" → gaze_target: "아이/child"
    - "모두 그를 향해" → gaze_target: "그/him"

    Args:
        narration: 나레이션/장면 설명 텍스트

    Returns:
        (gaze_target, gaze_instruction) 튜플
        - gaze_target: 시선 대상 (예: "child", "아이")
        - gaze_instruction: 시선 방향 지시문

    Example:
        >>> extract_gaze_target("마을 사람들이 걱정의 표정으로 아이를 보고 있다")
        (\'아이\', \'ALL characters MUST look toward and face the 아이 (child)\')
    '''
    pass
# WARNING: Decompyle incomplete


def _match_keywords(text = None, keyword_data = None):
    '''
    키워드 매칭 점수 계산

    Args:
        text: 분석할 텍스트
        keyword_data: 키워드 데이터 딕셔너리

    Returns:
        매칭된 키워드 수
    '''
    if not text:
        return 0
    score = None
    text_lower = text.lower()
    for kw in keyword_data.get('keywords_ko', []):
        if kw in text:
            score += 2
        for kw in keyword_data.get('keywords_en', []):
            if kw in text_lower:
                score += 1
            return score


def analyze_character_interaction(narration = None, character_count = None, candidate_targets = None):
    '''
    캐릭터 간 상호작용 분석

    Args:
        narration: 나레이션 텍스트
        character_count: 장면 내 캐릭터 수

    Returns:
        InteractionAnalysisResult: 상호작용 분석 결과

    Example:
        >>> result = analyze_character_interaction("두 사람이 서로를 노려보며 대치했다", 2)
        >>> result[\'interaction_type\']
        \'confrontation\'
        >>> result[\'interaction_prompt\']
        \'tense confrontation, hostile stare, ... 2 characters interacting\'
    '''
    if character_count < 2:
        return InteractionAnalysisResult(interaction_type = 'solo', character_count = character_count, positioning = '', relationship_dynamic = '', interaction_prompt = '', confidence = 0)
    if not None:
        return InteractionAnalysisResult(interaction_type = 'conversation', character_count = character_count, positioning = 'characters facing each other', relationship_dynamic = 'equal', interaction_prompt = f'''engaged conversation, {character_count} characters interacting''', confidence = 0.3)
    interaction_type = None
    best_score = 0
    best_data = INTERACTION_KEYWORDS['conversation']
    interaction_scores = { }
    for int_type, int_data in INTERACTION_KEYWORDS.items():
        score = _match_keywords(narration, int_data)
        interaction_scores[int_type] = score
        if score > best_score:
            best_score = score
            interaction_type = int_type
            best_data = int_data
        positioning = best_data.get('positioning', 'facing each other')
        for pos_type, pos_data in POSITIONING_KEYWORDS.items():
            pos_score = _match_keywords(narration, pos_data)
            if pos_score > 0:
                positioning = pos_data['prompt']
            
            relationship_dynamic = 'equal'
            for rel_type, rel_data in RELATIONSHIP_KEYWORDS.items():
                rel_score = _match_keywords(narration, rel_data)
                if rel_score > 0:
                    relationship_dynamic = rel_data['dynamic']
                
                if not interaction_type == 'romantic' and _has_explicit_romantic_intent(narration):
                    protection_score = interaction_scores.get('protection', 0)
                    conversation_score = interaction_scores.get('conversation', 0)
                    if relationship_dynamic == 'protective' and protection_score > 0:
                        interaction_type = 'protection'
                        best_data = INTERACTION_KEYWORDS['protection']
                        best_score = protection_score
                        print('[CharacterInteraction] Romantic downgraded to protection (no explicit romantic cue)')
                    elif conversation_score > 0:
                        interaction_type = 'conversation'
                        best_data = INTERACTION_KEYWORDS['conversation']
                        best_score = conversation_score
                        print('[CharacterInteraction] Romantic downgraded to conversation (no explicit romantic cue)')
    (gaze_target, gaze_instruction) = extract_gaze_target(narration, candidate_targets = candidate_targets)
    interaction_prompt = _build_interaction_prompt(interaction_type = interaction_type, narration = narration, character_count = character_count, positioning = positioning, relationship_dynamic = relationship_dynamic, default_prompt = best_data.get('prompt', ''))
    if gaze_instruction:
        interaction_prompt = ', '.join([
            interaction_prompt,
            gaze_instruction])
    confidence = min(1, best_score / 6) if best_score > 0 else 0.3
    if gaze_target:
        confidence = min(1, confidence + 0.2)
    return InteractionAnalysisResult(interaction_type = interaction_type, character_count = character_count, positioning = positioning, relationship_dynamic = relationship_dynamic, interaction_prompt = interaction_prompt, confidence = round(confidence, 2), gaze_target = gaze_target, gaze_instruction = gaze_instruction)


def get_interaction_prompt(narration = None, character_count = None, candidate_targets = None, min_confidence = (None, 0.3)):
    '''
    상호작용 프롬프트만 간단히 반환하는 헬퍼 함수

    Args:
        narration: 나레이션 텍스트
        character_count: 캐릭터 수
        min_confidence: 최소 신뢰도 (기본값 0.3)

    Returns:
        상호작용 프롬프트 문자열 또는 None
    '''
    if character_count < 2:
        return None
    result = None(narration, character_count, candidate_targets = candidate_targets)
    prompt = result.get('interaction_prompt')
    if result.get('confidence', 0) >= min_confidence and prompt:
        return prompt


def assign_screen_positions(character_count = None, shot_type = None):
