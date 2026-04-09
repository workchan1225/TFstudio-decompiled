# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: enhancer_selector.pyc (Python 3.11)

'''
Enhancer Selector - 신뢰도 기반 Enhancer 선택

프롬프트에 적용할 enhancer(강화 키워드)를
신뢰도 점수에 따라 최대 2개까지 선택합니다.

원칙:
- 신뢰도 0.7 이상인 enhancer만 선택
- 최대 2개까지만 적용 (과적용 방지)
- 스타일 템플릿과 호환되는 enhancer 우선
'''
from typing import Dict, List, Optional, Tuple
from dataclasses import dataclass
Enhancer = <NODE:12>()
ENHANCERS = {
    'high_quality': Enhancer(name = 'high_quality', keywords = [
        '8k',
        'ultra detailed',
        'high quality',
        'masterpiece'], confidence = 0.9, category = 'quality', compatible_styles = [
        'realistic',
        '3d_cartoon',
        'anime']),
    'cinematic': Enhancer(name = 'cinematic', keywords = [
        'cinematic lighting',
        'dramatic',
        'film grain',
        'bokeh'], confidence = 0.85, category = 'style', compatible_styles = [
        'realistic']),
    'professional': Enhancer(name = 'professional', keywords = [
        'professional photography',
        'studio lighting'], confidence = 0.8, category = 'quality', compatible_styles = [
        'realistic',
        'informational_simple']),
    'traditional_art': Enhancer(name = 'traditional_art', keywords = [
        'traditional painting',
        'brush strokes',
        'painterly'], confidence = 0.85, category = 'style', compatible_styles = [
        'minhwa',
        'traditional_ink']),
    'vibrant_colors': Enhancer(name = 'vibrant_colors', keywords = [
        'vibrant colors',
        'saturated',
        'colorful'], confidence = 0.8, category = 'style', compatible_styles = [
        '3d_cartoon',
        'anime',
        'minhwa']),
    'minimalist': Enhancer(name = 'minimalist', keywords = [
        'minimalist',
        'clean lines',
        'simple'], confidence = 0.8, category = 'style', compatible_styles = [
        'informational_simple']),
    'warm_atmosphere': Enhancer(name = 'warm_atmosphere', keywords = [
        'warm lighting',
        'golden hour',
        'cozy'], confidence = 0.7, category = 'atmosphere', compatible_styles = [
        'realistic',
        '3d_cartoon']),
    'dramatic_atmosphere': Enhancer(name = 'dramatic_atmosphere', keywords = [
        'dramatic',
        'moody',
        'intense'], confidence = 0.75, category = 'atmosphere', compatible_styles = [
        'realistic',
        'anime']),
    'soft_atmosphere': Enhancer(name = 'soft_atmosphere', keywords = [
        'soft lighting',
        'dreamy',
        'ethereal'], confidence = 0.7, category = 'atmosphere', compatible_styles = [
        'minhwa',
        'anime',
        'realistic']),
    'detailed_background': Enhancer(name = 'detailed_background', keywords = [
        'detailed background',
        'environment details'], confidence = 0.7, category = 'detail', compatible_styles = [
        'realistic',
        'anime',
        '3d_cartoon']),
    'character_focus': Enhancer(name = 'character_focus', keywords = [
        'character focused',
        'portrait style',
        'face details'], confidence = 0.75, category = 'detail', compatible_styles = [
        'realistic',
        'anime',
        '3d_cartoon']) }

class EnhancerSelector:
    '''
    신뢰도 기반 Enhancer 선택기

    컨텍스트와 스타일에 맞는 enhancer를 선택합니다.
    '''
    MAX_ENHANCERS = 2
    MIN_CONFIDENCE = 0.7
    
    def __init__(self = None, visual_category = None, context_type = None, genre = ('realistic', None, 'default')):
        '''
        Args:
            visual_category: 스타일 템플릿의 visual_category
            context_type: 감지된 컨텍스트 유형
            genre: 프로젝트 장르
        '''
        self.visual_category = visual_category
        self.context_type = context_type
        self.genre = genre

    
    def select_enhancers(self = None, scene_keywords = None, exclude = None):
        '''
        적절한 enhancer 선택

        Args:
            scene_keywords: 씬에서 감지된 키워드
            exclude: 제외할 enhancer 이름

        Returns:
            선택된 Enhancer 목록 (최대 2개)
        '''
        candidates = []
        if not exclude:
            exclude = []
            for name, enhancer in ENHANCERS.items():
                if name in exclude:
                    continue
                if self.visual_category not in enhancer.compatible_styles:
                    adjusted_conf = enhancer.confidence * 0.5
                else:
                    adjusted_conf = enhancer.confidence
                if self.context_type:
                    adjusted_conf += self._context_relevance_bonus(enhancer, self.context_type)
                if scene_keywords:
                    adjusted_conf += self._keyword_relevance_bonus(enhancer, scene_keywords)
                if adjusted_conf >= self.MIN_CONFIDENCE:
                    candidates.append((enhancer, adjusted_conf))
                candidates.sort(key = (lambda x: -x[1]))
                selected = []
                categories_used = set()
                for enhancer, conf in candidates:
                    if len(selected) >= self.MAX_ENHANCERS:
                        pass
                    elif enhancer.category not in categories_used:
                        selected.append(enhancer)
                        categories_used.add(enhancer.category)
                    return selected

    
    def _context_relevance_bonus(self = None, enhancer = None, context = None):
        '''컨텍스트 관련성 보너스 계산'''
        context_enhancer_map = {
            'battle': [
                'dramatic_atmosphere',
                'detailed_background'],
            'daily': [
                'warm_atmosphere',
                'soft_atmosphere'],
            'ceremony': [
                'professional',
                'traditional_art'],
            'outdoor': [
                'cinematic',
                'detailed_background'],
            'intimate': [
                'soft_atmosphere',
                'character_focus'] }
        relevant_enhancers = context_enhancer_map.get(context, [])
        return 0.1 if enhancer.name in relevant_enhancers else 0

    
    def _keyword_relevance_bonus(self = None, enhancer = None, scene_keywords = None):
        '''씬 키워드 관련성 보너스'''
        pass
    # WARNING: Decompyle incomplete

    
    def get_enhancer_keywords(self = None, enhancers = None):
        '''선택된 enhancer들의 키워드 목록 추출'''
        keywords = []
        for enhancer in enhancers:
            keywords.extend(enhancer.keywords[:2])
            return keywords



def select_best_enhancers(visual_category = None, context_type = dataclass, scene_keywords = None, max_enhancers = ('realistic', None, None, 2)):
    '''
    편의 함수: 최적 enhancer 선택

    Args:
        visual_category: 스타일 카테고리
        context_type: 컨텍스트 유형
        scene_keywords: 씬 키워드
        max_enhancers: 최대 enhancer 수

    Returns:
        (enhancer 키워드 목록, enhancer 상세 정보)
    '''
    selector = EnhancerSelector(visual_category = visual_category, context_type = context_type)
    enhancers = selector.select_enhancers(scene_keywords)[:max_enhancers]
    keywords = selector.get_enhancer_keywords(enhancers)
    details = enhancers()
    return (keywords, details)
