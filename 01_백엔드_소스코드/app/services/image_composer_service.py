# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: image_composer_service.pyc (Python 3.11)

'''
Image Composer Service
이미지 컴포지터 비즈니스 로직

- 컴포지션 저장/로드 (JSON)
- 프레임 미리보기 생성 (PIL)
- 영상 렌더링 (PIL + FFmpeg)
'''
import os
import json
import base64
import logging
import tempfile
import shutil
from datetime import datetime
from typing import Dict, List, Optional, Any
from pathlib import Path
from io import BytesIO
from PIL import Image, ImageDraw, ImageFont
from app.config.paths import get_projects_path, get_fonts_path
from app.utils.ffmpeg_wrapper import FFmpegWrapper
from app.models import Project
from app import db
from sqlalchemy.orm.attributes import flag_modified
logger = logging.getLogger(__name__)

class ImageComposerService:
    '''이미지 컴포지터 서비스'''
    
    def __init__(self = None, project_id = None):
        self.project_id = project_id
        self.project_folder = str(get_projects_path() / project_id)
        self.composer_folder = os.path.join(self.project_folder, 'composer')
        self.output_folder = os.path.join(self.project_folder, 'composer_output')
        os.makedirs(self.composer_folder, exist_ok = True)
        os.makedirs(self.output_folder, exist_ok = True)

    
    def save_composition(self = None, composition = None, sync_segments = None, apply_to_video = (None, True)):
        '''
        컴포지션 저장

        Args:
            composition: 컴포지션 데이터
            sync_segments: 동기화 세그먼트 (V1 트랙)
            apply_to_video: 영상 생성에 자동 적용 여부

        Returns:
            저장 결과
        '''
        composition['updatedAt'] = datetime.now().isoformat()
    # WARNING: Decompyle incomplete

    
    def _save_composer_enabled(self = None, composition = None):
        '''
        컴포지터 활성화 플래그 저장

        Args:
            composition: 컴포지션 데이터
        '''
        
        try:
            project = Project.query.get(self.project_id)
            if not project:
                return None
            settings = dict(project.video_settings) if None.video_settings else { }
            settings['composerEnabled'] = True
            canvas = composition.get('canvas', {
                'width': 1920,
                'height': 1080,
                'backgroundColor': '#000000' })
            canvas_width = canvas.get('width', 1920)
            canvas_height = canvas.get('height', 1080)
            is_portrait = canvas_height > canvas_width
            layers = composition.get('layers', [])
            if is_portrait:
                settings['portraitComposerLayers'] = layers
                settings['portraitComposerCanvas'] = canvas
                print('[ImageComposerService] Saving PORTRAIT composer layers')
            else:
                settings['landscapeComposerLayers'] = layers
                settings['landscapeComposerCanvas'] = canvas
                settings['composerLayers'] = layers
                settings['composerCanvas'] = canvas
                print('[ImageComposerService] Saving LANDSCAPE composer layers')
            project.video_settings = settings
            flag_modified(project, 'video_settings')
            db.session.commit()
            orientation = 'portrait' if is_portrait else 'landscape'
            print(f'''[ImageComposerService] Saved composerEnabled for project {self.project_id}, {len(layers)} {orientation} layers''')
            for i, layer in enumerate(layers[:5]):
                has_data_url = bool(layer.get('imageDataUrl'))
                has_image_url = bool(layer.get('imageUrl'))
                data_url_len = len(layer.get('imageDataUrl', '')) if has_data_url else 0
                print(f'''[ImageComposerService]   Layer {i}: trackId={layer.get('trackId')}, visible={layer.get('visible')}, startTime={layer.get('startTime')}, endTime={layer.get('endTime')}, hasImageDataUrl={has_data_url} (len={data_url_len}), hasImageUrl={has_image_url}, imageUrl={layer.get('imageUrl', 'N/A')[:100] if has_image_url else 'N/A'}''')
                return None
                except Exception:
                    e = None
                    logger.error(f'''Failed to save composerEnabled: {e}''')
                    db.session.rollback()
                    e = None
                    del e
                    return None
                    e = None
                    del e


    
    def _apply_to_image_timeline(self = None, sync_segments = None):
        '''
        동기화 세그먼트를 imageTimeline으로 변환하여 프로젝트에 적용

        Args:
            sync_segments: 동기화 세그먼트 목록
        '''
        
        try:
            project = Project.query.get(self.project_id)
            if not project:
                logger.warning(f'''Project {self.project_id} not found for imageTimeline sync''')
                return None
            segments = None
            for seg in sync_segments:
                segments.append({
                    'imageIndex': seg.get('imageIndex', 0),
                    'startTime': seg.get('startTime', 0),
                    'endTime': seg.get('endTime', 0),
                    'duration': seg.get('duration', seg.get('endTime', 0) - seg.get('startTime', 0)),
                    'imagePath': seg.get('imagePath'),
                    'imageUrl': seg.get('imageUrl') })
                total_duration = (lambda .0: pass# WARNING: Decompyle incomplete
)(sync_segments(), default = 0)
            settings = dict(project.video_settings) if project.video_settings else { }
            settings['imageTimeline'] = {
                'mode': 'composer',
                'segments': segments,
                'totalVideoDuration': total_duration }
            project.video_settings = settings
            flag_modified(project, 'video_settings')
            db.session.commit()
            logger.info(f'''Applied composition to imageTimeline for project {self.project_id}''')
            return None
        except Exception:
            e = None
            logger.error(f'''Failed to apply imageTimeline: {e}''')
            db.session.rollback()
            e = None
            del e
            return None
            e = None
            del e


    
    def load_composition(self = None):
        '''
        컴포지션 로드

        Returns:
            컴포지션 데이터 또는 None
        '''
        composition_path = os.path.join(self.composer_folder, 'composition.json')
        if not os.path.exists(composition_path):
            return None
        f = None(composition_path, 'r', encoding = 'utf-8')
        composition = json.load(f)
        None(None, None)

    
    def render_preview_frame(self = None, composition = None, frame_time = None, subtitle_data = (0, None)):
        """
        프레임 미리보기 생성

        Args:
            composition: 컴포지션 데이터
            frame_time: 프레임 시간 (초)
            subtitle_data: 자막 데이터 {'segments': [...], 'style': {...}}

        Returns:
            이미지 DataURL
        """
        canvas = composition.get('canvas', { })
        width = canvas.get('width', 1920)
        height = canvas.get('height', 1080)
        bg_color = canvas.get('backgroundColor', '#000000')
        image = Image.new('RGBA', (width, height), bg_color)
        layers = composition.get('layers', [])
        for layer in layers:
            if not layer.get('visible', True):
                continue
            layer_image = self._render_layer(layer, frame_time, composition)
            if layer_image:
                self._composite_layer(image, layer_image, layer)
            if subtitle_data:
                self._render_subtitle(image, frame_time, subtitle_data)
        buffer = BytesIO()
        image.convert('RGB').save(buffer, format = 'JPEG', quality = 85)
        buffer.seek(0)
        data_url = f'''data:image/jpeg;base64,{base64.b64encode(buffer.read()).decode()}'''
        return data_url

    
    def render_video(self = None, composition = None, export_settings = None, subtitle_data = (None,)):
        """
        컴포지션 영상 렌더링

        Args:
            composition: 컴포지션 데이터
            export_settings: 내보내기 설정
            subtitle_data: 자막 데이터 {'segments': [...], 'style': {...}}

        Returns:
            렌더링 결과
        """
        format_type = export_settings.get('format', 'mp4')
        quality = export_settings.get('quality', 'high')
        fps = export_settings.get('fps', 30)
        duration = export_settings.get('duration', 5)
        total_frames = int(duration * fps)
        canvas = composition.get('canvas', { })
        width = canvas.get('width', 1920)
        height = canvas.get('height', 1080)
        temp_dir = tempfile.mkdtemp(prefix = 'composer_')
        frames_dir = os.path.join(temp_dir, 'frames')
        os.makedirs(frames_dir, exist_ok = True)
        
        try:
            logger.info(f'''Rendering {total_frames} frames...''')
            for frame_idx in range(total_frames):
                frame_time = frame_idx / fps
                progress = frame_idx / total_frames
                frame_image = self._render_frame_with_animation(composition, frame_time, progress, subtitle_data)
                frame_path = os.path.join(frames_dir, f'''frame_{frame_idx:05d}.png''')
                frame_image.save(frame_path, 'PNG')
                output_filename = f'''composer_{datetime.now().strftime('%Y%m%d_%H%M%S')}.{format_type}'''
                output_path = os.path.join(self.output_folder, output_filename)
                bitrate_map = {
                    'low': '2M',
                    'medium': '5M',
                    'high': '10M' }
                bitrate = bitrate_map.get(quality, '5M')
                ffmpeg = FFmpegWrapper()
                ffmpeg.create_video_from_images(image_pattern = os.path.join(frames_dir, 'frame_%05d.png'), output_path = output_path, fps = fps, bitrate = bitrate)
                output_url = f'''/data/projects/{self.project_id}/composer_output/{output_filename}'''
                logger.info(f'''Rendered video: {output_path}''')
                shutil.rmtree(temp_dir, ignore_errors = True)
                return {
                    'outputPath': output_path.replace('\\', '/'),
                    'outputUrl': output_url }
                shutil.rmtree(temp_dir, ignore_errors = True)


    
    def list_assets(self = None):
        '''
        프로젝트의 사용 가능한 에셋 목록

        Returns:
            에셋 목록
        '''
        assets = []
        scene_images_path = os.path.join(self.project_folder, 'images', 'scenes')
        if os.path.exists(scene_images_path):
            for filename in os.listdir(scene_images_path):
                if filename.lower().endswith(('.png', '.jpg', '.jpeg', '.webp')):
                    file_path = os.path.join(scene_images_path, filename)
                    assets.append({
                        'id': f'''scene_{filename}''',
                        'type': 'scene',
                        'name': filename,
                        'thumbnailUrl': f'''/data/projects/{self.project_id}/images/scenes/{filename}''',
                        'imageUrl': f'''/data/projects/{self.project_id}/images/scenes/{filename}''',
                        'width': 0,
                        'height': 0 })
                media_path = os.path.join(self.project_folder, 'media')
                if os.path.exists(media_path):
                    for filename in os.listdir(media_path):
                        if filename.lower().endswith(('.png', '.jpg', '.jpeg', '.webp')):
                            assets.append({
                                'id': f'''media_{filename}''',
                                'type': 'library',
                                'name': filename,
                                'thumbnailUrl': f'''/data/projects/{self.project_id}/media/{filename}''',
                                'imageUrl': f'''/data/projects/{self.project_id}/media/{filename}''',
                                'width': 0,
                                'height': 0 })
                        return assets

    
    def _render_layer(self = None, layer = None, frame_time = None, composition = ('layer', Dict[(str, Any)], 'frame_time', float, 'composition', Dict[(str, Any)], 'return', Optional[Image.Image])):
        '''
        단일 레이어 렌더링

        Args:
            layer: 레이어 데이터
            frame_time: 프레임 시간
            composition: 컴포지션 데이터

        Returns:
            렌더링된 이미지
        '''
        image_data_url = layer.get('imageDataUrl')
        image_url = layer.get('imageUrl')
        image = None
        if image_data_url:
            
            try:
                (header, data) = image_data_url.split(',', 1)
                image_data = base64.b64decode(data)
                loaded_image = Image.open(BytesIO(image_data))
                image = loaded_image.convert('RGBA')
                
                try:
                    None(None, None)
                with None:
                    if not None:
                        
                        try:
                            
                            try:
                                pass
                            except Exception:
                                e = None
                                logger.warning(f'''Failed to load image from DataURL: {e}''')
                                e = None
                                del e
                                return None
                                e = None
                                del e
                                if image_url:
                                    
                                    try:
                                        file_path = None
                                        if image_url.startswith('/data/'):
                                            relative_path = image_url[6:].replace('/', os.sep)
                                            get_data_path = get_data_path
                                            import config.paths
                                            file_path = os.path.join(str(get_data_path()), relative_path)
                                        elif image_url.startswith('/api/projects/'):
                                            parts = image_url.split('/')
                                            if len(parts) >= 6:
                                                folder = parts[5]
                                                filename = '/'.join(parts[6:]).replace('/', os.sep)
                                                file_path = os.path.join(self.project_folder, folder, filename)
                                            else:
                                                logger.warning(f'''Unknown URL format: {image_url}''')
                                                return None
                                            if None:
                                                loaded_image = Image.open(file_path)
                                                image = loaded_image.convert('RGBA')
                                                
                                                try:
                                                    None(None, None)
                                                with None:
                                                    if not None:
                                                        
                                                        try:
                                                            
                                                            try:
                                                                pass
                                                            except Exception:
                                                                e = None
                                                                logger.warning(f'''Failed to load image from URL {image_url}: {e}''')
                                                                e = None
                                                                del e
                                                                return None
                                                                e = None
                                                                del e
                                                                return None

                                                            if not image:
                                                                return None
                                                            transform = None.get('transform', { })
                                                            target_width = int(transform.get('width', image.width))
                                                            target_height = int(transform.get('height', image.height))
                                                            rotation = transform.get('rotation', 0)
                                                            image_fit = layer.get('imageFit', 'fit')
                                                            if (target_width, target_height) != image.size:
                                                                (orig_width, orig_height) = image.size
                                                                if image_fit == 'stretch':
                                                                    image = image.resize((target_width, target_height), Image.Resampling.LANCZOS)
                                                                    print(f'''[ImageComposer] imageFit=stretch: {orig_width}x{orig_height} -> {target_width}x{target_height}''')
                                                                elif image_fit == 'fill':
                                                                    orig_ratio = orig_width / orig_height
                                                                    target_ratio = target_width / target_height
                                                                    if orig_ratio > target_ratio:
                                                                        new_height = target_height
                                                                        new_width = int(target_height * orig_ratio)
                                                                    else:
                                                                        new_width = target_width
                                                                        new_height = int(target_width / orig_ratio)
                                                                    image = image.resize((new_width, new_height), Image.Resampling.LANCZOS)
                                                                    left = (new_width - target_width) // 2
                                                                    top = (new_height - target_height) // 2
                                                                    image = image.crop((left, top, left + target_width, top + target_height))
                                                                    print(f'''[ImageComposer] imageFit=fill: {orig_width}x{orig_height} -> {target_width}x{target_height} (cropped)''')
                                                                elif image_fit == 'auto':
                                                                    print(f'''[ImageComposer] imageFit=auto: keeping original {orig_width}x{orig_height}''')
                                                                else:
                                                                    orig_ratio = orig_width / orig_height
                                                                    target_ratio = target_width / target_height
                                                                    if orig_ratio > target_ratio:
                                                                        new_width = target_width
                                                                        new_height = int(target_width / orig_ratio)
                                                                    else:
                                                                        new_height = target_height
                                                                        new_width = int(target_height * orig_ratio)
                                                                    image = image.resize((new_width, new_height), Image.Resampling.LANCZOS)
                                                                    print(f'''[ImageComposer] imageFit=fit: {orig_width}x{orig_height} -> {new_width}x{new_height}''')







        if rotation != 0:
            image = image.rotate(-rotation, expand = True, resample = Image.Resampling.BICUBIC)
        return image

    
    def _render_frame_with_animation(self = None, composition = None, frame_time = None, progress = (None,), subtitle_data = ('composition', Dict[(str, Any)], 'frame_time', float, 'progress', float, 'subtitle_data', Optional[Dict[(str, Any)]], 'return', Image.Image)):
        """
        애니메이션이 적용된 프레임 렌더링

        Args:
            composition: 컴포지션 데이터
            frame_time: 프레임 시간 (초)
            progress: 전체 진행률 (0~1)
            subtitle_data: 자막 데이터 {'segments': [...], 'style': {...}}

        Returns:
            렌더링된 프레임 이미지
        """
        canvas = composition.get('canvas', { })
        width = canvas.get('width', 1920)
        height = canvas.get('height', 1080)
        bg_color = canvas.get('backgroundColor', '#000000')
        frame = Image.new('RGBA', (width, height), bg_color)
        layers = composition.get('layers', [])
        for layer in layers:
            if not layer.get('visible', True):
                continue
            layer_image = self._render_layer(layer, frame_time, composition)
            if layer_image:
                animated_layer = self._apply_animation(layer_image, layer, progress)
                self._composite_layer(frame, animated_layer['image'], layer, animated_layer)
            if subtitle_data:
                self._render_subtitle(frame, frame_time, subtitle_data)
        return frame.convert('RGB')

    
    def _apply_animation(self = None, image = None, layer = None, progress = ('image', Image.Image, 'layer', Dict[(str, Any)], 'progress', float, 'return', Dict[(str, Any)])):
        '''
        레이어에 애니메이션 적용

        Args:
            image: 원본 이미지
            layer: 레이어 데이터
            progress: 진행률 (0~1)

        Returns:
            애니메이션 적용된 결과
        '''
        animation = layer.get('animation', { })
        preset = animation.get('preset', 'none')
        intensity = animation.get('intensity', 1)
        easing = animation.get('easing', 'ease_in_out')
        t = self._apply_easing(progress, easing)
        result = {
            'image': image,
            'offset_x': 0,
            'offset_y': 0,
            'opacity_modifier': 1 }
        if preset == 'none':
            return result
        if None == 'zoom_in':
            scale = 1 + 0.2 * intensity * t
            new_size = (int(image.width * scale), int(image.height * scale))
            result['image'] = image.resize(new_size, Image.Resampling.LANCZOS)
            result['offset_x'] = -(new_size[0] - image.width) // 2
            result['offset_y'] = -(new_size[1] - image.height) // 2
        elif preset == 'zoom_out':
            scale = 1.2 * intensity - 0.2 * intensity * t
            new_size = (int(image.width * scale), int(image.height * scale))
            result['image'] = image.resize(new_size, Image.Resampling.LANCZOS)
            result['offset_x'] = -(new_size[0] - image.width) // 2
            result['offset_y'] = -(new_size[1] - image.height) // 2
        elif preset == 'pan_left':
            result['offset_x'] = int(image.width * 0.1 * intensity * (1 - t))
        elif preset == 'pan_right':
            result['offset_x'] = int(-(image.width) * 0.1 * intensity * (1 - t))
        elif preset == 'pan_up':
            result['offset_y'] = int(image.height * 0.1 * intensity * (1 - t))
        elif preset == 'pan_down':
            result['offset_y'] = int(-(image.height) * 0.1 * intensity * (1 - t))
        elif preset == 'fade_in':
            result['opacity_modifier'] = t
        elif preset == 'fade_out':
            result['opacity_modifier'] = 1 - t
        return result

    
    def _apply_easing(self = None, t = None, easing = None):
        '''
        이징 함수 적용

        Args:
            t: 진행률 (0~1)
            easing: 이징 타입

        Returns:
            이징 적용된 값
        '''
        if easing == 'linear':
            return t
        if None == 'ease_in':
            return t * t
        if None == 'ease_out':
            return 1 - (1 - t) * (1 - t)
        if None == 'ease_in_out':
            return 3 * t * t - 2 * t * t * t

    
    def _composite_layer(self = None, canvas = None, layer_image = None, layer = (None,), animation_result = ('canvas', Image.Image, 'layer_image', Image.Image, 'layer', Dict[(str, Any)], 'animation_result', Optional[Dict[(str, Any)]])):
        '''
        레이어를 캔버스에 합성

        Args:
            canvas: 캔버스 이미지
            layer_image: 레이어 이미지
            layer: 레이어 데이터
            animation_result: 애니메이션 결과
        '''
        pass
    # WARNING: Decompyle incomplete

    
    def _render_subtitle(self = None, canvas = None, frame_time = None, subtitle_data = ('canvas', Image.Image, 'frame_time', float, 'subtitle_data', Dict[(str, Any)], 'return', None)):
        """
        자막을 캔버스에 렌더링

        Args:
            canvas: PIL Image 캔버스
            frame_time: 현재 시간 (초)
            subtitle_data: {
                'segments': [{ 'start', 'end', 'text' }, ...],
                'style': { 폰트, 색상, 위치 등 }
            }
        """
        segments = subtitle_data.get('segments', [])
        style = subtitle_data.get('style', { })
        current_subtitle = None
        for seg in segments:
            start = seg.get('start', 0)
            end = seg.get('end', 0)
            if  <= start, frame_time or start, frame_time < end:
                pass
            
            seg
        continue
        if not current_subtitle:
            return None
        None.get('text', '') = None
        if not text:
            return None
        (width, height) = None.size
        font_size = style.get('fontSize', 48)
        font_family = style.get('fontFamily', 'Pretendard-Bold')
        font = self._get_font(font_family, font_size)
        draw = ImageDraw.Draw(canvas)
        bbox = draw.textbbox((0, 0), text, font = font)
        text_width = bbox[2] - bbox[0]
        text_height = bbox[3] - bbox[1]
        use_custom = style.get('useCustomPosition', False)
        if use_custom:
            pos_x = int((style.get('positionX', 50) / 100) * width)
            pos_y = int((style.get('positionY', 90) / 100) * height)
        else:
            position = style.get('position', 'bottom')
            pos_x = width // 2
            pos_y = int(height * 0.1) if position == 'top' else int(height * 0.9)
        alignment = style.get('alignment', 'center')
        if alignment == 'center':
            pos_x -= text_width // 2
        elif alignment == 'right':
            pos_x -= text_width
        pos_y -= text_height // 2
        if style.get('enableBackground', False):
            bg_color = style.get('backgroundColor', '#000000')
            bg_opacity = style.get('backgroundOpacity', 0.7)
            padding = 10
            bg_rgba = self._hex_to_rgba(bg_color, bg_opacity)
            draw.rectangle([
                pos_x - padding,
                pos_y - padding,
                pos_x + text_width + padding,
                pos_y + text_height + padding], fill = bg_rgba)
        if style.get('enableStroke', False):
            stroke_color = style.get('strokeColor', '#000000')
            stroke_width = style.get('strokeWidth', 2)
            for dx in range(-stroke_width, stroke_width + 1):
                for dy in range(-stroke_width, stroke_width + 1):
                    if dx != 0 or dy != 0:
                        draw.text((pos_x + dx, pos_y + dy), text, font = font, fill = stroke_color)
                    if style.get('enableShadow', False):
                        shadow_color = style.get('shadowColor', '#000000')
                        shadow_offset_x = style.get('shadowOffsetX', 2)
                        shadow_offset_y = style.get('shadowOffsetY', 2)
                        draw.text((pos_x + shadow_offset_x, pos_y + shadow_offset_y), text, font = font, fill = shadow_color)
        font_color = style.get('fontColor', '#FFFFFF')
        draw.text((pos_x, pos_y), text, font = font, fill = font_color)

    
    def _get_font(self = None, font_family = None, font_size = None):
        '''
        폰트 로드

        Args:
            font_family: 폰트 이름
            font_size: 폰트 크기

        Returns:
            PIL ImageFont
        '''
        
        try:
            fonts_path = get_fonts_path()
            font_extensions = [
                '.ttf',
                '.otf',
                '.TTF',
                '.OTF']
            for ext in font_extensions:
                font_path = fonts_path / f'''{font_family}{ext}'''
                if font_path.exists():
                    
                    return None, ImageFont.truetype(str(font_path), font_size)
                for Path(windir) / 'Fonts' in fonts_path.iterdir():
                    if file.suffix.lower() in ('.ttf', '.otf') and font_family.lower() in file.stem.lower():
                        
                        return None, ImageFont.truetype(str(file), font_size)
                    if windows_fonts.exists():
                        malgun = windows_fonts / 'malgun.ttf'
                        if malgun.exists():
                            return ImageFont.truetype(str(malgun), font_size)
                        return None.load_default()
                    except Exception:
                        e = None
                        logger.warning(f'''Failed to load font {font_family}: {e}''')
                        del e
                        return None
                        None = 
                        del e


    
    def _hex_to_rgba(self = None, hex_color = None, opacity = None):
        '''
        HEX 색상을 RGBA 튜플로 변환

        Args:
            hex_color: HEX 색상 (#RRGGBB)
            opacity: 투명도 (0~1)

        Returns:
            RGBA 튜플
        '''
        hex_color = hex_color.lstrip('#')
        r = int(hex_color[0:2], 16)
        g = int(hex_color[2:4], 16)
        b = int(hex_color[4:6], 16)
        a = int(opacity * 255)
        return (r, g, b, a)

    
    def composite_overlay_layers(self, base_image_path, layers, output_path = None, canvas_width = None, canvas_height = None, frame_time = (1920, 1080, None, None), frame_duration = ('base_image_path', str, 'layers', List[Dict[(str, Any)]], 'output_path', str, 'canvas_width', int, 'canvas_height', int, 'frame_time', float, 'frame_duration', float, 'return', bool)):
        '''
        기본 이미지에 오버레이 레이어를 합성

        Args:
            base_image_path: 기본 이미지 경로
            layers: 컴포지터 레이어 목록 (V1은 제외, V2+ 오버레이만)
            output_path: 출력 이미지 경로
            canvas_width: 캔버스 너비
            canvas_height: 캔버스 높이
            frame_time: 이미지 표시 시작 시간 (초). None이면 타임코드 체크 안함.
            frame_duration: 이미지 표시 지속 시간 (초). frame_time과 함께 사용하여 범위 겹침 체크.

        Returns:
            성공 여부
        '''
        pass
    # WARNING: Decompyle incomplete

    
    def _resize_to_cover(self = None, image = None, target_width = None, target_height = ('center',), crop_gravity = ('image', Image.Image, 'target_width', int, 'target_height', int, 'crop_gravity', str, 'return', Image.Image)):
        """
        이미지를 cover 방식으로 리사이즈 (비율 유지, 빈 공간 없이 채움)

        Args:
            image: 원본 이미지
            target_width: 타겟 너비
            target_height: 타겟 높이
            crop_gravity: 크롭 방향 ('top', 'center', 'bottom')

        Returns:
            리사이즈된 이미지
        """
        img_ratio = image.width / image.height
        target_ratio = target_width / target_height
        if img_ratio > target_ratio:
            new_height = target_height
            new_width = int(target_height * img_ratio)
        else:
            new_width = target_width
            new_height = int(target_width / img_ratio)
        resized = image.resize((new_width, new_height), Image.Resampling.LANCZOS)
        left = (new_width - target_width) // 2
        if crop_gravity == 'top':
            top = 0
        elif crop_gravity == 'bottom':
            top = new_height - target_height
        else:
            top = (new_height - target_height) // 2
        cropped = resized.crop((left, top, left + target_width, top + target_height))
        return cropped

    
    def _render_layer_for_composite(self = None, layer = None):
        '''
        합성용 레이어 렌더링 (간소화 버전)

        Args:
            layer: 레이어 데이터

        Returns:
            렌더링된 이미지
        '''
        image_data_url = layer.get('imageDataUrl')
        image_url = layer.get('imageUrl')
        image = None
        if image_data_url:
            
            try:
                (header, data) = image_data_url.split(',', 1)
                image_data = base64.b64decode(data)
                loaded_image = Image.open(BytesIO(image_data))
                image = loaded_image.convert('RGBA')
                
                try:
                    None(None, None)
                with None:
                    if not None:
                        
                        try:
                            
                            try:
                                pass
                            except Exception:
                                e = None
                                logger.warning(f'''Failed to load image from DataURL: {e}''')
                                e = None
                                del e
                                return None
                                e = None
                                del e
                                if image_url:
                                    
                                    try:
                                        file_path = None
                                        if image_url.startswith('/data/'):
                                            relative_path = image_url[6:].replace('/', os.sep)
                                            get_data_path = get_data_path
                                            import config.paths
                                            file_path = os.path.join(str(get_data_path()), relative_path)
                                        elif image_url.startswith('/api/projects/'):
                                            parts = image_url.split('/')
                                            if len(parts) >= 6:
                                                folder = parts[5]
                                                filename = '/'.join(parts[6:]).replace('/', os.sep)
                                                file_path = os.path.join(self.project_folder, folder, filename)
                                            else:
                                                logger.warning(f'''Unknown URL format: {image_url}''')
                                                return None
                                            if None:
                                                loaded_image = Image.open(file_path)
                                                image = loaded_image.convert('RGBA')
                                                
                                                try:
                                                    None(None, None)
                                                with None:
                                                    if not None:
                                                        
                                                        try:
                                                            
                                                            try:
                                                                pass
                                                            except Exception:
                                                                e = None
                                                                logger.warning(f'''Failed to load image from URL {image_url}: {e}''')
                                                                e = None
                                                                del e
                                                                return None
                                                                e = None
                                                                del e
                                                                return None

                                                            if not image:
                                                                return None
                                                            transform = None.get('transform', { })
                                                            target_width = int(transform.get('width', image.width))
                                                            target_height = int(transform.get('height', image.height))
                                                            rotation = transform.get('rotation', 0)
                                                            image_fit = layer.get('imageFit', 'fit')
                                                            if (target_width, target_height) != image.size:
                                                                (orig_width, orig_height) = image.size
                                                                if image_fit == 'stretch':
                                                                    image = image.resize((target_width, target_height), Image.Resampling.LANCZOS)
                                                                elif image_fit == 'fill':
                                                                    orig_ratio = orig_width / orig_height
                                                                    target_ratio = target_width / target_height
                                                                    if orig_ratio > target_ratio:
                                                                        new_height = target_height
                                                                        new_width = int(target_height * orig_ratio)
                                                                    else:
                                                                        new_width = target_width
                                                                        new_height = int(target_width / orig_ratio)
                                                                    image = image.resize((new_width, new_height), Image.Resampling.LANCZOS)
                                                                    left = (new_width - target_width) // 2
                                                                    top = (new_height - target_height) // 2
                                                                    image = image.crop((left, top, left + target_width, top + target_height))
                                                                elif image_fit == 'auto':
                                                                    pass
                                                                else:
                                                                    orig_ratio = orig_width / orig_height
                                                                    target_ratio = target_width / target_height
                                                                    if orig_ratio > target_ratio:
                                                                        new_width = target_width
                                                                        new_height = int(target_width / orig_ratio)
                                                                    else:
                                                                        new_height = target_height
                                                                        new_width = int(target_height * orig_ratio)
                                                                    image = image.resize((new_width, new_height), Image.Resampling.LANCZOS)







        if rotation != 0:
            image = image.rotate(-rotation, expand = True, resample = Image.Resampling.BICUBIC)
        return image

    
    def render_animated_frames(self, base_image_path, layers, output_dir = None, duration = None, fps = None, canvas_width = (30, 1920, 1080), canvas_height = ('base_image_path', str, 'layers', List[Dict[(str, Any)]], 'output_dir', str, 'duration', float, 'fps', int, 'canvas_width', int, 'canvas_height', int, 'return', List[str])):
        '''
        애니메이션이 적용된 프레임들 렌더링 (샘플/미리보기 영상용)

        Args:
            base_image_path: 기본 이미지 경로
            layers: 컴포지터 레이어 목록
            output_dir: 출력 디렉토리
            duration: 지속 시간 (초)
            fps: 프레임 레이트
            canvas_width: 캔버스 너비
            canvas_height: 캔버스 높이

        Returns:
            렌더링된 프레임 파일 경로 목록
        '''
        frame_paths = []
        total_frames = int(duration * fps)
        
        try:
            loaded_base = Image.open(base_image_path)
            resized_base = self._resize_to_cover(loaded_base, canvas_width, canvas_height)
            if resized_base.mode != 'RGBA':
                base_image = resized_base.convert('RGBA')
            else:
                base_image = resized_base.copy()
                
                try:
                    None(None, None)
                with None:
                    if not None:
                        
                        try:
                            
                            try:
                                os.makedirs(output_dir, exist_ok = True)
                                for frame_idx in range(total_frames):
                                    progress = frame_idx / total_frames if total_frames > 0 else 0
                                    frame = base_image.copy()
                                    for layer in layers:
                                        if layer.get('trackId') == 'V1':
                                            continue
                                        if not layer.get('visible', True):
                                            continue
                                        layer_image = self._render_layer_for_composite(layer)
                                        if layer_image:
                                            animated = self._apply_animation(layer_image, layer, progress)
                                            self._composite_layer(frame, animated['image'], layer, animated)
                                        output_path = os.path.join(output_dir, f'''frame_{frame_idx:05d}.jpg''')
                                        frame.convert('RGB').save(output_path, 'JPEG', quality = 90)
                                        frame_paths.append(output_path)
                                        logger.debug(f'''Rendered {len(frame_paths)} animated frames to {output_dir}''')
                                        return frame_paths
                                        except Exception:
                                            e = None
                                            logger.error(f'''Failed to render animated frames: {e}''')
                                            del e
                                            return None
                                            None = 
                                            del e





    
    def has_animated_layers(self = None, layers = None):
        '''
        레이어 목록에 애니메이션이 있는 레이어가 있는지 확인

        Args:
            layers: 컴포지터 레이어 목록

        Returns:
            애니메이션 레이어 존재 여부
        '''
        for layer in layers:
            animation = layer.get('animation', { })
            preset = animation.get('preset', 'none')
            if preset != 'none':
                return True
            return False
