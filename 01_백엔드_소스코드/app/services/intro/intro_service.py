# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: intro_service.pyc (Python 3.11)

'''
Intro Service - 인트로 생성 오케스트레이터 (Facade)

인트로 전체 파이프라인을 조율합니다:
1. 하이라이트 추출
2. 후킹 텍스트 생성
3. 이미지 프롬프트 생성
4. TTS 생성
'''
import json
import logging
import os
from typing import Optional, List
from datetime import datetime
from intro_highlight_extractor import IntroHighlightExtractor
from intro_hook_generator import IntroHookGenerator
from intro_prompt_builder import IntroPromptBuilder
from intro_tts_service import IntroTTSService
from intro_types import HighlightResult, IntroData, IntroImage, IntroTTSSettings
logger = logging.getLogger(__name__)

class IntroService:
    '''인트로 생성 Facade'''
    
    def __init__(self):
        self.highlight_extractor = IntroHighlightExtractor()
        self.hook_generator = IntroHookGenerator()
        self.prompt_builder = IntroPromptBuilder()
        self.tts_service = IntroTTSService()

    
    def extract_highlights(self = None, scenes = None, api_key = None):
        '''하이라이트 장면 추출'''
        results = self.highlight_extractor.extract_highlights(scenes, api_key)
        return results()

    
    def generate_hook_text(self = None, narration_text = None, intro_type = None, api_key = ('highlight_question', None)):
        '''후킹 텍스트 생성'''
        return self.hook_generator.generate_hook_text(narration_text, intro_type, api_key)

    
    def generate_intro_prompt(self = None, narration_text = None, hook_text = None, effect = ('', 'fast_zoom', None), original_prompt_en = ('narration_text', str, 'hook_text', str, 'effect', str, 'original_prompt_en', Optional[str], 'return', str)):
        '''인트로 이미지 프롬프트 생성'''
        return self.prompt_builder.build_intro_prompt(narration_text, hook_text, effect, original_prompt_en)

    
    def generate_intro_tts(self = None, text = None, project_id = None, settings = (None,)):
        '''인트로 TTS 생성'''
        tts_settings = None
        if settings:
            tts_settings = IntroTTSSettings(engine = settings.get('engine', 'edge'), voice_id = settings.get('voiceId'), rate = settings.get('rate', 10), pitch = settings.get('pitch', 5), volume = settings.get('volume', 0))
        return self.tts_service.generate_intro_tts(text, project_id, tts_settings)

    
    def generate_full_intro(self, project_id, scenes, intro_type, template_id, hook_text, source_scene_id = None, duration = None, effect = None, generate_tts = ('highlight_question', None, None, None, 8, 'fast_zoom', False, None), api_key = ('project_id', str, 'scenes', List[dict], 'intro_type', str, 'template_id', Optional[str], 'hook_text', Optional[str], 'source_scene_id', Optional[str], 'duration', float, 'effect', str, 'generate_tts', bool, 'api_key', Optional[str], 'return', dict)):
        """
        인트로 전체 생성 파이프라인

        Returns:
            {
                'success': True,
                'highlights': [...],
                'hookText': '...',
                'imagePrompt': '...',
                'introData': {...},
                'ttsResult': {...}
            }
        """
        pass
    # WARNING: Decompyle incomplete

    
    def generate_auto_intro(self, project_id, scene_image_count, use_project_tts_settings = None, tts_override = None, regenerate_mode = None, image_settings_override = (3, True, None, 'all', None, None), pinned_indices = ('project_id', str, 'scene_image_count', int, 'use_project_tts_settings', bool, 'tts_override', Optional[dict], 'regenerate_mode', str, 'image_settings_override', Optional[dict], 'pinned_indices', Optional[List[int]], 'return', dict)):
        """
        자동 인트로 생성 파이프라인

        Args:
            regenerate_mode: 재생성 모드
                - 'all': 전체 재생성 (하이라이트 + 대본 + 이미지 + TTS)
                - 'images_only': 이미지만 재생성 (기존 대본/TTS 유지)
                - 'tts_only': TTS만 재생성 (기존 대본/이미지 유지)
                - 'images_and_tts': 이미지 + TTS 재생성 (기존 대본 유지)
        """
        
        try:
            Project = Project
            import app.models.project
            Settings = Settings
            import app.models.settings
            project = Project.query.get(project_id)
            if not project:
                return {
                    'success': False,
                    'error': '프로젝트를 찾을 수 없습니다.' }
            existing_intro = None
            if regenerate_mode != 'all':
                existing_result = self.get_intro_data(project_id)
                if existing_result.get('success'):
                    existing_intro = existing_result.get('introData', { })
                    logger.info(f'''[IntroService] 기존 인트로 데이터 로드: hookText={bool(existing_intro.get('hookText'))}, images={len(existing_intro.get('introImages', []))}, ttsAudioUrl={bool(existing_intro.get('ttsAudioUrl'))}''')
                else:
                    logger.warning(f'''[IntroService] 기존 인트로 데이터 로드 실패: {existing_result.get('error')}''')
            sg = self._load_scene_generation(project)
            scenes = self._extract_scenes_from_sg(sg)
            if scenes and regenerate_mode == 'all':
                return {
                    'success': False,
                    'error': '씬 데이터가 없습니다.' }
            None.info(f'''[IntroService] 자동 인트로 생성 시작 - 프로젝트: {project_id}, 모드: {regenerate_mode}''')
            if regenerate_mode == 'all':
                highlights = self.extract_highlights(scenes)
                logger.info(f'''[IntroService] 하이라이트 {len(highlights)}개 추출 완료''')
                hook_result = self.hook_generator.generate_hook_script(highlights)
                hook_script = hook_result.get('hookScript', '')
                hook_script_lines = hook_result.get('hookScriptLines', [])
                logger.info(f'''[IntroService] 후킹 대본 생성 완료: {len(hook_script_lines)}줄''')
            elif existing_intro:
                pass
            
            hook_script = ''
            hook_script_lines = existing_intro.get('hookScriptLines', []) if existing_intro else []
            highlights = []
            if scenes:
                highlights = self.extract_highlights(scenes)
            regen_images = regenerate_mode in ('all', 'images_only', 'images_and_tts')
            if regen_images:
                intro_prompts = self.prompt_builder.build_multi_scene_prompts(highlights = highlights, hook_script_lines = hook_script_lines, effect = 'fast_zoom', count = scene_image_count)
                scene_settings = self._extract_scene_settings_from_sg(sg)
                (character_images, characters) = self._extract_character_data_from_sg(sg)
                if image_settings_override:
                    if 'modelType' in image_settings_override:
                        scene_settings['engine'] = image_settings_override['modelType']
                    if 'includeKeywordText' in image_settings_override:
                        scene_settings['include_keyword_text'] = image_settings_override['includeKeywordText']
                    if 'includeCharacterReference' in image_settings_override:
                        scene_settings['include_character_reference'] = image_settings_override['includeCharacterReference']
                modification_direction = ''
                if image_settings_override and image_settings_override.get('modificationDirection'):
                    modification_direction = image_settings_override['modificationDirection']
                    logger.info(f'''[IntroService] 수정 방향 적용: {modification_direction[:100]}''')
                logger.info(f'''[IntroService] 이미지 설정: engine={scene_settings.get('engine')}, ratio={scene_settings.get('aspect_ratio')}, keyword={scene_settings.get('include_keyword_text')}, charRef={scene_settings.get('include_character_reference')}''')
                if not pinned_indices:
                    pinned = set([])
                    existing_images_map = { }
                    if pinned and existing_intro:
                        for img in existing_intro.get('introImages', []):
                            existing_images_map[img.get('index', -1)] = img
                            self._cleanup_old_intro_images(project_id, keep_indices = pinned)
                            if pinned:
                                logger.info(f'''[IntroService] 고정 이미지: {sorted(pinned)} (재생성 제외)''')
                intro_images = []
                for i, prompt in enumerate(intro_prompts):
                    if i in pinned and i in existing_images_map:
                        kept = IntroImage.from_dict(existing_images_map[i])
                        kept.index = i
                        intro_images.append(kept)
                        logger.info(f'''[IntroService] 인트로 이미지 {i + 1}/{scene_image_count} 고정 유지''')
                        continue
                    final_prompt = prompt
                    if modification_direction:
                        final_prompt = f'''{prompt}\n\nUser modification request: {modification_direction}'''
                    image_result = self._generate_intro_image(prompt = final_prompt, project_id = project_id, index = i, scene_settings = scene_settings, character_images = character_images, characters = characters)
                    intro_images.append(IntroImage(index = i, image_data_url = image_result.get('imageDataUrl', ''), prompt = prompt, image_path = image_result.get('imagePath', '')))
                    logger.info(f'''[IntroService] 인트로 이미지 {i + 1}/{scene_image_count} 생성 완료''')
                    
                    try:
                        continue
                        except Exception:
                            e = None
                            logger.error(f'''[IntroService] 인트로 이미지 {i + 1} 생성 실패: {e}''')
                            intro_images.append(IntroImage(index = i, prompt = prompt))
                            
                            try:
                                e = None
                                del e
                                continue
                                e = None
                                del e
                                
                                try:
                                    pass

                                existing_images = existing_intro.get('introImages', []) if existing_intro else []
                                intro_images = existing_images()
                                regen_tts = regenerate_mode in ('all', 'tts_only', 'images_and_tts')
                                tts_result = None
                                if not regen_tts and hook_script:
                                    logger.warning(f'''[IntroService] TTS 재생성 요청이지만 hook_script가 비어있습니다. (mode={regenerate_mode})''')
                                if regen_tts and hook_script:
                                    tts_settings = None
                                    if tts_override:
                                        tts_settings = IntroTTSSettings(engine = tts_override.get('engine', 'edge-tts'), voice_id = tts_override.get('voiceId'), rate = tts_override.get('rate', 0), pitch = tts_override.get('pitch', 0), volume = tts_override.get('volume', 0))
                                    elif use_project_tts_settings:
                                        tts_settings = self.tts_service.extract_project_tts_settings(project)
                                    logger.info(f'''[IntroService] TTS 생성 시작 - engine={tts_settings.engine if tts_settings else 'default'}, voice_id={tts_settings.voice_id if tts_settings else 'default'}, text_len={len(hook_script)}''')
                                    tts_result = self.tts_service.generate_intro_tts(hook_script, project_id, tts_settings)
                                    logger.info(f'''[IntroService] TTS 생성 완료: success={tts_result.get('success')}, audioUrl={tts_result.get('audioUrl')}, error={tts_result.get('error')}''')
                                tts_audio_url = None
                                duration = 8
                                if regen_tts and tts_result and tts_result.get('success'):
                                    tts_audio_url = tts_result.get('audioUrl')
                                    duration = tts_result.get('duration', 8)
                                elif regen_tts and existing_intro:
                                    tts_audio_url = existing_intro.get('ttsAudioUrl')
                                    duration = existing_intro.get('duration', 8)
                                first_image_path = intro_images[0].image_path if intro_images and intro_images[0].image_path else None
                                if highlights:
                                    pass
                                elif existing_intro:
                                    pass
                                
                                intro_data = 'highlight_question'(enabled = hook_script, intro_type = hook_script_lines, hook_text = highlights[0].get('sceneId'), hook_script_lines = existing_intro.get('sourceSceneId'), source_scene_id = None, duration = duration, effect = 'fast_zoom', tts_audio_url = tts_audio_url, intro_image_path = first_image_path, intro_images = intro_images, generated_at = datetime.utcnow().isoformat())
                                self.save_intro_data(project_id, intro_data.to_dict())
                                return {
                                    'success': hook_script,
                                    'hookScript': hook_script_lines,
                                    'hookScriptLines': (lambda .0: [ img.to_dict() for img in .0 ]),
                                    'introImages': intro_images(),
                                    'ttsResult': tts_result,
                                    'introData': intro_data.to_dict(),
                                    'regenerateMode': regenerate_mode }
                            except Exception:
                                e = None
                                logger.error(f'''[IntroService] 자동 인트로 생성 실패: {e}''', exc_info = True)
                                del e
                                return None
                                None = 
                                del e




    _load_scene_generation = (lambda project = None: try:
ProjectPaths = ProjectPathsimport app.utils.file_pathsproject_paths = ProjectPaths(project.id)scene_gen_path = project_paths.project_base / 'scene_generation.json'if scene_gen_path.exists():
f = open(scene_gen_path, 'r', encoding = 'utf-8')sg = json.load(f)try:
None(None, None)with None:
if not None:
try:
try:
if sg.get('sceneImages'):
sgexcept Exception:
e = Nonelogger.debug(f'''[IntroService] JSON 파일 로드 실패, DB 폴백: {e}''')e = Nonedel eexcept:
e = Nonedel eif not project.video_settings:
vs = { }if isinstance(vs, str):
vs = json.loads(vs)if isinstance(vs, dict):
vs.get('sceneGeneration', { }))()
    _extract_scenes_from_sg = (lambda sg = None:
