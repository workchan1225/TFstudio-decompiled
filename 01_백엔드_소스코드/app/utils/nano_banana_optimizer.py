# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: nano_banana_optimizer.pyc (Python 3.11)

'''
Nano Banana Pro (Google Whisk) 전용 프롬프트 최적화

Google의 엄격한 콘텐츠 필터를 우회하면서 시각적 의도를 유지하는 전략.

핵심 원칙:
1. 맥락 제공 (fictional, concept art, film still)
2. 구체적 세부사항 추가 (모호한 프롬프트 거부율 높음)
3. 미술 스타일 명시 ("digital art", "photorealistic" 등)
4. 캐릭터에 "fictional character" 명시

References:
- https://www.aifreeapi.com/en/posts/nano-banana-pro-image-generation-refused
- Google 공식: 필터가 "의도보다 훨씬 더 신중해졌다"
'''
from typing import Tuple, List, Optional
import re

class NanoBananaOptimizer:
    '''Nano Banana Pro (Google Whisk) 최적화 클래스'''
    SAFE_PREFIXES = {
        'realistic': 'Photorealistic digital art depicting a fictional scene,',
        'cinematic': 'Cinematic film still from a fictional movie,',
        'illustration': 'Professional digital illustration for entertainment media,',
        'animation': 'Stylized digital artwork with vibrant colors,',
        'traditional': 'Classical painting style artwork,',
        'informational': 'Clean informational graphic,' }
    PERSON_SAFETY_KEYWORDS = [
        'fictional character',
        'artistic interpretation',
        'concept art style']
    QUALITY_KEYWORDS = [
        'high-quality',
        'detailed composition',
        'professional lighting']
    ENHANCED_NEGATIVE_PROMPTS = [
        'gore',
        'graphic violence',
        'blood splatter',
        'bloody',
        'explicit content',
        'nsfw',
        'disturbing imagery',
        'real person',
        'celebrity',
        'public figure',
        'photorealistic face',
        'real human face',
        'child in danger',
        'minor in inappropriate situation']
    optimize_prompt = (lambda cls = None, prompt = None, visual_category = classmethod, has_characters = ('realistic', False, True), add_quality = ('prompt', str, 'visual_category', str, 'has_characters', bool, 'add_quality', bool, 'return', Tuple[(str, str)]): pass# WARNING: Decompyle incomplete
)()
    soften_dramatic_content = (lambda cls = None, prompt = None: if not prompt:
prompt# WARNING: Decompyle incomplete
)()
    add_safe_context = (lambda cls = None, prompt = None, context_type = classmethod: pass# WARNING: Decompyle incomplete
)()
    ensure_fictional_characters = (lambda cls = None, prompt = None: pass# WARNING: Decompyle incomplete
)()
    get_style_specific_negative = (lambda cls = None, visual_category = None: style_negatives = {
'realistic': 'cartoon, anime, illustration style, unrealistic',
'cinematic': 'amateur, low budget, home video, poor lighting',
'illustration': 'photorealistic, photo, 3D render',
'animation': 'realistic, photorealistic, uncanny valley',
'traditional': 'digital art, 3D, modern style',
'informational': 'photorealistic, photo, 3D render, realistic face' }if visual_category in style_negatives:
style_negatives[visual_category]base_category = visual_category.split('_')[0] if None else ''style_negatives.get(base_category, ''))()
    full_optimization = (lambda cls = None, prompt = None, visual_category = classmethod, has_characters = ('realistic', True, ''), negative_prompt = ('prompt', str, 'visual_category', str, 'has_characters', bool, 'negative_prompt', str, 'return', Tuple[(str, str)]): softened = cls.soften_dramatic_content(prompt)with_context = cls.add_safe_context(softened, visual_category)if has_characters:
with_fictional = cls.ensure_fictional_characters(with_context)else:
with_fictional = with_context(optimized, base_negative) = cls.optimize_prompt(with_fictional, visual_category = visual_category, has_characters = has_characters, add_quality = True)style_negative = cls.get_style_specific_negative(visual_category)negative_parts = (negative_prompt, base_negative, style_negative)()enhanced_negative = ', '.join(negative_parts)(optimized, enhanced_negative))()


def optimize_for_nano_banana(prompt = None, visual_category = None, has_characters = None, negative_prompt = ('realistic', True, '')):
    '''
    Nano Banana Pro 최적화 편의 함수

    Args:
        prompt: 원본 프롬프트
        visual_category: 시각 카테고리
        has_characters: 인물 포함 여부
        negative_prompt: 기존 네거티브 프롬프트

    Returns:
        Tuple[optimized_prompt, enhanced_negative_prompt]
    '''
    return NanoBananaOptimizer.full_optimization(prompt = prompt, visual_category = visual_category, has_characters = has_characters, negative_prompt = negative_prompt)
