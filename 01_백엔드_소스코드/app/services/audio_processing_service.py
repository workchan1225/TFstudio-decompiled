# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: audio_processing_service.pyc (Python 3.11)

'''
오디오 처리 서비스

무음 구간 제거 및 오디오 병합 기능을 제공합니다.
'''
import subprocess
import sys
import os
import logging
import tempfile
from pathlib import Path
from typing import List, Dict, Tuple, Optional, Callable
from copy import deepcopy
from app.config.paths import get_ffmpeg_path
logger = logging.getLogger(__name__)

class SilenceRemovalCancelledError(Exception):
    '''무음 제거 작업이 사용자에 의해 취소됨'''
    pass


class AudioProcessingService:
    '''오디오 처리 서비스 클래스'''
    remove_silence_regions = (lambda audio_path, silence_regions = None, min_gap = None, output_path = staticmethod, progress_callback = (0.15, None, None, None), cancel_check = ('audio_path', str, 'silence_regions', List[Dict], 'min_gap', float, 'output_path', Optional[str], 'progress_callback', Optional[Callable], 'cancel_check', Optional[Callable[([], bool)]], 'return', Tuple[(str, float, float)]): get_audio_duration = get_audio_durationimport app.utils.audio_silence_utilsif not silence_regions:
logger.info('[AudioProcessing] No silence regions to remove')(audio_path, 0, 0)audio_duration = get_audio_duration(audio_path)if audio_duration <= 0:
raise ValueError('오디오 길이를 확인할 수 없습니다')sorted_regions = sorted(silence_regions, key = (lambda r: r['start']))
        print(f'''[AudioProcessing] Calculating voice regions with min_gap={min_gap}''')
        print(f'''[AudioProcessing] Audio duration: {audio_duration}, Silence regions: {len(sorted_regions)}''')
        voice_regions = AudioProcessingService._calculate_voice_regions(audio_duration = audio_duration, silence_regions = sorted_regions, min_gap = min_gap)
        print(f'''[AudioProcessing] Calculated voice_regions count: {len(voice_regions)}''')
        if voice_regions:
            print(f'''[AudioProcessing] First voice region: {voice_regions[0]}''')
            print(f'''[AudioProcessing] Last voice region: {voice_regions[-1]}''')
        if not voice_regions:
            raise ValueError('제거 후 남은 음성 구간이 없습니다')
        if progress_callback:
            progress_callback('calculate', 1, 4, f'''음성 구간 {len(voice_regions)}개 계산 완료''')
        if cancel_check and cancel_check():
            raise SilenceRemovalCancelledError('무음 제거가 취소되었습니다')
        if not output_path:
            audio_dir = Path(audio_path).parent
            audio_name = Path(audio_path).stem
            output_path = str(audio_dir / f'''{audio_name}_trimmed.mp3''')
        trimmed_path = AudioProcessingService._extract_and_concat_segments(audio_path = audio_path, voice_regions = voice_regions, output_path = output_path, progress_callback = progress_callback, cancel_check = cancel_check)
        trimmed_duration = get_audio_duration(trimmed_path)
        removed_duration = audio_duration - trimmed_duration
        if progress_callback:
            progress_callback('verify', 4, 4, '결과 검증 완료')
        logger.info(f'''[AudioProcessing] Removed silence: {removed_duration:.2f}s, Original: {audio_duration:.2f}s -> Trimmed: {trimmed_duration:.2f}s''')
        return (trimmed_path, audio_duration, trimmed_duration)
)()
    _calculate_voice_regions = (lambda audio_duration = None, silence_regions = None, min_gap = staticmethod: voice_regions = []current_pos = 0print(f'''[_calculate_voice_regions] min_gap={min_gap}, half_gap={min_gap / 2}''')for i, region in enumerate(silence_regions):
silence_start = region['start']silence_end = region['end']silence_duration = silence_end - silence_starthalf_gap = min_gap / 2actual_remove_start = silence_start + half_gapactual_remove_end = silence_end - half_gapif i < 3:
print(f'''[_calculate_voice_regions] Region {i}: {silence_start:.3f}-{silence_end:.3f} ({silence_duration:.3f}s)''')print(f'''  -> actual_remove: {actual_remove_start:.3f}-{actual_remove_end:.3f}''')if actual_remove_end <= actual_remove_start:
if i < 3:
print('  -> SKIP (too short to remove)')continueif silence_start + half_gap > current_pos:
voice_regions.append({
'start': round(current_pos, 3),
'end': round(silence_start + half_gap, 3) })current_pos = silence_end - half_gapif current_pos < audio_duration:
voice_regions.append({
'start': round(current_pos, 3),
'end': round(audio_duration, 3) })voice_regions = voice_regions()logger.debug(f'''[AudioProcessing] Calculated {len(voice_regions)} voice regions''')voice_regions)()
    _extract_and_concat_segments = (lambda audio_path = None, voice_regions = None, output_path = staticmethod, progress_callback = (None, None), cancel_check = ('audio_path', str, 'voice_regions', List[Dict], 'output_path', str, 'progress_callback', Optional[Callable], 'cancel_check', Optional[Callable[([], bool)]], 'return', str): output_dir = Path(output_path).parentoutput_dir.mkdir(parents = True, exist_ok = True)temp_dir = tempfile.TemporaryDirectory()segment_files = []ffmpeg_exe = str(get_ffmpeg_path())total_segments = len(voice_regions)# WARNING: Decompyle incomplete
)()
    adjust_subtitle_timing = (lambda subtitle_layers = None, silence_regions = None, min_gap = staticmethod: pass# WARNING: Decompyle incomplete
)()
    adjust_merged_segments_timing = (lambda merged_segments = None, silence_regions = None, min_gap = staticmethod: pass# WARNING: Decompyle incomplete
)()
    adjust_timeline_images_timing = (lambda uploaded_images = None, silence_regions = None, min_gap = staticmethod: pass# WARNING: Decompyle incomplete
)()
    reverse_subtitle_timing = (lambda subtitle_layers = None, silence_regions = None, min_gap = staticmethod: pass# WARNING: Decompyle incomplete
)()
    calculate_removed_duration = (lambda silence_regions = None, min_gap = None: if not silence_regions:
0total_removed = Nonehalf_gap = min_gap / 2for region in silence_regions:
actual_duration = region['end'] - half_gap - (region['start'] + half_gap)if actual_duration > 0:
total_removed += actual_durationround(total_removed, 3))()
