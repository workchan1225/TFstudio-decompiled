# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: thumbnail_generation_service.pyc (Python 3.11)

'''
Thumbnail Generation Service
AI 기반 썸네일 생성 및 관리

Features:
- Multi-image composition with NanoBANANA Pro (up to 14 images)
- Text overlay with smart positioning
- Thumbnail candidates management
- Integration with ImageComposerService
'''
import os
import uuid
import logging
from typing import Dict, List, Optional, Any
from pathlib import Path
from datetime import datetime
from io import BytesIO
import base64
from PIL import Image, ImageDraw
import numpy as np
import cv2
from app.models import Project
from app.models.settings import Settings
from app import db
from app.config.paths import get_projects_path, get_data_path, get_static_path
from app.services.ai.google_provider import GoogleProvider
from app.services.image_composer_service import ImageComposerService
from app.services.thumbnail_similarity_service import ThumbnailSimilarityService
from app.services.google_auth_service import get_google_api_key_or_runtime_token, get_google_configuration_error_message
from app.utils.google_sdk import get_genai_client, get_genai_types
logger = logging.getLogger(__name__)

class ThumbnailGenerationService:
    '''썸네일 생성 서비스'''
    
    def __init__(self = None, project_id = None):
        self.project_id = project_id
        self.project_folder = get_projects_path() / project_id
        self.thumbnails_folder = self.project_folder / 'thumbnails'
        self.references_folder = self.thumbnails_folder / 'references'
        self.thumbnails_folder.mkdir(parents = True, exist_ok = True)
        self.references_folder.mkdir(parents = True, exist_ok = True)
        self.google_provider = GoogleProvider()
        self.image_composer = ImageComposerService(project_id)
        self.similarity_service = ThumbnailSimilarityService()
        cascade_path = os.path.join(cv2.data.haarcascades, 'haarcascade_frontalface_default.xml')
        self.face_cascade = cv2.CascadeClassifier(cascade_path)

    
    def generate_advanced_thumbnail(self = None, reference_images = None, scene_image_ids = None, text_overlay = (None, None, None), settings = ('reference_images', List[Dict[(str, Any)]], 'scene_image_ids', Optional[List[str]], 'text_overlay', Optional[Dict[(str, Any)]], 'settings', Optional[Dict[(str, Any)]], 'return', Dict[(str, Any)])):
        '''
        고급 썸네일 생성 (Multi-image composition + Text overlay)

        Args:
            reference_images: Reference images with roles
                [{"url": "...", "role": "background|person|object|style", "weight": 0.0-1.0}]
            scene_image_ids: Optional scene image IDs from project
            text_overlay: Optional text configuration
                {"mainText": "...", "autoPosition": bool, "style": {...}}
            settings: Generation settings
                {"model": "standard|pro-hq", "aspectRatio": "16:9", "resolution": "2k", "subject": "..."}

        Returns:
            Generated thumbnail candidate with metadata
        '''
        pass
    # WARNING: Decompyle incomplete

    
    def _load_reference_images(self = None, reference_images = None):
        '''
        Load and prepare reference images

        Args:
            reference_images: List of reference image configs

        Returns:
            List of loaded images with metadata
        '''
        loaded = []
        for ref in reference_images:
            url = ref['url']
            if url.startswith('data:'):
                image_data = self._base64_to_image(url)
            elif url.startswith('/data/'):
                relative_path = url[len('/data/'):]
                file_path = get_data_path() / relative_path
                image_data = Image.open(file_path)
            else:
                logger.warning(f'''External URL not supported: {url}''')
            if image_data.mode != 'RGB':
                image_data = image_data.convert('RGB')
            loaded.append({
                'image': image_data,
                'role': ref.get('role', 'reference'),
                'weight': ref.get('weight', 1),
                'url': url })
            except Exception:
                e = None
                logger.error(f'''Failed to load reference image {ref.get('url')}: {e}''')
                e = None
                del e
                continue
                e = None
                del e
            return loaded

    
    def _build_multi_image_prompt(self = None, reference_images = None, subject = None, style = (None, None), text_content = ('reference_images', List[Dict[(str, Any)]], 'subject', str, 'style', Optional[str], 'text_content', Optional[str], 'return', str)):
        '''
        Build prompt for NanoBANANA Pro with multiple image references

        Format:
        "Image1: [role description], Image2: [role description],
        Create a YouTube thumbnail with [subject] in [style] style.
        Include text: \'[text]\' prominently displayed."
        '''
        role_descriptions = {
            'background': 'Use as background scene',
            'person': 'Main person/character to include',
            'object': 'Object to feature prominently',
            'style': 'Visual style reference' }
        image_roles = []
        for i, ref in enumerate(reference_images, 1):
            role = ref.get('role', 'reference')
            weight = ref.get('weight', 1)
            role_desc = role_descriptions.get(role, 'Reference image')
            image_roles.append(f'''Image{i}: {role_desc} (weight: {weight:.1f})''')
        prompt_parts = [
            ', '.join(image_roles) if image_roles else '',
            f'''Create a compelling YouTube thumbnail featuring {subject}''' if subject else 'Create a compelling YouTube thumbnail',
            f'''Style: {style}''' if style else '',
            'High contrast, vibrant colors, professional composition, attention-grabbing design']
        prompt = (lambda .0: pass# WARNING: Decompyle incomplete
)(prompt_parts())
        return prompt

    
    def _call_gemini_image_api(self, prompt, reference_images = None, model = None, aspect_ratio = None, resolution = ('prompt', str, 'reference_images', List[Dict[(str, Any)]], 'model', str, 'aspect_ratio', str, 'resolution', str, 'return', bytes)):
        '''
        Call Google Gemini API for image generation

        Uses direct Gemini API call like scene_image_service.py for reliable
        multimodal image generation with reference images.

        Args:
            prompt: Text prompt
            reference_images: Loaded reference images with PIL Image objects
            model: Model name (nanobanana, nanobanana-pro, standard, pro-hq)
            aspect_ratio: Target aspect ratio (16:9, 9:16, 4:3, 1:1)
            resolution: Target resolution (HD, FHD, 2K, 4K)

        Returns:
            Generated image as bytes
        '''
        pass
    # WARNING: Decompyle incomplete

    
    def _apply_text_overlay(self = None, background_image = None, text_config = None):
        """
        Apply text overlay to generated image using PIL directly

        Args:
            background_image: Base image as bytes
            text_config: Text configuration
                {
                    mainText: str,
                    fontSize: int,
                    color: str,
                    strokeColor: str,
                    strokeWidth: int,
                    fontFamily: str,
                    position: {x, y} or str ('top' | 'center' | 'bottom'),
                    floatingTexts: [
                        {
                            text: str,
                            position: 'top-left' | 'top-right' | 'bottom-left' | 'bottom-right' | 'center-left' | 'center-right',
                            fontSize: int,
                            color: str,
                            backgroundColor: str (optional),
                            rotation: int (optional, degrees)
                        }
                    ]
                }

        Returns:
            Image with text overlay as bytes
        """
        ImageFont = ImageFont
        import PIL
        
        try:
            img = Image.open(BytesIO(background_image))
            if img.mode != 'RGBA':
                img = img.convert('RGBA')
            main_text = text_config.get('mainText', '')
            floating_texts = text_config.get('floatingTexts', [])
            if not main_text and floating_texts:
                logger.warning('No text provided for overlay')
                return background_image
            draw = None.Draw(img)
            if main_text:
                self._render_main_text(img, draw, text_config)
            if floating_texts:
                self._render_floating_texts(img, floating_texts)
            if img.mode == 'RGBA':
                background = Image.new('RGB', img.size, (255, 255, 255))
                background.paste(img, mask = img.split()[3] if len(img.split()) > 3 else None)
                img = background
            return self._image_to_bytes(img)
        except Exception:
            e = None
            logger.error(f'''Text overlay failed: {e}''', exc_info = True)
            del e
            return None
            None = 
            del e


    
    def _render_main_text(self = None, img = None, draw = None, text_config = ('img', Image.Image, 'draw', ImageDraw.ImageDraw, 'text_config', Dict[(str, Any)], 'return', None)):
        '''
        Render main text on the image

        Args:
            img: PIL Image object (will be modified in place)
            draw: ImageDraw context
            text_config: Text configuration
        '''
        ImageFont = ImageFont
        import PIL
        main_text = text_config.get('mainText', '')
        if not main_text:
            return None
        font_family = None.get('fontFamily', 'Pretendard-Bold')
        font_size = text_config.get('fontSize', 72)
        color = text_config.get('color', '#FFFFFF')
        stroke_color = text_config.get('strokeColor', '#000000')
        stroke_width = int(text_config.get('strokeWidth', 3))
        logger.info(f'''[TextOverlay] Applying main text: \'{main_text[:30]}...\' font_size={font_size}, color={color}''')
        font = self._get_font(font_family, font_size)
        bbox = draw.textbbox((0, 0), main_text, font = font)
        text_width = bbox[2] - bbox[0]
        text_height = bbox[3] - bbox[1]
        position = text_config.get('position', 'bottom')
    # WARNING: Decompyle incomplete

    
    def _render_floating_texts(self = None, img = None, floating_texts = None):
        '''
        Render floating texts (labels/badges) on the image

        Args:
            img: PIL Image object (will be modified in place)
            floating_texts: List of floating text configurations
        '''
        pass
    # WARNING: Decompyle incomplete

    
    def _hex_to_rgba(self = None, hex_color = None, alpha = None):
        """
        Convert hex color to RGBA tuple

        Args:
            hex_color: Hex color string (e.g., '#FF0000' or '#FF000080')
            alpha: Default alpha value if not specified in hex

        Returns:
            RGBA tuple (r, g, b, a)
        """
        
        try:
            hex_color = hex_color.lstrip('#')
            if len(hex_color) == 6:
                r = int(hex_color[0:2], 16)
                g = int(hex_color[2:4], 16)
                b = int(hex_color[4:6], 16)
                return (r, g, b, alpha)
            if None(hex_color) == 8:
                r = int(hex_color[0:2], 16)
                g = int(hex_color[2:4], 16)
                b = int(hex_color[4:6], 16)
                a = int(hex_color[6:8], 16)
                return (r, g, b, a)
            return (None, 255, 255, alpha)
        except Exception:
            return 


    
    def _get_font(self = None, font_family = None, font_size = None):
        '''
        Load font with fallback to system fonts

        Args:
            font_family: Font family name
            font_size: Font size in pixels

        Returns:
            PIL ImageFont object
        '''
        ImageFont = ImageFont
        import PIL
        font_paths = [
            self.project_folder / 'fonts' / f'''{font_family}.ttf''',
            self.project_folder / 'fonts' / f'''{font_family}.otf''',
            Path(os.environ.get('WINDIR', 'C:/Windows')) / 'Fonts' / f'''{font_family}.ttf''',
            Path(os.environ.get('WINDIR', 'C:/Windows')) / 'Fonts' / f'''{font_family}.otf''',
            Path(os.environ.get('WINDIR', 'C:/Windows')) / 'Fonts' / 'malgun.ttf',
            Path(os.environ.get('WINDIR', 'C:/Windows')) / 'Fonts' / 'NanumGothicBold.ttf',
            Path(os.environ.get('WINDIR', 'C:/Windows')) / 'Fonts' / 'gulim.ttc',
            get_static_path() / 'fonts' / f'''{font_family}.ttf''',
            get_static_path() / 'fonts' / 'Pretendard-Bold.ttf']
        for font_path in font_paths:
            if font_path.exists():
                
                return None, ImageFont.truetype(str(font_path), font_size)
            except Exception:
                continue
            logger.warning(f'''Font \'{font_family}\' not found, using fallback font''')
            
            try:
                os.path.join(windir, 'Fonts', 'arial.ttf') = os.environ.get('WINDIR', 'C:\\Windows')
                return ImageFont.truetype(arial_path, font_size)
            except Exception:
                e = None
                logger.warning(f'''Font fallback failed ({e}), using default''')
                del e
                return None
                None = 
                del e


    
    def _save_as_candidate(self = None, image_data = None, metadata = None):
        '''
        Save generated thumbnail as candidate

        Args:
            image_data: Image bytes
            metadata: Generation metadata

        Returns:
            Candidate object
        '''
        
        try:
            candidate_id = str(uuid.uuid4())[:8]
            filename = f'''{candidate_id}.jpg'''
            file_path = self.thumbnails_folder / filename
            img = Image.open(BytesIO(image_data))
            img.save(file_path, 'JPEG', quality = 95)
            url = f'''/data/projects/{self.project_id}/thumbnails/{filename}'''
            candidate = {
                'id': candidate_id,
                'url': url,
                'type': 'ai',
                'createdAt': datetime.now().isoformat(),
                'metadata': metadata }
            project = Project.query.get(self.project_id)
            if project:
                candidates = list(project.thumbnail_candidates) if project.thumbnail_candidates else []
                candidates.append(candidate)
                project.thumbnail_candidates = candidates
                db.session.commit()
            logger.info(f'''Saved candidate {candidate_id} to {url}''')
            return candidate
        except Exception:
            e = None
            logger.error(f'''Failed to save candidate: {e}''', exc_info = True)
            raise 
            e = None
            del e


    
    def _analyze_thumbnail_quality(self = None, image_data = None, text_overlay = None):
        """
        Comprehensive thumbnail quality analysis

        Args:
            image_data: Thumbnail image bytes
            text_overlay: Text overlay configuration (if applied)

        Returns:
            {
                'faceCount': 1,
                'facePositions': [{'x': 100, 'y': 200, 'width': 150, 'height': 150}],
                'clickabilityScore': 0.85,  # 0-1
                'textReadability': 0.92,    # 0-1
                'qualityMetrics': {
                    'contrastScore': 75.0,
                    'colorfulnessScore': 82.0,
                    'sharpnessScore': 68.0
                }
            }
        """
        
        try:
            face_analysis = self._detect_faces(image_data)
            quality_metrics = self.similarity_service.calculate_thumbnail_quality_score(image_data)
            clickability_score = self._calculate_clickability_score(quality_metrics, face_analysis['faceCount'])
            text_readability = 1
            if text_overlay and text_overlay.get('mainText'):
                text_readability = self._calculate_text_readability(image_data, text_overlay)
            return {
                'faceCount': face_analysis['faceCount'],
                'facePositions': face_analysis['facePositions'],
                'clickabilityScore': clickability_score,
                'textReadability': text_readability,
                'qualityMetrics': quality_metrics }
        except Exception:
            e = None
            logger.error(f'''Quality analysis failed: {e}''', exc_info = True)
            del e
            return None
            None = 
            del e


    
    def _detect_faces(self = None, image_data = None):
        """
        Detect faces in thumbnail using OpenCV Haar Cascades

        Args:
            image_data: Image bytes

        Returns:
            {
                'faceCount': 1,
                'facePositions': [{'x': 100, 'y': 200, 'width': 150, 'height': 150}]
            }
        """
        
        try:
            img = Image.open(BytesIO(image_data))
            img_array = np.array(img.convert('RGB'))
            img_bgr = cv2.cvtColor(img_array, cv2.COLOR_RGB2BGR)
            gray = cv2.cvtColor(img_bgr, cv2.COLOR_BGR2GRAY)
            faces = self.face_cascade.detectMultiScale(gray, scaleFactor = 1.1, minNeighbors = 5, minSize = (30, 30), flags = cv2.CASCADE_SCALE_IMAGE)
            face_positions = []
            for x, y, w, h in faces:
                face_positions.append({
                    'x': int(x),
                    'y': int(y),
                    'width': int(w),
                    'height': int(h) })
                return {
                    'faceCount': len(faces),
                    'facePositions': face_positions }
                except Exception:
                    e = None
                    logger.error(f'''Face detection failed: {e}''')
                    del e
                    return None
                    None = 
                    del e


    
    def _calculate_clickability_score(self = None, quality_metrics = None, face_count = None):
        '''
        Calculate clickability score based on multiple factors

        Formula:
        - Contrast: 30%
        - Colorfulness: 30%
        - Face presence: 40% (bonus if 1-2 faces detected)

        Args:
            quality_metrics: Quality metrics from ThumbnailSimilarityService
            face_count: Number of detected faces

        Returns:
            Clickability score (0-1)
        '''
        
        try:
            contrast = quality_metrics.get('contrastScore', 50) / 100
            colorfulness = quality_metrics.get('colorfulnessScore', 50) / 100
            if face_count == 0:
                face_score = 0.5
            elif  <= 1, face_count or 1, face_count <= 2:
                pass
            
        except:
            0.7 = 1

        clickability = contrast * 0.3 + colorfulness * 0.3 + face_score * 0.4
        return round(clickability, 2)
        except Exception:
            e = None
            logger.error(f'''Clickability calculation failed: {e}''')
            e = None
            del e
            return 0.5
            e = None
            del e

    
    def _calculate_text_readability(self = None, image_data = None, text_overlay = None):
        '''
        Calculate text readability score

        Factors:
        - Text-background contrast (70%)
        - Text size relative to image (30%)

        Args:
            image_data: Image bytes
            text_overlay: Text overlay configuration

        Returns:
            Readability score (0-1)
        '''
        
        try:
            img = Image.open(BytesIO(image_data))
            img_array = np.array(img.convert('RGB'))
            font_size = text_overlay.get('fontSize', 72)
            position = text_overlay.get('position', {
                'x': img.width // 2,
                'y': img.height // 2 })
            height = img.height
            relative_size = font_size / height
            if  <= 0.05, relative_size or 0.05, relative_size <= 0.1:
                pass
            
        except:
            if not  <= 0.03, relative_size or 0.03, relative_size < 0.05:
                pass
            else:
                1
            if  < 0.1, relative_size or 0.1, relative_size <= 0.15:
                pass
            
        except:
            pass
        except:
            0.5 = 0.8

        text_x = int(position.get('x', img.width // 2))
        text_y = int(position.get('y', img.height // 2))
        sample_size = 50
        x_start = max(0, text_x - sample_size // 2)
        x_end = min(img.width, text_x + sample_size // 2)
        y_start = max(0, text_y - sample_size // 2)
        y_end = min(img.height, text_y + sample_size // 2)
        background_region = img_array[(y_start:y_end, x_start:x_end)]
        bg_brightness = np.mean(background_region)
        text_color = text_overlay.get('color', '#FFFFFF')
        text_brightness = self._hex_to_brightness(text_color)
        contrast = abs(text_brightness - bg_brightness) / 255
        if contrast >= 0.5:
            contrast_score = 1
        elif contrast >= 0.3:
            contrast_score = 0.8
        else:
            contrast_score = 0.5
        readability = contrast_score * 0.7 + size_score * 0.3
        return round(readability, 2)
        except Exception:
            e = None
            logger.error(f'''Text readability calculation failed: {e}''')
            e = None
            del e
            return 0.5
            e = None
            del e

    
    def _hex_to_brightness(self = None, hex_color = None):
        """
        Convert hex color to brightness value (0-255)

        Args:
            hex_color: Hex color string (e.g., '#FFFFFF')

        Returns:
            Brightness value (0-255)
        """
        
        try:
            hex_color = hex_color.lstrip('#')
            r = int(hex_color[0:2], 16)
            g = int(hex_color[2:4], 16)
            b = int(hex_color[4:6], 16)
            brightness = 0.299 * r + 0.587 * g + 0.114 * b
            return brightness
        except Exception:
            e = None
            logger.warning(f'''Failed to parse hex color {hex_color}: {e}''')
            e = None
            del e
            return 127
            e = None
            del e


    
    def _base64_to_image(self = None, data_url = None):
        '''Convert base64 data URL to PIL Image'''
        (header, encoded) = data_url.split(',', 1)
        image_data = base64.b64decode(encoded)
        return Image.open(BytesIO(image_data))

    
    def _dataurl_to_bytes(self = None, data_url = None):
        '''Convert data URL to bytes'''
        (header, encoded) = data_url.split(',', 1)
        return base64.b64decode(encoded)

    
    def _image_to_bytes(self = None, img = None):
        '''Convert PIL Image to JPEG bytes'''
        buffer = BytesIO()
        img.save(buffer, format = 'JPEG', quality = 95)
        return buffer.getvalue()
