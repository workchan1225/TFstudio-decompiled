# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: font_utils.pyc (Python 3.11)

'''
폰트 경로 관리 유틸리티

PC가 변경되거나 폴더 구조가 다른 경우에도 폰트 디렉토리를 찾을 수 있도록
여러 가능한 경로를 탐색합니다.
'''
import os
from pathlib import Path
from typing import Optional
import logging
logger = logging.getLogger(__name__)
_FONTS_DIR_CACHE: Optional[str] = None

def find_fonts_directory():
    '''
    폰트 디렉토리를 찾습니다.

    여러 가능한 위치를 순서대로 탐색:
    1. 환경 변수 FONTS_DIR
    2. 중앙 경로 설정의 static/fonts

    Returns:
        폰트 디렉토리 절대 경로 또는 None
    '''
    pass
# WARNING: Decompyle incomplete


def get_fonts_directory():
    '''
    폰트 디렉토리를 반환합니다.
    찾을 수 없는 경우 기본 경로를 반환합니다.

    Returns:
        폰트 디렉토리 절대 경로
    '''
    fonts_dir = find_fonts_directory()
    if fonts_dir:
        return fonts_dir
    get_fonts_path = get_fonts_path
    import app.config.paths
    default_path = get_fonts_path()
    return str(default_path.resolve()) if isinstance(default_path, Path) else str(Path(default_path).resolve())


def get_font_file_path(font_filename = None):
    """
    특정 폰트 파일의 전체 경로를 반환합니다.

    Args:
        font_filename: 폰트 파일명 (예: 'Pretendard-Bold.otf')

    Returns:
        폰트 파일 절대 경로 또는 None
    """
    fonts_dir = get_fonts_directory()
    font_path = os.path.join(fonts_dir, font_filename)
    if os.path.exists(font_path):
        return font_path


def clear_cache():
    '''폰트 디렉토리 캐시를 초기화합니다.'''
    global _FONTS_DIR_CACHE
    _FONTS_DIR_CACHE = None
    logger.info('[FontUtils] Cache cleared')
