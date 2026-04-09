# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: thumbnail_similarity_service.pyc (Python 3.11)

'''
Thumbnail Similarity Service
이미지 유사도 분석 (Perceptual Hashing)

Features:
- pHash (Perceptual Hash) 기반 유사도 계산
- 빠른 중복 감지
- 색상 히스토그램 유사도
'''
import logging
from typing import Dict, List, Tuple
from PIL import Image
from io import BytesIO
import numpy as np
import imagehash
logger = logging.getLogger(__name__)

class ThumbnailSimilarityService:
    '''썸네일 유사도 분석 서비스'''
    
    def __init__(self = None, hash_size = None):
        '''
        Initialize similarity service

        Args:
            hash_size: Hash size for perceptual hashing (default 8)
        '''
        self.hash_size = hash_size

    
    def calculate_perceptual_similarity(self = None, image1_bytes = None, image2_bytes = None):
        '''
        Calculate perceptual similarity using pHash

        Args:
            image1_bytes: First image bytes
            image2_bytes: Second image bytes

        Returns:
            Similarity score (0-100, higher = more similar)
        '''
        
        try:
            img1 = Image.open(BytesIO(image1_bytes))
            img2 = Image.open(BytesIO(image2_bytes))
            hash1 = imagehash.phash(img1, hash_size = self.hash_size)
            hash2 = imagehash.phash(img2, hash_size = self.hash_size)
            hamming_distance = hash1 - hash2
            max_distance = self.hash_size ** 2
            similarity = (1 - hamming_distance / max_distance) * 100
            return max(0, min(100, similarity))
        except Exception:
            e = None
            logger.error(f'''Perceptual similarity calculation failed: {e}''')
            e = None
            del e
            return 0
            e = None
            del e


    
    def calculate_color_similarity(self = None, image1_bytes = None, image2_bytes = None):
        '''
        Calculate color histogram similarity

        Args:
            image1_bytes: First image bytes
            image2_bytes: Second image bytes

        Returns:
            Color similarity score (0-100)
        '''
        
        try:
            img1 = Image.open(BytesIO(image1_bytes)).convert('RGB')
            img2 = Image.open(BytesIO(image2_bytes)).convert('RGB')
            img1 = img1.resize((256, 256))
            img2 = img2.resize((256, 256))
            hist1_r = np.histogram(np.array(img1)[(:, :, 0)], bins = 256, range = (0, 256))[0]
            hist1_g = np.histogram(np.array(img1)[(:, :, 1)], bins = 256, range = (0, 256))[0]
            hist1_b = np.histogram(np.array(img1)[(:, :, 2)], bins = 256, range = (0, 256))[0]
            hist2_r = np.histogram(np.array(img2)[(:, :, 0)], bins = 256, range = (0, 256))[0]
            hist2_g = np.histogram(np.array(img2)[(:, :, 1)], bins = 256, range = (0, 256))[0]
            hist2_b = np.histogram(np.array(img2)[(:, :, 2)], bins = 256, range = (0, 256))[0]
            hist1_r = hist1_r / np.sum(hist1_r)
            hist1_g = hist1_g / np.sum(hist1_g)
            hist1_b = hist1_b / np.sum(hist1_b)
            hist2_r = hist2_r / np.sum(hist2_r)
            hist2_g = hist2_g / np.sum(hist2_g)
            hist2_b = hist2_b / np.sum(hist2_b)
            corr_r = np.corrcoef(hist1_r, hist2_r)[(0, 1)]
            corr_g = np.corrcoef(hist1_g, hist2_g)[(0, 1)]
            corr_b = np.corrcoef(hist1_b, hist2_b)[(0, 1)]
            avg_corr = (corr_r + corr_g + corr_b) / 3
            similarity = ((avg_corr + 1) / 2) * 100
            return max(0, min(100, similarity))
        except Exception:
            e = None
            logger.error(f'''Color similarity calculation failed: {e}''')
            e = None
            del e
            return 0
            e = None
            del e


    
    def compare_thumbnails(self = None, image1_bytes = None, image2_bytes = None, method = ('perceptual',)):
        """
        Comprehensive thumbnail comparison

        Args:
            image1_bytes: First image bytes
            image2_bytes: Second image bytes
            method: Comparison method ('perceptual', 'color', 'both')

        Returns:
            {
                'perceptualScore': 85.5,  # 0-100
                'colorScore': 78.2,       # 0-100
                'overallScore': 81.85,    # 0-100
                'isDuplicate': True       # overallScore > 90
            }
        """
        result = {
            'perceptualScore': None,
            'colorScore': None,
            'overallScore': 0,
            'isDuplicate': False }
        
        try:
            if method in ('perceptual', 'both'):
                result['perceptualScore'] = self.calculate_perceptual_similarity(image1_bytes, image2_bytes)
            if method in ('color', 'both'):
                result['colorScore'] = self.calculate_color_similarity(image1_bytes, image2_bytes)
            if method == 'perceptual':
                result['overallScore'] = result['perceptualScore']
            elif method == 'color':
                result['overallScore'] = result['colorScore']
            else:
                result['overallScore'] = result['perceptualScore'] * 0.7 + result['colorScore'] * 0.3
            result['isDuplicate'] = result['overallScore'] > 90
            return result
        except Exception:
            e = None
            logger.error(f'''Thumbnail comparison failed: {e}''')
            del e
            return None
            None = 
            del e


    
    def find_duplicates_in_batch(self = None, image_bytes_list = None, threshold = None):
        '''
        Find duplicate images in a batch

        Args:
            image_bytes_list: List of image bytes
            threshold: Similarity threshold (default 85%)

        Returns:
            List of (index1, index2, similarity_score) tuples
        '''
        duplicates = []
    # WARNING: Decompyle incomplete

    
    def calculate_thumbnail_quality_score(self = None, image_bytes = None):
        """
        Calculate overall thumbnail quality metrics

        Args:
            image_bytes: Thumbnail image bytes

        Returns:
            {
                'contrastScore': 75.0,     # 0-100 (higher = better contrast)
                'colorfulnessScore': 82.0, # 0-100 (higher = more colorful)
                'sharpnessScore': 68.0,    # 0-100 (higher = sharper)
                'overallScore': 75.0       # Average of above
            }
        """
        
        try:
            img = Image.open(BytesIO(image_bytes)).convert('RGB')
            img_array = np.array(img)
            gray = np.mean(img_array, axis = 2)
            contrast = np.std(gray)
            contrast_score = min(contrast * 2, 100)
            b = img_array[(:, :, 2)]
            g = img_array[(:, :, 1)]
            r = img_array[(:, :, 0)]
            rg_diff = np.abs(r.astype(float) - g.astype(float))
            yb_diff = np.abs(0.5 * (r.astype(float) + g.astype(float)) - b.astype(float))
            std_rg = np.std(rg_diff)
            std_yb = np.std(yb_diff)
            colorfulness = np.sqrt(std_rg ** 2 + std_yb ** 2)
            colorfulness_score = min(colorfulness * 2, 100)
            import cv2
            gray_cv = cv2.cvtColor(img_array, cv2.COLOR_RGB2GRAY)
            laplacian = cv2.Laplacian(gray_cv, cv2.CV_64F)
            sharpness = np.var(laplacian)
            sharpness_score = min(sharpness / 10, 100)
            overall_score = (contrast_score + colorfulness_score + sharpness_score) / 3
            return {
                'contrastScore': round(contrast_score, 1),
                'colorfulnessScore': round(colorfulness_score, 1),
                'sharpnessScore': round(sharpness_score, 1),
                'overallScore': round(overall_score, 1) }
        except Exception:
            e = None
            logger.error(f'''Quality score calculation failed: {e}''')
            del e
            return None
            None = 
            del e
