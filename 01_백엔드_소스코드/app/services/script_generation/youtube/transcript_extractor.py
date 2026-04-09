# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: transcript_extractor.pyc (Python 3.11)

'''
YouTube Transcript Extractor

YouTube 영상에서 자막을 추출하는 서비스
'''
import re
import logging
from typing import Optional, List, Dict, Any
from types import TranscriptSegment, VideoInfo, ExtractTranscriptResult
logger = logging.getLogger(__name__)

class TranscriptExtractor:
    '''
    YouTube 자막 추출기

    youtube-transcript-api 라이브러리를 사용하여
    YouTube 영상의 자막을 추출합니다.
    '''
    URL_PATTERNS = [
        '(?:v=|/)([0-9A-Za-z_-]{11}).*',
        '(?:embed/)([0-9A-Za-z_-]{11})',
        '(?:youtu\\.be/)([0-9A-Za-z_-]{11})',
        '(?:shorts/)([0-9A-Za-z_-]{11})']
    PREFERRED_LANGUAGES = [
        'ko',
        'en',
        'ja',
        'zh-Hans',
        'zh-Hant',
        'es',
        'pt',
        'de',
        'fr']
    
    def extract(self = None, youtube_url = None):
        '''
        YouTube URL에서 자막 추출

        Args:
            youtube_url: YouTube 영상 URL

        Returns:
            ExtractTranscriptResult: 자막 추출 결과
        '''
        
        try:
            YouTubeTranscriptApi = YouTubeTranscriptApi
            import youtube_transcript_api
            TranscriptsDisabled = TranscriptsDisabled
            NoTranscriptFound = NoTranscriptFound
            VideoUnavailable = VideoUnavailable
            import youtube_transcript_api._errors
        except ImportError:
            logger.error('youtube-transcript-api not installed')
            return 

        
        try:
            if not video_id:
                return ExtractTranscriptResult(success = False, error = '유효하지 않은 YouTube URL입니다.')
            self._extract_video_id(youtube_url).info(f'''Extracting transcript for video: {video_id}''')
            YouTubeTranscriptApi() = None
            transcript_list = api.list(video_id)
            transcript = self._select_best_transcript(transcript_list)
            transcript_data = transcript.fetch()
            segments = transcript_data()
            full_text = (lambda .0: [ s.text for s in .0 ])(segments())
            duration = 0
            if segments:
                last_segment = segments[-1]
                duration = last_segment.start + last_segment.duration
            video_info = VideoInfo(video_id = video_id, title = '', channel_name = '', duration = duration)
            logger.info(f'''Successfully extracted {len(segments)} segments, {len(full_text)} chars''')
            return ExtractTranscriptResult(success = True, transcript = segments, full_text = full_text, video_info = video_info, language = transcript.language_code)
        except ImportError:
            e = None
            logger.error(f'''Import error: {e}''')
            del e
            return None
            None = 
            del e
            except Exception:
                e = None
                error_type = type(e).__name__
                if 'TranscriptsDisabled' in error_type:
                    del e
                    return None
                if None in error_type:
                    del e
                    return None
                if None in error_type:
                    del e
                    return None
                if None in error_type:
                    del e
                    return None
                None.error(f'''Unexpected error extracting transcript: {e}''')
                del e
                return None
                None = 
                del e


    
    def _extract_video_id(self = None, url = None):
        '''URL에서 Video ID 추출'''
        for pattern in self.URL_PATTERNS:
            match = re.search(pattern, url)
            if match:
                
                return None, match.group(1)
            return None

    
    def _select_best_transcript(self = None, transcript_list = None):
        '''
        최적의 자막 선택

        우선순위:
        1. 수동 생성 자막 (선호 언어 순)
        2. 자동 생성 자막 (선호 언어 순)
        3. 아무 자막이나
        '''
        
        try:
            return transcript_list.find_manually_created_transcript(self.PREFERRED_LANGUAGES)
        except Exception:
            pass

        
        try:
            return transcript_list.find_generated_transcript(self.PREFERRED_LANGUAGES)
        except Exception:
            pass

        
        try:
            for transcript in transcript_list:
                if not transcript.is_generated:
                    
                    return None, transcript
        except Exception:
            pass

        for None in transcript_list:
            return None, transcript
            NoTranscriptFound
            raise NoTranscriptFound(video_id = '', requested_language_codes = self.PREFERRED_LANGUAGES, transcript_data = { })

    
    def get_video_info_from_api(self = None, video_id = None, api_key = None):
        '''
        YouTube Data API로 영상 정보 조회 (선택적)

        Args:
            video_id: YouTube 비디오 ID
            api_key: YouTube Data API 키 (없으면 환경변수에서)

        Returns:
            VideoInfo 또는 None
        '''
        import os
        if not api_key:
            pass
        api_key = os.environ.get('YOUTUBE_API_KEY')
        if not api_key:
            logger.warning('YouTube API key not available, skipping video info fetch')
            return None
        
        try:
            build = build
            import googleapiclient.discovery
            youtube = build('youtube', 'v3', developerKey = api_key)
            request = youtube.videos().list(part = 'snippet,contentDetails', id = video_id)
            response = request.execute()
            if not response.get('items'):
                return None
            item = None['items'][0]
            snippet = item.get('snippet', { })
            content_details = item.get('contentDetails', { })
            duration = self._parse_iso_duration(content_details.get('duration', ''))
            return VideoInfo(video_id = video_id, title = snippet.get('title', ''), channel_name = snippet.get('channelTitle', ''), duration = duration)
        except Exception:
            e = None
            logger.error(f'''Failed to fetch video info: {e}''')
            e = None
            del e
            return None
            e = None
            del e


    
    def _parse_iso_duration(self = None, duration = None):
