# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: overlay.pyc (Python 3.11)

'''
Overlay Type Definitions
오버레이 관련 타입 정의
'''
from enum import Enum
from typing import TypedDict, List, Optional
from datetime import datetime

class OverlayType(Enum, str):
    '''오버레이 종류'''
    FILM_GRAIN = 'film_grain'
    DUST = 'dust'
    LIGHT_LEAK = 'light_leak'
    RAIN = 'rain'
    SNOW = 'snow'
    FOG = 'fog'
    SPARKLE = 'sparkle'
    CUSTOM = 'custom'


class BlendMode(Enum, str):
    '''블렌드 모드'''
    SCREEN = 'screen'
    MULTIPLY = 'multiply'
    OVERLAY = 'overlay'
    LIGHTEN = 'lighten'
    SOFTLIGHT = 'soft_light'
    HARDLIGHT = 'hard_light'
    NORMAL = 'normal'


class OverlayItem(TypedDict):
    added_at: str = '오버레이 라이브러리 아이템'


class OverlayTrack(TypedDict):
    end_time: Optional[float] = '프로젝트 오버레이 트랙 설정'


class OverlaySettings(TypedDict):
    overlays: List[OverlayTrack] = '프로젝트 오버레이 설정'

BLEND_MODE_RECOMMENDATIONS = {
    BlendMode.LIGHTEN: [
        OverlayType.DUST],
    BlendMode.OVERLAY: [
        OverlayType.LIGHT_LEAK],
    BlendMode.MULTIPLY: [
        OverlayType.FOG],
    BlendMode.SCREEN: [
        OverlayType.FILM_GRAIN,
        OverlayType.DUST,
        OverlayType.LIGHT_LEAK,
        OverlayType.SPARKLE,
        OverlayType.RAIN,
        OverlayType.SNOW] }
BUILTIN_OVERLAYS = [
    {
        'id': 'builtin_retro_80s',
        'name': '80년대 텍스처',
        'type': OverlayType.CUSTOM.value,
        'filename': '160780-822846850_small.mp4',
        'recommended_blend_mode': BlendMode.SCREEN.value,
        'default_opacity': 0.6,
        'tags': [
            'retro',
            '80s',
            'texture'] },
    {
        'id': 'builtin_vhs_noise',
        'name': 'VHS 노이즈',
        'type': OverlayType.CUSTOM.value,
        'filename': '191238-889684892.mp4',
        'recommended_blend_mode': BlendMode.SCREEN.value,
        'default_opacity': 0.5,
        'tags': [
            'vhs',
            'noise',
            'vintage',
            'texture'] },
    {
        'id': 'builtin_static_noise',
        'name': '스태틱 노이즈',
        'type': OverlayType.CUSTOM.value,
        'filename': '200560-913040167_small.mp4',
        'recommended_blend_mode': BlendMode.SCREEN.value,
        'default_opacity': 0.4,
        'tags': [
            'static',
            'noise',
            'tv',
            'texture'] },
    {
        'id': 'builtin_film_frame',
        'name': '필름 프레임',
        'type': OverlayType.CUSTOM.value,
        'filename': '257447_small.mp4',
        'recommended_blend_mode': BlendMode.SCREEN.value,
        'default_opacity': 0.7,
        'tags': [
            'film',
            'frame',
            'texture'] },
    {
        'id': 'builtin_film_damage',
        'name': '필름 손상',
        'type': OverlayType.DUST.value,
        'filename': '267445.mp4',
        'recommended_blend_mode': BlendMode.SCREEN.value,
        'default_opacity': 0.6,
        'tags': [
            'film',
            'damage',
            'vintage',
            'texture'] },
    {
        'id': 'builtin_prism_retro',
        'name': '프리즘 레트로',
        'type': OverlayType.LIGHT_LEAK.value,
        'filename': '37145-412292849.mp4',
        'recommended_blend_mode': BlendMode.SCREEN.value,
        'default_opacity': 0.6,
        'tags': [
            'prism',
            'retro',
            'texture'] },
    {
        'id': 'builtin_grunge_crack',
        'name': '그런지 크랙',
        'type': OverlayType.CUSTOM.value,
        'filename': '81187-576082861.mp4',
        'recommended_blend_mode': BlendMode.SCREEN.value,
        'default_opacity': 0.5,
        'tags': [
            'grunge',
            'crack',
            'texture'] },
    {
        'id': 'builtin_retro_film',
        'name': '레트로 필름',
        'type': OverlayType.CUSTOM.value,
        'filename': '223849.mp4',
        'recommended_blend_mode': BlendMode.SCREEN.value,
        'default_opacity': 0.6,
        'tags': [
            'retro',
            'film',
            'texture'] },
    {
        'id': 'builtin_speed_lines',
        'name': '스피드 라인',
        'type': OverlayType.CUSTOM.value,
        'filename': '118783-715736187.mp4',
        'recommended_blend_mode': BlendMode.SCREEN.value,
        'default_opacity': 0.7,
        'tags': [
            'speed',
            'lines',
            'motion',
            'atmospheric'] },
    {
        'id': 'builtin_fog_smoke',
        'name': '안개/연기',
        'type': OverlayType.FOG.value,
        'filename': '66070-516904774.mp4',
        'recommended_blend_mode': BlendMode.SCREEN.value,
        'default_opacity': 0.6,
        'tags': [
            'fog',
            'smoke',
            'atmospheric'] },
    {
        'id': 'builtin_snow',
        'name': '눈 내림',
        'type': OverlayType.SNOW.value,
        'filename': '150150-797999302.mp4',
        'recommended_blend_mode': BlendMode.SCREEN.value,
        'default_opacity': 0.8,
        'tags': [
            'snow',
            'weather',
            'winter',
            'particle'] },
    {
        'id': 'builtin_glitter_sparkles',
        'name': '글리터 스파클',
        'type': OverlayType.SPARKLE.value,
        'filename': '15712-266043579_small.mp4',
        'recommended_blend_mode': BlendMode.SCREEN.value,
        'default_opacity': 0.8,
        'tags': [
            'glitter',
            'sparkle',
            'shine',
            'particle'] },
    {
        'id': 'builtin_fire_particles',
        'name': '불꽃 파티클',
        'type': OverlayType.CUSTOM.value,
        'filename': '219749.mp4',
        'recommended_blend_mode': BlendMode.SCREEN.value,
        'default_opacity': 0.8,
        'tags': [
            'fire',
            'particles',
            'particle'] },
    {
        'id': 'builtin_confetti',
        'name': '컨페티',
        'type': OverlayType.CUSTOM.value,
        'filename': '31150-384242148_small.mp4',
        'recommended_blend_mode': BlendMode.SCREEN.value,
        'default_opacity': 0.8,
        'tags': [
            'confetti',
            'celebration',
            'particle'] },
    {
        'id': 'builtin_floating_dots',
        'name': '떠다니는 점',
        'type': OverlayType.CUSTOM.value,
        'filename': '76733-560201119.mp4',
        'recommended_blend_mode': BlendMode.SCREEN.value,
        'default_opacity': 0.7,
        'tags': [
            'dots',
            'floating',
            'particle'] },
    {
        'id': 'builtin_fire_sparks',
        'name': '불꽃 스파크',
        'type': OverlayType.CUSTOM.value,
        'filename': '84469-585181045_small.mp4',
        'recommended_blend_mode': BlendMode.SCREEN.value,
        'default_opacity': 0.8,
        'tags': [
            'fire',
            'sparks',
            'particle'] },
    {
        'id': 'builtin_rain_overlay',
        'name': '비 오버레이',
        'type': OverlayType.RAIN.value,
        'filename': '166277-834580701.mp4',
        'recommended_blend_mode': BlendMode.SCREEN.value,
        'default_opacity': 0.7,
        'tags': [
            'rain',
            'overlay',
            'atmospheric'] },
    {
        'id': 'builtin_shimmer_glow',
        'name': '쉬머 글로우',
        'type': OverlayType.LIGHT_LEAK.value,
        'filename': '243313.mp4',
        'recommended_blend_mode': BlendMode.SCREEN.value,
        'default_opacity': 0.8,
        'tags': [
            'shimmer',
            'glow',
            'atmospheric'] },
    {
        'id': 'builtin_rain_droplets',
        'name': '빗방울',
        'type': OverlayType.RAIN.value,
        'filename': '70029-533273229.mp4',
        'recommended_blend_mode': BlendMode.SCREEN.value,
        'default_opacity': 0.7,
        'tags': [
            'rain',
            'droplets',
            'atmospheric'] },
    {
        'id': 'builtin_filmstrip_projector',
        'name': '필름스트립 프로젝터',
        'type': OverlayType.CUSTOM.value,
        'filename': '265403_small.mp4',
        'recommended_blend_mode': BlendMode.SCREEN.value,
        'default_opacity': 0.7,
        'tags': [
            'filmstrip',
            'projector',
            'texture'] },
    {
        'id': 'builtin_mosaic_blur',
        'name': '모자이크 블러',
        'type': OverlayType.CUSTOM.value,
        'filename': '265533_small.mp4',
        'recommended_blend_mode': BlendMode.SCREEN.value,
        'default_opacity': 0.5,
        'tags': [
            'mosaic',
            'blur',
            'texture'] },
    {
        'id': 'builtin_dust_particles',
        'name': '먼지 파티클',
        'type': OverlayType.DUST.value,
        'filename': '169399-841079604.mp4',
        'recommended_blend_mode': BlendMode.SCREEN.value,
        'default_opacity': 0.6,
        'tags': [
            'dust',
            'particles',
            'particle'] },
    {
        'id': 'builtin_snow_falling_alt',
        'name': '눈 내림 (대체)',
        'type': OverlayType.SNOW.value,
        'filename': '246642_small.mp4',
        'recommended_blend_mode': BlendMode.SCREEN.value,
        'default_opacity': 0.8,
        'tags': [
            'snow',
            'falling',
            'particle'] },
    {
        'id': 'builtin_joy_particles',
        'name': '행복 파티클',
        'type': OverlayType.SPARKLE.value,
        'filename': '42735-432102932.mp4',
        'recommended_blend_mode': BlendMode.SCREEN.value,
        'default_opacity': 0.8,
        'tags': [
            'joy',
            'particles',
            'particle'] },
    {
        'id': 'builtin_golden_particles',
        'name': '골든 파티클',
        'type': OverlayType.SPARKLE.value,
        'filename': '68637-528689451_small.mp4',
        'recommended_blend_mode': BlendMode.SCREEN.value,
        'default_opacity': 0.8,
        'tags': [
            'golden',
            'particles',
            'particle'] }]
