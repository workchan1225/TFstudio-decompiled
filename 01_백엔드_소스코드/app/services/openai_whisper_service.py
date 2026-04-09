# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: openai_whisper_service.pyc (Python 3.11)

'''
OpenAI Whisper API 서비스

저사양 PC에서도 고품질 음성 인식을 사용할 수 있도록 클라우드 기반 STT 제공
- 25MB 파일 제한 대응: 자동 청크 분할
- verbose_json 응답으로 단어별 타임스탬프 추출
- 세그먼트 분할 및 SRT 생성
'''
import logging
import os
import subprocess
import tempfile
from pathlib import Path
from typing import Optional, List, Dict, Callable, Tuple
from app.utils.ffmpeg_utils import get_ffmpeg_executable, get_ffprobe_executable
logger = logging.getLogger(__name__)

def log_debug(msg = None):
    '''디버그 로그 출력'''
    print(f'''[OpenAIWhisper] {msg}''')
    logger.info(msg)

MAX_FILE_SIZE = 26214400
CHUNK_DURATION = 300
HIGH_BITRATE_CHUNK_DURATION = 180

class OpenAIWhisperService:
    '''
    OpenAI Whisper API 서비스

    저사양 PC 사용자를 위한 클라우드 기반 음성 인식
    '''
    SUPPORTED_LANGUAGES = {
        'ko': 'ko',
        'en': 'en',
        'ja': 'ja',
        'zh': 'zh',
        'es': 'es',
        'fr': 'fr',
        'de': 'de' }
    SUPPORTED_FORMATS = [
        'flac',
        'mp3',
        'mp4',
        'mpeg',
        'mpga',
        'm4a',
        'ogg',
        'wav',
        'webm']
    
    def __init__(self = None, api_key = None):
        '''
        Args:
            api_key: OpenAI API 키 (없으면 Settings에서 로드)
        '''
        pass
    # WARNING: Decompyle incomplete

    
    def transcribe_audio(self = None, audio_path = None, language = None, progress_callback = ('ko', None)):
        '''
        오디오 파일에서 단어 단위 타임스탬프 추출

        Args:
            audio_path: 오디오 파일 경로
            language: 언어 코드 (기본값: "ko")
            progress_callback: 진행률 콜백 (progress: int, message: str)

        Returns:
            {
                \'status\': \'success\' | \'error\',
                \'words\': [{\'word\': str, \'start\': float, \'end\': float}],
                \'segments\': [{\'text\': str, \'start\': float, \'end\': float}],
                \'full_text\': str,
                \'duration\': float,
                \'message\': str
            }
        '''
        
        try:
            log_debug(f'''Transcribing: {audio_path}''')
            if not Path(audio_path).exists():
                return {
                    'status': 'error',
                    'message': f'''오디오 파일을 찾을 수 없습니다: {audio_path}''',
                    'words': [],
                    'segments': [],
                    'full_text': '' }
            language_code = None.SUPPORTED_LANGUAGES.get(language, language)
            log_debug(f'''Language: {language_code}''')
            file_size = os.path.getsize(audio_path)
            log_debug(f'''File size: {file_size / 1048576:.2f}MB''')
            if progress_callback:
                progress_callback(10, '오디오 분석 중...')
            duration = self._get_audio_duration(audio_path)
            log_debug(f'''Audio duration: {duration:.2f}s''')
            if file_size > MAX_FILE_SIZE:
                log_debug('파일이 25MB 초과, 청크 분할 처리')
                return self._transcribe_chunked(audio_path, language_code, duration, progress_callback)
            if None:
                progress_callback(30, 'OpenAI Whisper API 호출 중...')
            result = self._transcribe_single(audio_path, language_code)
            if result['status'] == 'error':
                return result
            result['duration'] = None
            if progress_callback:
                progress_callback(90, '처리 완료')
            return result
        except Exception:
            e = None
            error_msg = str(e)
            log_debug(f'''Transcription error: {error_msg}''')
            del e
            return None
            None = 
            del e


    
    def _transcribe_single(self = None, audio_path = None, language = None):
        '''단일 오디오 파일 전사'''
        
        try:
            audio_file = open(audio_path, 'rb')
            response = self.client.audio.transcriptions.create(model = 'whisper-1', file = audio_file, response_format = 'verbose_json', language = language, timestamp_granularities = [
                'word',
                'segment'])
            
            try:
                None(None, None)
            with None:
                if not None:
                    
                    try:
                        
                        try:
                            words = []
                            if hasattr(response, 'words') and response.words:
                                for w in response.words:
                                    words.append({
                                        'word': w.word,
                                        'start': w.start,
                                        'end': w.end })
                                    segments = []
                                    if hasattr(response, 'segments') and response.segments:
                                        for seg in response.segments:
                                            segments.append({
                                                'text': seg.text.strip(),
                                                'start': seg.start,
                                                'end': seg.end })
                            full_text = response.text if hasattr(response, 'text') else ''
                            log_debug(f'''Transcription complete: {len(words)} words, {len(segments)} segments''')
                            return {
                                'status': 'success',
                                'words': words,
                                'segments': segments,
                                'full_text': full_text,
                                'message': '음성 인식 완료' }
                        except Exception:
                            e = None
                            error_msg = str(e)
                            log_debug(f'''API call error: {error_msg}''')
                            if 'Invalid API Key' in error_msg or 'Incorrect API key' in error_msg:
                                error_msg = 'OpenAI API 키가 유효하지 않습니다. 설정에서 확인해주세요.'
                            elif 'insufficient_quota' in error_msg:
                                error_msg = 'OpenAI API 크레딧이 부족합니다. 결제 정보를 확인해주세요.'
                            elif 'rate_limit' in error_msg:
                                error_msg = 'API 요청 한도 초과입니다. 잠시 후 다시 시도해주세요.'
                            del e
                            return None
                            None = 
                            del e





    
    def _transcribe_chunked(self = None, audio_path = None, language = None, total_duration = (None,), progress_callback = ('audio_path', str, 'language', str, 'total_duration', float, 'progress_callback', Optional[Callable[([
        int,
        str], None)]], 'return', Dict)):
        '''25MB 초과 오디오를 청크로 분할하여 처리'''
        
        try:
            chunks = self._split_audio(audio_path, total_duration)
            log_debug(f'''분할된 청크 수: {len(chunks)}''')
            all_words = []
            all_segments = []
            all_text = []
            for chunk_path, offset in enumerate(chunks):
                if progress_callback:
                    progress = 20 + int((i / len(chunks)) * 60)
                    progress_callback(progress, f'''청크 {i + 1}/{len(chunks)} 처리 중...''')
                log_debug(f'''Processing chunk {i + 1}/{len(chunks)}, offset: {offset:.2f}s''')
                result = self._transcribe_single(chunk_path, language)
                os.unlink(chunk_path)
                
                try:
                    pass
                try:
                    pass
                if result['status'] == 'error':
                    log_debug(f'''Chunk {i + 1} failed: {result['message']}''')
                    continue

                for word in result['words']:
                    all_words.append(word)
                    for None in result['segments']:
                        all_segments.append(seg)
                        all_text.append(result['full_text'])
                        if not all_words and all_segments:
                            return {
                                'status': 'error',
                                'message': '모든 청크 처리 실패',
                                'words': [],
                                'segments': [],
                                'full_text': '' }
                        None.sort(key = (lambda x: x['start']))
                        all_segments.sort(key = (lambda x: x['start']))
                        if progress_callback:
                            progress_callback(90, '청크 병합 완료')
            return {
                'status': 'success',
                'words': all_words,
                'segments': all_segments,
                'full_text': ' '.join(all_text),
                'duration': total_duration,
                'message': f'''{len(chunks)}개 청크 처리 완료''' }
        except Exception:
            None = None
            error_msg = str(e)
            log_debug(f'''Chunked transcription error: {error_msg}''')
            del e
            return None
            None = 
            del e


    
    def _split_audio(self = None, audio_path = None, total_duration = None):
        '''오디오를 청크로 분할'''
        file_size = os.path.getsize(audio_path)
        bitrate = file_size / total_duration if total_duration > 0 else 0
        if bitrate > 80000:
            chunk_duration = HIGH_BITRATE_CHUNK_DURATION
        else:
            chunk_duration = CHUNK_DURATION
        log_debug(f'''Using chunk duration: {chunk_duration}s (bitrate: {bitrate / 1000:.1f} kB/s)''')
        chunks = []
        current_time = 0
        chunk_index = 0
    # WARNING: Decompyle incomplete

    
    def _extract_chunk(self, audio_path = None, start = None, end = None, index = ('audio_path', str, 'start', float, 'end', float, 'index', int, 'return', Optional[str])):
        '''FFmpeg로 오디오 청크 추출'''
        pass
    # WARNING: Decompyle incomplete

    
    def _get_audio_duration(self = None, audio_path = None):
        '''오디오 길이 확인 (FFprobe 사용)'''
        pass
    # WARNING: Decompyle incomplete

    
    def generate_srt(self, audio_path = None, output_path = None, language = None, max_chars_per_segment = ('ko', 25, None), progress_callback = ('audio_path', str, 'output_path', str, 'language', str, 'max_chars_per_segment', int, 'progress_callback', Optional[Callable[([
        int,
        str], None)]], 'return', Dict)):
        """
        오디오에서 SRT 자막 파일 생성

        Args:
            audio_path: 오디오 파일 경로
            output_path: 출력 SRT 파일 경로
            language: 언어 코드
            max_chars_per_segment: 세그먼트당 최대 글자수
            progress_callback: 진행률 콜백

        Returns:
            {
                'status': 'success' | 'error',
                'srt_path': str,
                'segments': list,
                'message': str
            }
        """
        
        try:
            result = self.transcribe_audio(audio_path, language, progress_callback)
            if result['status'] == 'error':
                return result
            segments = None.get('segments', [])
            if segments and result.get('words'):
                segments = self._words_to_segments(result['words'], max_chars_per_segment)
            if not segments:
                return {
                    'status': 'error',
                    'message': '세그먼트 생성 실패: 인식된 내용이 없습니다',
                    'segments': [] }
            None._write_srt_file(segments, output_path)
            log_debug(f'''SRT 생성 완료: {len(segments)}개 세그먼트''')
            return {
                'status': 'success',
                'srt_path': output_path,
                'segments': segments,
                'message': f'''{len(segments)}개 자막 세그먼트 생성 완료''' }
        except Exception:
            e = None
            error_msg = str(e)
            log_debug(f'''SRT generation error: {error_msg}''')
            del e
            return None
            None = 
            del e


    
    def _words_to_segments(self = None, words = None, max_chars = None):
        '''
        단어 목록을 세그먼트로 그룹화 (Whisper API segments fallback)

        Note: 이 함수는 Whisper API가 segments를 제공하지 않을 때만 호출됨
        자동 분할 없이 자연스러운 타이밍으로만 그룹화
        '''
        if not words:
            return []
        segments = None
        current_segment = {
            'text': '',
            'start': words[0]['start'],
            'end': words[0]['end'] }
        silence_threshold = 0.5
        for i, word in enumerate(words):
            word_text = word['word'].strip()
            if i > 0 and word['start'] - words[i - 1]['end'] > silence_threshold:
                if current_segment['text']:
                    segments.append(current_segment)
                current_segment = {
                    'text': word_text,
                    'start': word['start'],
                    'end': word['end'] }
                continue
            word['end'] = None
            if current_segment['text']:
                segments.append(current_segment)
        return segments

    
    def _split_long_segments(self = None, segments = None, max_chars = None):
        '''
        긴 세그먼트를 자연스럽게 분할

        분할 우선순위:
        1. 문장 경계 (마침표, 느낌표, 물음표)
        2. 단어 경계 (공백)
        3. 문자 경계 (최후 수단)
        '''
        import re
        result = []
        for seg in segments:
            text = seg['text'].strip()
            if len(text) <= max_chars:
                result.append(seg)
                continue
            duration = seg['end'] - seg['start']
            char_duration = duration / len(text) if len(text) > 0 else 0
            sentence_pattern = '([^.!?]*[.!?]+)'
            sentences = re.findall(sentence_pattern, text)
            if not sentences:
                sentences = [
                    text]
            else:
                remaining = re.sub(sentence_pattern, '', text).strip()
                if remaining:
                    sentences.append(remaining)
            current_start = seg['start']
            current_text = ''
            char_count = 0
            for sentence in sentences:
                sentence = sentence.strip()
                if not sentence:
                    continue
                if len(current_text) + len(sentence) <= max_chars:
                    current_text += ' ' if current_text else '' + sentence
                    char_count += len(sentence) + 1 if current_text else 0
                    continue
                if current_text:
                    segment_duration = char_count * char_duration
                    result.append({
                        'text': current_text.strip(),
                        'start': current_start,
                        'end': current_start + segment_duration })
                    current_start += segment_duration
                    current_text = ''
                    char_count = 0
                if len(sentence) > max_chars:
                    words = sentence.split()
                    temp_text = ''
                    temp_chars = 0
                    for word in words:
                        word_with_space = ' ' if temp_text else '' + word
                        if len(temp_text) + len(word_with_space) <= max_chars:
                            temp_text += word_with_space
                            temp_chars += len(word_with_space)
                            continue
                        if temp_text:
                            segment_duration = temp_chars * char_duration
                            result.append({
                                'text': temp_text.strip(),
                                'start': current_start,
                                'end': current_start + segment_duration })
                            current_start += segment_duration
                        temp_text = word
                        temp_chars = len(word)
                        if temp_text:
                            current_text = temp_text
                            char_count = temp_chars
                    continue
                current_text = sentence
                char_count = len(sentence)
                if current_text.strip():
                    result.append({
                        'text': current_text.strip(),
                        'start': current_start,
                        'end': seg['end'] })
            return result

    
    def _write_srt_file(self = None, segments = None, output_path = None):
        '''SRT 파일 작성'''
        output_dir = os.path.dirname(output_path)
        if output_dir:
            os.makedirs(output_dir, exist_ok = True)
        f = open(output_path, 'w', encoding = 'utf-8')
        for i, seg in enumerate(segments, 1):
            start_time = self._format_srt_time(seg['start'])
            end_time = self._format_srt_time(seg['end'])
            text = seg['text'].strip()
            f.write(f'''{i}\n''')
            f.write(f'''{start_time} --> {end_time}\n''')
            f.write(f'''{text}\n\n''')
            None(None, None)
            return None
            with None:
                if not None:
                    pass

    
    def _format_srt_time(self = None, seconds = None):
        '''초를 SRT 시간 형식으로 변환 (HH:MM:SS,mmm)'''
        hours = int(seconds // 3600)
        minutes = int((seconds % 3600) // 60)
        secs = int(seconds % 60)
        millis = int((seconds % 1) * 1000)
        return f'''{hours:02d}:{minutes:02d}:{secs:02d},{millis:03d}'''



def generate_srt_with_openai_whisper(audio_path, output_path = None, language = None, max_chars = None, api_key = ('ko', 25, None, None), progress_callback = ('audio_path', str, 'output_path', str, 'language', str, 'max_chars', int, 'api_key', str, 'progress_callback', Optional[Callable[([
    int,
    str], None)]], 'return', Dict)):
    """
    OpenAI Whisper API를 사용하여 SRT 자막 파일 생성

    저사양 PC에서도 사용 가능한 클라우드 기반 음성 인식

    Args:
        audio_path: 오디오 파일 경로
        output_path: 출력 SRT 파일 경로
        language: 언어 코드 (기본: 'ko')
        max_chars: 세그먼트당 최대 글자수
        api_key: OpenAI API 키 (없으면 Settings에서 로드)
        progress_callback: 진행률 콜백

    Returns:
        {
            'status': 'success' | 'error',
            'srt_path': str,
            'segments': list,
            'message': str
        }
    """
    
    try:
        service = OpenAIWhisperService(api_key = api_key)
        return service.generate_srt(audio_path = audio_path, output_path = output_path, language = language, max_chars_per_segment = max_chars, progress_callback = progress_callback)
    except Exception:
        e = None
        del e
        return None
        None = 
        del e
