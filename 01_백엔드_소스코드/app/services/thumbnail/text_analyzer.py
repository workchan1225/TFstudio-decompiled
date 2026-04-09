# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: text_analyzer.pyc (Python 3.11)

'''
Text Analyzer Module (Pipeline Stage 1)
레퍼런스 이미지에서 텍스트 및 스타일 분석

Features:
- Gemini 3.0 Vision API로 텍스트 감지 및 스타일 분석
- 레퍼런스 이미지 종합 분석 (텍스트, 색상, 구도, 분위기)
- OpenCV 기반 색상 팔레트 추출 (보조)
'''
import logging
from typing import Dict, Any, Optional, List
from io import BytesIO
from pathlib import Path
import cv2
import numpy as np
from PIL import Image
from types import ReferenceAnalysisResult, TextElement, TextPosition, FontProperties, ColorInfo, TextEffects, TextAlignment, StyleAnalysis, ColorPalette, LayoutInfo, LayoutAnalysisDetail, ImageDimensions, VisualGrammar, MidjourneyParams, NegativeSpace, TextStyleGuide
logger = logging.getLogger(__name__)

class TextAnalyzer:
    '''
    레퍼런스 이미지 분석 서비스

    Gemini 3.0 Vision을 사용하여 레퍼런스 이미지를
    종합적으로 분석합니다 (텍스트, 스타일, 색상, 구도 등).
    '''
    GEMINI_MODEL = 'gemini-2.5-flash'
    
    def __init__(self):
        self._vision_model = None

    
    def _get_vision_model(self):
        '''Lazy load Gemini 3.0 Vision model'''
        pass
    # WARNING: Decompyle incomplete

    
    def analyze_reference_image(self = None, image_bytes = None, image_path = None, image_url = (None, None, None)):
        '''
        레퍼런스 이미지 종합 분석

        Args:
            image_bytes: 이미지 바이트 데이터
            image_path: 로컬 이미지 경로
            image_url: 이미지 URL (data: 또는 /data/ 형식)

        Returns:
            ReferenceAnalysisResult: 분석 결과
        '''
        pass
    # WARNING: Decompyle incomplete

    
    def _load_image(self = None, image_bytes = None, image_path = None, image_url = (None, None, None)):
        '''이미지 로드 (다양한 소스 지원)'''
        
        try:
            if image_bytes:
                return Image.open(BytesIO(image_bytes))
            if None:
                return Image.open(image_path)
            if None:
                if image_url.startswith('data:'):
                    import base64
                    (header, data) = image_url.split(',', 1)
                    decoded = base64.b64decode(data)
                    return Image.open(BytesIO(decoded))
                if None.startswith('/data/'):
                    get_data_path = get_data_path
                    import app.config.paths
                    relative_path = image_url[len('/data/'):]
                    file_path = get_data_path() / relative_path
                    return Image.open(file_path)
                return None
            except Exception:
                e = None
                logger.error(f'''Failed to load image: {e}''')
                e = None
                del e
                return None
                e = None
                del e


    
    def _analyze_with_gemini(self = None, image = None):
        '''Gemini 3.0 Vision API로 종합 분석'''
        vision_model = self._get_vision_model()
    # WARNING: Decompyle incomplete

    
    def _extract_color_palette(self = None, img_array = None):
        '''OpenCV + K-means로 색상 팔레트 추출'''
        
        try:
            small = cv2.resize(img_array, (150, 150))
            pixels = small.reshape(-1, 3)
            KMeans = KMeans
            import sklearn.cluster
            kmeans = KMeans(n_clusters = 5, random_state = 42, n_init = 10)
            kmeans.fit(pixels)
            colors = []
            for center in kmeans.cluster_centers_:
                b = int(center[2])
                g = int(center[1])
                r = int(center[0])
                hex_color = f'''#{r:02X}{g:02X}{b:02X}'''
                colors.append(hex_color)
            return ColorPalette(main_colors = colors, primary_color = colors[0] if colors else '#FFFFFF', accent_colors = colors[1:3] if len(colors) > 1 else [])
        except ImportError:
            logger.warning('sklearn not available for color extraction')
            return 
            except Exception:
                logger.error(f'''Color palette extraction failed: {e}''')
                del e
                return None
                None = 
                del e


    
    def _build_text_elements(self = None, gemini_result = None, width = None, height = ('gemini_result', Dict[(str, Any)], 'width', int, 'height', int, 'return', List[TextElement])):
        '''Gemini 결과에서 TextElement 리스트 구성'''
        text_elements = []
        raw_elements = gemini_result.get('textElements', [])
        for idx, elem in enumerate(raw_elements):
            pos_data = elem.get('position', { })
            x = pos_data.get('x', 0)
            y = pos_data.get('y', 0)
            w = pos_data.get('width', 100)
            h = pos_data.get('height', 50)
            position = TextPosition(x = x, y = y, width = w, height = h, center_x = x + w // 2, center_y = y + h // 2, ratio_x = round((x + w / 2) / width, 3) if width > 0 else 0.5, ratio_y = round((y + h / 2) / height, 3) if height > 0 else 0.5)
            font = FontProperties(name = 'Detected Font', size_px = elem.get('fontSize', 48), weight = elem.get('fontWeight', 'bold'), style = 'normal')
            color_hex = elem.get('color', '#FFFFFF')
            color = ColorInfo(hex = color_hex, rgb = self._hex_to_rgb(color_hex), opacity = 1)
            effects = TextEffects(shadow_enabled = elem.get('hasShadow', True), shadow_color = elem.get('strokeColor', '#000000'), shadow_blur = 4, shadow_offset_x = 2, shadow_offset_y = 2, border_enabled = elem.get('strokeWidth', 0) > 0, border_color = elem.get('strokeColor', '#000000'), border_width = elem.get('strokeWidth', 0))
            h_align = elem.get('alignment', 'center')
            if position.ratio_y < 0.33:
                pass
            elif position.ratio_y > 0.66:
                pass
            
            v_align = 'middle'
            alignment = TextAlignment(horizontal = h_align if h_align in ('left', 'center', 'right') else 'center', vertical = v_align)
            text_elements.append(TextElement(text_id = f'''text_{idx}''', content = elem.get('content', ''), confidence = gemini_result.get('confidence', 0.8), position = position, font = font, color = color, effects = effects, alignment = alignment))
            except Exception:
                e = 'top'
                logger.warning(f'''Failed to parse text element {idx}: {e}''')
                e = None
                del e
                continue
                e = None
                del e
            return text_elements

    
    def _build_style_analysis(self = None, text_elements = None):
