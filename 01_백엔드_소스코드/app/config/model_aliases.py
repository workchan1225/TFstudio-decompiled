# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: model_aliases.pyc (Python 3.11)

'''
AI 모델 Alias 설정

하드코딩된 모델명 대신 중앙 집중식 alias를 사용합니다.
모델 변경 시 이 파일만 수정하면 됩니다.
'''
TEMPORAL_ANALYZER_MODEL = {
    'standard': 'gemini-2.5-flash',
    'pro-hq': 'gemini-2.5-pro' }
TEMPORAL_MODEL_FALLBACK_CHAIN = [
    'gemini-2.5-flash',
    'gemini-2.5-pro']
SCENE_SPLITTER_MODEL = {
    'standard': 'gemini-2.5-pro',
    'pro-hq': 'gemini-3-pro-preview' }
ANALYSIS_MODEL = {
    'standard': 'gemini-2.5-flash',
    'pro-hq': 'gemini-2.5-pro' }

def get_model_name(model_type = None, purpose = None):
    """
    모델 타입과 용도에 따른 모델명 반환

    Args:
        model_type: 'standard' 또는 'pro-hq'
        purpose: 'temporal', 'scene_split', 'analysis'

    Returns:
        모델명 문자열
    """
    model_maps = {
        'temporal': TEMPORAL_ANALYZER_MODEL,
        'scene_split': SCENE_SPLITTER_MODEL,
        'analysis': ANALYSIS_MODEL }
    model_map = model_maps.get(purpose, ANALYSIS_MODEL)
    return model_map.get(model_type, model_map.get('standard', 'gemini-2.5-flash'))


def get_fallback_chain(purpose = None):
    """
    용도별 fallback 모델 체인 반환

    Args:
        purpose: 'temporal', 'scene_split', 'analysis'

    Returns:
        fallback 모델명 리스트
    """
    fallback_chains = {
        'temporal': TEMPORAL_MODEL_FALLBACK_CHAIN,
        'scene_split': [
            'gemini-2.5-pro',
            'gemini-2.5-flash'],
        'analysis': [
            'gemini-2.5-flash',
            'gemini-2.5-pro'] }
    return fallback_chains.get(purpose, TEMPORAL_MODEL_FALLBACK_CHAIN)

_IMAGE_MODEL_MAP: dict[(str, str)] = {
    'standard': 'gemini-2.5-flash-image',
    'nanobanana': 'gemini-2.5-flash-image',
    'nanobanana2': 'gemini-3.1-flash-image-preview',
    'pro': 'gemini-3-pro-image-preview',
    'pro-hq': 'gemini-3-pro-image-preview',
    'nanobanana-pro': 'gemini-3-pro-image-preview' }
_DEFAULT_IMAGE_MODEL = 'gemini-2.5-flash-image'
VERTEX_AI_IMAGE_LOCATION = 'global'

def get_image_generation_location():
    """이미지 생성용 Vertex AI location 반환.

    Vertex AI 모드면 'global' (preview 모델 호환), 아니면 None.
    get_genai_client(location_override=...) 에 전달.
    """
    
    try:
        resolve_google_auth_config = resolve_google_auth_config
        import app.services.google_auth_service
        config = resolve_google_auth_config()
        if config.auth_mode == 'vertex_ai':
            return VERTEX_AI_IMAGE_LOCATION
    except Exception:
        pass



def resolve_image_model(engine = None, auth_mode = None):
