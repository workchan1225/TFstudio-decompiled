# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: character_rename_service.pyc (Python 3.11)

'''
Character Rename Service (등장인물 이름 변경 서비스)

등장인물 이름 변경 시 대본, TTS 데이터, 오디오 파일을 동기화합니다.
'''
import os
import re
import logging
from pathlib import Path
from typing import Dict, Any, Tuple, List, Optional
from copy import deepcopy
from app import db
from app.models.project import Project
from app.utils.file_paths import ProjectPaths
logger = logging.getLogger(__name__)

class CharacterRenameService:
    '''등장인물 이름 변경 및 관련 데이터 동기화 서비스'''
    
    def rename_character(self = None, project_id = None, unique_id = None, new_name = ('project_id', str, 'unique_id', str, 'new_name', str, 'return', Dict[(str, Any)])):
        """
        등장인물 이름 변경 (대본, TTS 데이터, 오디오 파일 동기화)

        Args:
            project_id: 프로젝트 ID
            unique_id: 등장인물 고유 ID (A, B, C 등)
            new_name: 새 이름

        Returns:
            {
                'status': 'success',
                'oldName': '홍길동',
                'newName': '김철수',
                'updatedScriptLines': 15,
                'updatedTtsReferences': 23,
                'renamedFiles': 10
            }

        Raises:
            ValueError: 검증 실패 시
            Exception: 처리 중 오류 발생 시
        """
        new_name = new_name.strip() if new_name else ''
        if not new_name:
            raise ValueError('이름을 입력해주세요')
        project = Project.query.get(project_id)
        if not project:
            raise ValueError('프로젝트를 찾을 수 없습니다')
    # WARNING: Decompyle incomplete

    
    def _update_script_speaker_names(self = None, script = None, old_name = None, new_name = ('script', str, 'old_name', str, 'new_name', str, 'return', Tuple[(str, int)])):
        '''
        대본에서 화자 태그 이름 변경

        Args:
            script: 원본 대본 텍스트
            old_name: 이전 이름
            new_name: 새 이름

        Returns:
            (변경된 대본, 변경된 줄 수)
        '''
        if not script:
            return (script, 0)
        pattern = f'''{re.escape(old_name)}(\\]?:\\s*)'''
        replacement = f'''\\g<1>{new_name}\\g<2>'''
        lines = script.split('\n')
        updated_lines = []
        change_count = 0
        for line in lines:
            (new_line, subs) = re.subn(pattern, replacement, line, count = 1, flags = re.MULTILINE)
            if subs > 0:
                change_count += 1
            updated_lines.append(new_line)
            return ('\n'.join(updated_lines), change_count)

    
    def _update_tts_data_speaker_names(self = None, tts_data = None, old_name = None, new_name = ('tts_data', Dict[(str, Any)], 'old_name', str, 'new_name', str, 'return', Tuple[(Dict[(str, Any)], int)])):
        '''
        TTS 데이터에서 화자 이름 및 경로 변경

        Args:
            tts_data: speaker_tts_data JSON
            old_name: 이전 이름
            new_name: 새 이름

        Returns:
            (변경된 TTS 데이터, 변경된 참조 수)
        '''
        if not tts_data:
            return (tts_data, 0)
        result = None(tts_data)
        change_count = 0
        voice_assignments = result.get('voiceAssignments', [])
        for va in voice_assignments:
            if va.get('speaker') == old_name:
                va['speaker'] = new_name
                change_count += 1
            audio_results = result.get('audioResults', [])
            for ar in audio_results:
                if ar.get('speaker') == old_name:
                    ar['speaker'] = new_name
                    change_count += 1
                if ar.get('audioUrl'):
                    ar['audioUrl'] = self._replace_name_in_path(ar['audioUrl'], old_name, new_name)
                for seg in ar.get('segments', []):
                    if seg.get('audioPath'):
                        seg['audioPath'] = self._replace_name_in_path(seg['audioPath'], old_name, new_name)
                    merged_segments = result.get('mergedSegments', [])
                    for ms in merged_segments:
                        if ms.get('speaker') == old_name:
                            ms['speaker'] = new_name
                            change_count += 1
                        subtitle_segments = result.get('subtitleSegments', [])
                        for ss in subtitle_segments:
                            if ss.get('speaker') == old_name:
                                ss['speaker'] = new_name
                                change_count += 1
                            for key in ('googleTtsSingle', 'edgeTtsSingle', 'geminiTtsSingle', 'typecastTtsSingle'):
                                if key in result:
                                    single_data = result[key]
                                    if isinstance(single_data, dict):
                                        for seg in single_data.get('segments', []):
                                            if seg.get('speaker') == old_name:
                                                seg['speaker'] = new_name
                                                change_count += 1
                                            for seg in single_data.get('subtitleSegments', []):
                                                if seg.get('speaker') == old_name:
                                                    seg['speaker'] = new_name
                                                    change_count += 1
                                                return (result, change_count)

    
    def _replace_name_in_path(self = None, path = None, old_name = None, new_name = ('path', str, 'old_name', str, 'new_name', str, 'return', str)):
        '''
        파일 경로에서 화자 이름 변경

        Args:
            path: 파일 경로
            old_name: 이전 이름
            new_name: 새 이름

        Returns:
            변경된 경로
        '''
        if not path:
            return path
        normalized_path = None.replace('\\', '/')
        dir_part = '/'.join(normalized_path.split('/')[:-1])
        filename = normalized_path.split('/')[-1]
        if filename.startswith(f'''{old_name}_'''):
            filename = f'''{new_name}_''' + filename[len(old_name) + 1:]
        elif filename == f'''{old_name}.mp3''':
            filename = f'''{new_name}.mp3'''
        return f'''{dir_part}/{filename}''' if dir_part else filename

    
    def _rename_audio_files(self = None, project_id = None, old_name = None, new_name = ('project_id', str, 'old_name', str, 'new_name', str, 'return', Tuple[(List[Tuple[(str, str)]], int)])):
        '''
        오디오 파일 이름 변경

        Args:
            project_id: 프로젝트 ID
            old_name: 이전 화자 이름
            new_name: 새 화자 이름

        Returns:
            (변경된 파일 목록 [(old_path, new_path), ...], 변경된 파일 수)
        '''
        renamed_files = []
        
        try:
            paths = ProjectPaths(project_id)
            tts_dir = str(paths.audio_dir())
            if not os.path.exists(tts_dir):
                logger.debug(f'''[CharacterRename] TTS directory not found: {tts_dir}''')
                return (renamed_files, 0)
            for filename in None.listdir(tts_dir):
                if filename.startswith(f'''{old_name}_''') or filename == f'''{old_name}.mp3''':
                    old_path = os.path.join(tts_dir, filename)
                    if filename.startswith(f'''{old_name}_'''):
                        new_filename = f'''{new_name}_''' + filename[len(old_name) + 1:]
                    else:
                        new_filename = f'''{new_name}.mp3'''
                    new_path = os.path.join(tts_dir, new_filename)
                    if os.path.exists(old_path):
                        os.rename(old_path, new_path)
                        renamed_files.append((old_path, new_path))
                        logger.debug(f'''[CharacterRename] Renamed: {filename} -> {new_filename}''')
        except Exception:
            e = None
            logger.error(f'''[CharacterRename] Error renaming audio files: {e}''')
            for old_path, new_path in renamed_files:
                if os.path.exists(new_path):
                    os.rename(new_path, old_path)
                except Exception:
                    restore_err = None
                    logger.error(f'''[CharacterRename] Failed to restore {new_path}: {restore_err}''')
                    restore_err = None
                    del restore_err
                    continue
                    restore_err = None
                    del restore_err
                raise 
                e = None
                del e
                return (renamed_files, len(renamed_files))



character_rename_service = CharacterRenameService()
