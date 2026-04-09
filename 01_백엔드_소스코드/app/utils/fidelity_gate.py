# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: fidelity_gate.pyc (Python 3.11)

'''
Fidelity Gate - 씬 나레이션 충실도 검증

씬 분할 시 AI가 원본에 없는 내용을 삽입하거나 (환각),
원문을 과도하게 변형하는 것을 감지합니다.

4가지 지표를 계산하여 종합 충실도 점수를 산출:
- sentence_overlap (40%): 원문 문장 보존율
- proper_noun_match (25%): 고유명사 일치율
- out_of_source_ratio (20%): 원본에 없는 내용 비율 (역가중치)
- length_distortion (15%): 길이 왜곡 정도 (역가중치)
'''
import re
from typing import Dict, List, Optional, Tuple
from dataclasses import dataclass, field
FidelityResult = <NODE:12>()

class FidelityGate:
    '''
    씬 나레이션 충실도 검증기

    AI 생성 씬의 narrationText가 원본 chapter_content를
    충실히 반영하는지 검증합니다.
    '''
    DEFAULT_THRESHOLD = 0.7
    WEIGHTS = {
        'sentence_overlap': 0.4,
        'proper_noun_match': 0.25,
        'out_of_source_ratio': 0.2,
        'length_distortion': 0.15 }
    KOREAN_NAME_PATTERN = re.compile('[가-힣]{2,4}(?:이|가|은|는|을|를|의|에게|한테|께서)?')
    ENGLISH_NAME_PATTERN = re.compile('\\b[A-Z][a-z]+(?:\\s+[A-Z][a-z]+)*\\b')
    
    def __init__(self = None, threshold = None):
        '''
        Args:
            threshold: 충실도 임계값 (기본 0.7)
        '''
        if not threshold:
            pass
        self.threshold = self.DEFAULT_THRESHOLD

    
    def calculate_fidelity_score(self = None, scene_narration = None, chapter_content = None, detected_characters = (None,)):
        '''
        씬 나레이션의 충실도 점수 계산

        Args:
            scene_narration: AI가 생성한 씬의 narrationText
            chapter_content: 원본 챕터 내용
            detected_characters: 감지된 캐릭터 목록 (선택)

        Returns:
            FidelityResult: 충실도 점수, 유효 여부, 이슈 목록
        '''
        issues = []
        details = { }
        if not scene_narration or chapter_content:
            return FidelityResult(fidelity_score = 0, is_valid = False, issues = [
                'Empty narration or chapter content'], details = {
                'error': 'missing_input' })
        (overlap_score, overlap_details) = None._calculate_sentence_overlap(scene_narration, chapter_content)
        details['sentence_overlap'] = overlap_details
        if overlap_score < 0.5:
            issues.append(f'''원문 문장 보존율 낮음: {overlap_score:.1%}''')
        (noun_score, noun_details) = self._calculate_proper_noun_match(scene_narration, chapter_content, detected_characters)
        details['proper_noun_match'] = noun_details
        if noun_score < 0.5:
            issues.append(f'''고유명사 불일치: {noun_details.get('mismatched', [])}''')
        (oos_ratio, oos_details) = self._calculate_out_of_source_ratio(scene_narration, chapter_content)
        oos_score = 1 - oos_ratio
        details['out_of_source'] = oos_details
        if oos_ratio > 0.3:
            issues.append(f'''원본에 없는 내용 {oos_ratio:.1%} 포함''')
        (distortion_score, distortion_details) = self._calculate_length_distortion(scene_narration, chapter_content)
        details['length_distortion'] = distortion_details
        if distortion_score < 0.7:
            issues.append(f'''길이 왜곡 감지: {distortion_details.get('ratio', 0):.1%}''')
        fidelity_score = overlap_score * self.WEIGHTS['sentence_overlap'] + noun_score * self.WEIGHTS['proper_noun_match'] + oos_score * self.WEIGHTS['out_of_source_ratio'] + distortion_score * self.WEIGHTS['length_distortion']
        is_valid = fidelity_score >= self.threshold
        return FidelityResult(fidelity_score = round(fidelity_score, 3), is_valid = is_valid, issues = issues, details = details)

    
    def _calculate_sentence_overlap(self = None, scene_narration = None, chapter_content = None):
        '''
        문장 단위 겹침률 계산
        씬 나레이션의 문장이 원본에 얼마나 포함되어 있는지 확인
        '''
        pass
    # WARNING: Decompyle incomplete

    
    def _calculate_proper_noun_match(self = None, scene_narration = None, chapter_content = None, detected_characters = (None,)):
        '''
        고유명사 일치율 계산
        씬에서 언급된 이름/지명이 원본에 있는지 확인
        '''
        pass
    # WARNING: Decompyle incomplete

    
    def _calculate_out_of_source_ratio(self = None, scene_narration = None, chapter_content = None):
        '''
        원본에 없는 내용 비율 계산
        씬 나레이션에서 원본에 전혀 없는 단어/구절 비율
        '''
        scene_words = set(self._tokenize_korean(scene_narration))
        chapter_words = set(self._tokenize_korean(chapter_content))
        stopwords = {
            '가',
            '과',
            '는',
            '도',
            '로',
            '를',
            '만',
            '에',
            '와',
            '은',
            '을',
            '의',
            '이',
            '같이',
            '까지',
            '부터',
            '에서',
            '으로',
            '처럼'}
        scene_words = scene_words - stopwords
        chapter_words = chapter_words - stopwords
        if not scene_words:
            return (0, {
                'scene_words': 0,
                'out_of_source': 0 })
        out_of_source = None - chapter_words
        oos_ratio = len(out_of_source) / len(scene_words)
        return (oos_ratio, {
            'scene_word_count': len(scene_words),
            'out_of_source_count': len(out_of_source),
            'out_of_source_words': list(out_of_source)[:20],
            'ratio': oos_ratio })

    
    def _calculate_length_distortion(self = None, scene_narration = None, chapter_content = None):
        '''
        길이 왜곡 계산
        씬 나레이션이 원본 대비 과도하게 길거나 짧은지 확인
        '''
        scene_len = len(scene_narration)
        chapter_len = len(chapter_content)
        if chapter_len == 0:
            return (0, {
                'scene_len': scene_len,
                'chapter_len': 0,
                'ratio': 0 })
        ratio = None / chapter_len
        if  <= 0.05, ratio or 0.05, ratio <= 0.5:
            pass
        

    
    def _split_sentences(self = None, text = None):
        '''문장 분리'''
        sentences = re.split('[.!?。]\\s*', text)
        return sentences()

    
    def _normalize_sentence(self = None, sentence = None):
        '''문장 정규화 (비교용)'''
        normalized = re.sub('\\s+', '', sentence)
        normalized = re.sub('[^\\w가-힣a-zA-Z0-9]', '', normalized)
        return normalized.lower()

    
    def _sentence_similarity(self = None, sent1 = None, sent2 = None):
        '''두 문장의 유사도 계산 (문자 기반)'''
        if not sent1 or sent2:
            return 0
        shorter = sent1 if None(sent1) <= len(sent2) else sent2
        longer = sent2 if len(sent1) <= len(sent2) else sent1
        if shorter in longer:
            return 1
        common_chars = None(shorter) & set(longer)
        similarity = len(common_chars) / len(set(shorter)) if shorter else 0
        return similarity

    
    def _extract_proper_nouns(self = None, text = None):
        '''고유명사 추출'''
        nouns = set()
        at_mentions = re.findall('@([가-힣a-zA-Z0-9_]+)', text)
        nouns.update(at_mentions)
        korean_names = re.findall('([가-힣]{2,4})(?:이|가|은|는|을|를|의|에게|한테|께서|씨|님)', text)
        nouns.update(korean_names)
        english_names = self.ENGLISH_NAME_PATTERN.findall(text)
        nouns.update(english_names)
        return nouns

    
    def _tokenize_korean(self = None, text = None):
        '''한국어 텍스트 토큰화 (간단한 버전)'''
        tokens = re.findall('[가-힣]+|[a-zA-Z]+|\\d+', text)
        return tokens()



def validate_scene_fidelity(scene_narration = None, chapter_content = dataclass, threshold = None, detected_characters = (0.7, None)):
    """
    편의 함수: 씬 충실도 검증

    Args:
        scene_narration: 씬 나레이션 텍스트
        chapter_content: 원본 챕터 내용
        threshold: 충실도 임계값 (기본 0.7)
        detected_characters: 감지된 캐릭터 목록

    Returns:
        Dict: {
            'fidelity_score': float,
            'is_valid': bool,
            'issues': List[str],
            'details': Dict
        }
    """
    gate = FidelityGate(threshold = threshold)
    result = gate.calculate_fidelity_score(scene_narration, chapter_content, detected_characters)
    return {
        'fidelity_score': result.fidelity_score,
        'is_valid': result.is_valid,
        'issues': result.issues,
        'details': result.details }


def batch_validate_scenes(scenes = None, chapter_content = None, threshold = None):
    """
    여러 씬의 충실도를 일괄 검증

    Args:
        scenes: 씬 목록 (각 씬에 narrationText 필드 필요)
        chapter_content: 원본 챕터 내용
        threshold: 충실도 임계값

    Returns:
        Dict: {
            'avg_fidelity': float,
            'all_valid': bool,
            'failed_scenes': List[int],
            'scene_results': List[Dict],
            'sentence_coverage': float,
            'missing_sentence_count': int,
            'missing_sentences': List[str]  # 누락된 문장 목록 (원본 형태)
        }
    """
    pass
# WARNING: Decompyle incomplete


def validate_regeneration_consistency(original_prompt = None, regenerated_prompt = None, characters = None, threshold = (None, 0.6)):
    """
    재생성 프롬프트의 원본 일관성 검증

    완화/재생성 시 원본 프롬프트와의 일관성을 검증합니다.
    캐릭터, 핵심 키워드 보존 여부를 확인합니다.

    Args:
        original_prompt: 원본 프롬프트
        regenerated_prompt: 재생성된 프롬프트
        characters: 캐릭터 목록 (선택)
        threshold: 일관성 임계값 (기본 0.6, 완화는 더 낮음)

    Returns:
        Dict: {
            'is_consistent': bool,
            'consistency_score': float,
            'preserved_anchors': List[str],
            'lost_anchors': List[str],
            'warnings': List[str]
        }
    """
    gate = FidelityGate(threshold = threshold)
    warnings = []
    preserved_anchors = []
    lost_anchors = []
    result = gate.calculate_fidelity_score(regenerated_prompt, original_prompt, characters)
    if characters:
        regenerated_lower = regenerated_prompt.lower()
        for char in characters:
            char_name = char.get('name', '')
            if char_name.startswith('@'):
                char_name = char_name[1:]
            if char_name:
                if char_name.lower() in regenerated_lower:
                    preserved_anchors.append(f'''character:{char_name}''')
                    continue
                lost_anchors.append(f'''character:{char_name}''')
                warnings.append(f'''Character \'{char_name}\' not found in regenerated prompt''')
            original_keywords = _extract_key_terms(original_prompt)
            regenerated_keywords = _extract_key_terms(regenerated_prompt)
            for kw in original_keywords:
                if kw.lower() in regenerated_prompt.lower():
                    preserved_anchors.append(f'''keyword:{kw}''')
                    continue
    len_ratio = len(regenerated_prompt) / len(original_prompt) if original_prompt else 0
    if len_ratio < 0.5:
        warnings.append(f'''Regenerated prompt is too short ({len_ratio:.0%} of original)''')
    elif len_ratio > 2:
        warnings.append(f'''Regenerated prompt is too long ({len_ratio:.0%} of original)''')
    if characters:
        pass
    is_consistent = len(lost_anchors) <= len(characters) // 2 if result.fidelity_score >= threshold else result.fidelity_score >= threshold
    return {
        'is_consistent': is_consistent,
        'consistency_score': round(result.fidelity_score, 3),
        'preserved_anchors': preserved_anchors,
        'lost_anchors': lost_anchors,
        'warnings': warnings + result.issues,
        'details': result.details }


def _extract_key_terms(text = None, max_terms = None):
    '''
    텍스트에서 핵심 키워드 추출 (간단한 버전)

    Args:
        text: 입력 텍스트
        max_terms: 최대 추출 개수

    Returns:
        List[str]: 핵심 키워드 목록
    '''
    stopwords = {
        '하고',
        '그러나',
        '그리고',
        'a',
        'an',
        'at',
        'be',
        'in',
        'is',
        'of',
        'on',
        'or',
        'to',
        'and',
        'are',
        'for',
        'had',
        'has',
        'the',
        'was',
        'been',
        'have',
        'look',
        'shot',
        'view',
        'were',
        'with',
        'being',
        'image',
        'photo',
        'scene',
        'style',
        'showing',
        '가',
        '과',
        '는',
        '도',
        '로',
        '를',
        '만',
        '에',
        '와',
        '은',
        '을',
        '의',
        '이',
        '같이',
        '까지',
        '부터',
        '에서',
        '으로',
        '처럼'}
    words = re.findall('[가-힣]{2,}|[a-zA-Z]{3,}', text)
    word_counts = { }
    for word in words:
        word_lower = word.lower()
        if word_lower not in stopwords:
            word_counts[word_lower] = word_counts.get(word_lower, 0) + 1
        sorted_words = sorted(word_counts.items(), key = (lambda x: x[1]), reverse = True)
        return sorted_words[:max_terms]()
