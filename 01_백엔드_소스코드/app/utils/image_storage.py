# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: image_storage.pyc (Python 3.11)

'''
장면 이미지 파일 저장/로드 유틸리티

Base64 이미지 데이터를 파일시스템에 저장하고 경로로 관리합니다.
JSON/DB에는 경로만 저장하여 크기 초과 문제를 해결합니다.

저장 구조:
    data/projects/{project_id}/images/scenes/scene_{index}.png
    data/projects/{project_id}/images/characters/char_{uniqueId}.png
    data/projects/{project_id}/images/assets/asset_{assetId}.png
'''
import base64
import logging
import os
import re
import shutil
from pathlib import Path
from typing import Optional, Tuple, Union
logger = logging.getLogger(__name__)

class SceneImageStorage:
    '''장면 이미지 저장/로드 관리 클래스'''
    
    def __init__(self = None, project_id = None, backend_dir = None):
        '''
        Args:
            project_id: 프로젝트 ID (UUID)
            backend_dir: 백엔드 루트 디렉토리 (None이면 자동 탐지)
        '''
        self.project_id = project_id
    # WARNING: Decompyle incomplete

    
    def ensure_directories(self):
        '''이미지 저장 디렉토리 생성'''
        self.scenes_dir.mkdir(parents = True, exist_ok = True)
        self.characters_dir.mkdir(parents = True, exist_ok = True)
        self.assets_dir.mkdir(parents = True, exist_ok = True)

    
    def _backup_existing_file(self = None, file_path = None, backup_dir = None):
        '''
        기존 파일을 백업 폴더로 복사 (타임스탬프 포함)

        Args:
            file_path: 백업할 원본 파일 경로
            backup_dir: 백업 디렉토리 경로

        Returns:
            백업 파일 경로 (상대 경로). 백업 불필요 또는 실패시 None
        '''
        if not file_path.exists():
            return None
        
        try:
            backup_dir.mkdir(parents = True, exist_ok = True)
            datetime = datetime
            import datetime
            timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
            stem = file_path.stem
            suffix = file_path.suffix
            backup_filename = f'''{stem}_{timestamp}{suffix}'''
            backup_path = backup_dir / backup_filename
            shutil.copy2(file_path, backup_path)
            relative_path = str(backup_path.relative_to(self._data_dir)).replace('\\', '/')
            logger.info(f'''Backed up existing file: {file_path.name} -> {backup_filename}''')
            return relative_path
        except Exception:
            e = None
            logger.warning(f'''Failed to backup file {file_path}: {e}''')
            e = None
            del e
            return None
            e = None
            del e


    
    def _parse_base64_data(self = None, base64_data = None):
        '''
        Base64 데이터 URL을 파싱하여 바이너리와 확장자 반환

        Args:
            base64_data: "data:image/png;base64,..." 형식의 데이터

        Returns:
            (바이너리 데이터, 확장자) 튜플. 실패시 (None, \'\')
        '''
        if not base64_data:
            return (None, '')
        
        try:
            if base64_data.startswith('data:'):
                match = re.match('data:image/(\\w+);base64,(.+)', base64_data)
                if match:
                    ext = match.group(1)
                    b64_content = match.group(2)
                    if ext == 'jpeg':
                        ext = 'jpg'
                    return (base64.b64decode(b64_content), ext)
                return (None.b64decode(base64_data), 'png')
            except Exception:
                e = None
                logger.error(f'''Failed to parse base64 data: {e}''')
                e = None
                del e
                return (None, '')
                e = None
                del e


    
    def save_scene_image(self = None, index = None, base64_data = None, is_local_upload = (False,)):
        '''
        장면 이미지를 파일로 저장

        Args:
            index: 장면 인덱스 (int 또는 "chapterIndex_sceneIndex" 형식의 문자열)
            base64_data: Base64 인코딩된 이미지 데이터
            is_local_upload: 로컬 업로드 여부 (True인 경우에만 기존 파일 백업)

        Returns:
            저장된 파일의 상대 경로 (backend 기준). 실패시 None
        '''
        logger.info(f'''[save_scene_image] START index={index}, is_local_upload={is_local_upload}, base64_data_len={len(base64_data) if base64_data else 0}''')
        if not base64_data:
            logger.warning(f'''[save_scene_image] base64_data is empty for index={index}''')
            return None
        None.ensure_directories()
        logger.info(f'''[save_scene_image] scenes_dir={self.scenes_dir}, exists={self.scenes_dir.exists()}''')
        (binary_data, ext) = self._parse_base64_data(base64_data)
    # WARNING: Decompyle incomplete

    
    def save_character_image(self = None, unique_id = None, base64_data = None, is_local_upload = (False,)):
        """
        캐릭터 참조 이미지를 파일로 저장

        Args:
            unique_id: 캐릭터 고유 ID (예: 'CHAR_A')
            base64_data: Base64 인코딩된 이미지 데이터
            is_local_upload: 로컬 업로드 여부 (True인 경우에만 기존 파일 백업)

        Returns:
            저장된 파일의 상대 경로. 실패시 None
        """
        if not base64_data or unique_id:
            return None
        None.ensure_directories()
        (binary_data, ext) = self._parse_base64_data(base64_data)
    # WARNING: Decompyle incomplete

    
    def save_asset_image(self = None, asset_id = None, base64_data = None, is_local_upload = (False,)):
        '''씬 자산 이미지를 파일로 저장.'''
        if not base64_data or asset_id:
            return None
        None.ensure_directories()
        (binary_data, ext) = self._parse_base64_data(base64_data)
    # WARNING: Decompyle incomplete

    
    def overwrite_media_file(self = None, target_path = None, base64_data = None):
        '''
        기존 미디어 파일을 새 이미지로 덮어쓰기 (파일명 유지)

        업로드된 미디어 파일의 내용만 교체하고 파일명은 유지합니다.
        "업로드된 미디어" 탭에서 교체된 이미지가 바로 보이도록 합니다.

        Args:
            target_path: 덮어쓸 파일의 상대 경로 (예: projects/{id}/images/ch2_1_xxx.png)
            base64_data: Base64 인코딩된 새 이미지

        Returns:
            성공 여부
        '''
        if not target_path or base64_data:
            logger.warning('overwrite_media_file: target_path or base64_data is empty')
            return False
        normalized_path = None.replace('\\', '/')
        logger.info(f'''[overwrite_media_file] Input target_path: {target_path[:100] if target_path else 'None'}''')
        logger.info(f'''[overwrite_media_file] normalized_path: {normalized_path}''')
        logger.info(f'''[overwrite_media_file] _data_dir: {self._data_dir}''')
        logger.info(f'''[overwrite_media_file] base64_data length: {len(base64_data) if base64_data else 0}''')
        if '..' in normalized_path:
            logger.warning(f'''overwrite_media_file: Path traversal attempt blocked: {normalized_path}''')
            return False
        full_path = None._data_dir / normalized_path
        logger.info(f'''[overwrite_media_file] full_path: {full_path}''')
    # WARNING: Decompyle incomplete

    
    def _normalize_stored_relative_path(self = None, raw_path = None):
        '''Normalize stored image path values across legacy formats.'''
        if not raw_path:
            normalized_path = str('').replace('\\', '/').strip()
            if not normalized_path:
                return ''
            if None.match('^/[A-Za-z]:/', normalized_path):
                normalized_path = normalized_path[1:]
        if normalized_path.startswith('/data/'):
            normalized_path = normalized_path[6:]
        elif normalized_path.startswith('data/'):
            normalized_path = normalized_path[5:]
        if not normalized_path.startswith('/') and normalized_path.startswith('//'):
            normalized_path = normalized_path.lstrip('/')
        return normalized_path

    
    def load_image_as_base64(self = None, relative_path = None):
        '''
        저장된 이미지를 Base64 데이터 URL로 로드

        Args:
            relative_path: data_dir 기준 상대 경로

        Returns:
            "data:image/png;base64,..." 형식의 데이터. 실패시 None
        '''
        if not relative_path:
            logger.debug('[SceneImageStorage] load_image_as_base64 called with empty path')
            return None
        
        try:
            normalized_path = self._normalize_stored_relative_path(relative_path)
            if not normalized_path:
                logger.debug('[SceneImageStorage] normalized path is empty after cleanup')
                return None
            None.info(f'''[SceneImageStorage] Loading image: {normalized_path}''')
            logger.debug(f'''[SceneImageStorage] data_dir: {self._data_dir}, backend_dir: {self.backend_dir}''')
            file_path = self._data_dir / normalized_path
            logger.debug(f'''[SceneImageStorage] Try 1 - data_dir path: {file_path}, exists: {file_path.exists()}''')
            if file_path.exists() and Path(normalized_path).is_absolute():
                file_path = Path(normalized_path)
                logger.debug(f'''[SceneImageStorage] Try 2 - absolute path: {file_path}, exists: {file_path.exists()}''')
            if not file_path.exists() and Path(normalized_path).is_absolute() and normalized_path.startswith('projects/'):
                file_path = self._data_dir / 'projects' / normalized_path
                logger.debug(f'''[SceneImageStorage] Try 3 - projects prefix path: {file_path}, exists: {file_path.exists()}''')
            if not file_path.exists():
                file_path = self.backend_dir / normalized_path
                logger.debug(f'''[SceneImageStorage] Try 4 - backend_dir path: {file_path}, exists: {file_path.exists()}''')
            if not file_path.exists():
                logger.error(f'''[SceneImageStorage] Image file not found after all attempts: {relative_path}''')
                logger.error(f'''[SceneImageStorage] Searched paths: data_dir={self._data_dir}, backend_dir={self.backend_dir}''')
                return None
            None.info(f'''[SceneImageStorage] Image found at: {file_path}''')
            ext = file_path.suffix.lower().lstrip('.')
            mime_type = {
                'png': 'image/png',
                'jpg': 'image/jpeg',
                'jpeg': 'image/jpeg',
                'gif': 'image/gif',
                'webp': 'image/webp' }.get(ext, 'image/png')
            f = open(file_path, 'rb')
            binary_data = f.read()
            
            try:
                None(None, None)
            with None:
                if not None:
                    
                    try:
                        
                        try:
                            b64_content = base64.b64encode(binary_data).decode('utf-8')
                            return f'''data:{mime_type};base64,{b64_content}'''
                        except Exception:
                            e = None
                            logger.error(f'''Failed to load image {relative_path}: {e}''')
                            e = None
                            del e
                            return None
                            e = None
                            del e





    
    def delete_all_images(self = None):
        '''
        프로젝트의 모든 장면/캐릭터 이미지 삭제

        Returns:
            성공 여부
        '''
        
        try:
            if self.scenes_dir.exists():
                shutil.rmtree(self.scenes_dir)
                logger.info(f'''Deleted scenes directory: {self.scenes_dir}''')
            if self.characters_dir.exists():
                shutil.rmtree(self.characters_dir)
                logger.info(f'''Deleted characters directory: {self.characters_dir}''')
            return True
        except Exception:
            e = None
            logger.error(f'''Failed to delete images for project {self.project_id}: {e}''')
            e = None
            del e
            return False
            e = None
            del e


    
    def delete_scene_images_only(self = None):
        '''
        프로젝트의 장면 이미지만 삭제 (캐릭터 이미지 유지)

        Returns:
            성공 여부
        '''
        
        try:
            if self.scenes_dir.exists():
                shutil.rmtree(self.scenes_dir)
                logger.info(f'''Deleted scenes directory only: {self.scenes_dir}''')
            return True
        except Exception:
            e = None
            logger.error(f'''Failed to delete scene images for project {self.project_id}: {e}''')
            e = None
            del e
            return False
            e = None
            del e


    
    def delete_scene_image_paths(self = None, stored_paths = None):
        '''Delete only the specified scene image files.'''
        
        try:
            scenes_dir_resolved = self.scenes_dir.resolve()
            removed_any = False
            for raw_path in stored_paths:
                normalized_path = self._normalize_stored_relative_path(raw_path)
                if not normalized_path:
                    continue
                candidate_path = self._data_dir / normalized_path
                resolved_candidate = candidate_path.resolve()
                
                try:
                    pass
                except Exception:
                    logger.warning(f'''Failed to resolve scene image path for deletion: {normalized_path}''')
                    
                    try:
                        continue
                        
                        try:
                            if not str(resolved_candidate).startswith(str(scenes_dir_resolved)):
                                logger.warning(f'''Skipping non-scene image path deletion outside scenes dir: {normalized_path}''')
                                continue
                            if resolved_candidate.exists() and resolved_candidate.is_file():
                                resolved_candidate.unlink()
                                removed_any = True
                            continue
                            if removed_any and self.scenes_dir.exists():
                                
                                try:
                                    next(self.scenes_dir.iterdir())
                                    
                                    try:
                                        pass
                                    except StopIteration:
                                        shutil.rmtree(self.scenes_dir)
                                        logger.info(f'''Deleted empty scenes directory: {self.scenes_dir}''')
                                        
                                        try:
                                            pass
                                        try:
                                            return True
                                        except Exception:
                                            e = None
                                            logger.error(f'''Failed to delete selected scene images for project {self.project_id}: {e}''')
                                            e = None
                                            del e
                                            return False
                                            e = None
                                            del e








    
    def migrate_base64_to_files(self = None, scene_images = None, character_images = None, asset_library = (None, None), scene_key_suffix = ('scene_images', list, 'character_images', list, 'asset_library', Optional[list], 'scene_key_suffix', Optional[str], 'return', Tuple[(list, list, list)])):
        '''
        기존 Base64 데이터를 파일로 마이그레이션

        Args:
            scene_images: sceneImages 리스트 (imageDataUrl 포함)
            character_images: characterImages 리스트 (imageDataUrl 포함)

        Returns:
            (업데이트된 scene_images, 업데이트된 character_images, 업데이트된 asset_library) 튜플
            - imageDataUrl은 제거되고 imagePath가 추가됨
        '''
        migrated_scenes = []
        migrated_characters = []
        migrated_assets = []
        logger.info(f'''[migrate_base64_to_files] Processing {len(scene_images)} scenes''')
        for idx, scene in enumerate(scene_images):
            scene_copy = dict(scene)
            has_image_path = bool(scene_copy.get('imagePath'))
            has_data_url = bool(scene_copy.get('imageDataUrl'))
            is_local = scene_copy.get('isLocalUpload', False)
            logger.info(f'''[migrate_base64_to_files] Scene {idx}: imagePath={has_image_path}, imageDataUrl={has_data_url}, isLocalUpload={is_local}''')
            if not scene_copy.get('imagePath') and scene_copy.get('imageDataUrl'):
                normalized_path = self._normalize_stored_relative_path(scene_copy['imagePath'])
                file_path = self._data_dir / normalized_path
                if not file_path.exists():
                    file_path = self.backend_dir / normalized_path
                if file_path.exists():
                    scene_copy['imagePath'] = normalized_path
                    scene_copy.pop('imageDataUrl', None)
                    migrated_scenes.append(scene_copy)
                    logger.info(f'''[migrate_base64_to_files] Scene {idx}: keeping existing file (no new imageDataUrl)''')
                    continue
            if scene_copy.get('imageDataUrl'):
                chapter_idx = scene_copy.get('chapterIndex', 0)
                scene_idx = scene_copy.get('sceneIndex', idx)
                unique_idx = f'''ch{chapter_idx + 1}_{scene_idx + 1}'''
                if scene_key_suffix:
                    safe_suffix = re.sub('[^a-zA-Z0-9_-]', '_', str(scene_key_suffix).strip())
                    if safe_suffix:
                        unique_idx = f'''{unique_idx}_{safe_suffix}'''
                is_local_upload = scene_copy.get('isLocalUpload', False)
                image_data_url_len = len(scene_copy['imageDataUrl']) if scene_copy.get('imageDataUrl') else 0
                logger.info(f'''[migrate_base64_to_files] Scene {idx} has imageDataUrl (len={image_data_url_len}), saving with isLocalUpload={is_local_upload}''')
                saved_path = self.save_scene_image(unique_idx, scene_copy['imageDataUrl'], is_local_upload = is_local_upload)
                if saved_path:
                    scene_copy['imagePath'] = saved_path
                    scene_copy.pop('imageDataUrl', None)
                    scene_copy.pop('isLocalUpload', None)
                    logger.info(f'''Migrated scene ch{chapter_idx}_sc{scene_idx} to file: {saved_path} (isLocalUpload={is_local_upload})''')
                else:
                    logger.error(f'''[migrate_base64_to_files] FAILED to save scene ch{chapter_idx}_sc{scene_idx} - save_scene_image returned None''')
            else:
                logger.info(f'''[migrate_base64_to_files] Scene {idx} has NO imageDataUrl (skipping save)''')
            migrated_scenes.append(scene_copy)
            for idx, char in enumerate(character_images):
                char_copy = dict(char)
                if not char_copy.get('uniqueId'):
                    if not char_copy.get('characterName'):
                        unique_id = f'''CHAR_{chr(65 + idx)}'''
                        char_copy['uniqueId'] = unique_id
                        if not char_copy.get('imagePath') and char_copy.get('imageDataUrl'):
                            normalized_path = self._normalize_stored_relative_path(char_copy['imagePath'])
                            file_path = self._data_dir / normalized_path
                            if not file_path.exists():
                                file_path = self.backend_dir / normalized_path
                            if file_path.exists():
                                char_copy['imagePath'] = normalized_path
                                char_copy.pop('imageDataUrl', None)
                                migrated_characters.append(char_copy)
                                logger.info(f'''[migrate_base64_to_files] Character {idx}: keeping existing file (no new imageDataUrl)''')
                                continue
                if char_copy.get('imageDataUrl') and unique_id:
                    if not char_copy.get('sourceType') == 'local_upload':
                        is_local_upload = char_copy.get('isLocalUpload', False)
                        saved_path = self.save_character_image(unique_id, char_copy['imageDataUrl'], is_local_upload = is_local_upload)
                        if saved_path:
                            char_copy['imagePath'] = saved_path
                            char_copy.pop('imageDataUrl', None)
                            char_copy.pop('isLocalUpload', None)
                            logger.info(f'''Migrated character {unique_id} to file: {saved_path} (isLocalUpload={is_local_upload})''')
                migrated_characters.append(char_copy)
                if not asset_library:
                    for idx, asset in enumerate([]):
                        asset_copy = dict(asset)
                        if not asset_copy.get('assetId'):
                            asset_id = str('').strip()
                            if not asset_copy.get('imagePath') and asset_copy.get('imageDataUrl'):
                                normalized_path = self._normalize_stored_relative_path(asset_copy['imagePath'])
                                file_path = self._data_dir / normalized_path
                                if not file_path.exists():
                                    file_path = self.backend_dir / normalized_path
                                if file_path.exists():
                                    asset_copy['imagePath'] = normalized_path
                                    asset_copy.pop('imageDataUrl', None)
                                    migrated_assets.append(asset_copy)
                                    continue
                        if asset_copy.get('imageDataUrl') and asset_id:
                            if not asset_copy.get('source') == 'uploaded':
                                is_local_upload = asset_copy.get('isLocalUpload', False)
                                saved_path = self.save_asset_image(asset_id, asset_copy['imageDataUrl'], is_local_upload = is_local_upload)
                                if saved_path:
                                    asset_copy['imagePath'] = saved_path
                                    asset_copy.pop('imageDataUrl', None)
                                    asset_copy.pop('isLocalUpload', None)
                        migrated_assets.append(asset_copy)
                        return (migrated_scenes, migrated_characters, migrated_assets)

    
    def restore_base64_data(self = None, scene_images = None, character_images = None, asset_library = (None,)):
        '''
        파일 경로에서 Base64 데이터를 복원 (API 응답용)

        Args:
            scene_images: sceneImages 리스트 (imagePath 포함)
            character_images: characterImages 리스트 (imagePath 포함)

        Returns:
            (복원된 scene_images, 복원된 character_images, 복원된 asset_library) 튜플
            - imagePath에서 imageDataUrl을 복원
        '''
        if not asset_library:
            logger.info(f'''[SceneImageStorage] restore_base64_data called: scene_images={len(scene_images)}, character_images={len(character_images)}, asset_library={len([])}''')
            restored_scenes = []
            restored_characters = []
            restored_assets = []
            scene_restore_success = 0
            scene_restore_fail = 0
            char_restore_success = 0
            char_restore_fail = 0
            asset_restore_success = 0
            asset_restore_fail = 0
            for idx, scene in enumerate(scene_images):
                scene_copy = dict(scene)
                if scene_copy.get('generatedVideoPath'):
                    video_rel_path = scene_copy['generatedVideoPath'].replace('\\', '/')
                    video_abs_path = self._data_dir / video_rel_path
                    if not video_abs_path.exists():
                        logger.debug(f'''[SceneImageStorage] Scene {idx} video not found, clearing path: {video_rel_path}''')
                        scene_copy['generatedVideoPath'] = None
                if scene_copy.get('imageDataUrl'):
                    restored_scenes.append(scene_copy)
                    scene_restore_success += 1
                    continue
                if scene_copy.get('imagePath'):
                    image_data = self.load_image_as_base64(scene_copy['imagePath'])
                    if image_data:
                        scene_copy['imageDataUrl'] = image_data
                        scene_restore_success += 1
                    else:
                        logger.warning(f'''[SceneImageStorage] Scene {idx} restore failed, preserving imagePath: {scene_copy.get('imagePath')}''')
                        scene_restore_fail += 1
                else:
                    logger.debug(f'''[SceneImageStorage] Scene {idx} has no imagePath''')
                restored_scenes.append(scene_copy)
                for idx, char in enumerate(character_images):
                    char_copy = dict(char)
                    if char_copy.get('imageDataUrl'):
                        restored_characters.append(char_copy)
                        char_restore_success += 1
                        continue
                    if char_copy.get('imagePath'):
                        image_data = self.load_image_as_base64(char_copy['imagePath'])
                        if image_data:
                            char_copy['imageDataUrl'] = image_data
                            char_restore_success += 1
                        else:
                            logger.warning(f'''[SceneImageStorage] Character {idx} restore failed, preserving imagePath: {char_copy.get('imagePath')}''')
                            char_restore_fail += 1
                    else:
                        logger.debug(f'''[SceneImageStorage] Character {idx} has no imagePath''')
                    restored_characters.append(char_copy)
                    if not asset_library:
                        for idx, asset in enumerate([]):
                            asset_copy = dict(asset)
                            if asset_copy.get('imageDataUrl'):
                                restored_assets.append(asset_copy)
                                asset_restore_success += 1
                                continue
                            if asset_copy.get('imagePath'):
                                image_data = self.load_image_as_base64(asset_copy['imagePath'])
                                if image_data:
                                    asset_copy['imageDataUrl'] = image_data
                                    asset_restore_success += 1
                                else:
                                    logger.warning(f'''[SceneImageStorage] Asset {idx} restore failed, preserving imagePath: {asset_copy.get('imagePath')}''')
                                    asset_restore_fail += 1
                            restored_assets.append(asset_copy)
                            logger.info(f'''[SceneImageStorage] restore_base64_data completed: scenes(success={scene_restore_success}, fail={scene_restore_fail}), characters(success={char_restore_success}, fail={char_restore_fail}), assets(success={asset_restore_success}, fail={asset_restore_fail})''')
                            return (restored_scenes, restored_characters, restored_assets)

    
    def scan_character_images_from_disk(self = None, analyzed_characters = None):
