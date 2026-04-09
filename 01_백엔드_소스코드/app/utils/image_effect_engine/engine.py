# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: engine.pyc (Python 3.11)

'''
이미지 효과 엔진 메인 클래스

OpenCV로 프레임별 효과 적용 후 FFmpeg로 인코딩
서브픽셀 정밀도의 부드러운 효과 제공
'''
import os
import logging
import math
import hashlib
from typing import List, Dict, Optional, Callable, Tuple
import numpy as np
import cv2
from pipeline import FFmpegPipeline
from effects import get_effect
logger = logging.getLogger(__name__)

def _validate_path(path = None):
    '''
    경로 검증 및 정규화

    Path traversal 공격 방지를 위한 검증
    - ".." 시퀀스 차단
    - 절대 경로로 정규화

    Args:
        path: 검증할 파일 경로

    Returns:
        정규화된 절대 경로

    Raises:
        ValueError: 경로 검증 실패 시
    '''
    if not path:
        raise ValueError('Empty path')
    abs_path = os.path.abspath(path)
    if '..' in path.split(os.sep) or '..' in path.split('/'):
        logger.warning(f'''Path traversal detected in: {path}''')
        raise ValueError(f'''Path traversal not allowed: {path}''')
    return abs_path


def _imread_unicode(image_path = None):
    '''
    한글/유니코드 경로 지원 이미지 로드

    Windows에서 cv2.imread()는 유니코드 경로를 지원하지 않음
    np.frombuffer + cv2.imdecode 조합으로 우회

    Args:
        image_path: 이미지 파일 경로

    Returns:
        BGR 형식의 이미지 배열 또는 None (로드 실패 시)
    '''
    
    try:
        validated_path = _validate_path(image_path)
        f = open(validated_path, 'rb')
        file_bytes = np.frombuffer(f.read(), dtype = np.uint8)
        
        try:
            None(None, None)
        with None:
            if not None:
                
                try:
                    
                    try:
                        image = cv2.imdecode(file_bytes, cv2.IMREAD_COLOR)
                        return image
                    except ValueError:
                        e = None
                        logger.error(f'''Path validation failed: {e}''')
                        e = None
                        del e
                        return None
                        e = None
                        del e
                        except FileNotFoundError:
                            logger.error(f'''Image file not found: {image_path}''')
                            return None
                        except PermissionError:
                            logger.error(f'''Permission denied: {image_path}''')
                            return None
                        except Exception:
                            e = None
                            logger.error(f'''Failed to load image: {image_path}, error: {e}''')
                            e = None
                            del e
                            return None
                            e = None
                            del e






class ImageEffectEngine:
    """
    OpenCV + FFmpeg 하이브리드 이미지 효과 엔진

    핵심 원리:
    1. 서브픽셀 정밀도의 affine 변환 (cv2.warpAffine)
    2. smoothstep 이징으로 부드러운 가속/감속
    3. 스트리밍 방식으로 메모리 효율적 처리
    4. FFmpeg pipe로 GPU 가속 인코딩

    사용 예시:
    ```python
    engine = ImageEffectEngine(
        output_path='output.mp4',
        resolution=(1920, 1080),
        fps=30
    )
    engine.process_images(
        image_paths=['img1.jpg', 'img2.jpg'],
        durations=[3.0, 5.0],
        effect_settings={'effect': 'zoom_in', 'zoomStart': 1.0, 'zoomEnd': 1.3}
    )
    ```
    """
    DEFAULT_FPS = 30
    DEFAULT_QUALITY = 23
    MIN_MOTION_DURATION_SEC = 1.2
    MAX_MOTION_DURATION_SEC = 10
    _SUPPORTED_EFFECTS = {
        'pan',
        'rotate',
        'static',
        'fade_in',
        'zoom_in',
        'fade_out',
        'zoom_out',
        'ken_burns'}
    _BASE_ONE_WAY_DURATIONS = {
        'zoom_in': 4.5,
        'zoom_out': 4.5,
        'pan': 5,
        'rotate': 4,
        'ken_burns': 3 }
    
    def __init__(self, output_path, resolution = None, fps = None, encoder = None, quality = ((1920, 1080), DEFAULT_FPS, 'auto', DEFAULT_QUALITY, None), ffmpeg_path = ('output_path', str, 'resolution', Tuple[(int, int)], 'fps', int, 'encoder', str, 'quality', int, 'ffmpeg_path', Optional[str])):
        """
        Args:
            output_path: 출력 영상 파일 경로
            resolution: 출력 해상도 (width, height)
            fps: 프레임 레이트 (기본: 30)
            encoder: 인코더 ('auto', 'h264_nvenc', 'libx264')
            quality: 품질 (CRF/CQ 값, 낮을수록 고품질)
            ffmpeg_path: FFmpeg 실행 파일 경로

        Raises:
            ValueError: 출력 경로 검증 실패 시
        """
        self.output_path = _validate_path(output_path)
        self.fps = fps
        self.encoder = encoder
        self.quality = quality
        self.ffmpeg_path = ffmpeg_path
        self.width = resolution[0] + resolution[0] % 2
        self.height = resolution[1] + resolution[1] % 2
        self._total_frames = 0
        self._processed_frames = 0

    _parse_speed_multiplier = (lambda speed_setting = None: pass# WARNING: Decompyle incomplete
)()
    _normalize_pan_direction = (lambda direction_value = None, fallback = None: if not direction_value:
fallbackdirection = None(direction_value).lower()direction_map = {
'left_to_right': 'right',
'right_to_left': 'left',
'top_to_bottom': 'down',
'bottom_to_top': 'up' }normalized = direction_map.get(direction, direction)if normalized in ('left', 'right', 'up', 'down', 'random'):
normalized)()
    _stable_random_direction = (lambda scene_index = None, image_path = None: key = f'''{scene_index}:{os.path.basename(image_path)}'''digest = hashlib.sha1(key.encode('utf-8')).digest()directions = ('left', 'right', 'up', 'down')directions[digest[0] % len(directions)])()
    
    def _normalize_scene_settings(self = None, effect_settings = None, scene_index = None, image_path = ('effect_settings', Dict, 'scene_index', int, 'image_path', str, 'return', Tuple[(str, str, float, Dict)])):
        '''
        장면 설정 정규화

        Returns:
            (normalized_effect, motion_mode, speed_mult, normalized_settings)
            - motion_mode: one_shot | loop | continuous | roundtrip_once | static
        '''
        settings = dict(effect_settings)
        if not settings.get('effect', 'static'):
            raw_effect = str('static').lower()
            if raw_effect in ('none', ''):
                raw_effect = 'static'
        if raw_effect == 'zoom':
            raw_effect = 'zoom_loop'
        if raw_effect in ('rotate_cw', 'rotate_ccw'):
            settings['rotateDirection'] = 'clockwise' if raw_effect == 'rotate_cw' else 'counter_clockwise'
            raw_effect = 'rotate'
        motion_mode = 'one_shot'
        normalized_effect = raw_effect
        if raw_effect.endswith('_continuous'):
            normalized_effect = raw_effect[:-11]
            motion_mode = 'continuous'
        elif raw_effect.endswith('_loop'):
            normalized_effect = raw_effect[:-5]
            motion_mode = 'loop'
        if motion_mode == 'one_shot' and raw_effect in ('pan', 'ken_burns') and isinstance(settings.get('loop'), bool):
            motion_mode = 'loop' if settings.get('loop') else 'one_shot'
        if normalized_effect == 'zoom':
            normalized_effect = 'zoom_in'
        raw_speed = settings.get('speed', 1)
        if not isinstance(raw_speed, (int, float, str)):
            raw_speed = 1
        speed_mult = self._parse_speed_multiplier(raw_speed)
        if raw_effect in ('zoom_loop', 'zoom_continuous'):
            
            try:
                zoom_start = float(settings.get('zoomStart', 1))
                zoom_end = float(settings.get('zoomEnd', settings.get('zoomLevel', 1.3)))
            except (TypeError, ValueError):
                zoom_start = 1
                zoom_end = 1.3

            normalized_effect = 'zoom_out' if zoom_start > zoom_end else 'zoom_in'
        if normalized_effect == 'rotate':
            rotate_angle = settings.get('rotateAngle', settings.get('rotateEnd', 15))
            
            try:
                rotate_angle = abs(float(rotate_angle))
            except (TypeError, ValueError):
                rotate_angle = 15

            rotate_angle = max(0, min(45, rotate_angle))
            settings['rotateStart'] = 0
            settings['rotateEnd'] = rotate_angle
            rotate_direction = settings.get('rotateDirection')
            if rotate_direction not in ('clockwise', 'counter_clockwise'):
                rotate_direction = 'clockwise' if scene_index % 2 == 0 else 'counter_clockwise'
            settings['rotateDirection'] = rotate_direction
            rotate_mode = settings.get('rotateMode', 'one-way')
            if motion_mode == 'one_shot' and rotate_mode == 'round-trip':
                motion_mode = 'roundtrip_once'
        if normalized_effect in ('pan', 'ken_burns'):
            pan_direction = self._normalize_pan_direction(settings.get('panDirection', 'left'))
            if pan_direction == 'random':
                if motion_mode == 'loop':
                    settings['multiDirection'] = True
                    settings['panDirection'] = 'left'
                else:
                    settings['panDirection'] = self._stable_random_direction(scene_index, image_path)
            else:
                settings['panDirection'] = pan_direction
        if normalized_effect not in self._SUPPORTED_EFFECTS:
            logger.warning(f'''Unknown OpenCV effect \'{raw_effect}\', falling back to static''')
            normalized_effect = 'static'
            motion_mode = 'static'
        settings['effect'] = normalized_effect
        settings['speed'] = speed_mult
        return (normalized_effect, motion_mode, speed_mult, settings)

    
    def _compute_one_way_duration(self = None, normalized_effect = None, settings = None, speed_mult = ('normalized_effect', str, 'settings', Dict, 'speed_mult', float, 'return', float)):
        '''
        효과량에 비례한 한 방향 모션 시간 계산.

        핵심:
        - 장면 길이와 분리
        - 줌/팬/회전량이 클수록 더 오래 걸림
        - speed 배율로 최종 시간 조정
        '''
        base_duration = self._BASE_ONE_WAY_DURATIONS.get(normalized_effect, 4.5)
        amount_factor = 1
        if normalized_effect in ('zoom_in', 'zoom_out'):
            
            try:
                zoom_start = float(settings.get('zoomStart', 1))
                zoom_end = float(settings.get('zoomEnd', settings.get('zoomLevel', 1.3)))
            except (TypeError, ValueError):
                zoom_start = 1
                zoom_end = 1.3

            zoom_delta = abs(zoom_end - zoom_start)
            amount_factor = max(0.35, min(3, zoom_delta / 0.2))
        elif normalized_effect == 'pan':
            
            try:
                pan_amount = float(settings.get('panAmount', 30))
            except (TypeError, ValueError):
                pan_amount = 30

            amount_factor = max(0.35, min(3, pan_amount / 30))
        elif normalized_effect == 'rotate':
            
            try:
                rotate_angle = float(settings.get('rotateAngle', settings.get('rotateEnd', 15)))
            except (TypeError, ValueError):
                rotate_angle = 15

            amount_factor = max(0.35, min(3, abs(rotate_angle) / 15))
        elif normalized_effect == 'ken_burns':
            
            try:
                zoom_start = float(settings.get('zoomStart', 1))
                zoom_end = float(settings.get('zoomEnd', settings.get('zoomLevel', 1.3)))
                pan_amount = float(settings.get('panAmount', 20))
            except (TypeError, ValueError):
                zoom_start = 1
                zoom_end = 1.3
                pan_amount = 20

            zoom_factor = max(0.35, min(3, abs(zoom_end - zoom_start) / 0.2))
            pan_factor = max(0.35, min(3, pan_amount / 30))
            amount_factor = max(zoom_factor, pan_factor)
        one_way = base_duration * amount_factor / max(speed_mult, 0.1)
        return max(self.MIN_MOTION_DURATION_SEC, min(self.MAX_MOTION_DURATION_SEC, one_way))

    
    def _compute_progress(self = None, frame_idx = None, motion_mode = None, one_way_duration = ('frame_idx', int, 'motion_mode', str, 'one_way_duration', float, 'return', float)):
        '''모션 모드에 따른 진행률 계산 (0~1)'''
        frame_time = frame_idx / max(float(self.fps), 1)
        min_time = 1 / max(float(self.fps), 1)
        if motion_mode == 'loop':
            cycle_time = max(one_way_duration * 2, min_time * 4)
            phase = (frame_time % cycle_time) / cycle_time
            return phase * 2 if phase <= 0.5 else (1 - phase) * 2
        if None == 'roundtrip_once':
            total_time = max(one_way_duration * 2, min_time)
            phase = min(frame_time / total_time, 1)
            return phase * 2 if phase <= 0.5 else (1 - phase) * 2
        if None == 'continuous':
            total_time = max(one_way_duration, min_time)
            return max(0, min(frame_time / total_time, 1))
        if None == 'static':
            return 1
        total_time = None(one_way_duration, min_time)
        return max(0, min(frame_time / total_time, 1))

    
    def process_images(self, image_paths, durations = None, effect_settings = None, per_scene_effects = None, fit_mode = (None, 'cover', None), progress_callback = ('image_paths', List[str], 'durations', List[float], 'effect_settings', Dict, 'per_scene_effects', Optional[Dict[(int, Dict)]], 'fit_mode', str, 'progress_callback', Optional[Callable[([
        float,
        int,
        int], None)]], 'return', str)):
        """
        이미지 리스트에 효과를 적용하고 영상 생성

        Args:
            image_paths: 이미지 경로 리스트
            durations: 각 이미지 표시 시간 (초)
            effect_settings: 기본 효과 설정
            per_scene_effects: 장면별 개별 효과 {index: settings}
            fit_mode: 이미지 맞춤 모드 ('cover', 'contain', 'fill')
            progress_callback: 진행률 콜백 (progress, current_frame, total_frames)

        Returns:
            생성된 영상 파일 경로
        """
        pass
    # WARNING: Decompyle incomplete

    _MULTI_DIRECTIONS = ('left', 'up', 'right', 'down')
    
    def _process_single_image(self, pipeline, image_path, duration, effect_settings = None, scene_index = None, fit_mode = None, progress_callback = ('pipeline', FFmpegPipeline, 'image_path', str, 'duration', float, 'effect_settings', Dict, 'scene_index', int, 'fit_mode', str, 'progress_callback', Optional[Callable[([
        float,
        int,
        int], None)]])):
        '''단일 이미지 처리'''
        image = _imread_unicode(image_path)
    # WARNING: Decompyle incomplete

    
    def process_single_image_to_frames(self, image_path = None, duration = None, effect_settings = None, scene_index = (0, 'cover'), fit_mode = ('image_path', str, 'duration', float, 'effect_settings', Dict, 'scene_index', int, 'fit_mode', str, 'return', List[np.ndarray])):
        '''
        단일 이미지를 프레임 리스트로 변환 (디버깅/테스트용)

        Returns:
            프레임 리스트 (BGR 형식)
        '''
        image = _imread_unicode(image_path)
    # WARNING: Decompyle incomplete



def create_video_with_opencv_effects(image_paths, durations, effect_settings, output_path, resolution, fps = None, per_scene_effects = None, encoder = None, quality = ((1920, 1080), 30, None, 'auto', 23, None), progress_callback = ('image_paths', List[str], 'durations', List[float], 'effect_settings', Dict, 'output_path', str, 'resolution', Tuple[(int, int)], 'fps', int, 'per_scene_effects', Optional[Dict[(int, Dict)]], 'encoder', str, 'quality', int, 'progress_callback', Optional[Callable[([
    float,
    int,
    int], None)]], 'return', str)):
    """
    OpenCV 기반 이미지 효과 영상 생성 (편의 함수)

    FFmpegWrapper에서 호출하기 위한 인터페이스

    Args:
        image_paths: 이미지 경로 리스트
        durations: 각 이미지 표시 시간 (초)
        effect_settings: 효과 설정
        output_path: 출력 영상 경로
        resolution: 출력 해상도 (width, height)
        fps: 프레임 레이트 (기본: 30)
        per_scene_effects: 장면별 개별 효과
        encoder: 인코더 ('auto', 'h264_nvenc', 'libx264')
        quality: 품질 (CRF/CQ 값)
        progress_callback: 진행률 콜백

    Returns:
        생성된 영상 파일 경로
    """
    engine = ImageEffectEngine(output_path = output_path, resolution = resolution, fps = fps, encoder = encoder, quality = quality)
    return engine.process_images(image_paths = image_paths, durations = durations, effect_settings = effect_settings, per_scene_effects = per_scene_effects, progress_callback = progress_callback)
