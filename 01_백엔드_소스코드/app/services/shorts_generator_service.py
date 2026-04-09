# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: shorts_generator_service.pyc (Python 3.11)

'''
Shorts Generator Service

YouTube Shorts 영상 생성 서비스.
원본 영상에서 클립을 추출하고 9:16 세로형으로 변환합니다.
'''
import logging
import os
import subprocess
import sys
import uuid
import json
from pathlib import Path
from typing import List, Dict, Any, Optional, Tuple
from datetime import datetime
logger = logging.getLogger(__name__)
from app.models.project import Project
from app.services.subtitle_service import get_font_info_for_ass
from app.utils.ffmpeg_utils import probe_media_duration, probe_video_dimensions
from app.utils.ffmpeg_wrapper import FFmpegWrapper
from app.utils.file_paths import ProjectPaths

class ShortsGeneratorService:
    '''YouTube Shorts 영상 생성 서비스'''
    SHORTS_WIDTH = 1080
    SHORTS_HEIGHT = 1920
    BITRATE_PRESETS = {
        'low': 8,
        'medium': 12,
        'high': 15,
        'ultra': 20 }
    
    def __init__(self = None, project = None):
        '''
        초기화

        Args:
            project: Project 모델 인스턴스
        '''
        self.project = project
        self.paths = ProjectPaths(project.id)
        self.ffmpeg = FFmpegWrapper(project_id = project.id)
        self.shorts_dir = self.paths.project_base / 'shorts'
        self.shorts_dir.mkdir(parents = True, exist_ok = True)

    
    def _calculate_video_timeout(self = None, duration_seconds = None, min_timeout = None):
        '''Calculate timeout for CPU-based shorts encoding operations.'''
        safe_duration = max(float(duration_seconds), 0)
        if safe_duration <= 0:
            return min_timeout
        return None.ffmpeg.calculate_timeout(safe_duration, multiplier = 8, min_timeout = min_timeout)

    TRANSITION_TYPES = [
        'none',
        'fade',
        'slide_left',
        'slide_right',
        'dissolve']
    DEFAULT_SUBTITLE_STYLE = {
        'fontFamily': 'Pretendard-Bold',
        'fontSize': 60,
        'fontColor': '#FFFFFF',
        'strokeColor': '#000000',
        'strokeWidth': 3,
        'enableStroke': True,
        'position': 'bottom',
        'enableBackground': True,
        'backgroundColor': '#000000',
        'backgroundOpacity': 70 }
    _clamp = (lambda value = None, minimum = None, maximum = staticmethod: max(minimum, min(maximum, value)))()
    
    def _build_text_layout(self = None, style_settings = None, kind = None):
        default_margin_percent = 2.5 if kind == 'subtitle' else 0
        default_max_width = 92 if kind == 'subtitle' else 88
        if not style_settings.get('fontSize', 60):
            raw_font_size = int(60)
            font_size = max(1, int(raw_font_size * 1.5))
            if not style_settings.get('alignment', 'center'):
                alignment = str('center')
                if not style_settings.get('horizontalMargin', default_margin_percent):
                    horizontal_margin_percent = self._clamp(float(default_margin_percent), 0, 40)
                    margin_px = int(self.SHORTS_WIDTH * (horizontal_margin_percent / 100))
                    text_area_width_px = max(1, self.SHORTS_WIDTH - margin_px * 2)
                    if not style_settings.get('maxWidth', default_max_width):
                        max_width_percent = self._clamp(float(default_max_width), 40, 100)
                        wrap_width_px = max(1, int(text_area_width_px * (max_width_percent / 100)))
                        raw_x_percent = self._resolve_x_position_percent(style_settings)
        raw_y_percent = self._resolve_y_position_percent(style_settings, default_y_percent = 10 if kind == 'title' else 88)
        raw_x_px = int(self.SHORTS_WIDTH * (raw_x_percent / 100))
        raw_y_px = int(self.SHORTS_HEIGHT * (raw_y_percent / 100))
        estimated_height_px = max(1, int(font_size * 1.5))
        min_y = int(estimated_height_px / 2)
        max_y = int(self.SHORTS_HEIGHT - estimated_height_px / 2)
        clamped_y = int(self._clamp(raw_y_px, min_y, max_y))
        if alignment == 'left':
            min_x = margin_px
            max_x = self.SHORTS_WIDTH - margin_px - wrap_width_px
        elif alignment == 'right':
            min_x = margin_px + wrap_width_px
            max_x = self.SHORTS_WIDTH - margin_px
        else:
            half_width = wrap_width_px / 2
            min_x = margin_px + half_width
            max_x = self.SHORTS_WIDTH - margin_px - half_width
        clamped_x = int(self._clamp(raw_x_px, min_x, max_x))
        return {
            'fontSizePx': font_size,
            'marginPx': margin_px,
            'textAreaWidthPx': text_area_width_px,
            'wrapWidthPx': wrap_width_px,
            'rawX': raw_x_px,
            'rawY': raw_y_px,
            'clampedX': clamped_x,
            'clampedY': clamped_y }

    _calculate_char_width = (lambda char = None, font_size = None: if  <= '가', char or '가', char <= '힣':
passfont_size * 1if char.isalnum() and ord(char) < 128:
font_size * 0.5if None == ' ':
font_size * 0.3None * 0.6)()
    
    def _wrap_text_to_width(self = None, text = None, font_size = None, max_width = ('text', str, 'font_size', int, 'max_width', int, 'return', str)):
        pass
    # WARNING: Decompyle incomplete

    
    def generate_shorts(self, clips, settings, progress_callback, merge_mode, transition = None, subtitle_style = None, title_overlay = None, sentences = (None, None, False, None, None, None, None, None), thumbnail_settings = ('clips', List[Dict[(str, Any)]], 'settings', Dict[(str, Any)], 'progress_callback', callable, 'merge_mode', bool, 'transition', Dict[(str, Any)], 'subtitle_style', Dict[(str, Any)], 'title_overlay', Dict[(str, Any)], 'sentences', List[Dict[(str, Any)]], 'thumbnail_settings', Dict[(str, Any)], 'return', List[Dict[(str, Any)]])):
        """
        쇼츠 영상 생성

        Args:
            clips: 클립 정보 리스트 [{start_seconds, end_seconds, ...}]
            settings: 생성 설정 {bitrate, include_subtitle, include_bgm, conversion_mode}
            progress_callback: 진행 상황 콜백 함수 (current, total, message)
            merge_mode: True이면 여러 클립을 하나의 쇼츠로 병합
            transition: 트랜지션 설정 {type: 'fade'|'slide_left'|..., duration: 0.5}
            subtitle_style: 자막 스타일 설정
            title_overlay: 제목 오버레이 설정
            thumbnail_settings: 썸네일 설정 (첫 프레임 커스터마이징)

        Returns:
            생성된 쇼츠 정보 리스트
        """
        pass
    # WARNING: Decompyle incomplete

    
    def generate_single_shorts(self, clip, settings = None, subtitle_style = None, title_overlay = None, clip_index = (None, None, None, 0, None), sentences = ('clip', Dict[(str, Any)], 'settings', Dict[(str, Any)], 'subtitle_style', Dict[(str, Any)], 'title_overlay', Dict[(str, Any)], 'clip_index', int, 'sentences', List[Dict[(str, Any)]], 'return', Dict[(str, Any)])):
        '''
        단일 쇼츠 영상 생성 — 프로젝트 이미지+오디오에서 9:16 직접 렌더링

        기존 최종 영상을 재사용하지 않고, 선택 구간의 이미지와 오디오를
        원본에서 가져와 9:16(1080x1920)으로 새롭게 생성합니다.
        '''
        pass
    # WARNING: Decompyle incomplete

    
    def _slice_images_for_clip(self = None, start_seconds = None, end_seconds = None):
        '''클립 시간 범위에 해당하는 이미지와 duration을 슬라이스'''
        resolve_data_path = resolve_data_path
        import app.utils.file_paths
        if not self.project.video_settings:
            video_settings = { }
            raw_images = video_settings.get('uploadedImages', [])
            image_timeline = video_settings.get('imageTimeline')
            data_dir = self.paths.data_dir
            uploaded_images = []
            for img in raw_images:
                if isinstance(img, str):
                    uploaded_images.append({
                        'path': img,
                        'duration': 5 })
                    continue
                if isinstance(img, dict):
                    uploaded_images.append(img)
                segments = []
                if image_timeline and isinstance(image_timeline, dict) and image_timeline.get('segments'):
                    cumulative = 0
                    for seg in image_timeline['segments']:
                        img_idx = seg.get('imageIndex', 0)
                        if not seg.get('duration'):
                            if not seg.get('endTime', 0) - seg.get('startTime', 0):
                                seg_duration = float(5)
                                if img_idx < len(uploaded_images):
                                    img_path = resolve_data_path(data_dir, uploaded_images[img_idx].get('path', ''))
                                    segments.append({
                                        'path': str(img_path),
                                        'start': cumulative,
                                        'end': cumulative + seg_duration,
                                        'duration': seg_duration })
                        cumulative += seg_duration
        cumulative = 0
        for img in uploaded_images:
            if not img.get('duration', 5):
                img_duration = float(5)
                img_path = resolve_data_path(data_dir, img.get('path', ''))
                segments.append({
                    'path': str(img_path),
                    'start': cumulative,
                    'end': cumulative + img_duration,
                    'duration': img_duration })
                cumulative += img_duration
                continue
                clip_images = []
                clip_durations = []
                for seg in segments:
                    overlap_start = max(seg['start'], start_seconds)
                    overlap_end = min(seg['end'], end_seconds)
                    overlap = overlap_end - overlap_start
                    if overlap > 0.05:
                        clip_images.append(seg['path'])
                        clip_durations.append(overlap)
                    return (clip_images, clip_durations)

    
    def _get_audio_path(self = None):
        '''프로젝트의 오디오 파일 경로'''
        audio_url = self.project.get_final_audio_url() if hasattr(self.project, 'get_final_audio_url') else None
        if not audio_url:
            return None
        audio_filename = None.split('/')[-1].split('?')[0]
        audio_dir = self.paths.project_base / 'audio'
        audio_path = audio_dir / audio_filename
        if audio_path.exists():
            return audio_path
        resolve_data_path = resolve_data_path
        import app.utils.file_paths
        resolved = resolve_data_path(self.paths.data_dir, audio_url)
        if os.path.exists(resolved):
            return Path(resolved)

    
    def _add_audio_segment_to_video(self, video_path, audio_path = None, output_path = None, audio_start = None, audio_duration = (15,), bitrate = ('video_path', Path, 'audio_path', Path, 'output_path', Path, 'audio_start', float, 'audio_duration', float, 'bitrate', int, 'return', None)):
        '''영상에 오디오의 특정 구간만 추출하여 합성'''
        timeout = self._calculate_video_timeout(audio_duration)
        args = [
            '-y',
            '-i',
            str(video_path),
            '-ss',
            str(audio_start),
            '-t',
            str(audio_duration),
            '-i',
            str(audio_path),
            '-map',
            '0:v:0',
            '-map',
            '1:a:0',
            '-c:v',
            'copy',
            '-c:a',
            'aac',
            '-b:a',
            '192k',
            '-shortest',
            str(output_path)]
        self.ffmpeg.run_command(args, timeout = timeout, output_path = str(output_path))

    _escape_ffmpeg_path = (lambda path_str = None: escaped = path_str.replace('\\', '/')if len(escaped) >= 2 and escaped[1] == ':':
escaped = escaped[0] + '\\:' + escaped[2:]escaped)()
    
    def _get_fonts_dir_escaped(self = None):
        '''ASS fontsdir용 폰트 디렉토리 경로 (이스케이프 적용)'''
        
        try:
            get_fonts_directory = get_fonts_directory
            import app.utils.font_utils
            fonts_dir = get_fonts_directory()
            if fonts_dir:
                return self._escape_ffmpeg_path(str(fonts_dir))
        except Exception:
            pass


    
    def _get_source_video_path(self = None):
