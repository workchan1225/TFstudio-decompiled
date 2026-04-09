# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: conflict_resolver.pyc (Python 3.11)

'''
Dynamic Conflict Resolver - 신뢰도 기반 동적 충돌 해결

하드코딩된 억제 규칙 대신 신뢰도 점수와
스타일 템플릿 호환성으로 충돌을 해결합니다.

핵심 원칙:
- 특정 장르에서 특정 컨텍스트를 완전 차단하지 않음
- 신뢰도 점수로 경쟁하여 승자 결정
- 동점 시 스타일 템플릿과 호환성 높은 쪽 선택
'''
from typing import Dict, List, Optional, Tuple
from dataclasses import dataclass
ConflictInfo = <NODE:12>()
STYLE_COMPATIBILITY_MATRIX = {
    'minhwa': {
        'compatible': [
            'traditional',
            'ink',
            'brush',
            'folk',
            'painterly'],
        'incompatible': {
            'photorealistic': 0.3,
            'cinematic': 0.6,
            '8k': 0.5 } },
    'realistic': {
        'compatible': [
            'cinematic',
            '8k',
            'detailed',
            'photorealistic',
            'film'],
        'incompatible': {
            'anime': 0.5,
            'cartoon': 0.4,
            'stylized': 0.6 } },
    '3d_cartoon': {
        'compatible': [
            'vibrant',
            'stylized',
            '3d',
            'cartoon',
            'colorful'],
        'incompatible': {
            'gritty': 0.5,
            'dark': 0.5,
            'realistic': 0.6 } },
    'anime': {
        'compatible': [
            'cel-shaded',
            'vibrant',
            'anime',
            'manga',
            'stylized'],
        'incompatible': {
            'photorealistic': 0.4,
            'film grain': 0.5 } },
    'traditional_ink': {
        'compatible': [
            'ink wash',
            'brush',
            'monochrome',
            'traditional'],
        'incompatible': {
            'vibrant colors': 0.4,
            'photorealistic': 0.3 } },
    'informational_simple': {
        'compatible': [
            'simple',
            'clean',
            'minimal',
            'flat',
            'diagram'],
        'incompatible': {
            'detailed': 0.5,
            'complex': 0.4,
            'cinematic': 0.5 } } }

class DynamicConflictResolver:
    '''
    신뢰도 기반 동적 충돌 해결기

    하드코딩 규칙 대신 점수 경쟁으로 결정합니다.
    '''
    
    def __init__(self = None, style_template = None, genre = None):
