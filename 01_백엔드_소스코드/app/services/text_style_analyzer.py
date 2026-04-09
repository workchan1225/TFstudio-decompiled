# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: text_style_analyzer.pyc (Python 3.11)

'''
Text Style Analyzer Service
참조 썸네일에서 텍스트 스타일 추출

Features:
- OCR 텍스트 감지
- 색상 추출 (text, stroke, shadow)
- 폰트 크기 추정
- 효과 감지 (glow, gradient, 3D)
'''
import cv2
import numpy as np
import logging
from typing import Dict, List, Optional
from PIL import Image
from io import BytesIO
import colorsys
logger = logging.getLogger(__name__)

class TextStyleAnalyzer:
    '''텍스트 스타일 분석 서비스'''
    
    def analyze_text_style(self = None, image_bytes = None):
        '''
        이미지에서 텍스트 스타일 추출

        Args:
            image_bytes: 이미지 bytes

        Returns:
            {
                "textStyle": {
                    "fontSize": 72,
                    "color": "#FFFFFF",
                    "stroke": {"color": "#000000", "width": 3},
                    "shadow": {"offsetX": 2, "offsetY": 2, "blur": 4, "color": "#000000"}
                },
                "detectedTexts": [
                    {"text": "AMAZING", "position": {"x": 100, "y": 50, "width": 300, "height": 80}}
                ]
            }
        '''
        
        try:
            img = Image.open(BytesIO(image_bytes))
            img_array = np.array(img.convert('RGB'))
            text_regions = self._detect_text_regions(img_array)
            if not text_regions:
                logger.warning('No text detected in image')
                return {
                    'textStyle': self._get_default_style(),
                    'detectedTexts': [] }
            styles = None
            for region in text_regions:
                cropped = self._crop_region(img_array, region)
                style = self._analyze_region_style(cropped, region)
                styles.append(style)
                merged_style = self._merge_styles(styles)
                return {
                    'textStyle': (lambda .0: [ {
'text': region.get('text', ''),
'position': {
'x': region['x'],
'y': region['y'],
'width': region['width'],
'height': region['height'] } } for region in .0 ]),
                    'detectedTexts': text_regions() }
                except Exception:
                    e = None
                    logger.error(f'''Text style analysis failed: {e}''', exc_info = True)
                    del e
                    return None
                    None = 
                    del e


    
    def _detect_text_regions(self = None, image = None):
        '''
        텍스트 영역 감지 (간단한 방법 - OpenCV 기반)

        Note: 실제 프로덕션에서는 Google Cloud Vision API 또는
        Tesseract OCR을 사용하는 것이 더 정확함

        Args:
            image: RGB image array

        Returns:
            List of text regions with bounding boxes
        '''
        
        try:
            gray = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)
            (_, binary) = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)
            (contours, _) = cv2.findContours(binary, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
            regions = []
            for contour in contours:
                (x, y, w, h) = cv2.boundingRect(contour)
                if w > 50 and h > 20 and w < image.shape[1] * 0.8 and h < image.shape[0] * 0.3:
                    aspect_ratio = w / h
                    if  < 1.5, aspect_ratio or 1.5, aspect_ratio < 15:
                        pass
                    
                    regions.append({
                        'x': int(x),
                        'y': int(y),
                        'width': int(w),
                        'height': int(h),
                        'text': 'TEXT' })
                regions.sort(key = (lambda r: r['y']))
                return regions[:5]
                except Exception:
                    logger.error(f'''Text detection failed: {e}''')
                    del e
                    return None
                    None = 
                    del e


    
    def _crop_region(self = None, image = None, region = None):
        '''
        Crop image region

        Args:
            image: Full image
            region: Region dict with x, y, width, height

        Returns:
            Cropped image
        '''
        y = region['y']
        x = region['x']
        h = region['height']
        w = region['width']
        return image[(y:y + h, x:x + w)]

    
    def _analyze_region_style(self = None, region = None, region_info = None):
        '''
        단일 텍스트 영역의 스타일 분석

        Args:
            region: Cropped text region
            region_info: Region metadata

        Returns:
            Style dict
        '''
        text_color = self._extract_text_color(region)
        font_size = self._estimate_font_size(region_info['height'])
        (has_stroke, stroke_color, stroke_width) = self._detect_stroke(region)
        (has_shadow, shadow_params) = self._detect_shadow(region)
        style = {
            'fontSize': font_size,
            'color': text_color }
        if has_stroke:
            style['stroke'] = {
                'color': stroke_color,
                'width': stroke_width }
        if has_shadow:
            style['shadow'] = shadow_params
        return style

    
    def _extract_text_color(self = None, region = None):
        '''
        Extract dominant text color (excluding background)

        Args:
            region: Text region

        Returns:
            Hex color string
        '''
        
        try:
            pixels = region.reshape(-1, 3)
            KMeans = KMeans
            import sklearn.cluster
            kmeans = KMeans(n_clusters = 3, random_state = 0, n_init = 10)
            kmeans.fit(pixels)
            colors = kmeans.cluster_centers_.astype(int)
            labels = kmeans.labels_
            counts = np.bincount(labels)
            sorted_indices = np.argsort(counts)[::-1]
            text_color_idx = sorted_indices[1] if len(sorted_indices) > 1 else sorted_indices[0]
            text_color = colors[text_color_idx]
            return f'''#{text_color[0]:02x}{text_color[1]:02x}{text_color[2]:02x}'''.upper()
        except Exception:
            e = None
            logger.error(f'''Color extraction failed: {e}''')
            e = None
            del e
            return '#FFFFFF'
            e = None
            del e


    
    def _estimate_font_size(self = None, region_height = None):
        '''
        Estimate font size from region height

        Rough approximation: font_size ≈ height * 0.8

        Args:
            region_height: Height of text region in pixels

        Returns:
            Estimated font size in points
        '''
        estimated_size = int(region_height * 0.75)
        return max(12, min(estimated_size, 200))

    
    def _detect_stroke(self = None, region = None):
        '''
        Detect text stroke (outline)

        Args:
            region: Text region

        Returns:
            (has_stroke, stroke_color, stroke_width)
        '''
        
        try:
            gray = cv2.cvtColor(region, cv2.COLOR_RGB2GRAY)
            edges = cv2.Canny(gray, 50, 150)
            edge_ratio = np.sum(edges > 0) / edges.size
            has_stroke = edge_ratio > 0.1
            if has_stroke:
                edge_mask = edges > 0
                if np.any(edge_mask):
                    edge_pixels = region[edge_mask]
                    avg_edge_color = np.mean(edge_pixels, axis = 0).astype(int)
                    stroke_color = f'''#{avg_edge_color[0]:02x}{avg_edge_color[1]:02x}{avg_edge_color[2]:02x}'''.upper()
                else:
                    stroke_color = '#000000'
                stroke_width = max(1, int(region.shape[0] * 0.05))
                return (True, stroke_color, stroke_width)
            return None
        except Exception:
            e = None
            logger.error(f'''Stroke detection failed: {e}''')
            e = None
            del e
            return (False, None, 0)
            e = None
            del e


    
    def _detect_shadow(self = None, region = None):
        '''
        Detect text shadow

        Args:
            region: Text region

        Returns:
            (has_shadow, shadow_params)
        '''
        
        try:
            gray = cv2.cvtColor(region, cv2.COLOR_RGB2GRAY)
            gx = cv2.Sobel(gray, cv2.CV_64F, 1, 0, ksize = 3)
            gy = cv2.Sobel(gray, cv2.CV_64F, 0, 1, ksize = 3)
            gradient_mag = np.sqrt(gx ** 2 + gy ** 2)
            avg_gradient = np.mean(gradient_mag)
            has_shadow = avg_gradient > 20
            if has_shadow:
                shadow_params = {
                    'offsetX': 2,
                    'offsetY': 2,
                    'blur': 4,
                    'color': '#000000' }
                return (True, shadow_params)
            return None
        except Exception:
            e = None
            logger.error(f'''Shadow detection failed: {e}''')
            e = None
            del e
            return (False, None)
            e = None
            del e


    
    def _merge_styles(self = None, styles = None):
        '''
        Merge multiple style dicts into one (most common values)

        Args:
            styles: List of style dicts

        Returns:
            Merged style dict
        '''
        if not styles:
            return self._get_default_style()
        avg_font_size = np.mean((lambda .0: [ s['fontSize'] for s in .0 ])(styles()))
        colors = styles()
        most_common_color = max(set(colors), key = colors.count)
        merged = {
            'fontSize': avg_font_size,
            'color': most_common_color }
        strokes = styles()
        if strokes:
            merged['stroke'] = strokes[0]
        shadows = styles()
        if shadows:
            merged['shadow'] = shadows[0]
        return merged

    
    def _get_default_style(self = None):
        '''
        Get default text style (fallback)

        Returns:
            Default style dict
        '''
        return {
            'fontSize': 72,
            'color': '#FFFFFF',
            'stroke': {
                'color': '#000000',
                'width': 3 },
            'shadow': {
                'offsetX': 2,
                'offsetY': 2,
                'blur': 4,
                'color': '#000000' } }

    
    def extract_dominant_colors(self = None, image_bytes = None, k = None):
        '''
        Extract dominant colors from image

        Args:
            image_bytes: Image bytes
            k: Number of colors to extract

        Returns:
            List of hex color strings
        '''
        
        try:
            img = Image.open(BytesIO(image_bytes))
            img_array = np.array(img.convert('RGB'))
            pixels = img_array.reshape(-1, 3)
            if len(pixels) > 10000:
                indices = np.random.choice(len(pixels), 10000, replace = False)
                pixels = pixels[indices]
            KMeans = KMeans
            import sklearn.cluster
            kmeans = KMeans(n_clusters = k, random_state = 0, n_init = 10)
            kmeans.fit(pixels)
            colors = kmeans.cluster_centers_.astype(int)
            hex_colors = colors()
            return hex_colors
        except Exception:
            e = None
            logger.error(f'''Dominant color extraction failed: {e}''')
            del e
            return None
            None = 
            del e
