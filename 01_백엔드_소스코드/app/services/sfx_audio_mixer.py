# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: sfx_audio_mixer.pyc (Python 3.11)

'''
SFX 오디오 믹서

FFmpeg amix 필터를 사용하여 다중 SFX 트랙을 믹싱합니다.
메인 오디오(나레이션/TTS)와 SFX를 합성합니다.
'''
import os
import json
import subprocess
import logging
import uuid
from typing import Dict, List, Optional, Any
from pathlib import Path
from dataclasses import dataclass
from app.config.paths import get_data_path, get_ffmpeg_path
from app.utils.file_paths import ProjectPaths
logger = logging.getLogger(__name__)
MixSettings = <NODE:12>()

class SFXAudioMixer:
    '''SFX 오디오 믹서 클래스'''
    
    def __init__(self = None, project_id = None):
        '''
        Args:
            project_id: 프로젝트 ID (파일 저장 경로용)
        '''
        self.project_id = project_id
        self.ffmpeg_path = get_ffmpeg_path()
        if project_id:
            project_paths = ProjectPaths(project_id)
            project_paths.ensure_directories()
            self.output_dir = project_paths.project_base / 'audio'
        else:
            self.output_dir = get_data_path() / 'temp' / 'mix'
        self.output_dir.mkdir(parents = True, exist_ok = True)

    
    def mix_sfx_with_main_audio(self = None, main_audio_path = None, sfx_tracks = None, output_filename = (None, None), settings = ('main_audio_path', str, 'sfx_tracks', List[Dict], 'output_filename', Optional[str], 'settings', Optional[MixSettings], 'return', Dict[(str, Any)])):
        '''
        메인 오디오와 SFX 트랙들을 믹싱

        Args:
            main_audio_path: 메인 오디오 파일 경로
            sfx_tracks: SFX 트랙 리스트
            output_filename: 출력 파일명 (없으면 자동 생성)
            settings: 믹싱 설정

        Returns:
            믹싱 결과
        '''
        if not settings:
            settings = MixSettings()
        resolved_main_audio = self._resolve_file_path(main_audio_path)
        if not resolved_main_audio or Path(resolved_main_audio).exists():
            logger.error(f'''[SFXMixer] Main audio not found: {main_audio_path} -> resolved: {resolved_main_audio}''')
            return {
                'success': False,
                'error': f'''Main audio not found: {main_audio_path}''' }
        main_audio_path = None
        enabled_tracks = sfx_tracks()
        if not enabled_tracks:
            return self._copy_main_audio(main_audio_path, output_filename, settings)
        if not (lambda .0: pass# WARNING: Decompyle incomplete
):
            output_filename = f'''sfx_mixed_{uuid.uuid4().hex[:8]}.{settings.output_format}'''
        output_path = self.output_dir / output_filename
    # WARNING: Decompyle incomplete

    
    def _build_mix_command(self, main_audio_path = None, sfx_tracks = None, output_path = None, settings = ('main_audio_path', str, 'sfx_tracks', List[Dict], 'output_path', str, 'settings', MixSettings, 'return', List[str])):
        '''
        FFmpeg 믹싱 명령 구성

        amix 필터 대신 adelay + amix 조합으로 정확한 타이밍 제어
        '''
        cmd = [
            str(self.ffmpeg_path),
            '-y']
        cmd.extend([
            '-i',
            main_audio_path])
        valid_tracks = []
        for track in sfx_tracks:
            file_path = self._resolve_file_path(track.get('fileUrl', ''))
            if file_path and Path(file_path).exists():
                cmd.extend([
                    '-i',
                    file_path])
                valid_tracks.append(track)
                logger.info(f'''[SFXMixer] Added SFX input: {file_path}''')
                continue
            logger.warning(f'''[SFXMixer] Skipping invalid SFX: {track.get('fileUrl', '')}''')
            if not valid_tracks:
                logger.info('[SFXMixer] No valid SFX tracks, returning main audio only')
                return None
            filter_complex = None._build_filter_graph(valid_tracks, settings)
            logger.info(f'''[SFXMixer] Filter complex: {filter_complex}''')
            cmd.extend([
                '-filter_complex',
                filter_complex])
            cmd.extend([
                '-map',
                '[out]',
                '-ar',
                str(settings.sample_rate),
                '-ac',
                str(settings.channels)])
            cmd.append(output_path)
            return cmd

    
    def _build_filter_graph(self = None, sfx_tracks = None, settings = None):
        '''
        FFmpeg 필터 그래프 구성

        각 SFX에 adelay를 적용하고 모든 스트림을 amix로 합침
        '''
        filters = []
        mix_inputs = [
            '[0:a]']
        for i, track in enumerate(sfx_tracks, start = 1):
            timing = track.get('timing', { })
            start_ms = int(timing.get('startTime', 0) * 1000)
            track_settings = track.get('settings', { })
            volume = track_settings.get('volume', 2) * settings.sfx_volume_multiplier
            fade_in = track_settings.get('fadeIn', 0)
            fade_out = track_settings.get('fadeOut', 0)
            filter_chain = []
            if start_ms > 0:
                filter_chain.append(f'''adelay={start_ms}|{start_ms}''')
            filter_chain.append(f'''volume={volume:.2f}''')
            duration = track.get('duration', 1)
            if fade_in > 0:
                filter_chain.append(f'''afade=t=in:st=0:d={fade_in}''')
            if fade_out > 0:
                fade_start = max(0, duration - fade_out)
                filter_chain.append(f'''afade=t=out:st={fade_start}:d={fade_out}''')
            input_label = f'''[{i}:a]'''
            output_label = f'''[sfx{i}]'''
            filter_str = f'''{input_label}{','.join(filter_chain)}{output_label}'''
            filters.append(filter_str)
            mix_inputs.append(output_label)
            num_inputs = len(mix_inputs)
            mix_filter = f'''{''.join(mix_inputs)}amix=inputs={num_inputs}:duration=longest:dropout_transition=2[out]'''
            filters.append(mix_filter)
            return ';'.join(filters)

    
    def _resolve_file_path(self = None, file_url = None):
        '''파일 URL을 실제 경로로 변환'''
        if not file_url:
            return None
        if None(file_url).is_absolute() and Path(file_url).exists():
            return file_url
        if None.startswith('/data/'):
            data_path = get_data_path()
            relative = file_url[6:]
            full_path = data_path / relative
            if full_path.exists():
                return str(full_path)
            if None.startswith('projects/'):
                data_path = get_data_path()
                full_path = data_path / file_url
                if full_path.exists():
                    return str(full_path)
                if None.project_id:
                    project_paths = ProjectPaths(self.project_id)
                    for base in (project_paths.audio_dir(), project_paths.project_base):
                        full_path = base / file_url
                        if full_path.exists():
                            
                            return None, str(full_path)
                        return None

    
    def _copy_main_audio(self = None, main_audio_path = None, output_filename = None, settings = ('main_audio_path', str, 'output_filename', Optional[str], 'settings', MixSettings, 'return', Dict[(str, Any)])):
        '''SFX 없이 메인 오디오만 복사/변환'''
        if not output_filename:
            output_filename = f'''audio_{uuid.uuid4().hex[:8]}.{settings.output_format}'''
        output_path = self.output_dir / output_filename
        cmd = [
            str(self.ffmpeg_path),
            '-y',
            '-i',
            main_audio_path,
            '-ar',
            str(settings.sample_rate),
            '-ac',
            str(settings.channels),
            str(output_path)]
        import sys
        kwargs = {
            'capture_output': True,
            'stdin': subprocess.DEVNULL,
            'check': True,
            'timeout': 120 }
        if sys.platform == 'win32':
            kwargs['creationflags'] = subprocess.CREATE_NO_WINDOW
    # WARNING: Decompyle incomplete

    
    def create_sfx_preview(self = None, sfx_tracks = None, duration = None, start_time = (10, 0)):
        '''
        SFX 트랙들의 미리듣기 생성 (메인 오디오 없이)

        Args:
            sfx_tracks: SFX 트랙 리스트
            duration: 미리듣기 길이 (초)
            start_time: 시작 시간

        Returns:
            미리듣기 결과
        '''
        enabled_tracks = sfx_tracks()
        if not enabled_tracks:
            return {
                'success': False,
                'error': 'No enabled tracks' }
        end_time = (lambda .0: pass# WARNING: Decompyle incomplete
) + duration
        relevant_tracks = []
    # WARNING: Decompyle incomplete

    
    def _build_preview_command(self = None, tracks = None, duration = None, output_path = ('tracks', List[Dict], 'duration', float, 'output_path', str, 'return', List[str])):
        '''미리듣기용 FFmpeg 명령 구성'''
        cmd = [
            str(self.ffmpeg_path),
            '-y']
        cmd.extend([
            '-f',
            'lavfi',
            '-i',
            f'''anullsrc=r=44100:cl=stereo:d={duration}'''])
        for track in tracks:
            file_path = self._resolve_file_path(track.get('fileUrl', ''))
            if file_path:
                cmd.extend([
                    '-i',
                    file_path])
            filters = []
            mix_inputs = [
                '[0:a]']
            for i, track in enumerate(tracks, start = 1):
                timing = track.get('timing', { })
                start_ms = int(timing.get('startTime', 0) * 1000)
                volume = track.get('settings', { }).get('volume', 2)
                filter_parts = []
                if start_ms > 0:
                    filter_parts.append(f'''adelay={start_ms}|{start_ms}''')
                filter_parts.append(f'''volume={volume:.2f}''')
                output_label = f'''[p{i}]'''
                filter_str = f'''[{i}:a]{','.join(filter_parts)}{output_label}'''
                filters.append(filter_str)
                mix_inputs.append(output_label)
                num_inputs = len(mix_inputs)
                mix_filter = f'''{''.join(mix_inputs)}amix=inputs={num_inputs}:duration=first[out]'''
                filters.append(mix_filter)
                cmd.extend([
                    '-filter_complex',
                    ';'.join(filters)])
                cmd.extend([
                    '-map',
                    '[out]',
                    '-t',
                    str(duration),
                    output_path])
                return cmd



def mix_project_sfx(project_id = None, main_audio_path = dataclass, sfx_tracks = None, master_volume = (1, 1), sfx_volume = ('project_id', str, 'main_audio_path', str, 'sfx_tracks', List[Dict], 'master_volume', float, 'sfx_volume', float, 'return', Dict[(str, Any)])):
    '''
    프로젝트의 SFX 믹싱 편의 함수

    Args:
        project_id: 프로젝트 ID
        main_audio_path: 메인 오디오 경로
        sfx_tracks: SFX 트랙 리스트
        master_volume: 마스터 볼륨
        sfx_volume: SFX 볼륨 배율

    Returns:
        믹싱 결과
    '''
    mixer = SFXAudioMixer(project_id = project_id)
    settings = MixSettings(master_volume = master_volume, sfx_volume_multiplier = sfx_volume)
    return mixer.mix_sfx_with_main_audio(main_audio_path = main_audio_path, sfx_tracks = sfx_tracks, settings = settings)


def create_sfx_only_preview(sfx_tracks = None, duration = None, start_time = None, project_id = (10, 0, None)):
    '''
    SFX만 미리듣기 생성 편의 함수
    '''
    mixer = SFXAudioMixer(project_id = project_id)
    return mixer.create_sfx_preview(sfx_tracks, duration, start_time)
