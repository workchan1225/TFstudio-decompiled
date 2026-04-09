# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: base_tts_engine.pyc (Python 3.11)

'''
TTS 엔진 추상 베이스 클래스

모든 TTS 엔진이 구현해야 하는 공통 인터페이스를 정의합니다.
'''
from abc import ABC, abstractmethod
from typing import Dict, List, Optional, Any
from dataclasses import dataclass, field
from pathlib import Path
TTSResult = <NODE:12>()
TTSEngineConfig = <NODE:12>()

class BaseTTSEngine(ABC):
    '''TTS 엔진 추상 베이스 클래스'''
    
    def __init__(self = None, config = None, **kwargs):
        self.config = config
        self._init_params = kwargs

    engine_type = (lambda self = None: self.config.engine_type)()
    audio_format = (lambda self = None: self.config.audio_format)()
    generate_single_line = (lambda self = None, text = None, output_path = abstractmethod: pass)()
    
    def preprocess_text(self = None, text = None, language = None):
        '''
        텍스트 전처리 (선택적 오버라이드)
        기본값: 변환 없음
        '''
        return text.strip()

    
    def get_audio_duration(self = None, audio_path = None):
        '''오디오 파일의 duration 측정 (기본 구현)'''
        
        try:
            FFmpegWrapper = FFmpegWrapper
            import app.utils.ffmpeg_wrapper
            ffmpeg = FFmpegWrapper()
            return ffmpeg.get_video_duration(audio_path)
        except Exception:
            import soundfile as sf
            (data, sr) = sf.read(audio_path)
            return
