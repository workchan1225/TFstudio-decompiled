# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: scene_context_analyzer.pyc (Python 3.11)

'''
장면 상황 분석 및 동적 의상 결정 유틸리티

장면 설명에서 상황/맥락을 분석하여 캐릭터에게 적절한 의상을 동적으로 결정합니다.
얼굴/외모는 일관성을 유지하되, 의상만 장면에 맞게 변경됩니다.
'''
from typing import Dict, Optional, Tuple
import re
SCENE_CONTEXT_KEYWORDS = {
    'battle': {
        'keywords_ko': [
            '전투',
            '싸움',
            '싸우',
            '무술',
            '공격',
            '방어',
            '전쟁',
            '격투',
            '결투',
            '난투',
            '칼을',
            '칼로',
            '검을',
            '검으로',
            '무기를',
            '무장',
            '교전',
            '충돌'],
        'keywords_en': [
            'fight',
            'battle',
            'combat',
            'sword',
            'weapon',
            'attack',
            'war',
            'martial',
            'duel',
            'clash'],
        'priority': 10 },
    'ceremony': {
        'keywords_ko': [
            '궁궐',
            '접견',
            '조회',
            '혼례',
            '결혼',
            '장례',
            '제사',
            '예식',
            '입궐',
            '왕',
            '대전'],
        'keywords_en': [
            'palace',
            'ceremony',
            'court',
            'wedding',
            'funeral',
            'ritual',
            'formal',
            'royal'],
        'priority': 9 },
    'sleep': {
        'keywords_ko': [
            '잠든',
            '잠들',
            '잠자',
            '수면',
            '침실',
            '침대',
            '기상',
            '눕다',
            '누운',
            '누워',
            '잠옷'],
        'keywords_en': [
            'sleeping',
            'asleep',
            'bedroom',
            'in bed',
            'lying on bed',
            'nightgown',
            'pajamas',
            'wake up'],
        'priority': 8 },
    'bath': {
        'keywords_ko': [
            '목욕',
            '씻',
            '수영',
            '온천',
            '욕실',
            '샤워',
            '목욕탕'],
        'keywords_en': [
            'bath',
            'swim',
            'wash',
            'hot spring',
            'pool',
            'shower'],
        'priority': 8 },
    'labor': {
        'keywords_ko': [
            '밭',
            '농사',
            '노동',
            '땔감',
            '물길',
            '빨래',
            '농장일'],
        'keywords_en': [
            'farm',
            'work',
            'field',
            'labor',
            'carry',
            'wood',
            'chore',
            'laundry'],
        'priority': 6 },
    'outdoor': {
        'keywords_ko': [
            '바다',
            '여행',
            '걷다',
            '걸어',
            '숲',
            '야외',
            '바깥',
            '거리',
            '마을',
            '공원',
            '등산'],
        'keywords_en': [
            'road',
            'mountain',
            'travel',
            'journey',
            'walk',
            'forest',
            'outdoor',
            'street',
            'village'],
        'priority': 5 },
    'meal': {
        'keywords_ko': [
            '식사',
            '밥',
            '먹',
            '음식',
            '술',
            '주막',
            '식탁',
            '요리',
            '저녁',
            '점심',
            '아침밥'],
        'keywords_en': [
            'meal',
            'eat',
            'food',
            'drink',
            'dinner',
            'lunch',
            'breakfast',
            'tavern',
            'restaurant'],
        'priority': 4 },
    'daily': {
        'keywords_ko': [
            '집에서',
            '거실',
            '실내',
            '앉아',
            '앉은',
            '대화',
            '이야기',
            '일상',
            '평소'],
        'keywords_en': [
            'home',
            'room',
            'sitting',
            'talk',
            'conversation',
            'daily',
            'usual'],
        'priority': 3 } }
TEMPORAL_PERIOD_KEYWORDS = {
    'flashback': {
        'keywords_ko': [
            '회상',
            '과거',
            '옛날',
            '그 시절',
            '추억',
            '젊은 시절',
            '어린 시절',
            '그 해',
            '그 날',
            '년 전',
            '세 전',
            '수십 년 전',
            '과거로',
            '되돌아',
            '회고',
            '옛 시절',
            '젊었을 때',
            '어렸을 때',
            '지난 날',
            '지난날',
            '옛 모습',
            '플래시백',
            '전쟁터',
            '전쟁 중',
            '참전'],
        'keywords_en': [
            'flashback',
            'past',
            'memory',
            'those days',
            'years ago',
            'young days',
            'childhood',
            'back then',
            'reminisce',
            'remember when',
            'recall',
            'looking back',
            'in the past',
            'wartime',
            'during the war',
            'veteran'],
        'priority': 10 },
    'present': {
        'keywords_ko': [
            '지금',
            '현재',
            '오늘',
            '요즘',
            '이제',
            '지금은',
            '지금의',
            '오늘날',
            '현시점'],
        'keywords_en': [
            'now',
            'present',
            'today',
            'currently',
            'nowadays',
            'modern day',
            'these days',
            'contemporary',
            'normal day',
            'everyday',
            'ordinary'],
        'priority': 5 } }

def _contains_english_keyword(text_lower = None, keyword = None):
    '''영문 키워드 단어 경계 매칭 (war/warm 같은 부분 매칭 오탐 방지).'''
    if not keyword:
        return False
    pattern = f'''{re.escape(keyword.lower())}(?![a-z])'''
    return bool(re.search(pattern, text_lower))

MODERN_OUTFITS = {
    'battle': {
        'male': 'tactical combat gear, protective vest',
        'female': 'tactical combat gear, protective vest',
        'default': 'combat-ready attire' },
    'ceremony': {
        'male': 'formal suit and tie, elegant dress shoes',
        'female': 'elegant formal dress, sophisticated jewelry',
        'default': 'formal ceremonial attire' },
    'sleep': {
        'male': 'comfortable pajamas, relaxed sleepwear',
        'female': 'comfortable nightgown or pajamas',
        'default': 'comfortable sleepwear' },
    'bath': {
        'male': 'towel wrapped, minimal clothing',
        'female': 'towel wrapped, minimal covering',
        'default': 'bathing attire' },
    'labor': {
        'male': 'work clothes, practical sturdy outfit',
        'female': 'work clothes, practical sturdy outfit',
        'default': 'practical work attire' },
    'outdoor': {
        'male': 'casual outdoor wear, comfortable walking shoes',
        'female': 'casual outdoor wear, comfortable walking shoes',
        'default': 'casual outdoor attire' },
    'meal': {
        'male': 'casual smart wear',
        'female': 'casual smart wear',
        'default': 'casual comfortable clothing' },
    'daily': {
        'male': 'casual everyday wear',
        'female': 'casual everyday wear',
        'default': 'casual comfortable clothing' },
    'default': {
        'male': 'appropriate clothing for the scene',
        'female': 'appropriate clothing for the scene',
        'default': 'appropriate attire' } }
TEMPORAL_OUTFIT_RULES = {
    'flashback': {
        'WAR_MILITARY': {
            'battle': {
                'male': 'young Korean soldier in Korean War era military uniform, M1 steel helmet, olive drab combat fatigues, canvas boots, period-accurate 1950s military gear',
                'female': 'young woman in 1950s wartime attire, simple practical clothing or nurse uniform' },
            'daily': {
                'male': 'young soldier in off-duty military attire, simple uniform shirt, 1950s style',
                'female': 'young woman in simple 1950s civilian dress, period-appropriate casual wear' },
            'default': {
                'male': 'young soldier in Korean War era military uniform, M1 helmet, olive drab fatigues',
                'female': 'young woman in 1950s wartime civilian or nurse attire' } },
        'default': {
            'battle': {
                'male': 'younger version in period-appropriate combat attire',
                'female': 'younger version in period-appropriate practical clothing' },
            'daily': {
                'male': 'younger version in vintage casual clothing, period-appropriate style',
                'female': 'younger version in vintage dress or casual clothing, period-appropriate style' },
            'default': {
                'male': 'younger version in period-appropriate casual clothing',
                'female': 'younger version in period-appropriate casual clothing' } } },
    'present': {
        'WAR_MILITARY': {
            'daily': {
                'male': 'elderly Korean man in comfortable modern casual clothes, cardigan or vest, reading glasses',
                'female': 'elderly Korean woman in comfortable modern casual clothes, soft colors' },
            'ceremony': {
                'male': 'elderly Korean man in formal suit with military veteran medals and ribbons',
                'female': 'elderly Korean woman in formal hanbok or elegant modern dress' },
            'default': {
                'male': 'elderly Korean man in comfortable modern casual clothes, warm cardigan',
                'female': 'elderly Korean woman in comfortable modern casual clothes' } },
        'default': {
            'daily': {
                'male': 'current age, modern everyday casual clothing',
                'female': 'current age, modern everyday casual clothing' },
            'default': {
                'male': 'current age, appropriate modern clothing',
                'female': 'current age, appropriate modern clothing' } } } }
JOSEON_OUTFITS = {
    'royal': {
        'battle': {
            'male': 'royal military armor with dragon emblem, golden helmet',
            'female': 'ceremonial protective hanbok' },
        'ceremony': {
            'male': 'gonryongpo (dragon robe), ikseonkwan cap, jade belt',
            'female': 'wonsam ceremonial robe, jokduri coronet' },
        'sleep': {
            'male': 'comfortable silk undergarments, inner robe',
            'female': 'comfortable silk undergarments, inner robe' },
        'daily': {
            'male': 'casual royal hanbok, comfortable dopo',
            'female': 'casual royal dangui, comfortable chima' },
        'outdoor': {
            'male': 'travel hanbok with light dopo',
            'female': 'travel hanbok with jangot covering' },
        'default': {
            'male': 'elegant royal hanbok',
            'female': 'elegant royal hanbok' } },
    'yangban': {
        'battle': {
            'male': 'mubok (martial attire), light armor',
            'female': 'protective hanbok' },
        'ceremony': {
            'male': 'gwanbok (official robe), samo hat',
            'female': 'formal dangui jacket, layered silk chima' },
        'sleep': {
            'male': 'jeoksam (undershirt), sokbaji (underpants)',
            'female': 'jeoksam, sokchima (underskirt)' },
        'daily': {
            'male': 'dopo (scholar coat), black gat hat',
            'female': 'jeogori-chima, simple binyeo' },
        'outdoor': {
            'male': 'durumagi coat, gat hat',
            'female': 'jangot (face cover), travel hanbok' },
        'labor': {
            'male': 'simple jeogori-baji, no gat',
            'female': 'simple jeogori-chima, tied hair' },
        'meal': {
            'male': 'comfortable dopo or durumagi',
            'female': 'comfortable jeogori-chima' },
        'default': {
            'male': 'dopo (scholar overcoat), black gat hat',
            'female': 'refined jeogori-chima, silver binyeo' } },
    'sangmin': {
        'battle': {
            'male': 'rough cotton fighting clothes',
            'female': 'simple protective hanbok' },
        'ceremony': {
            'male': 'best white hanbok, clean and neat',
            'female': 'best hanbok, clean and neat' },
        'sleep': {
            'male': 'simple jeoksam, sokbaji',
            'female': 'simple jeoksam, sokchima' },
        'daily': {
            'male': 'white baji-jeogori, cloth headband',
            'female': 'white jeogori-chima, simple tied hair' },
        'outdoor': {
            'male': 'white baji-jeogori, straw sandals',
            'female': 'white jeogori-chima, straw sandals' },
        'labor': {
            'male': 'worn work clothes, cotton baji-jeogori',
            'female': 'short working chima, simple jeogori' },
        'bath': {
            'male': 'minimal covering, cloth wrap',
            'female': 'minimal covering, cloth wrap' },
        'default': {
            'male': 'simple white baji-jeogori, no gat, cloth headband',
            'female': 'simple white jeogori-chima, hair simply tied' } },
    'cheonmin': {
        'battle': {
            'male': 'worn rough clothing',
            'female': 'worn rough clothing' },
        'default': {
            'male': 'worn coarse hemp clothing, patched fabric, barefoot',
            'female': 'worn simple jeogori-chima, patched, barefoot' } } }

def analyze_scene_context(scene_description = None):
    """
    장면 설명에서 상황/맥락을 분석

    Args:
        scene_description: 장면 설명 텍스트

    Returns:
        {
            'context_type': 'battle' | 'ceremony' | 'daily' | 'sleep' | 'outdoor' | 'labor' | 'meal' | 'bath' | 'default',
            'confidence': 0.0-1.0,
            'matched_keywords': list of matched keywords
        }
    """
    pass
# WARNING: Decompyle incomplete


def analyze_temporal_period(scene_description = None):
    """
    장면 설명에서 시간대(과거 회상/현재) 분석

    Args:
        scene_description: 장면 설명 텍스트

    Returns:
        {
            'temporal_period': 'flashback' | 'present' | 'default',
            'confidence': 0.0-1.0,
            'matched_keywords': list of matched keywords
        }
    """
    pass
# WARNING: Decompyle incomplete


def get_dynamic_outfit(scene_description = None, character = None, style_context = None, social_class = ('modern', None, None), genre = ('scene_description', str, 'character', Dict, 'style_context', str, 'social_class', Optional[str], 'genre', Optional[str], 'return', str)):
    """
    장면 상황, 시간대, 장르를 바탕으로 적절한 의상 프롬프트 생성

    Args:
        scene_description: 장면 설명
        character: 캐릭터 정보 dict
        style_context: 'modern', 'joseon', 'medieval' 등
        social_class: 조선시대인 경우 신분 ('royal', 'yangban', 'sangmin', 'cheonmin')
        genre: 프로젝트 장르 ('WAR_MILITARY', 'ROMANCE', 'ACTION' 등)

    Returns:
        의상 프롬프트 문자열
    """
    if not character.get('primaryOutfitEn'):
        pass
    if not character.get('primaryOutfit'):
        original_outfit = character.get('clothing')
        context = analyze_scene_context(scene_description)
        context_type = context['context_type']
        temporal = analyze_temporal_period(scene_description)
        temporal_period = temporal['temporal_period']
        gender = character.get('gender', 'unknown')
        if gender not in ('male', 'female'):
            gender = 'default'
    extreme_contexts = ('battle', 'sleep', 'bath')
    if style_context in ('modern', None, '') and original_outfit:
        if context_type not in extreme_contexts:
            print(f'''[SceneContextAnalyzer] Preserving original outfit for consistency: {original_outfit[:50]}...''')
            return original_outfit
        None(f'''[SceneContextAnalyzer] Extreme context \'{context_type}\' detected - allowing outfit change''')
    if style_context == 'joseon':
        print(f'''[SceneContextAnalyzer] Historical context \'joseon\' detected - applying Joseon costume (temporal={temporal_period} ignored)''')
    elif temporal_period != 'default' and temporal['confidence'] >= 0.3:
        outfit = _get_temporal_outfit(temporal_period, context_type, gender, genre)
        if outfit:
            print(f'''[SceneContextAnalyzer] scene=\'{scene_description[:50]}...\' -> temporal={temporal_period}, context={context_type}, genre={genre}, outfit=\'{outfit[:50]}...\'''')
            return outfit
        if None == 'joseon':
            if not social_class:
                detect_social_class = detect_social_class
                import joseon_costume_data
                char_description = ' '.join([
                    character.get('profile', ''),
                    character.get('appearance', ''),
                    character.get('englishDescription', ''),
                    character.get('name', '')])
                (social_class, _) = detect_social_class(char_description)
            class_outfits = JOSEON_OUTFITS.get(social_class, JOSEON_OUTFITS.get('sangmin', { }))
            context_outfits = class_outfits.get(context_type, class_outfits.get('default', { }))
            if isinstance(context_outfits, dict):
                outfit = context_outfits.get(gender, context_outfits.get('male', ''))
            else:
                outfit = str(context_outfits)
            if not outfit:
                default_outfits = class_outfits.get('default', { })
                outfit = default_outfits.get(gender, default_outfits.get('male', 'traditional hanbok'))
            else:
                context_outfits = MODERN_OUTFITS.get(context_type, MODERN_OUTFITS['default'])
                outfit = context_outfits.get(gender, context_outfits.get('default', 'appropriate clothing'))
    print(f'''[SceneContextAnalyzer] scene=\'{scene_description[:50]}...\' -> context={context_type}, outfit=\'{outfit[:50]}...\'''')
    return outfit


def _get_temporal_outfit(temporal_period = None, context_type = None, gender = None, genre = (None,)):
    """
    시간대(과거/현재)와 장르에 맞는 복장 반환

    Args:
        temporal_period: 'flashback' 또는 'present'
        context_type: 상황 유형 ('battle', 'daily', 'ceremony' 등)
        gender: 'male' 또는 'female'
        genre: 프로젝트 장르 ('WAR_MILITARY' 등)

    Returns:
        복장 프롬프트 문자열 또는 None
    """
    period_rules = TEMPORAL_OUTFIT_RULES.get(temporal_period)
    if not period_rules:
        return None
    genre_rules = None
    if genre:
        genre_upper = genre.upper().replace(' ', '_').replace('-', '_')
        genre_rules = period_rules.get(genre_upper)
    if not genre_rules:
        genre_rules = period_rules.get('default', { })
    context_outfits = genre_rules.get(context_type, genre_rules.get('default', { }))
    if isinstance(context_outfits, dict):
        outfit = context_outfits.get(gender, context_outfits.get('male', ''))
    else:
        outfit = str(context_outfits)
    return outfit if outfit else None


def get_face_identity_prompt(character = None):
    '''
    캐릭터의 얼굴/외모 특징만 추출 (의상 제외)
    이 부분은 모든 장면에서 일관되게 사용됨

    Args:
        character: 캐릭터 정보 dict

    Returns:
        얼굴/외모 프롬프트 문자열 (의상 제외)
    '''
    gender = character.get('gender', 'unknown')
    if gender == 'male':
        pass
    elif gender == 'female':
        pass
    
    gender_en = 'person'
    parts = []
    identity = f'''Korean {gender_en}'''
    age_range = character.get('ageRange', '')
    if age_range:
        identity += f''' in {age_range}'''
    parts.append(identity)
    if not character.get('hairstyleEn', ''):
        hairstyle_en = character.get('hairstyle', '')
        if hairstyle_en:
            parts.append(hairstyle_en)
    if not character.get('distinctiveFeaturesEn', ''):
        distinctive_en = character.get('distinctiveFeatures', '')
        if distinctive_en:
            parts.append(distinctive_en)
    return ', '.join(parts)

KOREAN_FACE_FEATURES = {
    'male': {
        'base': 'distinct East Asian facial structure',
        'elderly': 'deep rough wrinkles, weathered skin characteristic of elderly Koreans',
        'middle': 'mature East Asian features, slight wrinkles around eyes',
        'young': 'youthful East Asian features, smooth skin',
        'child': 'round childlike face, bright innocent eyes' },
    'female': {
        'base': 'distinct East Asian facial structure',
        'elderly': 'gentle wrinkles, graceful aging, warm wise eyes',
        'middle': 'mature refined features, elegant East Asian bone structure',
        'young': 'youthful East Asian features, delicate skin',
        'child': 'round childlike face, bright curious eyes' } }
KOREAN_APPEARANCE_FEATURES = {
    'skin': 'Korean skin tone, East Asian complexion',
    'hair_black': 'natural black hair, typical of East Asians',
    'hair_grey': 'grey hair mixed with black, natural aging',
    'eyes': 'monolid or double eyelid eyes, dark brown iris' }

def get_enhanced_korean_features(gender = None, age_group = None, include_skin = None):
    """
    Whisk 최적화를 위한 강화된 한국인 특징 프롬프트 생성

    Args:
        gender: 'male' 또는 'female'
        age_group: 'child', 'young', 'middle', 'elderly', 'default'
        include_skin: 피부톤 설명 포함 여부

    Returns:
        강화된 한국인 특징 프롬프트
    """
    if gender not in ('male', 'female'):
        gender = 'male'
    features = KOREAN_FACE_FEATURES.get(gender, KOREAN_FACE_FEATURES['male'])
    parts = []
    parts.append(features['base'])
    if age_group in features:
        parts.append(features[age_group])
    elif age_group == 'default':
        pass
    
    if include_skin:
        parts.append(KOREAN_APPEARANCE_FEATURES['skin'])
    return ', '.join(parts)


def get_whisk_ethnicity_prefix(character = None, scene_description = None):
    '''
    Whisk 프롬프트 시작에 추가할 인종 강화 프리픽스 생성

    정보성.txt의 "인종 고정" 전략 적용

    Args:
        character: 캐릭터 정보 dict
        scene_description: 장면 설명 (시간대 분석용)

    Returns:
        인종 강화 프리픽스 문자열
    '''
    gender = character.get('gender', 'male')
    gender_en = 'man' if gender == 'male' else 'woman'
    age_range = character.get('ageRange', '')
    age_group = _detect_age_group_from_text(age_range)
    temporal = analyze_temporal_period(scene_description)
    if temporal['temporal_period'] == 'flashback':
        if age_group == 'elderly':
            age_group = 'young'
        elif age_group == 'middle':
            age_group = 'young'
    if age_group == 'elderly':
        age_desc = 'elderly'
    elif age_group == 'middle':
        age_desc = 'middle-aged'
    elif age_group == 'young':
        age_desc = 'young'
    elif age_group == 'child':
        age_desc = 'young'
    else:
        age_desc = ''
    if age_desc:
        prefix = f'''Authentic {age_desc} Korean {gender_en}'''
    else:
        prefix = f'''Authentic Korean {gender_en}'''
    face_features = get_enhanced_korean_features(gender, age_group, include_skin = False)
    if face_features:
        prefix += f''', {face_features}'''
    prefix += '. South Korean distinct facial features are crucial.'
    return prefix


def _detect_age_group_from_text(text = None):
    '''
    텍스트에서 나이 그룹 감지 (내부 함수)
    '''
    pass
# WARNING: Decompyle incomplete


def get_whisk_prompt_structure(content_type = None, setting = None, characters = None, scene_description = ('content_type', str, 'setting', str, 'characters', list, 'scene_description', str, 'return', Dict)):
    """
    Whisk 최적화 프롬프트 구조 생성

    정보성.txt의 프롬프트 구조 적용:
    - 정보성: (인종+장소) → (캐릭터) → (화풍 제어)
    - 드라마틱: (분위기+화풍) → (인물+구도) → (배경)

    Args:
        content_type: 'informational' 또는 'dramatic'
        setting: 배경 설정
        characters: 캐릭터 목록
        scene_description: 장면 설명

    Returns:
        {
            'structure_type': 구조 유형,
            'sections': [섹션별 지침],
            'prefix': 프롬프트 시작 문구,
            'suffix': 프롬프트 마무리 문구
        }
    """
    if content_type == 'informational':
        return {
            'structure_type': 'informational',
            'sections': [
                'core_declaration',
                'character_info',
                'style_control'],
            'prefix': '',
            'suffix': 'Focus on detailed character design, neutral lighting to show features clearly.' }
    return {
        'structure_type': None,
        'sections': [
            'mood_style',
            'character_pose',
            'character_detail',
            'background'],
        'prefix': '',
        'suffix': 'Maintain the texture and color palette of the referenced style image.' }


def build_whisk_optimized_character_block(character = None, scene_description = None, include_outfit = None):
    '''
    Whisk 최적화 캐릭터 블록 생성

    정보성.txt의 캐릭터 표현 규칙 적용:
    - 강력한 인종/민족 표현
    - 나이에 따른 시각적 특징 필수 포함
    - 구체적인 외모 묘사

    Args:
        character: 캐릭터 정보 dict
        scene_description: 장면 설명 (동적 의상용)
        include_outfit: 의상 포함 여부

    Returns:
        캐릭터 블록 문자열
    '''
    name = character.get('name', 'Character')
    gender = character.get('gender', 'male')
    if gender == 'male':
        pass
    elif gender == 'female':
        pass
    
    gender_en = 'person'
    age_range = character.get('ageRange', '')
    age_group = _detect_age_group_from_text(age_range)
    parts = []
    if age_group == 'elderly':
        parts.append(f'''Authentic elderly Korean {gender_en} in {age_range}''')
    elif age_group == 'middle':
        parts.append(f'''Middle-aged Korean {gender_en} in {age_range}''')
    elif age_group == 'young':
        parts.append(f'''Young Korean {gender_en} in {age_range}''')
    else:
        parts.append(f'''Korean {gender_en}''')
    face_features = get_enhanced_korean_features(gender, age_group, include_skin = False)
    if face_features:
        parts.append(face_features)
    if not character.get('hairstyleEn', ''):
        hairstyle = character.get('hairstyle', '')
        if hairstyle:
            parts.append(hairstyle)
    if not character.get('distinctiveFeaturesEn', ''):
        distinctive = character.get('distinctiveFeatures', '')
        if distinctive:
            parts.append(distinctive)
    if include_outfit:
        outfit = get_dynamic_outfit(scene_description, character)
        if outfit:
            parts.append(f'''wearing {outfit}''')
    return f'''@{name}: {', '.join(parts)}'''
