# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: subtitle_layer_utils.pyc (Python 3.11)

'''
Subtitle Layer Utils - TTS별 자막 레이어 관리

각 TTS 모델이 생성한 자막을 subtitle_layers에 저장/업데이트합니다.
기존 레이어를 덮어쓰지 않고 TTS 모델별로 별도 레이어를 유지합니다.
'''
import logging
from typing import List, Optional
from sqlalchemy.orm.attributes import flag_modified
logger = logging.getLogger(__name__)
TTS_LAYER_IDS = {
    'web': 'web-tts-layer',
    'google': 'google-tts-layer',
    'edge': 'edge-tts-layer',
    'chirp3hd': 'chirp3hd-tts-layer',
    'gemini': 'chirp3hd-tts-layer',
    'gemini-native': 'gemini-native-tts-layer',
    'speaker': 'speaker-tts-layer',
    'speaker-merged': 'speaker-tts-layer' }

def update_or_add_subtitle_layer(project, layer_id, segments, layer_name = None, visible = None, order = None, style = ('자막', True, 0, None, None), language = ('layer_id', str, 'segments', List[dict], 'layer_name', str, 'visible', bool, 'order', int, 'style', Optional[dict], 'language', Optional[str], 'return', None)):
    """
    프로젝트의 subtitle_layers에 레이어 추가 또는 업데이트

    기존 레이어가 있으면 업데이트하고, 없으면 새로 추가합니다.
    다른 TTS 모델의 레이어는 유지됩니다.

    Args:
        project: Project 모델 인스턴스
        layer_id: 레이어 ID (예: 'google-tts-layer', 'edge-tts-layer')
        segments: 자막 세그먼트 리스트 [{id, start, end, text}, ...]
        layer_name: 레이어 표시 이름
        visible: 레이어 표시 여부
        order: 레이어 순서
        style: 스타일 설정 (선택)
        language: 언어 이름 (예: '한국어', '日本語') - 다국어 지원
    """
    if not segments:
        logger.warning(f'''[SubtitleLayer] Empty segments for layer {layer_id}, skipping''')
        return None
    new_layer = {
        'id': None,
        'name': layer_name,
        'visible': visible,
        'order': order,
        'segments': segments }
    if style:
        new_layer['style'] = style
    if not project.subtitle_layers:
        existing_layers = []
        if not isinstance(existing_layers, list):
            existing_layers = []
    layer_index = None
# WARNING: Decompyle incomplete


def get_subtitle_layer_by_id(project = None, layer_id = None):
    '''
    특정 ID의 자막 레이어 가져오기

    Args:
        project: Project 모델 인스턴스
        layer_id: 레이어 ID

    Returns:
        레이어 dict 또는 None
    '''
    if not project.subtitle_layers:
        return None
    for layer in None.subtitle_layers:
        if isinstance(layer, dict) and layer.get('id') == layer_id:
            
            return None, layer
        return None


def get_subtitle_layer_by_tts_type(project = None, tts_type = None):
    """
    TTS 타입으로 자막 레이어 가져오기

    Args:
        project: Project 모델 인스턴스
        tts_type: TTS 타입 ('google', 'edge', 'chirp3hd', 'web')

    Returns:
        레이어 dict 또는 None
    """
    layer_id = TTS_LAYER_IDS.get(tts_type)
    if not layer_id:
        logger.warning(f'''[SubtitleLayer] Unknown TTS type: {tts_type}''')
        return None
    return None(project, layer_id)


def remove_subtitle_layer(project = None, layer_id = None):
    '''
    특정 ID의 자막 레이어 제거

    Args:
        project: Project 모델 인스턴스
        layer_id: 레이어 ID

    Returns:
        제거 성공 여부
    '''
    pass
# WARNING: Decompyle incomplete


def list_subtitle_layer_ids(project = None):
