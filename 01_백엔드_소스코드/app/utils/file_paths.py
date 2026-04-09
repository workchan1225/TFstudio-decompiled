# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: file_paths.pyc (Python 3.11)

'''
프로젝트별 파일 경로 관리 헬퍼

카테고리 기반 폴더 구조에서 프로젝트 기반 폴더 구조로 전환하기 위한 유틸리티 클래스입니다.

기존 구조:
    data/uploads/images/{project_id}/
    data/uploads/scripts/{project_id}_*.txt
    data/outputs/audio/{project_id}_*.mp3
    data/outputs/videos/{project_id}_*.mp4

새 구조:
    data/projects/{project_id}/images/
    data/projects/{project_id}/scripts/
    data/projects/{project_id}/audio/
    data/projects/{project_id}/videos/
    data/projects/{project_id}/subtitles/
    data/projects/{project_id}/temp/
'''
from pathlib import Path
import os
import tempfile

def resolve_data_path(data_dir = None, relative_path = None):
    """
    DB에 저장된 상대 경로를 data_dir 기준 절대 경로로 안전하게 해석.

    DB에 '/data/projects/...' (레거시) 또는 'projects/...' (정상) 형식이 혼재할 수 있음.
    Windows에서 os.path.join(base, '/data/...') 하면 절대경로로 해석되어
    잘못된 경로(C:/data/...)가 되는 문제를 방지.

    Args:
        data_dir: 데이터 디렉토리 (Path 또는 str)
        relative_path: DB에서 가져온 경로 문자열

    Returns:
        절대 경로 문자열
    """
    if not relative_path:
        return str(data_dir)
    clean = None.replace('\\', '/')
    if clean.startswith('/data/'):
        clean = clean[6:]
    elif clean.startswith('data/'):
        clean = clean[5:]
    clean = clean.lstrip('/')
    return os.path.join(str(data_dir), clean)


class ProjectPaths:
    '''프로젝트별 파일 경로 생성 및 관리 헬퍼 클래스'''
    
    def __init__(self = None, project_id = None, backend_dir = None):
        '''
        프로젝트 경로 헬퍼 초기화

        Args:
            project_id: 프로젝트 ID (UUID)
            backend_dir: 백엔드 루트 디렉토리 경로 (None이면 자동 탐지)
        '''
        self.project_id = project_id
    # WARNING: Decompyle incomplete

    data_dir = (lambda self = None: self._data_dir)()
    
    def ensure_directories(self = None, project_name = None):
        '''프로젝트 폴더 구조 생성

        images, scripts, audio, videos, subtitles, temp 폴더를 생성합니다.
        이미 존재하는 경우 무시됩니다.

        Args:
            project_name: 프로젝트 이름 (선택적, 제공 시 project-info.txt 생성)
        '''
        dirs = [
            'images',
            'scripts',
            'audio',
            'videos',
            'subtitles',
            'bgm',
            'temp']
        for dir_name in dirs:
            dir_path = self.project_base / dir_name
            dir_path.mkdir(parents = True, exist_ok = True)
            if project_name:
                import re
                safe_name = re.sub('[<>:"/\\\\|?*]', '', project_name).strip()
                if not safe_name:
                    safe_name = 'PROJECT-INFO'
                info_file = self.project_base / f'''{safe_name}.txt'''
                info_content = f'''프로젝트 이름: {project_name}\n프로젝트 ID: {self.project_id}\n\n이 폴더는 "{project_name}" 프로젝트의 모든 파일을 포함합니다.\n- images/: 업로드된 이미지 및 비디오\n- audio/: 오디오 파일 (TTS 생성 또는 업로드)\n- videos/: 최종 렌더링된 영상\n- scripts/: 스크립트 파일\n- subtitles/: 자막 파일\n- bgm/: BGM (배경 음악) 파일\n- temp/: 임시 파일\n'''
                (fd, temp_path_str) = tempfile.mkstemp(prefix = f'''{safe_name}_''', suffix = '.tmp', dir = self.project_base)
                temp_path = Path(temp_path_str)
                
                try:
                    temp_fp = os.fdopen(fd, 'w', encoding = 'utf-8')
                    temp_fp.write(info_content)
                    
                    try:
                        None(None, None)
                    with None:
                        if not None:
                            
                            try:
                                
                                try:
                                    temp_path.replace(info_file)
                                except Exception:
                                    temp_path.unlink(missing_ok = True)
                                    raise 

                                for old_txt in self.project_base.glob('*.txt'):
                                    if old_txt != info_file:
                                        old_txt.unlink()
                                        print(f'''[ProjectPaths] Removed old project info file: {old_txt}''')
                                    print(f'''[ProjectPaths] Created project info file: {info_file}''')
                                    return None
                                    return None




    
    def images_dir(self = None):
        '''이미지 폴더 경로'''
        return self.project_base / 'images'

    
    def scripts_dir(self = None):
        '''스크립트 폴더 경로'''
        return self.project_base / 'scripts'

    
    def audio_dir(self = None):
        '''오디오 폴더 경로'''
        return self.project_base / 'audio'

    
    def videos_dir(self = None):
        '''비디오 폴더 경로'''
        return self.project_base / 'videos'

    
    def subtitles_dir(self = None):
        '''자막 폴더 경로'''
        return self.project_base / 'subtitles'

    
    def bgm_dir(self = None):
        '''BGM 폴더 경로'''
        return self.project_base / 'bgm'

    
    def temp_dir(self = None):
        '''임시 파일 폴더 경로'''
        return self.project_base / 'temp'

    exports_dir = (lambda self = None: self.project_base / 'exports')()
    
    def relative_path(self = None, absolute_path = None):
        """
        절대 경로를 상대 경로로 변환

        Args:
            absolute_path: 변환할 절대 경로

        Returns:
            data 디렉토리 기준 상대 경로 문자열 (항상 forward slash 사용)
            예: 'projects/uuid/images/0.jpg'
        """
        
        try:
            rel_path = absolute_path.relative_to(self._data_dir)
            return str(rel_path).replace('\\', '/')
        except ValueError:
            rel_path = absolute_path.relative_to(self.backend_dir)
            return 
            except ValueError:
                return 


    
    def script_path(self = None, filename = None):
        '''
        스크립트 파일 경로 생성

        Args:
            filename: 파일명 (project_id_ 접두사는 자동 추가됨)

        Returns:
            절대 파일 경로
            예: /backend/data/projects/uuid/scripts/uuid_script.txt
        '''
        if filename.startswith(f'''{self.project_id}_'''):
            return self.scripts_dir() / filename
        return None.scripts_dir() / f'''{self.project_id}_{filename}'''

    
    def audio_path(self = None, filename = None):
        '''
        오디오 파일 경로 생성

        Args:
            filename: 파일명 (project_id_ 접두사는 자동 추가됨)

        Returns:
            절대 파일 경로
            예: /backend/data/projects/uuid/audio/uuid_audio.mp3
        '''
        if filename.startswith(f'''{self.project_id}_'''):
            return self.audio_dir() / filename
        return None.audio_dir() / f'''{self.project_id}_{filename}'''

    
    def video_path(self = None, filename = None):
        '''
        비디오 파일 경로 생성

        Args:
            filename: 파일명 (project_id_ 접두사는 자동 추가됨)

        Returns:
            절대 파일 경로
            예: /backend/data/projects/uuid/videos/uuid_final.mp4
        '''
        if filename.startswith(f'''{self.project_id}_'''):
            return self.videos_dir() / filename
        return None.videos_dir() / f'''{self.project_id}_{filename}'''

    
    def subtitle_path(self = None, filename = None):
        '''
        자막 파일 경로 생성

        Args:
            filename: 파일명 (project_id_ 접두사는 자동 추가됨)

        Returns:
            절대 파일 경로
            예: /backend/data/projects/uuid/subtitles/uuid_subtitle.srt
        '''
        if filename.startswith(f'''{self.project_id}_'''):
            return self.subtitles_dir() / filename
        return None.subtitles_dir() / f'''{self.project_id}_{filename}'''

    
    def image_path(self = None, filename = None):
        '''
        이미지 파일 경로 생성

        Args:
            filename: 파일명 (접두사 없음, 인덱스 기반)

        Returns:
            절대 파일 경로
            예: /backend/data/projects/uuid/images/0.jpg
        '''
        return self.images_dir() / filename

    
    def temp_path(self = None, filename = None):
        '''
        임시 파일 경로 생성

        Args:
            filename: 파일명

        Returns:
            절대 파일 경로
            예: /backend/data/projects/uuid/temp/temp.mp4
        '''
        return self.temp_dir() / filename

    
    def url_to_abs_path(self = None, url = None):
        """
        URL 또는 상대 경로를 절대 경로로 변환

        Args:
            url: 상대 URL 경로 (예: 'projects/uuid/audio/file.mp3' 또는 '/data/projects/...')

        Returns:
            절대 파일 경로 문자열
        """
        if not url:
            return ''
        url = None.replace('\\', '/')
        if url.startswith('/data/'):
            url = url[6:]
        elif url.startswith('data/'):
            url = url[5:]
        url = url.lstrip('/')
        abs_path = self._data_dir / url
        return str(abs_path)

    
    def abs_path_to_url(self = None, abs_path = None):
        """
        절대 경로를 URL (상대 경로)로 변환

        Args:
            abs_path: 절대 파일 경로

        Returns:
            상대 URL 경로 (예: '/data/projects/uuid/audio/file.mp3')
        """
        if not abs_path:
            return ''
        abs_path = None(abs_path)
        
        try:
            rel_path = abs_path.relative_to(self._data_dir)
            return '/data/' + str(rel_path).replace('\\', '/')
        except ValueError:
            return
