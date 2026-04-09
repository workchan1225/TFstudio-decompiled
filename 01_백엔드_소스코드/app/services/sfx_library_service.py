# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: sfx_library_service.pyc (Python 3.11)

'''
SFX 라이브러리 서비스

프로젝트 간 재사용 가능한 SFX를 관리합니다.
로컬 저장, 검색, 즐겨찾기 기능을 제공합니다.
'''
import os
import json
import shutil
import logging
import uuid
from typing import Dict, List, Optional, Any
from pathlib import Path
from datetime import datetime
from app.config.paths import get_data_path
logger = logging.getLogger(__name__)
LIBRARY_FOLDER = 'sfx_library'
METADATA_FILE = 'library_index.json'
MAX_LIBRARY_SIZE_MB = 500

class SFXLibraryService:
    '''SFX 라이브러리 관리 서비스'''
    
    def __init__(self):
        '''라이브러리 초기화'''
        self.library_path = get_data_path() / LIBRARY_FOLDER
        self.library_path.mkdir(parents = True, exist_ok = True)
        self.metadata_path = self.library_path / METADATA_FILE
        self._ensure_metadata_exists()

    
    def _ensure_metadata_exists(self = None):
        '''메타데이터 파일 초기화'''
        if not self.metadata_path.exists():
            initial_data = {
                'version': '1.0',
                'createdAt': datetime.utcnow().isoformat(),
                'items': [] }
            self._save_metadata(initial_data)
            return None

    
    def _load_metadata(self = None):
        '''메타데이터 로드'''
        
        try:
            f = open(self.metadata_path, 'r', encoding = 'utf-8')
            
            try:
                None(None, None)
                return 
                with None:
                    if not None, json.load(f):
                        
                        try:
                            
                            try:
                                return None
                            except Exception:
                                logger.error(f'''[SFXLibrary] Failed to load metadata: {e}''')
                                del e
                                return None
                                None = 
                                del e





    
    def _save_metadata(self = None, data = None):
        '''메타데이터 저장'''
        
        try:
            f = open(self.metadata_path, 'w', encoding = 'utf-8')
            json.dump(data, f, ensure_ascii = False, indent = 2)
            
            try:
                None(None, None)
                return None
                with None:
                    if not None:
                        
                        try:
                            
                            try:
                                return None
                            except Exception:
                                e = None
                                logger.error(f'''[SFXLibrary] Failed to save metadata: {e}''')
                                e = None
                                del e
                                return None
                                e = None
                                del e





    
    def check_duplicate(self = None, name = None, original_filename = None):
        '''
        중복 항목 확인

        Args:
            name: SFX 이름
            original_filename: 원본 파일명 (선택)

        Returns:
            중복 항목이 있으면 해당 항목, 없으면 None
        '''
        data = self._load_metadata()
        name_lower = name.lower().strip()
        for item in data.get('items', []):
            if item.get('name', '').lower().strip() == name_lower:
                
                return None, item
            if None and item_original and item_original.lower() == original_filename.lower():
                
                return item.get('metadata', { }).get('original_filename', ''), item
            return None

    
    def add_to_library(self, source_path, name, description = None, category = None, tags = None, metadata = ('', 'action', None, None, False), allow_duplicate = ('source_path', str, 'name', str, 'description', str, 'category', str, 'tags', Optional[List[str]], 'metadata', Optional[Dict], 'allow_duplicate', bool, 'return', Dict[(str, Any)])):
        '''
        SFX를 라이브러리에 추가

        Args:
            source_path: 원본 파일 경로
            name: SFX 이름
            description: 설명
            category: 카테고리 (action, ambient, voice, music, ui, nature)
            tags: 태그 목록
            metadata: 추가 메타데이터
            allow_duplicate: 중복 허용 여부 (기본 False)

        Returns:
            추가 결과
        '''
        source = Path(source_path)
        if not source.exists():
            return {
                'success': False,
                'error': f'''File not found: {source_path}''' }
        original_filename = metadata.get('original_filename') if None else None
    # WARNING: Decompyle incomplete

    
    def remove_from_library(self = None, item_id = None):
        '''
        SFX를 라이브러리에서 제거

        Args:
            item_id: 항목 ID

        Returns:
            제거 결과
        '''
        pass
    # WARNING: Decompyle incomplete

    
    def get_library_items(self, category, tags, search, favorites_only = None, sort_by = None, sort_order = None, limit = (None, None, None, False, 'addedAt', 'desc', 50, 0), offset = ('category', Optional[str], 'tags', Optional[List[str]], 'search', Optional[str], 'favorites_only', bool, 'sort_by', str, 'sort_order', str, 'limit', int, 'offset', int, 'return', Dict[(str, Any)])):
        '''
        라이브러리 항목 조회

        Args:
            category: 카테고리 필터
            tags: 태그 필터
            search: 검색어 (이름, 설명)
            favorites_only: 즐겨찾기만
            sort_by: 정렬 기준 (addedAt, name, usageCount)
            sort_order: 정렬 순서 (asc, desc)
            limit: 조회 개수
            offset: 오프셋

        Returns:
            항목 목록
        '''
        pass
    # WARNING: Decompyle incomplete

    
    def get_item(self = None, item_id = None):
        '''
        단일 항목 조회

        Args:
            item_id: 항목 ID

        Returns:
            항목 정보 또는 None
        '''
        data = self._load_metadata()
        for item in data.get('items', []):
            if item['id'] == item_id:
                item['fileUrl'] = f'''/data/{LIBRARY_FOLDER}/{item['filename']}'''
                
                return None, item
            return None

    
    def update_item(self = None, item_id = None, updates = None):
        '''
        항목 정보 업데이트

        Args:
            item_id: 항목 ID
            updates: 업데이트할 필드들

        Returns:
            업데이트 결과
        '''
        data = self._load_metadata()
        for item in data.get('items', []):
            if item['id'] == item_id:
                allowed_fields = [
                    'name',
                    'description',
                    'category',
                    'tags',
                    'isFavorite',
                    'metadata']
                for field in allowed_fields:
                    if field in updates:
                        item[field] = updates[field]
                    item['updatedAt'] = datetime.utcnow().isoformat()
                    data['updatedAt'] = datetime.utcnow().isoformat()
                    self._save_metadata(data)
                    item['fileUrl'] = f'''/data/{LIBRARY_FOLDER}/{item['filename']}'''
                    
                    return None, {
                        'success': True,
                        'item': item }
                    return {
                        'success': False,
                        'error': 'Item not found' }

    
    def toggle_favorite(self = None, item_id = None):
        '''즐겨찾기 토글'''
        data = self._load_metadata()
        for item in data.get('items', []):
            if item['id'] == item_id:
                item['isFavorite'] = not item.get('isFavorite', False)
                data['updatedAt'] = datetime.utcnow().isoformat()
                self._save_metadata(data)
                
                return None, {
                    'success': True,
                    'isFavorite': item['isFavorite'] }
            return {
                'success': False,
                'error': 'Item not found' }

    
    def increment_usage(self = None, item_id = None):
        '''사용 횟수 증가'''
        data = self._load_metadata()
        for item in data.get('items', []):
            if item['id'] == item_id:
                item['usageCount'] = item.get('usageCount', 0) + 1
                item['lastUsedAt'] = datetime.utcnow().isoformat()
                self._save_metadata(data)
                return None
            return None

    
    def get_categories(self = None):
        '''카테고리별 항목 수 반환'''
        data = self._load_metadata()
        items = data.get('items', [])
        category_counts = { }
        for item in items:
            cat = item.get('category', 'unknown')
            category_counts[cat] = category_counts.get(cat, 0) + 1
            categories = category_counts.items()()
            categories.sort(key = (lambda x: x['count']), reverse = True)
            return categories

    
    def get_popular_tags(self = None, limit = None):
        '''인기 태그 반환'''
        data = self._load_metadata()
        items = data.get('items', [])
        tag_counts = { }
        for item in items:
            for tag in item.get('tags', []):
                tag_counts[tag] = tag_counts.get(tag, 0) + 1
                tags = tag_counts.items()()
                tags.sort(key = (lambda x: x['count']), reverse = True)
                return tags[:limit]

    
    def get_library_stats(self = None):
        '''라이브러리 통계'''
        data = self._load_metadata()
        items = data.get('items', [])
        total_size = (lambda .0: pass# WARNING: Decompyle incomplete
)(items())
        total_usage = (lambda .0: pass# WARNING: Decompyle incomplete
)(items())
        favorites = (lambda .0: pass# WARNING: Decompyle incomplete
)(items())
        return {
            'totalItems': len(items),
            'totalSizeBytes': total_size,
            'totalSizeMB': round(total_size / 1048576, 2),
            'totalUsage': total_usage,
            'favorites': favorites,
            'categories': self.get_categories(),
            'maxSizeMB': MAX_LIBRARY_SIZE_MB,
            'usedPercent': round((total_size / (MAX_LIBRARY_SIZE_MB * 1024 * 1024)) * 100, 1) }

    
    def _check_storage_limit(self = None, new_file_size = None):
        '''저장 용량 확인'''
        data = self._load_metadata()
        items = data.get('items', [])
        current_size = (lambda .0: pass# WARNING: Decompyle incomplete
)(items())
        max_size = MAX_LIBRARY_SIZE_MB * 1024 * 1024
        return current_size + new_file_size <= max_size

    
    def import_from_project(self = None, project_id = None, sfx_tracks = None, auto_name = (True,)):
        '''
        프로젝트의 SFX를 라이브러리로 가져오기

        Args:
            project_id: 프로젝트 ID
            sfx_tracks: 가져올 SFX 트랙 리스트
            auto_name: 자동 이름 생성 여부

        Returns:
            가져오기 결과
        '''
        imported = []
        failed = []
        for track in sfx_tracks:
            file_path = self._resolve_track_path(track.get('fileUrl', ''))
            if not file_path or Path(file_path).exists():
                failed.append({
                    'trackId': track.get('id'),
                    'error': 'File not found' })
                continue
            name = track.get('name', '')
            if not auto_name and name:
                name = f'''SFX_{track.get('metadata', { }).get('category', 'unknown')}_{len(imported) + 1}'''
            result = self.add_to_library(source_path = file_path, name = name, description = track.get('description', ''), category = track.get('metadata', { }).get('category', 'action'), tags = track.get('metadata', { }).get('tags', []), metadata = {
                'sourceProject': project_id,
                'originalTrackId': track.get('id'),
                'duration': track.get('duration') })
            if result.get('success'):
                imported.append(result['item'])
                continue
            failed.append({
                'trackId': track.get('id'),
                'error': result.get('error') })
            return {
                'success': len(imported) > 0,
                'imported': imported,
                'importedCount': len(imported),
                'failed': failed,
                'failedCount': len(failed) }

    
    def _resolve_track_path(self = None, file_url = None):
