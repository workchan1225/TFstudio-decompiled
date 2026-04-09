# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: intro_tts_service.pyc (Python 3.11)

'''
Intro TTS Service - 인트로 전용 TTS

기존 TTS 엔진을 재활용하되, 인트로에 최적화된 파라미터(속도/피치)를 적용합니다.
'''
import os
import logging
from typing import Optional
from pathlib import Path
from intro_types import IntroTTSSettings
logger = logging.getLogger(__name__)

class IntroTTSService:
    '''인트로 나레이션 TTS 생성 (기존 엔진 재활용)'''
    DEFAULT_INTRO_RATE = 10
    DEFAULT_INTRO_PITCH = 5
    
    def generate_intro_tts(self = None, text = None, project_id = None, settings = (None,)):
        """
        인트로 TTS 생성

        Args:
            text: 후킹 텍스트
            project_id: 프로젝트 ID
            settings: TTS 설정 (없으면 기본값)

        Returns:
            {'success': True, 'audioUrl': '/data/...', 'audioPath': '...', 'duration': float}
        """
        if not text or text.strip():
            return {
                'success': False,
                'error': '텍스트가 비어있습니다.' }
        if not None:
            settings = IntroTTSSettings()
            
            try:
                get_data_path = get_data_path
                import app.config.paths
                output_dir = get_data_path() / 'projects' / str(project_id) / 'intro'
                output_dir.mkdir(parents = True, exist_ok = True)
                output_path = str(output_dir / 'intro_tts.mp3')
                if not settings.engine:
                    engine = 'edge'
                    logger.info(f'''[IntroTTS] TTS 생성 시작 - engine={engine}, voice_id={settings.voice_id}, text={text[:50]}...''')
                    if engine in ('edge', 'edge-tts'):
                        return self._generate_edge_tts(text, output_path, settings)
                    if None in ('google-tts', 'google-voice', 'google', 'googlecloud'):
                        return self._generate_google_tts(text, output_path, settings)
                    if None in ('gemini-tts', 'gemini-voice', 'chirp3hd', 'chirp3-hd'):
                        return self._generate_chirp3hd_tts(text, output_path, settings)
                    if None in ('gemini-native-tts', 'gemini-native'):
                        return self._generate_gemini_native_tts(text, output_path, settings)
                    if None in ('elevenlabs',):
                        return self._generate_elevenlabs_tts(text, output_path, settings)
                    if None in ('supertonic-tts', 'supertonic'):
                        return self._generate_supertonic_tts(text, output_path, settings)
                    None.info(f'''[IntroTTS] 엔진 {engine} -> Edge 폴백''')
                    return self._generate_edge_tts(text, output_path, settings)
                except Exception:
                    e = None
                    logger.error(f'''[IntroTTS] TTS 생성 실패: {e}''')
                    del e
                    return None
                    None = 
                    del e


    
    def _generate_edge_tts(self = None, text = None, output_path = None, settings = ('text', str, 'output_path', str, 'settings', IntroTTSSettings, 'return', dict)):
        '''Edge TTS로 인트로 나레이션 생성'''
        pass
    # WARNING: Decompyle incomplete

    
    def _generate_google_tts(self = None, text = None, output_path = None, settings = ('text', str, 'output_path', str, 'settings', IntroTTSSettings, 'return', dict)):
        '''Google Cloud TTS로 인트로 나레이션 생성'''
        
        try:
            GoogleTTSService = GoogleTTSService
            import app.services.google_tts_service
            if not settings.voice_id:
                voice_name = 'ko-KR-Neural2-A'
            speed = settings.speed if settings.speed else 1
            pitch = float(settings.pitch) if settings.pitch else 0
            service = GoogleTTSService()
            result = service.generate_speech(text = text, voice_name = voice_name, speaking_rate = speed, pitch = pitch, output_path = output_path)
            if result and result.get('status') == 'success':
                return self._build_success_result(output_path)
            return {
                'success': None,
                'error': result.get('message', 'Google TTS 생성 실패') }
        except Exception:
            e = None
            logger.error(f'''[IntroTTS] Google TTS 실패: {e}''')
            logger.info('[IntroTTS] Edge TTS로 폴백')
            del e
            return None
            None = 
            del e


    
    def _generate_gemini_native_tts(self = None, text = None, output_path = None, settings = ('text', str, 'output_path', str, 'settings', IntroTTSSettings, 'return', dict)):
        '''Gemini Native TTS로 인트로 나레이션 생성'''
        
        try:
            GeminiNativeTTSService = GeminiNativeTTSService
            import app.services.gemini_native_tts_service
            if not settings.voice_id:
                voice_name = 'Kore'
                service = GeminiNativeTTSService()
                result = service.generate_speech(text = text, voice_name = voice_name, output_path = output_path)
                if result and result.get('status') == 'success':
                    return self._build_success_result(output_path)
                return {
                    'success': None,
                    'error': result.get('error', 'Gemini Native TTS 생성 실패') }
            except Exception:
                e = None
                logger.error(f'''[IntroTTS] Gemini Native TTS 실패: {e}''')
                logger.info('[IntroTTS] Edge TTS로 폴백')
                del e
                return None
                None = 
                del e


    
    def _generate_elevenlabs_tts(self = None, text = None, output_path = None, settings = ('text', str, 'output_path', str, 'settings', IntroTTSSettings, 'return', dict)):
        '''ElevenLabs TTS로 인트로 나레이션 생성'''
        
        try:
            ElevenLabsEngine = ElevenLabsEngine
            import app.services.tts.engines.elevenlabs_engine
            TTSEngineConfig = TTSEngineConfig
            import app.services.tts.base_tts_engine
            voice_id = settings.voice_id
            if not voice_id:
                return {
                    'success': False,
                    'error': 'ElevenLabs voice_id가 필요합니다.' }
            config = TTSEngineConfig(engine_type = 'elevenlabs')
            engine = ElevenLabsEngine(config)
            result = engine.generate_single_line(text = text, output_path = output_path, voice_id = voice_id)
            if result and result.status == 'success':
                return self._build_success_result(output_path)
            return {
                'success': None,
                'error': getattr(result, 'error', 'ElevenLabs TTS 생성 실패') }
        except Exception:
            e = None
            logger.error(f'''[IntroTTS] ElevenLabs TTS 실패: {e}''')
            logger.info('[IntroTTS] Edge TTS로 폴백')
            del e
            return None
            None = 
            del e


    
    def _generate_supertonic_tts(self = None, text = None, output_path = None, settings = ('text', str, 'output_path', str, 'settings', IntroTTSSettings, 'return', dict)):
        '''Supertonic TTS로 인트로 나레이션 생성'''
        
        try:
            SupertonicEngine = SupertonicEngine
            import app.services.tts.engines.supertonic_engine
            TTSEngineConfig = TTSEngineConfig
            import app.services.tts.base_tts_engine
            if not settings.voice_id:
                voice_id = 'F1'
            speed = settings.speed if settings.speed else 1
            config = TTSEngineConfig(engine_type = 'supertonic', audio_format = 'wav', sample_rate = 24000, line_folder_name = 'supertonic_single')
            engine = SupertonicEngine(config = config)
            result = engine.generate_single_line(text = text, output_path = output_path, voice_id = voice_id, speed = speed)
            if result and result.status == 'success':
                if not result.audio_path:
                    actual_path = output_path
                    return self._build_success_result(actual_path)
                return {
                    'success': result.audio_path,
                    'error': getattr(result, 'error', 'Supertonic TTS 생성 실패') }
            except Exception:
                e = None
                logger.error(f'''[IntroTTS] Supertonic TTS 실패: {e}''')
                logger.info('[IntroTTS] Edge TTS로 폴백')
                del e
                return None
                None = 
                del e


    
    def _generate_chirp3hd_tts(self = None, text = None, output_path = None, settings = ('text', str, 'output_path', str, 'settings', IntroTTSSettings, 'return', dict)):
        '''Chirp3 HD (gemini-tts) TTS로 인트로 나레이션 생성'''
        
        try:
            Chirp3HDEngine = Chirp3HDEngine
            import app.services.tts.engines.chirp3hd_engine
            TTSEngineConfig = TTSEngineConfig
            import app.services.tts.base_tts_engine
            if not settings.voice_id:
                voice_name = 'ko-KR-Chirp3-HD-Achernar'
            speaking_rate = settings.speed if settings.speed else 1
            config = TTSEngineConfig(engine_type = 'chirp3hd', audio_format = 'mp3', sample_rate = 24000, line_folder_name = 'chirp3hd_single')
            engine = Chirp3HDEngine(config = config)
            result = engine.generate_single_line(text = text, output_path = output_path, voice_name = voice_name, speaking_rate = speaking_rate)
            if result and result.status == 'success':
                if not result.audio_path:
                    actual_path = output_path
                    return self._build_success_result(actual_path)
                return {
                    'success': result.audio_path,
                    'error': getattr(result, 'error', 'Chirp3 HD TTS 생성 실패') }
            except Exception:
                e = None
                logger.error(f'''[IntroTTS] Chirp3 HD TTS 실패: {e}''')
                logger.info('[IntroTTS] Edge TTS로 폴백')
                del e
                return None
                None = 
                del e


    
    def _build_success_result(self = None, output_path = None):
        '''TTS 성공 결과 빌드 (공통) - 볼륨 노멀라이즈 포함'''
        if os.path.exists(output_path):
            self._normalize_audio(output_path)
            get_data_path = get_data_path
            import app.config.paths
            data_path = get_data_path()
            rel_path = str(Path(output_path).relative_to(data_path)).replace('\\', '/')
            audio_url = f'''/data/{rel_path}'''
            duration = self._get_audio_duration(output_path)
            return {
                'success': True,
                'audioUrl': audio_url,
                'audioPath': output_path,
                'duration': duration }
        return {
            'success': None,
            'error': 'TTS 파일 생성 실패' }

    _normalize_audio = (lambda file_path = None, target_lufs = None: try:
FFmpegWrapper = FFmpegWrapperimport app.utils.ffmpeg_wrapperimport shutiloutput_file = Path(file_path)normalized_path = str(output_file.parent / f'''{output_file.stem}_normalized{output_file.suffix}''')ffmpeg = FFmpegWrapper()ffmpeg.normalize_audio_loudness(input_path = file_path, output_path = normalized_path, target_lufs = target_lufs)if os.path.exists(normalized_path) and os.path.getsize(normalized_path) > 0:
shutil.move(normalized_path, file_path)logger.info(f'''[IntroTTS] 볼륨 정규화 완료 (EBU R128 {target_lufs} LUFS): {file_path}''')NoneNone.warning(f'''[IntroTTS] 볼륨 정규화 파일 생성 실패, 원본 유지: {file_path}''')Noneexcept Exception:
e = Nonelogger.warning(f'''[IntroTTS] 볼륨 정규화 실패 (원본 유지): {e}''')e = Nonedel eNonee = Nonedel e)()
    _get_audio_duration = (lambda file_path = None: try:
MutagenFile = Fileimport mutagenaudio = MutagenFile(file_path)if audio and audio.info:
round(audio.info.length, 1)except Exception:
pass0)()
    _METHOD_TO_ENGINE: dict = {
        'edge-tts': ('edge-tts', 'edgeTtsSingle', 'ko-KR-InJoonNeural'),
        'google-voice': ('google-tts', 'googleTtsSingle', 'ko-KR-Neural2-A'),
        'gemini-voice': ('gemini-tts', 'geminiTtsSingle', 'ko-KR-Chirp3-HD-Achernar'),
        'gemini-native': ('gemini-native-tts', 'geminiNativeTtsSingle', 'Kore'),
        'elevenlabs': ('elevenlabs', 'elevenLabsTtsSingle', None),
        'supertonic': ('supertonic', 'supertonicTtsSingle', 'F1') }
    _VOICE_TYPE_TO_SINGLE_KEY: dict = {
        'edge-tts': 'edgeTtsSingle',
        'edge': 'edgeTtsSingle',
        'neural2': 'googleTtsSingle',
        'chirp3-hd': 'geminiTtsSingle',
        'gemini-native': 'geminiNativeTtsSingle',
        'elevenlabs': 'elevenLabsTtsSingle',
        'supertonic': 'supertonicTtsSingle' }
    extract_project_tts_settings = (lambda project = None, language = None: pass# WARNING: Decompyle incomplete
)()
    _extract_from_voice_assignment = (lambda assignment = None, lang = None: engine = assignment.get('ttsMethod', 'edge-tts')voice_id = assignment.get('voiceId')pitch = assignment.get('pitch', 0)volume = assignment.get('volume', 0)rate = assignment.get('rate', 0)speed = assignment.get('speed')if engine in ('gemini-tts', 'chirp3hd'):
speaking_rate = assignment.get('speakingRate')if speaking_rate:
speed = float(speaking_rate)elif engine == 'elevenlabs':
el_speed = assignment.get('elevenLabsSpeed')if el_speed:
speed = float(el_speed)if speed and speed != 1:
rate = int((speed - 1) * 100)logger.info(f'''[IntroTTS] 화자별 TTS 설정 추출: engine={engine}, voice_id={voice_id}, rate={rate}, pitch={pitch}, speed={speed}, lang={lang}''')IntroTTSSettings(engine = engine, voice_id = voice_id, rate = rate, pitch = pitch, volume = volume, speed = speed if speed else None))()
