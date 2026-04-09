# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: overlay_video_generator.pyc (Python 3.11)

__doc__ = '\n오버레이 비디오 생성 유틸리티\n\n프론트엔드 CSS keyframes 애니메이션을 기반으로\n애니메이션이 포함된 WebM 비디오를 생성합니다.\n\nPNG 시퀀스 → FFmpeg → WebM (VP9, alpha 채널 지원)\n'
import os
import subprocess
import sys
import tempfile
import shutil
from pathlib import Path
from typing import List, Dict, Any, Tuple, Optional
from PIL import Image, ImageDraw, ImageFilter
import math
from overlay_generator import create_radial_gradient, generate_overlay_image
from ffmpeg_utils import get_ffmpeg_executable
OVERLAY_ANIMATIONS: Dict[(str, Dict[(str, Any)])] = {
    'floating_lights': {
        'duration': 8,
        'fps': 30,
        'keyframes': [
            (0, {
                'bg_y': 100,
                'scale': 1 }),
            (0.5, {
                'bg_y': -50,
                'scale': 1.1 }),
            (1, {
                'bg_y': 100,
                'scale': 1 })] },
    'bokeh': {
        'duration': 8,
        'fps': 30,
        'keyframes': [
            (0, {
                'translate_x': 0,
                'scale': 1 }),
            (0.25, {
                'translate_x': 40,
                'scale': 1.03 }),
            (0.5, {
                'translate_x': 80,
                'scale': 1 }),
            (0.75, {
                'translate_x': 40,
                'scale': 0.97 }),
            (1, {
                'translate_x': 0,
                'scale': 1 })] },
    'fog': {
        'duration': 8,
        'fps': 30,
        'keyframes': [
            (0, {
                'translate_x_pct': -30,
                'opacity': 0.7 }),
            (0.5, {
                'translate_x_pct': 30,
                'opacity': 1 }),
            (1, {
                'translate_x_pct': -30,
                'opacity': 0.7 })] },
    'particles': {
        'duration': 8,
        'fps': 30,
        'keyframes': [
            (0, {
                'bg_y': 100,
                'opacity': 0.8 }),
            (0.5, {
                'bg_y': -100,
                'opacity': 0.8 }),
            (1, {
                'bg_y': 100,
                'opacity': 0.8 })] },
    'lens_flare': {
        'duration': 8,
        'fps': 30,
        'keyframes': [
            (0, {
                'translate_x_pct': -30,
                'translate_y_pct': -30,
                'rotate': 0,
                'opacity': 0.5 }),
            (0.5, {
                'translate_x_pct': 30,
                'translate_y_pct': 30,
                'rotate': 10,
                'opacity': 1 }),
            (1, {
                'translate_x_pct': -30,
                'translate_y_pct': -30,
                'rotate': 0,
                'opacity': 0.5 })] },
    'glow_orbs': {
        'duration': 8,
        'fps': 30,
        'keyframes': [
            (0, {
                'translate_x': 0,
                'translate_y': 0 }),
            (0.2, {
                'translate_x': 40,
                'translate_y': -30 }),
            (0.4, {
                'translate_x': 70,
                'translate_y': 20 }),
            (0.6, {
                'translate_x': 30,
                'translate_y': 50 }),
            (0.8, {
                'translate_x': -20,
                'translate_y': 20 }),
            (1, {
                'translate_x': 0,
                'translate_y': 0 })] },
    'prism': {
        'duration': 8,
        'fps': 30,
        'keyframes': [
            (0, {
                'translate_x_pct': -100,
                'rotate': -5,
                'opacity': 0.3 }),
            (0.5, {
                'translate_x_pct': 100,
                'rotate': 5,
                'opacity': 0.6 }),
            (1, {
                'translate_x_pct': -100,
                'rotate': -5,
                'opacity': 0.3 })] },
    'light_leak': {
        'duration': 8,
        'fps': 30,
        'keyframes': [
            (0, {
                'translate_x_pct': -20,
                'translate_y_pct': -20,
                'scale': 1.2,
                'opacity': 0.6 }),
            (0.5, {
                'translate_x_pct': 10,
                'translate_y_pct': 10,
                'scale': 1.3,
                'opacity': 1 }),
            (1, {
                'translate_x_pct': -20,
                'translate_y_pct': -20,
                'scale': 1.2,
                'opacity': 0.6 })] } }

def interpolate_keyframes(keyframes = None, progress = None):
    '''
    keyframes 사이를 선형 보간

    Args:
        keyframes: [(progress, {params}), ...] 형태의 keyframe 리스트
        progress: 0-1 사이의 진행률

    Returns:
        보간된 파라미터 딕셔너리
    '''
    if not keyframes:
        return { }
    if None <= keyframes[0][0]:
        return keyframes[0][1].copy()
    if None >= keyframes[-1][0]:
        return keyframes[-1][1].copy()
    for i in None(len(keyframes) - 1):
        (p1, params1) = keyframes[i]
        (p2, params2) = keyframes[i + 1]
        if  <= p1, progress or p1, progress <= p2:
            pass
        
        t * t * (3 - 2 * t) = (progress - p1) / (p2 - p1) if p2 > p1 else 0
        result = { }
        for key in params1:
            v1 = params1.get(key, 0)
            v2 = params2.get(key, v1)
            result[key] = v1 + (v2 - v1) * t
            
            return None, result
            return keyframes[-1][1].copy()


def apply_transform_to_image(img, translate_x, translate_y, translate_x_pct = None, translate_y_pct = None, scale = None, rotate = (0, 0, 0, 0, 1, 0, 1), opacity_factor = ('img', Image.Image, 'translate_x', float, 'translate_y', float, 'translate_x_pct', float, 'translate_y_pct', float, 'scale', float, 'rotate', float, 'opacity_factor', float, 'return', Image.Image)):
    '''
    이미지에 CSS transform과 유사한 변환 적용

    Args:
        img: 원본 RGBA 이미지
        translate_x: X 이동 (픽셀)
        translate_y: Y 이동 (픽셀)
        translate_x_pct: X 이동 (% of width)
        translate_y_pct: Y 이동 (% of height)
        scale: 스케일
        rotate: 회전 (도)
        opacity_factor: 투명도 배율

    Returns:
        변환된 RGBA 이미지
    '''
    pass
# WARNING: Decompyle incomplete


def generate_animated_overlay_frame(overlay_type, width = None, height = None, intensity = None, params = ('overlay_type', str, 'width', int, 'height', int, 'intensity', float, 'params', Dict[(str, float)], 'return', Image.Image)):
    '''
    애니메이션 파라미터가 적용된 단일 프레임 생성

    Args:
        overlay_type: 오버레이 타입
        width, height: 프레임 크기
        intensity: 기본 강도
        params: 애니메이션 파라미터 (translate, scale, opacity 등)

    Returns:
        RGBA 이미지 프레임
    '''
    opacity_factor = params.get('opacity', 1)
    base_img = generate_overlay_image(overlay_type, width, height, intensity = intensity, opacity = 0.8)
# WARNING: Decompyle incomplete


def generate_overlay_frames(overlay_type = None, width = None, height = None, intensity = (1920, 1080, 1)):
    '''
    오버레이 애니메이션의 모든 프레임 생성

    Args:
        overlay_type: 오버레이 타입
        width, height: 프레임 크기
        intensity: 효과 강도

    Returns:
        프레임 이미지 리스트
    '''
    anim = OVERLAY_ANIMATIONS.get(overlay_type)
    if not anim:
        base_img = generate_overlay_image(overlay_type, width, height, intensity, 0.8)
        return [
            base_img] if base_img else []
    frames = None
    total_frames = int(anim['duration'] * anim['fps'])
    for frame_idx in range(total_frames):
        progress = frame_idx / total_frames
        params = interpolate_keyframes(anim['keyframes'], progress)
        frame = generate_animated_overlay_frame(overlay_type, width, height, intensity, params)
        frames.append(frame)
        if frame_idx % 30 == 0:
            print(f'''[OverlayVideo] {overlay_type}: frame {frame_idx}/{total_frames}''')
        return frames


def create_overlay_video(overlay_type = None, output_path = None, width = None, height = (1920, 1080, 1), intensity = ('overlay_type', str, 'output_path', str, 'width', int, 'height', int, 'intensity', float, 'return', Optional[str])):
    '''
    오버레이 애니메이션을 WebM 비디오로 생성

    Args:
        overlay_type: 오버레이 타입
        output_path: 출력 경로 (.webm)
        width, height: 비디오 크기
        intensity: 효과 강도

    Returns:
        생성된 파일 경로 또는 None
    '''
    anim = OVERLAY_ANIMATIONS.get(overlay_type, {
        'fps': 30 })
    fps = anim.get('fps', 30)
    print(f'''[OverlayVideo] Generating {overlay_type} ({width}x{height})...''')
    frames = generate_overlay_frames(overlay_type, width, height, intensity)
    if not frames:
        print(f'''[OverlayVideo] No frames generated for {overlay_type}''')
        return None
    temp_dir = None.mkdtemp(prefix = f'''overlay_{overlay_type}_''')
# WARNING: Decompyle incomplete


def get_overlay_video_dir():
    '''오버레이 비디오 저장 디렉토리 반환 (EXE/개발 환경 모두 지원)'''
    get_static_path = get_static_path
    import app.config.paths
    base_dir = get_static_path() / 'overlays'
    base_dir.mkdir(parents = True, exist_ok = True)
    return base_dir

# WARNING: Decompyle incomplete
