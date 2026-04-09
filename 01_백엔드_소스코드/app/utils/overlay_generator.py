# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: overlay_generator.pyc (Python 3.11)

'''
오버레이 이미지 생성 유틸리티

프론트엔드 CSS 효과와 동일한 오버레이 이미지를 생성하여
FFmpeg overlay 필터로 합성할 수 있도록 합니다.
'''
import os
import tempfile
from typing import Tuple, Optional
from PIL import Image, ImageDraw, ImageFilter
import math

def create_radial_gradient(size = None, center = None, radius = None, color = (0.8,), alpha = ('size', Tuple[(int, int)], 'center', Tuple[(float, float)], 'radius', float, 'color', Tuple[(int, int, int)], 'alpha', float, 'return', Image.Image)):
    '''
    방사형 그라데이션 원 생성

    Args:
        size: 이미지 크기 (width, height)
        center: 원 중심 위치 (0-1 비율)
        radius: 반지름 (0-1 비율, 너비 기준)
        color: RGB 색상
        alpha: 최대 투명도 (0-1)

    Returns:
        RGBA 이미지
    '''
    (width, height) = size
    cx = int(center[0] * width)
    cy = int(center[1] * height)
    r = int(radius * width)
    img = Image.new('RGBA', size, (0, 0, 0, 0))
# WARNING: Decompyle incomplete


def generate_floating_lights(width = None, height = None, intensity = None, opacity = (0.8, 0.8)):
    '''
    떠다니는 조명 효과 생성 (7개의 황금색 빛점)

    프론트엔드 CSS 참조: frontend/src/components/effects/overlays/OverlayLayer.tsx
    '''
    img = Image.new('RGBA', (width, height), (0, 0, 0, 0))
    lights = [
        (0.05, 0.15, 0.08, (255, 230, 180), 0.8),
        (0.25, 0.45, 0.1, (255, 200, 150), 0.7),
        (0.45, 0.25, 0.07, (255, 220, 170), 0.75),
        (0.65, 0.65, 0.09, (255, 240, 200), 0.65),
        (0.85, 0.35, 0.08, (255, 210, 160), 0.7),
        (0.15, 0.75, 0.1, (255, 230, 190), 0.6),
        (0.95, 0.85, 0.07, (255, 220, 170), 0.7)]
    for x_pct, y_pct, r_pct, color, light_alpha in lights:
        light = create_radial_gradient((width, height), (x_pct, y_pct), r_pct * intensity, color, alpha = opacity * light_alpha * 0.3)
        img = Image.alpha_composite(img, light)
        img = img.filter(ImageFilter.GaussianBlur(radius = width * 0.02))
        return img


def generate_particles(width = None, height = None, intensity = None, opacity = (0.8, 0.8)):
    '''
    떠다니는 입자 효과 생성 (작은 빛나는 점들)

    프론트엔드 CSS 참조: frontend/src/components/effects/overlays/OverlayLayer.tsx
    CSS: 3-4px 크기의 작은 점들 (backgroundSize: 200px 기준)
    '''
    img = Image.new('RGBA', (width, height), (0, 0, 0, 0))
    particles = [
        (0.1, 0.2, 0.015, (255, 255, 255), 0.8),
        (0.3, 0.6, 0.01, (255, 255, 220), 0.7),
        (0.5, 0.3, 0.0125, (255, 240, 200), 0.75),
        (0.7, 0.7, 0.01, (255, 255, 255), 0.65),
        (0.9, 0.4, 0.015, (255, 250, 220), 0.7),
        (0.2, 0.85, 0.01, (255, 255, 240), 0.6),
        (0.8, 0.1, 0.0125, (255, 255, 255), 0.7)]
    for x_pct, y_pct, r_pct, color, particle_alpha in particles:
        particle = create_radial_gradient((width, height), (x_pct, y_pct), r_pct * (1 + intensity), color, alpha = opacity * particle_alpha * 0.3)
        img = Image.alpha_composite(img, particle)
        return img


def generate_bokeh(width = None, height = None, intensity = None, opacity = (0.8, 0.8)):
    '''
    보케 효과 생성 (큰 블러 원)

    프론트엔드 CSS 참조: frontend/src/components/effects/overlays/OverlayLayer.tsx
    '''
    img = Image.new('RGBA', (width, height), (0, 0, 0, 0))
    orbs = [
        (0.1, 0.15, 0.12, (100, 200, 255), 0.6),
        (0.9, 0.2, 0.1, (255, 100, 200), 0.55),
        (0.75, 0.8, 0.15, (100, 255, 180), 0.5),
        (0.2, 0.75, 0.12, (255, 220, 100), 0.45),
        (0.5, 0.45, 0.18, (200, 150, 255), 0.4)]
    for x_pct, y_pct, r_pct, color, orb_alpha in orbs:
        orb = create_radial_gradient((width, height), (x_pct, y_pct), r_pct * intensity, color, alpha = opacity * orb_alpha * 0.3)
        img = Image.alpha_composite(img, orb)
        img = img.filter(ImageFilter.GaussianBlur(radius = width * 0.05))
        return img


def generate_light_leak(width = None, height = None, intensity = None, opacity = (0.8, 0.8)):
    '''
    빛샘 효과 생성 (대각선 그라데이션)

    프론트엔드 CSS 참조: frontend/src/components/effects/overlays/OverlayLayer.tsx
    CSS: linear-gradient(135deg, rgba(255,100,50,0.6) 0%, rgba(255,180,80,0.4) 30%,
                                  rgba(255,220,100,0.25) 60%, transparent 85%)
    '''
    img = Image.new('RGBA', (width, height), (0, 0, 0, 0))
    color_stops = [
        (0, (255, 100, 50), 0.6),
        (0.3, (255, 180, 80), 0.4),
        (0.6, (255, 220, 100), 0.25),
        (0.85, (0, 0, 0), 0)]
    for y in range(height):
        for x in range(width):
            progress = (x / width + y / height) / 2
            (r, g, b, a) = (0, 0, 0, 0)
            for i in range(len(color_stops) - 1):
                (p1, c1, a1) = color_stops[i]
                (p2, c2, a2) = color_stops[i + 1]
                if  <= p1, progress or p1, progress <= p2:
                    pass
                
                int(c1[0] + (c2[0] - c1[0]) * t) = (progress - p1) / (p2 - p1) if p2 > p1 else 0
                g = int(c1[1] + (c2[1] - c1[1]) * t)
                b = int(c1[2] + (c2[2] - c1[2]) * t)
                a = int(255 * opacity * (a1 + (a2 - a1) * t) * intensity * 0.5)
            if a > 0:
                img.putpixel((x, y), (r, g, b, a))
            img = img.filter(ImageFilter.GaussianBlur(radius = width * 0.03))
            return img


def generate_fog(width = None, height = None, intensity = None, opacity = (0.8, 0.8)):
    '''
    안개 효과 생성 (수평 그라데이션)

    프론트엔드 CSS 참조: frontend/src/components/effects/overlays/OverlayLayer.tsx
    CSS: linear-gradient(90deg, rgba(220,220,235,0.5) 0%, rgba(200,200,220,0.3) 50%,
                                rgba(220,220,235,0.5) 100%)
    '''
    img = Image.new('RGBA', (width, height), (0, 0, 0, 0))
    for y in range(height):
        for x in range(width):
            progress = x / width
            if progress <= 0.5:
                t = progress / 0.5
                r = int(220 - 20 * t)
                g = int(220 - 20 * t)
                b = int(235 - 15 * t)
                alpha_factor = 0.5 - 0.2 * t
            else:
                t = (progress - 0.5) / 0.5
                r = int(200 + 20 * t)
                g = int(200 + 20 * t)
                b = int(220 + 15 * t)
                alpha_factor = 0.3 + 0.2 * t
            a = int(255 * opacity * alpha_factor * intensity * 0.6)
            img.putpixel((x, y), (r, g, b, a))
            img = img.filter(ImageFilter.GaussianBlur(radius = width * 0.08))
            return img


def generate_lens_flare(width = None, height = None, intensity = None, opacity = (0.8, 0.8)):
    '''
    렌즈 플레어 효과 생성

    프론트엔드 CSS 참조: frontend/src/components/effects/overlays/OverlayLayer.tsx
    CSS: radial-gradient(ellipse at 30% 30%, rgba(255,200,150,0.6) 0%, transparent 25%),
         radial-gradient(circle at 35% 35%, rgba(255,255,200,0.4) 0%, transparent 8%),
         radial-gradient(ellipse at 60% 60%, rgba(150,200,255,0.3) 0%, transparent 20%),
         radial-gradient(circle at 70% 40%, rgba(255,180,255,0.25) 0%, transparent 10%)
    '''
    img = Image.new('RGBA', (width, height), (0, 0, 0, 0))
    flares = [
        (0.3, 0.3, 0.25, (255, 200, 150), 0.6),
        (0.35, 0.35, 0.08, (255, 255, 200), 0.4),
        (0.6, 0.6, 0.2, (150, 200, 255), 0.3),
        (0.7, 0.4, 0.1, (255, 180, 255), 0.25)]
    for x_pct, y_pct, r_pct, color, flare_alpha in flares:
        flare = create_radial_gradient((width, height), (x_pct, y_pct), r_pct * intensity, color, alpha = opacity * flare_alpha * 0.3)
        img = Image.alpha_composite(img, flare)
        img = img.filter(ImageFilter.GaussianBlur(radius = width * 0.02))
        return img


def generate_glow_orbs(width = None, height = None, intensity = None, opacity = (0.8, 0.8)):
    '''
    빛 구슬 효과 생성 - 프론트엔드 CSS와 동기화

    프론트엔드 CSS 참조: frontend/src/components/effects/overlays/OverlayLayer.tsx
    '''
    img = Image.new('RGBA', (width, height), (0, 0, 0, 0))
    orbs = [
        (0.15, 0.25, 0.25, (100, 200, 255), 0.7),
        (0.8, 0.3, 0.22, (255, 150, 200), 0.6),
        (0.6, 0.75, 0.24, (150, 255, 200), 0.55),
        (0.3, 0.7, 0.23, (255, 220, 150), 0.5)]
    for x_pct, y_pct, r_pct, color, orb_alpha in orbs:
        orb = create_radial_gradient((width, height), (x_pct, y_pct), r_pct * intensity, color, alpha = opacity * orb_alpha * 0.3)
        img = Image.alpha_composite(img, orb)
        img = img.filter(ImageFilter.GaussianBlur(radius = width * 0.04))
        return img


def generate_prism(width = None, height = None, intensity = None, opacity = (0.8, 0.8)):
    '''
    프리즘 효과 생성 (대각선 무지개 그라데이션)

    프론트엔드 CSS 참조: frontend/src/components/effects/overlays/OverlayLayer.tsx
    CSS: linear-gradient(135deg, rgba(255,0,0,0.2) 0%, ... transparent 100%)
    '''
    img = Image.new('RGBA', (width, height), (0, 0, 0, 0))
    color_stops = [
        (0, (255, 0, 0), 0.2),
        (0.14, (255, 127, 0), 0.2),
        (0.28, (255, 255, 0), 0.2),
        (0.42, (0, 255, 0), 0.2),
        (0.57, (0, 0, 255), 0.2),
        (0.71, (75, 0, 130), 0.2),
        (0.85, (148, 0, 211), 0.2),
        (1, (0, 0, 0), 0)]
    for y in range(height):
        for x in range(width):
            progress = (x / width + y / height) / 2
            (r, g, b, a) = (0, 0, 0, 0)
            for i in range(len(color_stops) - 1):
                (p1, c1, a1) = color_stops[i]
                (p2, c2, a2) = color_stops[i + 1]
                if  <= p1, progress or p1, progress <= p2:
                    pass
                
                int(c1[0] + (c2[0] - c1[0]) * t) = (progress - p1) / (p2 - p1) if p2 > p1 else 0
                g = int(c1[1] + (c2[1] - c1[1]) * t)
                b = int(c1[2] + (c2[2] - c1[2]) * t)
                a = int(255 * opacity * (a1 + (a2 - a1) * t) * intensity * 0.5)
            if a > 0:
                img.putpixel((x, y), (r, g, b, a))
            img = img.filter(ImageFilter.GaussianBlur(radius = width * 0.05))
            return img


def generate_overlay_image(overlay_type = None, width = None, height = None, intensity = (0.8, 0.8), opacity = ('overlay_type', str, 'width', int, 'height', int, 'intensity', float, 'opacity', float, 'return', Optional[Image.Image])):
    '''
    오버레이 타입에 맞는 이미지 생성

    Args:
        overlay_type: 오버레이 타입 (floating_lights, particles, etc.)
        width: 영상 너비
        height: 영상 높이
        intensity: 강도 (0-1)
        opacity: 투명도 (0-1)

    Returns:
        RGBA 이미지 또는 None (지원하지 않는 타입)
    '''
    generators = {
        'floating_lights': generate_floating_lights,
        'particles': generate_particles,
        'bokeh': generate_bokeh,
        'light_leak': generate_light_leak,
        'fog': generate_fog,
        'lens_flare': generate_lens_flare,
        'glow_orbs': generate_glow_orbs,
        'prism': generate_prism }
    generator = generators.get(overlay_type)
    if generator:
        return generator(width, height, intensity, opacity)


def save_overlay_to_temp(img = None, prefix = None):
    '''
    오버레이 이미지를 임시 파일로 저장

    Args:
        img: RGBA 이미지
        prefix: 파일명 접두사

    Returns:
        저장된 파일 경로

    Warning:
        이 함수는 임시 파일을 생성하지만 자동으로 삭제하지 않습니다.
        호출자는 반드시 사용 후 os.unlink(path)로 파일을 삭제해야 합니다.

    Example:
        >>> temp_path = save_overlay_to_temp(img)
        >>> try:
        >>>     # 파일 사용
        >>>     process_image(temp_path)
        >>> finally:
        >>>     os.unlink(temp_path)
    '''
    (fd, path) = tempfile.mkstemp(suffix = '.png', prefix = f'''{prefix}_''')
    os.close(fd)
    img.save(path, 'PNG')
    return path
