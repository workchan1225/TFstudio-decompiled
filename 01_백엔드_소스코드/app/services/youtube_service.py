# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: youtube_service.pyc (Python 3.11)

'''
YouTube Data API v3 서비스
OAuth 2.0 인증 및 영상 업로드 기능
'''
import os
import json
import logging
import time
from datetime import datetime, timezone
from typing import Optional, Dict, Any, Callable
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import Flow
from google.auth.transport.requests import Request
from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload
from googleapiclient.errors import HttpError
logger = logging.getLogger(__name__)

class UploadCancelledError(Exception):
    '''Raised when upload is cancelled by user request.'''
    pass


class YouTubeService:
    '''YouTube Data API v3 통합 서비스'''
    SCOPES = [
        'https://www.googleapis.com/auth/youtube.upload',
        'https://www.googleapis.com/auth/youtube.readonly']
    API_SERVICE_NAME = 'youtube'
    API_VERSION = 'v3'
    THUMBNAIL_UPLOAD_RETRY_DELAYS_SECONDS = (2, 5, 10)
    REDIRECT_URI = 'urn:ietf:wg:oauth:2.0:oob'
    
    def __init__(self = None, credentials_dict = None):
        '''
        YouTube 서비스 초기화

        Args:
            credentials_dict: OAuth credentials 딕셔너리
                {token, refresh_token, token_uri, client_id, client_secret, scopes}
        '''
        self.credentials = None
        self.youtube = None
    # WARNING: Decompyle incomplete

    
    def _build_service(self):
        '''YouTube API 서비스 객체 생성'''
        logger.info(f'''[YouTube] 서비스 빌드 시작 - credentials: {self.credentials is not None}, valid: {self.credentials.valid if self.credentials else 'N/A'}''')
        if self.credentials and self.credentials.valid:
            self.youtube = build(self.API_SERVICE_NAME, self.API_VERSION, credentials = self.credentials)
            logger.info('[YouTube] 서비스 빌드 완료 (valid credentials)')
            return None
        if None.credentials and self.credentials.expired and self.credentials.refresh_token:
            logger.info('[YouTube] 토큰 만료 - refresh 시도')
            self.credentials.refresh(Request())
            self.youtube = build(self.API_SERVICE_NAME, self.API_VERSION, credentials = self.credentials)
            logger.info('[YouTube] 서비스 빌드 완료 (refreshed credentials)')
            return None
        None.warning(f'''[YouTube] 서비스 빌드 실패 - credentials valid: {self.credentials.valid if self.credentials else 'None'}, expired: {self.credentials.expired if self.credentials else 'N/A'}, has_refresh: {bool(self.credentials.refresh_token) if self.credentials else 'N/A'}''')

    generate_auth_url = (lambda client_secrets = None: flow = Flow.from_client_config(client_secrets, scopes = YouTubeService.SCOPES, redirect_uri = YouTubeService.REDIRECT_URI)(auth_url, _) = flow.authorization_url(access_type = 'offline', prompt = 'consent')auth_url)()
    exchange_code_for_credentials = (lambda code = None, client_secrets = None: flow = Flow.from_client_config(client_secrets, scopes = YouTubeService.SCOPES, redirect_uri = YouTubeService.REDIRECT_URI)flow.fetch_token(code = code)credentials = flow.credentials{
'token': credentials.token,
'refresh_token': credentials.refresh_token,
'token_uri': credentials.token_uri,
'client_id': credentials.client_id,
'client_secret': credentials.client_secret,
'scopes': list(credentials.scopes) if credentials.scopes else [] })()
    
    def upload_video(self, file_path, metadata = None, scheduled_time = None, ai_disclosure = None, should_cancel = (None, 'NOT_APPLICABLE', None, None), progress_callback = ('file_path', str, 'metadata', Dict[(str, Any)], 'scheduled_time', Optional[str], 'ai_disclosure', str, 'should_cancel', Optional[Callable[([], bool)]], 'progress_callback', Optional[Callable[([
        float], None)]], 'return', Dict[(str, Any)])):
        '''
        YouTube에 영상 업로드

        Args:
            file_path: 업로드할 영상 파일 경로
            metadata: 영상 메타데이터
                {
                    title: 제목,
                    description: 설명,
                    tags: [태그1, 태그2, ...],
                    categoryId: 카테고리 ID (기본 "22" = People & Blogs),
                    privacyStatus: \'public\' | \'private\' | \'unlisted\'
                }
            scheduled_time: 예약 시간 (ISO 8601 UTC 형식)
                예: "2025-12-12T08:00:00.000Z"
            ai_disclosure: AI 콘텐츠 공개 (\'DISCLOSED\' | \'NOT_APPLICABLE\')
            should_cancel: 취소 요청 여부 콜백 (True 반환 시 업로드 중단)
            progress_callback: 업로드 진행률 콜백 (0.0 ~ 1.0)

        Returns:
            업로드 결과
            {
                videoId: YouTube 영상 ID,
                videoUrl: YouTube 영상 URL,
                uploadDate: 업로드 시간 (ISO 8601),
                scheduledTime: 예약 시간 (있는 경우)
            }

        Raises:
            FileNotFoundError: 영상 파일이 없는 경우
            HttpError: YouTube API 에러 (할당량 초과, 인증 실패 등)
        '''
        if not os.path.exists(file_path):
            raise FileNotFoundError(f'''영상 파일을 찾을 수 없습니다: {file_path}''')
        if not self.youtube:
            self._build_service()
        if not self.youtube:
            raise RuntimeError('YouTube 서비스를 초기화할 수 없습니다. 인증이 필요합니다.')
        body = {
            'snippet': {
                'title': metadata.get('title', 'Untitled Video'),
                'description': metadata.get('description', ''),
                'tags': metadata.get('tags', []),
                'categoryId': metadata.get('categoryId', '22') },
            'status': {
                'privacyStatus': metadata.get('privacyStatus', 'private'),
                'selfDeclaredMadeForKids': metadata.get('madeForKids', False),
                'artificial_intelligence_details': {
                    'disclosure': ai_disclosure } } }
        if scheduled_time:
            body['status']['publishAt'] = scheduled_time
            if body['status']['privacyStatus'] == 'public':
                body['status']['privacyStatus'] = 'private'
        media_file = MediaFileUpload(file_path, chunksize = 8388608, resumable = True, mimetype = 'video/*')
    # WARNING: Decompyle incomplete

    
    def delete_video(self = None, video_id = None):
        '''YouTube 영상 삭제'''
        if not self.youtube:
            self._build_service()
        if not self.youtube:
            raise RuntimeError('YouTube 서비스를 초기화할 수 없습니다. 인증이 필요합니다.')
        request = self.youtube.videos().delete(id = video_id)
        request.execute()

    
    def get_video_status(self = None, video_id = None):
        """
        업로드된 영상 상태 확인

        Args:
            video_id: YouTube 영상 ID

        Returns:
            영상 상태 정보
            {
                videoId: ID,
                title: 제목,
                uploadStatus: 'uploaded' | 'processed' | 'failed',
                privacyStatus: 'public' | 'private' | 'unlisted',
                publishedAt: 공개 시간 (있는 경우)
            }
        """
        if not self.youtube:
            self._build_service()
        
        try:
            request = self.youtube.videos().list(part = 'snippet,status', id = video_id)
            response = request.execute()
            if not response.get('items'):
                raise Exception(f'''영상을 찾을 수 없습니다: {video_id}''')
            video = response['items'][0]
            return {
                'videoId': video_id,
                'title': video['snippet']['title'],
                'uploadStatus': video['status']['uploadStatus'],
                'privacyStatus': video['status']['privacyStatus'],
                'publishedAt': video['snippet'].get('publishedAt') }
        except HttpError:
            e = None
            error_message = str(e)
            raise Exception(f'''영상 상태 조회 실패: {error_message}''')
            e = None
            del e


    
    def revoke_credentials(self):
        '''
        OAuth credentials 취소

        Google 계정 연동을 해제합니다.
        '''
        if self.credentials or self.credentials.token:
            
            try:
                import requests
                revoke_url = 'https://oauth2.googleapis.com/revoke'
                requests.post(revoke_url, params = {
                    'token': self.credentials.token }, headers = {
                    'content-type': 'application/x-www-form-urlencoded' }, timeout = 30)
                self.credentials = None
                self.youtube = None
                return None
            except Exception:
                e = None
                self.credentials = None
                self.youtube = None
                raise Exception(f'''인증 취소 실패: {str(e)}''')
                e = None
                del e
                return None
                return None


    
    def upload_thumbnail(self = None, video_id = None, thumbnail_path = None):
        '''
        영상에 커스텀 썸네일 업로드

        Args:
            video_id: YouTube 영상 ID
            thumbnail_path: 썸네일 이미지 파일 경로 (JPG, PNG)

        Returns:
            업로드 결과
            {
                success: True/False,
                message: 결과 메시지
            }

        Raises:
            FileNotFoundError: 썸네일 파일이 없는 경우
            Exception: 썸네일 업로드 실패

        Note:
            - 이미지 요구사항: 1280x720 픽셀 (16:9 비율 권장)
            - 파일 크기: 2MB 이하
            - 형식: JPG, PNG, GIF, BMP
            - YouTube Shorts는 커스텀 썸네일 업로드 불가
        '''
        if not os.path.exists(thumbnail_path):
            raise FileNotFoundError(f'''썸네일 파일을 찾을 수 없습니다: {thumbnail_path}''')
        if not self.youtube:
            self._build_service()
        if not self.youtube:
            raise RuntimeError('YouTube 서비스를 초기화할 수 없습니다. 인증이 필요합니다.')
        for attempt in range(len(self.THUMBNAIL_UPLOAD_RETRY_DELAYS_SECONDS) + 1):
            request = self.youtube.thumbnails().set(videoId = video_id, media_body = MediaFileUpload(thumbnail_path))
            response = request.execute()
            
            return None, {
                'success': True,
                'message': '썸네일이 업로드되었습니다.',
                'thumbnailUrl': response.get('items', [
                    { }])[0].get('default', { }).get('url', '') }
            except HttpError:
                (error_status, error_reason, error_message) = self._parse_http_error(e)
                if attempt < len(self.THUMBNAIL_UPLOAD_RETRY_DELAYS_SECONDS):
                    should_retry = self._should_retry_thumbnail_upload(error_status, error_reason, error_message)
                    if should_retry:
                        delay = self.THUMBNAIL_UPLOAD_RETRY_DELAYS_SECONDS[attempt]
                        logger.warning(f'''[YouTube] 썸네일 업로드 재시도 예정: attempt={attempt + 1}, status={error_status}, reason={error_reason}, delay={delay}s, message={error_message}''')
                        time.sleep(delay)
                        e = None
                        del e
                        continue
                raise Exception(f'''썸네일 업로드 실패: {error_message}''')
                e = None
                del e
            return None

    _parse_http_error = (lambda error = None: status = getattr(getattr(error, 'resp', None), 'status', None)try:
error_content = json.loads(error.content.decode('utf-8'))except Exception:
error_content = { }error_reason = str(error_content.get('error', { }).get('errors', [
{ }])[0].get('reason', '')).strip()error_message = str(error_content.get('error', { }).get('message', str(error))).strip()(status, error_reason, error_message))()
    _should_retry_thumbnail_upload = (lambda status = None, reason = None, message = staticmethod: pass# WARNING: Decompyle incomplete
)()
    
    def get_credentials_dict(self = None):
        '''
        현재 credentials를 딕셔너리로 반환 (DB 저장용)

        Returns:
            Credentials 딕셔너리 또는 None
        '''
        if not self.credentials:
            return None
        return {
            'token': None.credentials.token,
            'refresh_token': self.credentials.refresh_token,
            'token_uri': self.credentials.token_uri,
            'client_id': self.credentials.client_id,
            'client_secret': self.credentials.client_secret,
            'scopes': list(self.credentials.scopes) if self.credentials.scopes else [] }

    
    def get_channel_info(self = None):
        '''
        현재 인증된 사용자의 YouTube 채널 정보 조회

        Returns:
            채널 정보 딕셔너리
            {
                channelId: 채널 ID,
                channelTitle: 채널 이름,
                channelUrl: 채널 URL,
                thumbnailUrl: 프로필 이미지 URL
            }

        Note:
            youtube.upload 스코프로도 mine=True 채널 정보 조회 가능
        '''
        if not self.youtube:
            self._build_service()
        if not self.youtube:
            return None
        
        try:
            request = self.youtube.channels().list(part = 'snippet', mine = True)
            response = request.execute()
            if not response.get('items'):
                return None
            channel = None['items'][0]
            snippet = channel.get('snippet', { })
            thumbnails = snippet.get('thumbnails', { })
            return {
                'channelId': channel.get('id'),
                'channelTitle': snippet.get('title', ''),
                'channelUrl': f'''https://www.youtube.com/channel/{channel.get('id')}''',
                'thumbnailUrl': thumbnails.get('default', { }).get('url', '') }
        except HttpError:
            e = None
            logger.warning(f'''[YouTube] get_channel_info HttpError: {e}''')
            e = None
            del e
            return None
            e = None
            del e
            except Exception:
                e = None
                logger.warning(f'''[YouTube] get_channel_info Exception: {e}''')
                e = None
                del e
                return None
                e = None
                del e


    
    def verify_token(self = None):
        """
        토큰 유효성을 실제 API 호출로 검증

        Returns:
            {
                'valid': bool - 토큰이 유효한지,
                'error': str | None - 오류 메시지 (invalid_grant 등),
                'needs_reauth': bool - 재인증이 필요한지
            }
        """
        if not self.credentials:
            return {
                'valid': False,
                'error': 'No credentials',
                'needs_reauth': True }
        if None.credentials.expired and self.credentials.refresh_token:
            
            try:
                logger.info('[YouTube] verify_token: 토큰 만료됨, refresh 시도')
                self.credentials.refresh(Request())
                self._build_service()
                logger.info('[YouTube] verify_token: refresh 성공')
            except Exception:
                e = None
                error_str = str(e)
                logger.warning(f'''[YouTube] verify_token: refresh 실패 - {error_str}''')
                if 'invalid_grant' in error_str:
                    del e
                    return None
                del e
                return None
                None = 
                del e

            if not self.youtube:
                self._build_service()
        if not self.youtube:
            return {
                'valid': False,
                'error': 'Failed to build service',
                'needs_reauth': True }
        
        try:
            request = self.youtube.channels().list(part = 'id', mine = True)
            response = request.execute()
            if response.get('items'):
                return {
                    'valid': True,
                    'error': None,
                    'needs_reauth': False }
            return {
                'valid': None,
                'error': 'No channel found',
                'needs_reauth': False }
        except HttpError:
            e = None
            error_str = str(e)
            logger.warning(f'''[YouTube] verify_token HttpError: {error_str}''')
            if e.resp.status in (401, 403):
                del e
                return None
            del e
            return None
            None = 
            del e
            except Exception:
                e = None
                error_str = str(e)
                logger.warning(f'''[YouTube] verify_token Exception: {error_str}''')
                if 'invalid_grant' in error_str:
                    del e
                    return None
                del e
                return None
                None = 
                del e
