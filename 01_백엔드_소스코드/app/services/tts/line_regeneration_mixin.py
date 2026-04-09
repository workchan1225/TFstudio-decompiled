# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: line_regeneration_mixin.pyc (Python 3.11)

'''
TTS 줄별 재생성 공통 Mixin

모든 TTS 엔진에서 공유하는 줄별 재생성 및 재병합 로직을 제공합니다.
'''
import os
import logging
from pathlib import Path
from typing import List, Dict, Any, Optional
from dataclasses import dataclass
from app.utils.atomic_media_write import atomic_audio_output, cleanup_atomic_audio_output, create_atomic_audio_temp_path, finalize_atomic_audio_output
from base_tts_engine import TTSResult
logger = logging.getLogger(__name__)
SegmentInfo = <NODE:12>()

class LineRegenerationMixin:
    '''
    TTS 줄별 재생성 공통 기능 Mixin

    이 Mixin을 상속받는 클래스는 다음을 구현해야 합니다:
    - generate_single_line(text, output_path, **engine_params) -> TTSResult
    - config.line_folder_name (줄별 오디오 저장 폴더명)
    '''
    
    def get_line_audio_dir(self = None, project_dir = None):
        '''
        줄별 오디오 저장 디렉토리 반환

        Args:
            project_dir: 프로젝트 루트 디렉토리

        Returns:
            Path: 줄별 오디오 저장 경로 (예: project_dir/audio/chirp3hd_single/)
        '''
        folder_name = getattr(self.config, 'line_folder_name', 'tts_single')
        line_dir = Path(project_dir) / 'audio' / folder_name
        line_dir.mkdir(parents = True, exist_ok = True)
        return line_dir

    
    def get_line_audio_path(self = None, project_dir = None, line_index = None):
        '''
        특정 줄의 오디오 파일 경로 반환

        Args:
            project_dir: 프로젝트 루트 디렉토리
            line_index: 줄 인덱스 (1-based)

        Returns:
            str: 오디오 파일 경로
        '''
        audio_format = getattr(self.config, 'audio_format', 'wav')
        line_dir = self.get_line_audio_dir(project_dir)
        return str(line_dir / f'''line_{line_index:04d}.{audio_format}''')

    
    def regenerate_line(self = None, project_dir = None, line_index = None, text = ('project_dir', str, 'line_index', int, 'text', str, 'return', TTSResult), **engine_params):
        '''
        특정 줄 재생성

        Args:
            project_dir: 프로젝트 루트 디렉토리
            line_index: 줄 인덱스 (1-based)
            text: 재생성할 텍스트
            **engine_params: 엔진별 파라미터 (voice_id, speed 등)

        Returns:
            TTSResult: 생성 결과
        '''
        output_path = self.get_line_audio_path(project_dir, line_index)
        logger.info(f'''[LineRegenerationMixin] 줄 재생성: index={line_index}, path={output_path}''')
        if os.path.exists(output_path):
            os.remove(output_path)
        temp_output_path = create_atomic_audio_temp_path(output_path)
    # WARNING: Decompyle incomplete

    
    def remerge_audio_from_segments(self, segments = None, output_path = None, silence_duration = None, normalize = (0.4, True, -16), target_lufs = ('segments', List[SegmentInfo], 'output_path', str, 'silence_duration', float, 'normalize', bool, 'target_lufs', float, 'return', TTSResult)):
        '''
        세그먼트 오디오들을 하나로 병합

        Args:
            segments: 세그먼트 정보 리스트
            output_path: 출력 파일 경로
            silence_duration: 세그먼트 간 묵음 길이 (초)
            normalize: 볼륨 정규화 여부
            target_lufs: 목표 LUFS (정규화 시)

        Returns:
            TTSResult: 병합 결과
        '''
        
        try:
            FFmpegWrapper = FFmpegWrapper
            import app.utils.ffmpeg_wrapper
            import soundfile as sf
            import numpy as np
            ffmpeg = FFmpegWrapper()
            sample_rate = getattr(self.config, 'sample_rate', 24000)
            silence_samples = int(silence_duration * sample_rate)
            silence = np.zeros(silence_samples, dtype = np.float32)
            all_audio = []
            updated_segments = []
            current_time = 0
            sorted_segments = sorted(segments, key = (lambda s: s.index))
            for i, seg in enumerate(sorted_segments):
                if not os.path.exists(seg.audio_path):
                    logger.warning(f'''[Remerge] 오디오 파일 없음, 무음 대체: {seg.audio_path}''')
                    estimated_duration = seg.duration if seg.duration > 0 else 1
                    audio_data = np.zeros(int(sample_rate * estimated_duration), dtype = np.float32)
                    duration = estimated_duration
                else:
                    (audio_data, sr) = sf.read(seg.audio_path)
                    if sr != sample_rate:
                        import tempfile
                        tmp = tempfile.NamedTemporaryFile(suffix = '.wav', delete = False)
                        tmp_path = tmp.name
                        
                        try:
                            None(None, None)
                        with None:
                            if not None:
                                
                                try:
                                    
                                    try:
                                        ffmpeg.resample_audio(seg.audio_path, tmp_path, sample_rate)
                                        (audio_data, sr) = sf.read(tmp_path)
                                        os.remove(tmp_path)
                                        if len(audio_data.shape) > 1:
                                            audio_data = audio_data.mean(axis = 1)
                                        duration = len(audio_data) / sample_rate
                                        if not seg.original_audio_path:
                                            seg_info = SegmentInfo(index = seg.index, audio_path = seg.audio_path, start = current_time, end = current_time + duration, duration = duration, text = seg.text, tts_content = seg.tts_content, is_regenerated = seg.is_regenerated, original_audio_path = seg.audio_path)
                                            updated_segments.append(seg_info)
                                            all_audio.append(audio_data.astype(np.float32))
                                            if i < len(sorted_segments) - 1:
                                                all_audio.append(silence)
                                                current_time += duration + silence_duration
                                                continue
                                        current_time += duration
                                        continue
                                        if not all_audio:
                                            return TTSResult(status = 'error', error = '병합할 오디오가 없습니다')
                                        merged_audio = None.concatenate(all_audio)
                                        if normalize:
                                            merged_audio = self._normalize_audio(merged_audio, target_lufs)
                                        atomic_output_path = atomic_audio_output(output_path)
                                        os.makedirs(os.path.dirname(atomic_output_path), exist_ok = True)
                                        sf.write(atomic_output_path, merged_audio, sample_rate)
                                        if normalize:
                                            normalized_output = None
                                            output_path_obj = Path(atomic_output_path)
                                            normalized_output = str(output_path_obj.with_name(f'''{output_path_obj.stem}_loudnorm{output_path_obj.suffix}'''))
                                            ffmpeg.normalize_audio_loudness(input_path = atomic_output_path, output_path = normalized_output, target_lufs = target_lufs)
                                            if os.path.exists(normalized_output) and os.path.getsize(normalized_output) > 0:
                                                os.replace(normalized_output, atomic_output_path)
                                                logger.info(f'''[Remerge] loudnorm 적용 완료: target={target_lufs} LUFS''')
                                            else:
                                                logger.warning('[Remerge] loudnorm 출력 파일이 없어 RMS 정규화 결과 유지')
                                        else:
                                            except Exception:
                                                loudnorm_err = None
                                                logger.warning(f'''[Remerge] loudnorm 적용 실패, RMS 정규화 결과 유지: {loudnorm_err}''')
                                                loudnorm_err = None
                                                del loudnorm_err
                                            except:
                                                loudnorm_err = None
                                                del loudnorm_err
                                            if normalized_output and os.path.exists(normalized_output):
                                                os.remove(normalized_output)
                                            else:
                                                except Exception:
                                                    pass
                                                except Exception:
                                                    
                                                    try:
                                                        None(None, None)
                                                    with None:
                                                        if not None:
                                                            
                                                            try:
                                                                
                                                                try:
                                                                    calculated_duration = current_time
                                                                    if not ffmpeg.get_video_duration(output_path):
                                                                        actual_duration = calculated_duration
                                                                        if actual_duration > 0 and calculated_duration > 0 and abs(actual_duration - calculated_duration) > 0.1:
                                                                            scale_factor = actual_duration / calculated_duration
                                                                            logger.debug(f'''[Remerge] 타이밍 보정: 계산={calculated_duration:.3f}s, 실제={actual_duration:.3f}s, scale={scale_factor:.4f}''')
                                                                            for seg in updated_segments:
                                                                                seg.start = round(seg.start * scale_factor, 3)
                                                                                seg.end = round(seg.end * scale_factor, 3)
                                                                                seg.duration = round(seg.end - seg.start, 3)
                                                                                total_duration = actual_duration
                                                                                logger.info(f'''[Remerge] 병합 완료: {len(updated_segments)}개 세그먼트, {total_duration:.2f}초''')
                                                                                for s in updated_segments:
                                                                                    print(f'''[Remerge DEBUG] seg #{s.index}: text=\'{s.text[:30] if s.text else 'EMPTY'}...\', ttsContent=\'{s.tts_content[:30] if s.tts_content else 'NONE'}...\', isRegenerated={s.is_regenerated}''', flush = True)
                                                                                    return 'success'(status = output_path, audio_path = total_duration, duration = 'segments', extra = {
                                                                                        (lambda .0: [ {
'index': s.index,
'start': round(s.start, 3),
'end': round(s.end, 3),
'duration': round(s.duration, 3),
'text': s.text,
'audioPath': s.audio_path,
'ttsContent': s.tts_content,
'isRegenerated': s.is_regenerated } for s in .0 if s.original_audio_path ]): updated_segments() })
                                                                                    except Exception:
                                                                                        e = None
                                                                                        logger.error(f'''[Remerge] 병합 실패: {e}''')
                                                                                        del e
                                                                                        return None
                                                                                        None = 
                                                                                        del e








    
    def _normalize_audio(self = None, audio = None, target_lufs = None):
        '''
        오디오 볼륨 정규화 (LUFS 기반)

        Args:
            audio: 오디오 데이터 (numpy array)
            target_lufs: 목표 LUFS

        Returns:
            np.ndarray: 정규화된 오디오
        '''
        import numpy as np
        rms = np.sqrt(np.mean(audio ** 2))
        if rms > 0:
            target_rms = 10 ** (target_lufs / 20)
            gain = target_rms / rms
            gain = min(gain, 1 / (np.max(np.abs(audio)) + 1e-06))
            audio = audio * gain
        return audio

    
    def save_line_audios(self = None, project_dir = None, lines = None, **engine_params):
        """
        여러 줄의 오디오를 개별 파일로 저장

        Args:
            project_dir: 프로젝트 루트 디렉토리
            lines: 줄 정보 리스트 [{'index': 1, 'text': '...', 'audio': bytes}, ...]
            **engine_params: 엔진별 파라미터

        Returns:
            List[TTSResult]: 각 줄의 저장 결과
        """
        results = []
        line_dir = self.get_line_audio_dir(project_dir)
        for line in lines:
            index = line.get('index', 0)
            audio_data = line.get('audio')
            text = line.get('text', '')
            if not audio_data:
                results.append(TTSResult(status = 'error', error = f'''줄 {index}: 오디오 데이터 없음'''))
                continue
            audio_format = getattr(self.config, 'audio_format', 'wav')
            output_path = str(line_dir / f'''line_{index:04d}.{audio_format}''')
            atomic_output_path = atomic_audio_output(output_path)
            f = open(atomic_output_path, 'wb')
            f.write(audio_data)
            None(None, None)
        with None:
            if not None:
                pass
        None(None, None)
