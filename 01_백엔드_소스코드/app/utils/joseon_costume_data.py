# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: joseon_costume_data.pyc (Python 3.11)

'''
조선시대 신분별 한복 데이터 및 프롬프트 생성 유틸리티

신분 계층:
- royal (왕족): 왕, 왕비, 대비, 세자, 공주, 대군
- yangban (양반): 사대부, 유생, 양반 부인
- jungin (중인): 역관, 의원, 서리
- sangmin (양민/평민): 농민, 상인, 장인
- cheonmin (천민): 노비, 백정, 기생(특수)

Sources:
- https://namu.wiki/w/한복/종류
- https://seoulblend.com/k-blends/k-style/hanbok-class-distinctions
- https://1440review.com/2025/09/26/hanbok-in-joseon-korea/
'''
from typing import Dict, List, Optional, Tuple
import re
JOSEON_COSTUMES = {
    'royal': {
        'name_ko': '왕족/궁중',
        'name_en': 'Royal/Palace',
        'male': {
            'garments': [
                'gonryongpo (dragon robe)',
                'ikseonkwan (royal winged cap)',
                'golden dragon embroidery with five claws',
                'royal court hanbok',
                'ceremonial silk robes'],
            'accessories': [
                'jade belt (okdae)',
                'royal seal',
                'golden thread embroidery'],
            'prompt_en': 'wearing elaborate gonryongpo (dragon robe) with golden five-clawed dragon embroidery, ikseonkwan (royal winged cap), luxurious silk fabric, jade belt, royal court attire, imperial Korean traditional dress',
            'prompt_ko': '화려한 곤룡포(용포)를 입고, 금실로 수놓은 오조룡 문양, 익선관, 고급 비단, 옥대, 궁중 의복' },
        'female': {
            'garments': [
                'wonsam (ceremonial robe)',
                'hwarot (wedding/ceremonial robe)',
                'dangui (formal jacket)',
                'daesam-chima (layered court skirt)'],
            'accessories': [
                'jokduri (ceremonial coronet)',
                'binyeo (ornamental hairpin)',
                'norigae (decorative tassel)',
                'golden phoenix embroidery'],
            'prompt_en': 'wearing elaborate wonsam or hwarot ceremonial robe with phoenix embroidery, dangui jacket, daesam-chima layered silk skirt, jokduri coronet, golden binyeo hairpin, royal norigae ornaments, luxurious palace attire',
            'prompt_ko': '화려한 원삼 또는 활옷을 입고, 봉황 자수, 당의, 대삼치마, 족두리, 금 비녀, 노리개, 궁중 예복' },
        'colors': [
            'yellow (imperial)',
            'red',
            'purple',
            'gold',
            'deep blue'],
        'fabric': 'finest silk brocade, satin, gold thread embroidery' },
    'yangban': {
        'name_ko': '양반',
        'name_en': 'Nobleman/Aristocrat',
        'male': {
            'garments': [
                'dopo (scholar overcoat)',
                'hakchangui (crane-decorated robe)',
                'durumagi (outer coat)',
                'baji-jeogori (trousers and jacket)'],
            'accessories': [
                'gat (black horsehair hat)',
                'manggeon (headband)',
                'fan (buchae)',
                'jade accessories'],
            'prompt_en': 'wearing dopo (scholar overcoat) or hakchangui, black gat (traditional horsehair hat), manggeon headband, refined silk jeogori and baji, nobleman scholarly attire, dignified posture',
            'prompt_ko': '도포 또는 학창의를 입고, 검은 갓, 망건, 고급 비단 저고리와 바지, 양반 선비 복장, 위엄 있는 자세' },
        'female': {
            'garments': [
                'jeogori-chima (jacket and skirt)',
                'dangui (formal jacket)',
                'samhoejang jeogori (three-color trim jacket)',
                'layered underskirts (3-5 layers)'],
            'accessories': [
                'binyeo (silver/jade hairpin)',
                'dwikkoji (back hairpin)',
                'norigae (decorative tassel)',
                'embroidered pouch'],
            'prompt_en': 'wearing refined samhoejang jeogori with colored collar and cuffs, layered silk chima skirt, elegant binyeo hairpin, norigae ornaments, yangban noblewoman attire, graceful and dignified',
            'prompt_ko': '삼회장저고리를 입고, 색동 깃과 소매, 겹겹의 비단 치마, 은 비녀, 노리개, 양반 부인 복장, 우아하고 품위 있는' },
        'colors': [
            'blue',
            'green',
            'jade green',
            'light purple',
            'subtle refined colors'],
        'fabric': 'high-quality silk, ramie cloth, light embroidery' },
    'jungin': {
        'name_ko': '중인',
        'name_en': 'Middle Class',
        'male': {
            'garments': [
                'durumagi (outer coat)',
                'jeogori-baji (jacket and trousers)',
                'practical hanbok without elaborate decorations'],
            'accessories': [
                'gat (horsehair hat, simpler style)',
                'manggeon (headband)'],
            'prompt_en': 'wearing practical durumagi and hanbok, simple gat hat, modest but neat appearance, middle-class Joseon attire, no elaborate decorations',
            'prompt_ko': '실용적인 두루마기와 한복, 단순한 갓, 검소하지만 단정한 외모, 중인 복장' },
        'female': {
            'garments': [
                'jeogori-chima (simpler style)',
                'banhoejang jeogori (single-color trim)'],
            'accessories': [
                'simple binyeo (hairpin)',
                'modest norigae'],
            'prompt_en': 'wearing modest banhoejang jeogori and chima, simple hairpin, practical middle-class attire, neat appearance',
            'prompt_ko': '검소한 반회장저고리와 치마, 단순한 비녀, 실용적인 중인 복장, 단정한 외모' },
        'colors': [
            'green',
            'brown',
            'muted blue',
            'gray-blue'],
        'fabric': 'cotton, light silk, practical materials' },
    'sangmin': {
        'name_ko': '양민/평민',
        'name_en': 'Commoner',
        'male': {
            'garments': [
                'simple baji-jeogori (trousers and jacket)',
                'no outer coat',
                'patched or worn clothing (for poor)'],
            'accessories': [
                'no gat (horsehair hat)',
                'simple headband or cloth wrap',
                'straw sandals (jipsin)'],
            'prompt_en': 'wearing simple white or gray baji-jeogori, no gat hat, cloth headband, rough cotton or hemp fabric, commoner peasant attire, plain practical clothing, straw sandals',
            'prompt_ko': '흰색 또는 회색 바지저고리, 갓 없음, 천 머리띠, 거친 무명이나 삼베, 평민 농민 복장, 소박하고 실용적인 옷, 짚신' },
        'female': {
            'garments': [
                'simple jeogori-chima',
                'short chima (working)',
                'no layered underskirts'],
            'accessories': [
                'simple hair tied back',
                'no ornaments',
                'practical apron for work'],
            'prompt_en': 'wearing simple white or undyed jeogori and chima, no decorations, hair simply tied, cotton or hemp fabric, commoner woman attire, practical working clothes',
            'prompt_ko': '흰색 또는 무염색 저고리와 치마, 장식 없음, 단순히 묶은 머리, 무명이나 삼베, 평민 여성 복장, 실용적인 일상복' },
        'colors': [
            'white (baekui minjeok)',
            'gray',
            'brown',
            'undyed natural'],
        'fabric': 'cotton (moo-myung), hemp (sam-be), rough cloth' },
    'cheonmin': {
        'name_ko': '천민',
        'name_en': 'Lowborn/Slave',
        'male': {
            'garments': [
                'coarse worn clothing',
                'patched rough fabric',
                'minimal simple garments'],
            'accessories': [
                'no accessories',
                'bare feet or straw sandals'],
            'prompt_en': 'wearing worn coarse clothing, patched rough hemp fabric, minimal simple garments, no accessories, bare feet or straw sandals, lowborn servant attire, poor humble appearance',
            'prompt_ko': '낡고 거친 옷, 기운 거친 삼베, 최소한의 단순한 의복, 장신구 없음, 맨발 또는 짚신, 천민 하인 복장, 가난하고 초라한 외모' },
        'female': {
            'garments': [
                'worn simple jeogori-chima',
                'short working skirt',
                'patched fabric'],
            'accessories': [
                'no ornaments',
                'simple tied hair'],
            'prompt_en': 'wearing worn simple jeogori and short chima, patched rough fabric, no ornaments, simply tied hair, lowborn servant woman attire, humble practical clothing',
            'prompt_ko': '낡은 저고리와 짧은 치마, 기운 거친 천, 장신구 없음, 단순히 묶은 머리, 천민 여성 복장, 초라하고 실용적인 옷' },
        'colors': [
            'brown',
            'dirty white',
            'undyed',
            'faded'],
        'fabric': 'coarse hemp, rough cotton, worn fabric' },
    'gisaeng': {
        'name_ko': '기생',
        'name_en': 'Gisaeng (Entertainer)',
        'note': 'Special case: allowed to wear colorful clothes despite low status',
        'female': {
            'garments': [
                'colorful jeogori-chima',
                'elaborate hanbok',
                'same as yangban in appearance'],
            'accessories': [
                'elaborate binyeo',
                'gold/silver norigae',
                'makeup'],
            'prompt_en': 'wearing colorful elaborate hanbok like yangban, decorative binyeo hairpins, gold norigae ornaments, gisaeng entertainer attire, elegant and alluring appearance',
            'prompt_ko': '화려한 한복을 입고, 장식적인 비녀, 금 노리개, 기생 복장, 우아하고 매혹적인 외모' },
        'colors': [
            'vibrant colors allowed',
            'red',
            'pink',
            'green'],
        'fabric': 'silk, satin (same as yangban)' } }
SOCIAL_CLASS_KEYWORDS = {
    'royal': {
        'ko': [
            '왕',
            '대왕',
            '임금',
            '상감',
            '전하',
            '왕비',
            '대비',
            '중전',
            '마마',
            '세자',
            '공주',
            '대군',
            '옹주',
            '궁녀',
            '내시',
            '상궁'],
        'en': [
            'king',
            'queen',
            'prince',
            'princess',
            'royal',
            'emperor',
            'empress',
            'crown prince',
            'palace lady',
            'eunuch'] },
    'yangban': {
        'ko': [
            '양반',
            '사대부',
            '선비',
            '유생',
            '대감',
            '나으리',
            '영감',
            '서방님',
            '마님',
            '아씨',
            '규수',
            '부인',
            '정승',
            '판서',
            '참판',
            '참의'],
        'en': [
            'nobleman',
            'aristocrat',
            'scholar',
            'yangban',
            'lord',
            'lady',
            'minister',
            'official',
            'noble'] },
    'jungin': {
        'ko': [
            '중인',
            '역관',
            '의원',
            '통역',
            '서리',
            '아전',
            '향리'],
        'en': [
            'middle class',
            'interpreter',
            'doctor',
            'clerk',
            'local official'] },
    'sangmin': {
        'ko': [
            '평민',
            '양민',
            '상인',
            '농민',
            '백성',
            '장인',
            '주모',
            '주인장',
            '촌놈',
            '농부',
            '어부',
            '대장장이'],
        'en': [
            'commoner',
            'peasant',
            'farmer',
            'merchant',
            'craftsman',
            'fisherman',
            'villager',
            'townsfolk'] },
    'cheonmin': {
        'ko': [
            '천민',
            '노비',
            '종',
            '하인',
            '머슴',
            '백정',
            '광대',
            '무당'],
        'en': [
            'slave',
            'servant',
            'lowborn',
            'butcher',
            'entertainer',
            'shaman'] },
    'gisaeng': {
        'ko': [
            '기생',
            '기녀',
            '해어화'],
        'en': [
            'gisaeng',
            'courtesan',
            'entertainer'] } }

def get_costume_by_class(social_class = None, gender = None):
    """
    신분과 성별에 따른 한복 정보 반환

    Args:
        social_class: 'royal', 'yangban', 'jungin', 'sangmin', 'cheonmin', 'gisaeng'
        gender: 'male' or 'female'

    Returns:
        Dict with garments, accessories, prompts, colors, fabric info
    """
    if social_class not in JOSEON_COSTUMES:
        social_class = 'sangmin'
    costume_data = JOSEON_COSTUMES[social_class]
    if social_class == 'gisaeng':
        gender = 'female'
    gender_data = costume_data.get(gender, costume_data.get('female', { }))
    return {
        'social_class': social_class,
        'social_class_name_ko': costume_data.get('name_ko', ''),
        'social_class_name_en': costume_data.get('name_en', ''),
        'gender': gender,
        'garments': gender_data.get('garments', []),
        'accessories': gender_data.get('accessories', []),
        'prompt_en': gender_data.get('prompt_en', ''),
        'prompt_ko': gender_data.get('prompt_ko', ''),
        'colors': costume_data.get('colors', []),
        'fabric': costume_data.get('fabric', '') }


def detect_social_class(text = None):
    """
    텍스트에서 조선시대 신분 감지

    Args:
        text: 캐릭터 설명 또는 장면 설명 텍스트

    Returns:
        Tuple[social_class, confidence]
        - social_class: 감지된 신분 ('royal', 'yangban', 'jungin', 'sangmin', 'cheonmin', 'gisaeng')
        - confidence: 신뢰도 (0.0 ~ 1.0)
    """
    if not text:
        return ('sangmin', 0.3)
    text_lower = None.lower()
    scores = { }
    for social_class, keywords in SOCIAL_CLASS_KEYWORDS.items():
        score = 0
        for keyword in keywords.get('ko', []):
            if keyword in text:
                score += 2
            for keyword in keywords.get('en', []):
                if keyword in text_lower:
                    score += 1
                scores[social_class] = score
                if max(scores.values()) == 0:
                    return ('sangmin', 0.3)
                best_class = None(scores, key = scores.get)
                confidence = min(1, scores[best_class] / 4)
                return (best_class, confidence)


def detect_gender(text = None):
    """
    텍스트에서 성별 감지

    Args:
        text: 캐릭터 설명 텍스트

    Returns:
        'male' or 'female'
    """
    pass
# WARNING: Decompyle incomplete


def build_costume_prompt(character_description = None, social_class = None, gender = None, language = (None, None, 'en')):
    """
    캐릭터 설명으로부터 한복 프롬프트 생성

    Args:
        character_description: 캐릭터 설명
        social_class: 명시적 신분 (없으면 자동 감지)
        gender: 명시적 성별 (없으면 자동 감지)
        language: 'en' or 'ko'

    Returns:
        한복 설명 프롬프트
    """
    if not social_class:
        (social_class, _) = detect_social_class(character_description)
    if not gender:
        gender = detect_gender(character_description)
    costume = get_costume_by_class(social_class, gender)
    if language == 'ko':
        prompt = costume.get('prompt_ko', '')
    else:
        prompt = costume.get('prompt_en', '')
    return prompt


def get_all_social_classes():
    '''
    모든 신분 정보 반환 (UI 드롭다운용)

    Returns:
        List of dicts with id, name_ko, name_en
    '''
    return [
        {
            'id': 'royal',
            'name_ko': '왕족/궁중',
            'name_en': 'Royal/Palace' },
        {
            'id': 'yangban',
            'name_ko': '양반',
            'name_en': 'Nobleman' },
        {
            'id': 'jungin',
            'name_ko': '중인',
            'name_en': 'Middle Class' },
        {
            'id': 'sangmin',
            'name_ko': '양민/평민',
            'name_en': 'Commoner' },
        {
            'id': 'cheonmin',
            'name_ko': '천민',
            'name_en': 'Lowborn' },
        {
            'id': 'gisaeng',
            'name_ko': '기생',
            'name_en': 'Gisaeng' }]
