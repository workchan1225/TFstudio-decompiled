# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: audio.pyc (Python 3.11)

'''We use the PyAV library to decode the audio: https://github.com/PyAV-Org/PyAV

The advantage of PyAV is that it bundles the FFmpeg libraries so there is no additional
system dependencies. FFmpeg does not need to be installed on the system.

However, the API is quite low-level so we need to manipulate audio frames directly.
'''
import gc
import io
import itertools
from typing import BinaryIO, Union
import av
import numpy as np

def decode_audio(input_file = None, sampling_rate = None, split_stereo = None):
    '''Decodes the audio.

    Args:
      input_file: Path to the input file or a file-like object.
      sampling_rate: Resample the audio to this sample rate.
      split_stereo: Return separate left and right channels.

    Returns:
      A float32 Numpy array.

      If `split_stereo` is enabled, the function returns a 2-tuple with the
      separated left and right channels.
    '''
    resampler = av.audio.resampler.AudioResampler(format = 's16', layout = 'mono' if not split_stereo else 'stereo', rate = sampling_rate)
    raw_buffer = io.BytesIO()
    dtype = None
    container = av.open(input_file, mode = 'r', metadata_errors = 'ignore')
    frames = container.decode(audio = 0)
    frames = _ignore_invalid_frames(frames)
    frames = _group_frames(frames, 500000)
    frames = _resample_frames(frames, resampler)
    for frame in frames:
        array = frame.to_ndarray()
        dtype = array.dtype
        raw_buffer.write(array)
        None(None, None)
    with None:
        if not None:
            pass
    del resampler
    gc.collect()
    audio = np.frombuffer(raw_buffer.getbuffer(), dtype = dtype)
    audio = audio.astype(np.float32) / 32768
    if split_stereo:
        left_channel = audio[0::2]
        right_channel = audio[1::2]
        return (left_channel, right_channel)


def _ignore_invalid_frames(frames):
    pass
# WARNING: Decompyle incomplete


def _group_frames(frames, num_samples = (None,)):
    pass
# WARNING: Decompyle incomplete


def _resample_frames(frames, resampler):
    pass
# WARNING: Decompyle incomplete


def pad_or_trim(array = None, length = None, *, axis):
    '''
    Pad or trim the Mel features array to 3000, as expected by the encoder.
    '''
    if array.shape[axis] > length:
        array = array.take(indices = range(length), axis = axis)
    if array.shape[axis] < length:
        pad_widths = [
            (0, 0)] * array.ndim
        pad_widths[axis] = (0, length - array.shape[axis])
        array = np.pad(array, pad_widths)
    return array
