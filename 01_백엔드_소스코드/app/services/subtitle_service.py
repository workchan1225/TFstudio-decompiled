# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: subtitle_service.pyc (Python 3.11)

import logging
from pathlib import Path
import json
import warnings
import re
warnings.filterwarnings('ignore', category = FutureWarning)
from app.utils.file_naming import generate_subtitle_filename
from app.services.subtitle_runtime_style_resolver import calculate_runtime_position, resolve_runtime_subtitle_style, resolve_runtime_title_layer_style
logger = logging.getLogger(__name__)
PREVIEW_LANDSCAPE_WIDTH = 1280
PREVIEW_LANDSCAPE_HEIGHT = 720
PREVIEW_PORTRAIT_WIDTH = 720
PREVIEW_PORTRAIT_HEIGHT = 1280
_FONTS_MAPPING_CACHE = None

def get_fonts_mapping():
    '''폰트 매핑 데이터 로드 (캐시됨)'''
    pass
# WARNING: Decompyle incomplete


def get_font_family_name(font_name = None):
