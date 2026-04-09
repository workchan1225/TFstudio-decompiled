# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: vad.pyc (Python 3.11)

import bisect
import functools
import os
from dataclasses import dataclass
from typing import Dict, List, Optional, Tuple
import numpy as np
from faster_whisper.utils import get_assets_path
VadOptions = <NODE:12>()

def get_speech_timestamps(audio = None, vad_options = None, sampling_rate = dataclass, **kwargs):
    '''This method is used for splitting long audios into speech chunks using silero VAD.

    Args:
      audio: One dimensional float array.
      vad_options: Options for VAD processing.
      sampling rate: Sampling rate of the audio.
      kwargs: VAD options passed as keyword arguments for backward compatibility.

    Returns:
      List of dicts containing begin and end samples of each speech chunk.
    '''
    pass
# WARNING: Decompyle incomplete


def collect_chunks(audio = None, chunks = None, sampling_rate = None, max_duration = (16000, float('inf'))):
    '''This function merges the chunks of audio into chunks of max_duration (s) length.'''
    if not chunks:
        chunk_metadata = {
            'offset': 0,
            'duration': 0,
            'segments': [] }
        return ([
            np.array([], dtype = np.float32)], [
            chunk_metadata])
    audio_chunks = None
    chunks_metadata = []
    current_segments = []
    current_duration = 0
    total_duration = 0
    current_audio = np.array([], dtype = np.float32)
    for chunk in chunks:
        if current_duration + chunk['end'] - chunk['start'] > max_duration * sampling_rate:
            audio_chunks.append(current_audio)
            chunk_metadata = {
                'offset': total_duration / sampling_rate,
                'duration': current_duration / sampling_rate,
                'segments': current_segments }
            total_duration += current_duration
            chunks_metadata.append(chunk_metadata)
            current_segments = []
            current_audio = audio[chunk['start']:chunk['end']]
            current_duration = chunk['end'] - chunk['start']
            continue
        current_segments.append(chunk)
        current_audio = np.concatenate((current_audio, audio[chunk['start']:chunk['end']]))
        current_duration += chunk['end'] - chunk['start']
        audio_chunks.append(current_audio)
        chunk_metadata = {
            'offset': total_duration / sampling_rate,
            'duration': current_duration / sampling_rate,
            'segments': current_segments }
        chunks_metadata.append(chunk_metadata)
        return (audio_chunks, chunks_metadata)


class SpeechTimestampsMap:
    '''Helper class to restore original speech timestamps.'''
    
    def __init__(self = None, chunks = None, sampling_rate = None, time_precision = (2,)):
        self.sampling_rate = sampling_rate
        self.time_precision = time_precision
        self.chunk_end_sample = []
        self.total_silence_before = []
        previous_end = 0
        silent_samples = 0
        for chunk in chunks:
            silent_samples += chunk['start'] - previous_end
            previous_end = chunk['end']
            self.chunk_end_sample.append(chunk['end'] - silent_samples)
            self.total_silence_before.append(silent_samples / sampling_rate)
            return None

    
    def get_original_time(self = None, time = None, chunk_index = None, is_end = (None, False)):
        pass
    # WARNING: Decompyle incomplete

    
    def get_chunk_index(self = None, time = None, is_end = None):
        sample = int(time * self.sampling_rate)
        if sample in self.chunk_end_sample and is_end:
            return self.chunk_end_sample.index(sample)
        return None(bisect.bisect(self.chunk_end_sample, sample), len(self.chunk_end_sample) - 1)


get_vad_model = (lambda : path = os.path.join(get_assets_path(), 'silero_vad_v6.onnx')SileroVADModel(path))()

class SileroVADModel:
    
    def __init__(self, path):
        
        try:
            import onnxruntime
        except ImportError:
            e = None
            raise RuntimeError('Applying the VAD filter requires the onnxruntime package'), e
            e = None
            del e

        opts = onnxruntime.SessionOptions()
        opts.inter_op_num_threads = 1
        opts.intra_op_num_threads = 1
        opts.enable_cpu_mem_arena = False
        opts.log_severity_level = 4
        self.session = onnxruntime.InferenceSession(path, providers = [
            'CPUExecutionProvider'], sess_options = opts)

    
    def __call__(self = None, audio = None, num_samples = None, context_size_samples = (512, 64)):
        pass
    # WARNING: Decompyle incomplete
