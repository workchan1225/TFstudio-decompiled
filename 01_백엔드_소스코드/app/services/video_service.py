# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: video_service.pyc (Python 3.11)

'''
영상 생성 서비스
TTS, 이미지, 자막을 결합하여 완성된 영상 생성
'''
import os
import logging
from pathlib import Path
from typing import Optional, Dict, List
import uuid
from datetime import datetime
from app.utils.ffmpeg_wrapper import FFmpegWrapper
from app.services.google_service import GoogleService
from app.utils.file_paths import ProjectPaths
logger = logging.getLogger(__name__)

class VideoService:
    '''영상 생성 및 처리 서비스'''
    
    def __init__(self):
        self.ffmpeg = FFmpegWrapper()
        self.google_service = None

    
    def _get_google_service(self = None, api_key = None):
        '''Google 서비스 인스턴스 가져오기'''
        if not self.google_service:
            self.google_service = GoogleService(api_key = api_key)
        return self.google_service

    
    def generate_video(self, project_id, script = None, image_urls = None, settings = None, api_key = (None,), output_dir = ('project_id', str, 'script', str, 'image_urls', List[str], 'settings', Dict, 'api_key', str, 'output_dir', str, 'return', Dict)):
        '''
        프로젝트로부터 완성된 영상 생성

        Args:
            project_id: 프로젝트 ID
            script: 대본 텍스트
            image_urls: 이미지 URL 리스트
            settings: 영상 설정 (해상도, TTS 음성, 자막 등)
            api_key: Google API 키 (TTS 사용)
            output_dir: 출력 디렉토리 (deprecated, ProjectPaths 사용)

        Returns:
            결과 딕셔너리 (status, video_url, message)
        '''
        
        try:
            logger.info(f'''영상 생성 시작: 프로젝트 {project_id}''')
            paths = ProjectPaths(project_id)
            paths.ensure_directories()
            project_output_dir = str(paths.videos_dir())
            temp_dir = str(paths.temp_dir())
            logger.info('1단계: TTS 음성 생성 중...')
            audio_path = self._generate_audio(script, api_key, settings.get('tts_voice', 'ko-KR-Standard-A'), temp_dir)
            logger.info('2단계: 이미지 다운로드 중...')
            image_paths = self._download_images(image_urls, temp_dir)
            if not image_paths:
                raise Exception('사용 가능한 이미지가 없습니다')
            subtitle_path = None
            if settings.get('add_subtitles', False):
                logger.info('3단계: 자막 생성 중...')
                subtitle_path = self._generate_subtitles(script, temp_dir)
            logger.info('4단계: 영상 합성 중...')
            resolution = settings.get('resolution', '1920x1080')
            fps = settings.get('fps', 30)
            timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
            output_filename = f'''video_{project_id}_{timestamp}.mp4'''
            output_path = os.path.join(project_output_dir, output_filename)
            final_video_path = self.ffmpeg.create_video_with_audio_and_subtitle(image_paths = image_paths, audio_path = audio_path, subtitle_path = subtitle_path, output_path = output_path, duration_per_image = settings.get('duration_per_image', 3), fps = fps, resolution = resolution)
            logger.info(f'''영상 생성 완료: {final_video_path}''')
            get_data_path = get_data_path
            import app.config.paths
            data_dir = get_data_path()
            
            try:
                relative_path = os.path.relpath(final_video_path, start = str(data_dir))
                video_url = f'''/data/{relative_path.replace(os.sep, '/')}'''
                
                try:
                    pass
                except ValueError:
                    relative_path = os.path.basename(final_video_path)
                    video_url = f'''/data/{relative_path}'''
                    
                    try:
                        pass
                    try:
                        return {
                            'status': 'success',
                            'video_url': video_url,
                            'video_path': final_video_path,
                            'message': '영상이 성공적으로 생성되었습니다' }
                    except Exception:
                        e = None
                        logger.error(f'''영상 생성 오류: {str(e)}''', exc_info = True)
                        del e
                        return None
                        None = 
                        del e





    
    def _generate_audio(self, text = None, api_key = None, voice_name = None, output_dir = ('text', str, 'api_key', str, 'voice_name', str, 'output_dir', str, 'return', str)):
        '''
        TTS로 음성 파일 생성

        Args:
            text: 변환할 텍스트
            api_key: Google API 키
            voice_name: TTS 음성 이름
            output_dir: 출력 디렉토리

        Returns:
            생성된 오디오 파일 경로
        '''
        texttospeech = texttospeech
        import google.cloud
        configure_legacy_genai = configure_legacy_genai
        import app.utils.google_sdk
        genai = configure_legacy_genai(api_key)
        
        try:
            gTTS = gTTS
            import gtts
            import io
            tts = gTTS(text = text, lang = 'ko')
            output_path = os.path.join(output_dir, f'''audio_{uuid.uuid4().hex[:8]}.mp3''')
            tts.save(output_path)
            logger.info(f'''TTS 음성 생성 완료: {output_path}''')
            return output_path
        except ImportError:
            logger.warning('gTTS 라이브러리가 설치되지 않았습니다. 더미 오디오 파일을 사용합니다.')
            output_path = os.path.join(output_dir, f'''audio_{uuid.uuid4().hex[:8]}.mp3''')
            self.ffmpeg.run_command([
                '-f',
                'lavfi',
                '-i',
                'anullsrc=r=44100:cl=stereo',
                '-t',
                '5',
                '-y',
                output_path])
            return 


    
    def _download_images(self = None, image_urls = None, output_dir = None):
        '''
        이미지 URL들을 다운로드

        Args:
            image_urls: 이미지 URL 리스트
            output_dir: 출력 디렉토리

        Returns:
            다운로드된 이미지 파일 경로 리스트
        '''
        import requests
        import base64
        Image = Image
        import PIL
        BytesIO = BytesIO
        import io
        downloaded_paths = []
        for idx, url in enumerate(image_urls):
            if url.startswith('data:image'):
                (header, encoded) = url.split(',', 1)
                image_data = base64.b64decode(encoded)
                image = Image.open(BytesIO(image_data))
                output_path = os.path.join(output_dir, f'''image_{idx:03d}.png''')
                image.save(output_path)
                downloaded_paths.append(output_path)
            elif url.startswith('http'):
                response = requests.get(url, timeout = 30)
                response.raise_for_status()
                image = Image.open(BytesIO(response.content))
                output_path = os.path.join(output_dir, f'''image_{idx:03d}.png''')
                image.save(output_path)
                downloaded_paths.append(output_path)
            elif os.path.exists(url):
                downloaded_paths.append(url)
            else:
                logger.warning(f'''이미지 파일을 찾을 수 없음: {url}''')
            except Exception:
                e = None
                logger.error(f'''이미지 다운로드 실패 ({url}): {e}''')
                e = None
                del e
                continue
                e = None
                del e
            logger.info(f'''{len(downloaded_paths)}개 이미지 다운로드 완료''')
            return downloaded_paths

    
    def _generate_subtitles(self = None, text = None, output_dir = None):
        '''
        간단한 SRT 자막 파일 생성

        Args:
            text: 자막 텍스트
            output_dir: 출력 디렉토리

        Returns:
            생성된 자막 파일 경로
        '''
        output_path = os.path.join(output_dir, f'''subtitle_{uuid.uuid4().hex[:8]}.srt''')
        sentences = text.split('.')
        srt_content = []
        current_time = 0
        for idx, sentence in enumerate(sentences, 1):
            sentence = sentence.strip()
            if not sentence:
                continue
            start_time = self._format_srt_time(current_time)
            end_time = self._format_srt_time(current_time + 3)
            srt_content.append(f'''{idx}\n''')
            srt_content.append(f'''{start_time} --> {end_time}\n''')
            srt_content.append(f'''{sentence}.\n\n''')
            current_time += 3
            f = open(output_path, 'w', encoding = 'utf-8')
            f.writelines(srt_content)
            None(None, None)
        with None:
            if not None:
                pass
        logger.info(f'''자막 파일 생성 완료: {output_path}''')
        return output_path

    
    def _format_srt_time(self = None, seconds = None):
        '''SRT 시간 형식으로 변환 (HH:MM:SS,mmm)'''
        hours = int(seconds // 3600)
        minutes = int((seconds % 3600) // 60)
        secs = int(seconds % 60)
        millisecs = int((seconds % 1) * 1000)
        return f'''{hours:02d}:{minutes:02d}:{secs:02d},{millisecs:03d}'''
