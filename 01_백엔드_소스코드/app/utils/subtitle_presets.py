# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: subtitle_presets.pyc (Python 3.11)

'''
자막 스타일 프리셋 정의
사용자가 빠르게 선택할 수 있는 미리 정의된 자막 스타일
'''
SUBTITLE_PRESETS = {
    'youtube': {
        'name': 'YouTube 스타일',
        'description': '유튜브에서 많이 사용되는 기본 자막 스타일',
        'fontFamily': 'Arial',
        'fontSize': 28,
        'fontColor': '#FFFFFF',
        'backgroundColor': 'rgba(0,0,0,0.75)',
        'strokeColor': '#000000',
        'strokeWidth': 3,
        'position': 'bottom',
        'alignment': 'center' },
    'professional': {
        'name': '전문가용',
        'description': '깔끔하고 전문적인 스타일',
        'fontFamily': 'Arial',
        'fontSize': 24,
        'fontColor': '#FFFFFF',
        'backgroundColor': 'rgba(0,0,0,0.85)',
        'strokeColor': '#1A1A1A',
        'strokeWidth': 2,
        'position': 'bottom',
        'alignment': 'center' },
    'bold': {
        'name': '볼드체',
        'description': '눈에 띄는 강조 스타일',
        'fontFamily': 'Arial',
        'fontSize': 32,
        'fontColor': '#FFFF00',
        'backgroundColor': 'rgba(0,0,0,0.9)',
        'strokeColor': '#000000',
        'strokeWidth': 4,
        'position': 'bottom',
        'alignment': 'center' },
    'minimal': {
        'name': '미니멀',
        'description': '깔끔한 미니멀 스타일 (배경 없음)',
        'fontFamily': 'Arial',
        'fontSize': 26,
        'fontColor': '#FFFFFF',
        'backgroundColor': 'rgba(0,0,0,0)',
        'strokeColor': '#000000',
        'strokeWidth': 3,
        'position': 'bottom',
        'alignment': 'center' },
    'retro': {
        'name': '레트로',
        'description': '복고풍 자막 스타일',
        'fontFamily': 'Arial',
        'fontSize': 30,
        'fontColor': '#00FF00',
        'backgroundColor': 'rgba(0,0,0,0.8)',
        'strokeColor': '#004400',
        'strokeWidth': 2,
        'position': 'bottom',
        'alignment': 'center' } }

def get_preset(preset_name = None):
    '''
    프리셋 이름으로 자막 스타일 가져오기

    Args:
        preset_name: 프리셋 이름 (youtube, professional, bold, minimal, retro)

    Returns:
        자막 스타일 딕셔너리
    '''
    return SUBTITLE_PRESETS.get(preset_name, SUBTITLE_PRESETS['youtube'])


def list_presets():
    '''
    모든 사용 가능한 프리셋 목록 반환

    Returns:
        프리셋 딕셔너리 (이름 -> 스타일)
    '''
    return SUBTITLE_PRESETS


def get_preset_names():
    '''
    프리셋 이름 목록만 반환

    Returns:
        프리셋 이름 리스트
    '''
    return list(SUBTITLE_PRESETS.keys())
