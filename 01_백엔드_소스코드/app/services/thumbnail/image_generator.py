# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: image_generator.pyc (Python 3.11)

'''
Image Generator Module (Pipeline Stage 5)
NanoBanana Pro (Gemini 3.0 Image) 기반 이미지 생성

Features:
- Gemini 3.0 Pro Image API를 통한 고품질 이미지 생성
- 레퍼런스 이미지 기반 스타일 전이
- 다중 해상도 지원 (1K/2K/4K)
- 품질 검증 및 분석
'''
import os
import uuid
import logging
from typing import Dict, List, Optional, Any, Tuple
from io import BytesIO
import base64
from PIL import Image
import numpy as np
import cv2
from app.services.google_auth_service import get_google_api_key_or_runtime_token, get_google_configuration_error_message
from types import ReferenceAnalysisResult, OptimizationResult, GenerationResult, GeneratedThumbnail, ThumbnailAnalysis, QualityMetrics
logger = logging.getLogger(__name__)

class ImageGenerator:
    '''
    NanoBanana Pro (Gemini 3.0 Image) 기반 이미지 생성 서비스

    레퍼런스 이미지와 최적화된 프롬프트를 사용하여
    고품질 YouTube 썸네일을 생성합니다.
    '''
    RESOLUTION_MAPPING = {
        'HD': '1K',
        'FHD': '1K',
        '1K': '1K',
        '2K': '2K',
        '4K': '4K' }
    
    def __init__(self = None, project_id = None):
        self.project_id = project_id
        self.project_folder = None
        self.thumbnails_folder = None
        if project_id:
            self._setup_folders()
        cascade_path = os.path.join(cv2.data.haarcascades, 'haarcascade_frontalface_default.xml')
        self.face_cascade = cv2.CascadeClassifier(cascade_path)

    
    def _setup_folders(self):
        '''프로젝트 폴더 설정'''
        if not self.project_id:
            return None
        get_projects_path = get_projects_path
        import app.config.paths
        self.project_folder = get_projects_path() / self.project_id
        self.thumbnails_folder = self.project_folder / 'thumbnails'
        self.thumbnails_folder.mkdir(parents = True, exist_ok = True)

    
    def generate_thumbnail(self, prompt, reference_images, analysis, model = None, aspect_ratio = None, resolution = None, apply_text_overlay = (None, 'nanobanana-pro', '16:9', '2K', False, None), text_config = ('prompt', str, 'reference_images', List[Dict[(str, Any)]], 'analysis', Optional[ReferenceAnalysisResult], 'model', str, 'aspect_ratio', str, 'resolution', str, 'apply_text_overlay', bool, 'text_config', Optional[Dict[(str, Any)]], 'return', GenerationResult)):
        '''
        썸네일 이미지 생성

        Args:
            prompt: 최적화된 프롬프트
            reference_images: 레퍼런스 이미지 리스트
                [{"image": PIL.Image, "role": "style|person|background", "weight": 0.0-1.0}]
            analysis: 1단계 분석 결과 (선택)
            model: 사용할 모델 (nanobanana-pro, standard 등)
            aspect_ratio: 종횡비 (16:9, 4:3, 1:1, 9:16)
            resolution: 해상도 (1K, 2K, 4K)
            apply_text_overlay: 텍스트 오버레이 적용 여부
            text_config: 텍스트 설정

        Returns:
            GenerationResult: 생성 결과
        '''
        
        try:
            image_bytes = self._call_gemini_image_api(prompt = prompt, reference_images = reference_images, model = model, aspect_ratio = aspect_ratio, resolution = resolution)
            if apply_text_overlay and text_config:
                image_bytes = self._apply_text_overlay(image_bytes, text_config)
            candidate = self._save_as_candidate(image_data = image_bytes, metadata = {
                'generationMethod': 'ai-pipeline',
                'aiModel': model,
                'prompt': prompt[:500],
                'aspectRatio': aspect_ratio,
                'resolution': resolution })
            thumbnail_analysis = self._analyze_thumbnail_quality(image_bytes, text_config)
            return GenerationResult(candidate = candidate, analysis = thumbnail_analysis, image_bytes = image_bytes)
        except Exception:
            e = None
            logger.error(f'''Thumbnail generation failed: {e}''', exc_info = True)
            raise 
            e = None
            del e


    
    def _call_gemini_image_api(self, prompt, reference_images = None, model = None, aspect_ratio = None, resolution = ('prompt', str, 'reference_images', List[Dict[(str, Any)]], 'model', str, 'aspect_ratio', str, 'resolution', str, 'return', bytes)):
        '''Gemini API로 이미지 생성'''
        pass
    # WARNING: Decompyle incomplete

    
    def _image_to_bytes(self = None, image = None):
        '''PIL Image를 bytes로 변환'''
        buffer = BytesIO()
        if image.mode != 'RGB':
            image = image.convert('RGB')
        image.save(buffer, format = 'JPEG', quality = 95)
        return buffer.getvalue()

    
    def _apply_text_overlay(self = None, background_image = None, text_config = None):
        '''텍스트 오버레이 적용 (한글 지원)'''
        ImageDraw = ImageDraw
        ImageFont = ImageFont
        import PIL
        import platform
        img = Image.open(BytesIO(background_image))
        if img.mode != 'RGBA':
            img = img.convert('RGBA')
        draw = ImageDraw.Draw(img)
        (width, height) = img.size
        main_text = text_config.get('mainText', '')
    # WARNING: Decompyle incomplete

    
    def _save_as_candidate(self = None, image_data = None, metadata = None):
        '''후보로 저장'''
        candidate_id = str(uuid.uuid4())[:8]
        if not self.project_id or self.thumbnails_folder:
            b64_data = base64.b64encode(image_data).decode('utf-8')
            url = f'''data:image/jpeg;base64,{b64_data}'''
            logger.info('[ImageGenerator] Candidate as data URL (no project)')
        else:
            filename = f'''{candidate_id}.jpg'''
            filepath = self.thumbnails_folder / filename
            f = open(filepath, 'wb')
            f.write(image_data)
            None(None, None)
        with None:
            if not None:
                pass
        url = f'''/data/projects/{self.project_id}/thumbnails/{filename}'''.replace('\\', '/')
        logger.info(f'''[ImageGenerator] Candidate saved: {url}''')
        return GeneratedThumbnail(id = candidate_id, url = url, type = 'ai', metadata = metadata)

    
    def _analyze_thumbnail_quality(self = None, image_bytes = None, text_config = None):
        '''썸네일 품질 분석'''
        
        try:
            img = Image.open(BytesIO(image_bytes))
            img_array = np.array(img.convert('RGB'))
            (face_count, face_positions) = self._detect_faces(img_array)
            quality_metrics = self._calculate_quality_metrics(img_array)
            clickability_score = self._calculate_clickability_score(quality_metrics, face_count)
            text_readability = 0
            if text_config and text_config.get('mainText'):
                text_readability = self._calculate_text_readability(quality_metrics, text_config)
            return ThumbnailAnalysis(clickability_score = clickability_score, face_count = face_count, face_positions = face_positions, text_readability = text_readability, quality_metrics = quality_metrics)
        except Exception:
            e = None
            logger.error(f'''Thumbnail analysis failed: {e}''')
            del e
            return None
            None = 
            del e


    
    def _detect_faces(self = None, img_array = None):
        '''얼굴 감지'''
        gray = cv2.cvtColor(img_array, cv2.COLOR_RGB2GRAY)
        faces = self.face_cascade.detectMultiScale(gray, scaleFactor = 1.1, minNeighbors = 5, minSize = (30, 30))
        face_positions = faces()
        return (len(faces), face_positions)

    
    def _calculate_quality_metrics(self = None, img_array = None):
        '''품질 메트릭 계산'''
        gray = cv2.cvtColor(img_array, cv2.COLOR_RGB2GRAY)
        contrast_score = float(np.std(gray))
        b = img_array[(:, :, 2)]
        g = img_array[(:, :, 1)]
        r = img_array[(:, :, 0)]
        rg = r.astype(float) - g.astype(float)
        yb = 0.5 * (r.astype(float) + g.astype(float)) - b.astype(float)
        colorfulness_score = float(np.sqrt(np.std(rg) ** 2 + np.std(yb) ** 2) + 0.3 * np.sqrt(np.mean(rg) ** 2 + np.mean(yb) ** 2))
        laplacian = cv2.Laplacian(gray, cv2.CV_64F)
        sharpness_score = float(laplacian.var())
        return QualityMetrics(contrast_score = min(100, contrast_score), colorfulness_score = min(100, colorfulness_score), sharpness_score = min(100, sharpness_score / 10))

    
    def _calculate_clickability_score(self = None, metrics = None, face_count = None):
        '''클릭 가능성 점수 계산'''
        contrast_weight = 0.3
        color_weight = 0.3
        sharpness_weight = 0.2
        face_weight = 0.2
        contrast_norm = min(1, metrics.contrast_score / 70)
        color_norm = min(1, metrics.colorfulness_score / 50)
        sharpness_norm = min(1, metrics.sharpness_score / 100)
        face_norm = min(1, face_count / 2) if face_count > 0 else 0.5
        score = contrast_weight * contrast_norm + color_weight * color_norm + sharpness_weight * sharpness_norm + face_weight * face_norm
        return round(score, 2)

    
    def _calculate_text_readability(self = None, metrics = None, text_config = None):
        '''텍스트 가독성 점수'''
        font_size = text_config.get('fontSize', 72)
        stroke_width = text_config.get('strokeWidth', 0)
        size_score = min(1, font_size / 48)
        stroke_score = min(1, stroke_width / 3) if stroke_width > 0 else 0.5
        contrast_score = min(1, metrics.contrast_score / 70)
        return round(size_score * 0.4 + stroke_score * 0.3 + contrast_score * 0.3, 2)


_default_generator: Optional[ImageGenerator] = None

def get_image_generator(project_id = None):
    '''
    ImageGenerator 인스턴스 생성/반환

    Args:
        project_id: 프로젝트 ID (없으면 기본 인스턴스 반환)

    Returns:
        ImageGenerator 인스턴스
    '''
    if project_id:
        return ImageGenerator(project_id)
# WARNING: Decompyle incomplete
