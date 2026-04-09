# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: intro_prompt_builder.pyc (Python 3.11)

'''
Intro Prompt Builder - 인트로 이미지 프롬프트 생성

인트로에 최적화된 극적 앵글/조명의 이미지 프롬프트를 생성합니다.
다중 이미지 시 카메라 샷/앵글/구도를 자동 변경하여 시각적 다양성을 보장합니다.
'''
import logging
from typing import Optional
logger = logging.getLogger(__name__)
_DIVERSITY_PROFILES = [
    {
        'shot': 'wide establishing shot',
        'angle': 'slightly low-angle',
        'orientation': 'three-quarter view facing slightly left',
        'lighting': 'dramatic side lighting with deep shadows',
        'placement': 'subject off-center using rule of thirds' },
    {
        'shot': 'medium close-up',
        'angle': 'eye-level',
        'orientation': 'profile view looking right',
        'lighting': 'warm backlight with rim light silhouette edge',
        'placement': 'subject positioned left third of frame' },
    {
        'shot': 'dynamic over-the-shoulder perspective',
        'angle': 'high-angle looking down',
        'orientation': 'back three-quarter view',
        'lighting': 'cool blue ambient with single warm accent light',
        'placement': 'depth layering with foreground blur element' },
    {
        'shot': 'extreme close-up detail',
        'angle': 'dutch angle tilted 15 degrees',
        'orientation': 'facing camera with intense gaze',
        'lighting': 'high contrast chiaroscuro with strong key light',
        'placement': 'tight crop filling 80% of frame' },
    {
        'shot': 'full body environmental shot',
        'angle': "bird's-eye overhead view",
        'orientation': 'seen from above, body angled diagonally',
        'lighting': 'soft diffused overcast with subtle color gradient',
        'placement': 'centered in vast negative space' },
    {
        'shot': 'medium shot waist-up',
        'angle': 'low-angle looking up heroically',
        'orientation': 'three-quarter view facing right',
        'lighting': 'golden hour warm side light with long shadows',
        'placement': 'subject right third, leading space left' },
    {
        'shot': 'wide cinematic landscape with small figure',
        'angle': 'eye-level distant',
        'orientation': 'silhouette walking away',
        'lighting': 'dramatic backlight with lens flare',
        'placement': 'figure small in lower third, environment dominant' }]

def _get_diversity_instruction(index = None):
    '''인덱스별 다양성 프로파일을 프롬프트 지시문으로 변환'''
    profile = _DIVERSITY_PROFILES[index % len(_DIVERSITY_PROFILES)]
    return f'''CAMERA: {profile['shot']}, {profile['angle']}. CHARACTER FRAMING: {profile['orientation']}. LIGHTING: {profile['lighting']}. COMPOSITION: {profile['placement']}. IMPORTANT: Avoid static front-facing portrait composition. '''


class IntroPromptBuilder:
    '''인트로 전용 이미지 프롬프트 빌더'''
    INTRO_STYLE_MODIFIERS = {
        'fast_zoom': 'extreme close-up, dramatic zoom, shallow depth of field, intense focus',
        'glitch': 'glitch art overlay, digital distortion, cyberpunk aesthetic, neon highlights',
        'flash_cut': 'high contrast, dramatic lighting, chiaroscuro, cinematic still frame',
        'fade_dramatic': 'soft vignette, moody atmosphere, dramatic silhouette, golden hour lighting',
        'none': 'cinematic composition, professional photography, balanced lighting' }
    
    def build_intro_prompt(self, narration_text = None, hook_text = None, effect = None, original_prompt_en = ('', 'fast_zoom', None, 0), scene_index = ('narration_text', str, 'hook_text', str, 'effect', str, 'original_prompt_en', Optional[str], 'scene_index', int, 'return', str)):
        '''
        인트로 이미지 프롬프트 생성

        Args:
            narration_text: 장면 나레이션
            hook_text: 후킹 텍스트
            effect: 인트로 효과
            original_prompt_en: 원본 영문 프롬프트 (있으면 기반으로 강화)
            scene_index: 씬 인덱스 (다양성 프로파일 선택용)

        Returns:
            인트로 최적화된 영문 프롬프트
        '''
        style_modifier = self.INTRO_STYLE_MODIFIERS.get(effect, self.INTRO_STYLE_MODIFIERS['none'])
        diversity = _get_diversity_instruction(scene_index)
        if original_prompt_en:
            prompt = f'''[INTRO HOOK SCENE] {original_prompt_en}. {diversity}{style_modifier}, ultra-dramatic, movie trailer quality, 8K resolution, emotional intensity, viewer hook moment. DO NOT include any text or watermark in the image.'''
        else:
            prompt = f'''[INTRO HOOK SCENE] A dramatic cinematic still depicting: {narration_text[:200]}. {diversity}{style_modifier}, ultra-dramatic, movie trailer quality, 8K resolution, emotional intensity, viewer hook moment. Photorealistic, hyper-detailed, professional cinematography. DO NOT include any text or watermark in the image.'''
        return prompt

    
    def build_multi_scene_prompts(self = None, highlights = None, hook_script_lines = None, effect = ('fast_zoom', 3), count = ('highlights', list, 'hook_script_lines', list, 'effect', str, 'count', int, 'return', list)):
        '''
        N개 인트로 씬 이미지 프롬프트 생성

        Args:
            highlights: 하이라이트 장면 목록
            hook_script_lines: 후킹 대본 줄 목록
            effect: 인트로 효과
            count: 생성할 이미지 수

        Returns:
            프롬프트 문자열 리스트
        '''
        prompts = []
        style_modifier = self.INTRO_STYLE_MODIFIERS.get(effect, self.INTRO_STYLE_MODIFIERS['none'])
        for i in range(count):
            narration = ''
            original_prompt = ''
            if i < len(highlights):
                h = highlights[i]
                narration = h.get('narrationText', h.get('narration_text', ''))
                original_prompt = h.get('promptEn', h.get('prompt_en', ''))
            diversity = _get_diversity_instruction(i)
            if original_prompt:
                prompt = f'''[INTRO HOOK SCENE {i + 1}] {original_prompt}. {diversity}{style_modifier}, ultra-dramatic, movie trailer quality, 8K resolution, emotional intensity, viewer hook moment. DO NOT include any text or watermark in the image.'''
            elif narration:
                prompt = f'''[INTRO HOOK SCENE {i + 1}] A dramatic cinematic still depicting: {narration[:200]}. {diversity}{style_modifier}, ultra-dramatic, movie trailer quality, 8K resolution, emotional intensity, viewer hook moment. Photorealistic, hyper-detailed, professional cinematography. DO NOT include any text or watermark in the image.'''
            else:
                prompt = f'''[INTRO HOOK SCENE {i + 1}] A dramatic cinematic establishing shot. {diversity}{style_modifier}, ultra-dramatic, movie trailer quality, 8K resolution, emotional intensity. DO NOT include any text or watermark in the image.'''
            prompts.append(prompt)
            return prompts

    
    def enhance_for_intro(self = None, base_prompt = None, effect = None):
        '''기존 프롬프트를 인트로용으로 강화'''
        style_modifier = self.INTRO_STYLE_MODIFIERS.get(effect, self.INTRO_STYLE_MODIFIERS['none'])
        return f'''[INTRO] {base_prompt}, {style_modifier}, movie trailer quality, emotional hook'''
