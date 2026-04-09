# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: text_placement_optimizer.pyc (Python 3.11)

'''
Text Placement Optimizer Service
스마트 텍스트 배치를 위한 Saliency 기반 최적화

Features:
- Saliency map generation (OpenCV)
- Grid-based position candidates
- Collision detection
- Position scoring (empty space, contrast, alignment)
'''
import cv2
import numpy as np
import logging
from typing import List, Dict, Tuple, Optional
from PIL import Image
from io import BytesIO
logger = logging.getLogger(__name__)

class TextPlacementOptimizer:
    '''텍스트 배치 최적화 서비스'''
    
    def suggest_positions(self = None, background = None, text_size = None, avoid_regions = (None,)):
        '''
        최적의 텍스트 위치 제안 (Saliency map 기반)

        Args:
            background: 배경 이미지 (PIL Image)
            text_size: 텍스트 박스 크기 (width, height)
            avoid_regions: 피해야 할 영역 리스트
                [{"x": 100, "y": 200, "width": 300, "height": 150}, ...]

        Returns:
            List of position suggestions sorted by score
                [{"position": {"x": 100, "y": 500}, "score": 89, "reason": "..."}, ...]
        '''
        
        try:
            img_array = np.array(background.convert('RGB'))
            saliency_map = self.generate_saliency_map(img_array)
            grid = self._create_position_grid(img_array.shape[:2], text_size, step = 50)
            suggestions = []
            for pos in grid:
                if avoid_regions or self._has_collision(pos, text_size, []):
                    continue
                score = self.calculate_position_score(pos, text_size, saliency_map, img_array)
                suggestions.append({
                    'position': {
                        'x': pos[0],
                        'y': pos[1] },
                    'score': int(score),
                    'reason': self._generate_reason(score, pos, img_array.shape[:2]) })
                suggestions.sort(key = (lambda s: s['score']), reverse = True)
                return suggestions[:5]
                except Exception:
                    e = None
                    logger.error(f'''Position suggestion failed: {e}''', exc_info = True)
                    del e
                    return None
                    None = 
                    del e


    
    def generate_saliency_map(self = None, image = None):
        '''
        Saliency map 생성 (OpenCV 사용)

        Args:
            image: BGR 이미지 (numpy array)

        Returns:
            Saliency map (0-1 normalized)
        '''
        
        try:
            gray = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)
            saliency = cv2.saliency.StaticSaliencySpectralResidual_create()
            (success, saliency_map) = saliency.computeSaliency(image)
            if not success:
                logger.warning('Spectral residual failed, using edge detection')
                saliency_map = self._edge_based_saliency(gray)
            saliency_map = cv2.normalize(saliency_map, None, 0, 1, cv2.NORM_MINMAX)
            return saliency_map
        except Exception:
            e = None
            logger.error(f'''Saliency map generation failed: {e}''')
            del e
            return None
            None = 
            del e


    
    def _edge_based_saliency(self = None, gray = None):
        '''
        Fallback: Edge 기반 saliency (간단한 방법)

        Args:
            gray: Grayscale image

        Returns:
            Edge-based saliency map
        '''
        sobelx = cv2.Sobel(gray, cv2.CV_64F, 1, 0, ksize = 3)
        sobely = cv2.Sobel(gray, cv2.CV_64F, 0, 1, ksize = 3)
        magnitude = np.sqrt(sobelx ** 2 + sobely ** 2)
        magnitude = cv2.normalize(magnitude, None, 0, 1, cv2.NORM_MINMAX)
        return magnitude.astype(np.float32)

    
    def calculate_position_score(self, position = None, text_size = None, saliency_map = None, background = ('position', Tuple[(int, int)], 'text_size', Tuple[(int, int)], 'saliency_map', np.ndarray, 'background', np.ndarray, 'return', float)):
        '''
        위치 점수 계산

        Score formula:
            empty_space_score * 0.5 +
            contrast_score * 0.3 +
            alignment_score * 0.2

        Args:
            position: (x, y) position
            text_size: (width, height)
            saliency_map: Saliency map
            background: Background image

        Returns:
            Score (0-100)
        '''
        (x, y) = position
        (w, h) = text_size
        if x + w > background.shape[1] or y + h > background.shape[0]:
            return 0
        text_region = None[(y:y + h, x:x + w)]
        avg_saliency = np.mean(text_region)
        empty_space_score = (1 - avg_saliency) * 100
        contrast_score = self._calculate_contrast(background, x, y, w, h) * 100
        alignment_score = self._calculate_alignment(position, background.shape[:2]) * 100
        total_score = empty_space_score * 0.5 + contrast_score * 0.3 + alignment_score * 0.2
        return min(total_score, 100)

    
    def _calculate_contrast(self, image, x = None, y = None, w = None, h = ('image', np.ndarray, 'x', int, 'y', int, 'w', int, 'h', int, 'return', float)):
        '''
        Calculate background contrast for text readability

        Args:
            image: Background image
            x, y, w, h: Text region

        Returns:
            Contrast score (0-1)
        '''
        
        try:
            region = image[(y:y + h, x:x + w)]
            gray_region = cv2.cvtColor(region, cv2.COLOR_RGB2GRAY)
            std_dev = np.std(gray_region)
            contrast = min(std_dev / 100, 1)
            return contrast
        except Exception:
            e = None
            logger.error(f'''Contrast calculation failed: {e}''')
            e = None
            del e
            return 0.5
            e = None
            del e


    
    def _calculate_alignment(self = None, position = None, image_shape = None):
        '''
        Calculate alignment score

        Prefers:
        - Center positions
        - Rule of thirds positions

        Args:
            position: (x, y)
            image_shape: (height, width)

        Returns:
            Alignment score (0-1)
        '''
        pass
    # WARNING: Decompyle incomplete

    
    def _create_position_grid(self = None, image_shape = None, text_size = None, step = (50,)):
        '''
        Create grid of candidate positions

        Args:
            image_shape: (height, width)
            text_size: (width, height)
            step: Grid step size in pixels

        Returns:
            List of (x, y) positions
        '''
        (h, w) = image_shape
        (text_w, text_h) = text_size
        positions = []
        margin = 30
        for y in range(margin, h - text_h - margin, step):
            for x in range(margin, w - text_w - margin, step):
                positions.append((x, y))
                return positions

    
    def _has_collision(self = None, position = None, text_size = None, avoid_regions = ('position', Tuple[(int, int)], 'text_size', Tuple[(int, int)], 'avoid_regions', List[Dict[(str, int)]], 'return', bool)):
        '''
        Check if position collides with avoid regions

        Args:
            position: (x, y)
            text_size: (width, height)
            avoid_regions: List of regions to avoid

        Returns:
            True if collision detected
        '''
        (x, y) = position
        (w, h) = text_size
        for region in avoid_regions:
            ry = region['y']
            rx = region['x']
            rh = region['height']
            rw = region['width']
            if not x + w < rx and x > rx + rw and y + h < ry and y > ry + rh:
                return True
            return False

    
    def _generate_reason(self = None, score = None, position = None, image_shape = ('score', float, 'position', Tuple[(int, int)], 'image_shape', Tuple[(int, int)], 'return', str)):
        '''
        Generate human-readable reason for score

        Args:
            score: Position score
            position: (x, y)
            image_shape: (height, width)

        Returns:
            Reason string
        '''
        (x, y) = position
        (h, w) = image_shape
        reasons = []
        if score >= 80:
            reasons.append('최적 위치')
        elif score >= 60:
            reasons.append('양호한 위치')
        else:
            reasons.append('사용 가능')
        if y < h // 3:
            reasons.append('상단')
        elif y > 2 * h // 3:
            reasons.append('하단')
        else:
            reasons.append('중앙')
        if x < w // 3:
            reasons.append('좌측')
        elif x > 2 * w // 3:
            reasons.append('우측')
        if score >= 70:
            reasons.append('깨끗한 배경')
        return ', '.join(reasons)

    
    def _get_fallback_positions(self = None, image_size = None, text_size = None):
        '''
        Get fallback positions if saliency detection fails

        Args:
            image_size: (width, height)
            text_size: (text_width, text_height)

        Returns:
            List of fallback positions
        '''
        (w, h) = image_size
        (tw, th) = text_size
        positions = [
            {
                'position': {
                    'x': (w - tw) // 2,
                    'y': 50 },
                'score': 80,
                'reason': '상단 중앙' },
            {
                'position': {
                    'x': (w - tw) // 2,
                    'y': h - th - 50 },
                'score': 75,
                'reason': '하단 중앙' },
            {
                'position': {
                    'x': (w - tw) // 2,
                    'y': (h - th) // 2 },
                'score': 70,
                'reason': '정중앙' },
            {
                'position': {
                    'x': 50,
                    'y': 50 },
                'score': 65,
                'reason': '상단 좌측' },
            {
                'position': {
                    'x': w - tw - 50,
                    'y': 50 },
                'score': 65,
                'reason': '상단 우측' }]
        return positions
