# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: feature_extractor.pyc (Python 3.11)

import numpy as np

class FeatureExtractor:
    
    def __init__(self, feature_size, sampling_rate, hop_length, chunk_length, n_fft = (80, 16000, 160, 30, 400)):
        self.n_fft = n_fft
        self.hop_length = hop_length
        self.chunk_length = chunk_length
        self.n_samples = chunk_length * sampling_rate
        self.nb_max_frames = self.n_samples // hop_length
        self.time_per_frame = hop_length / sampling_rate
        self.sampling_rate = sampling_rate
        self.mel_filters = self.get_mel_filters(sampling_rate, n_fft, n_mels = feature_size).astype('float32')

    get_mel_filters = (lambda sr, n_fft, n_mels = (128,): n_mels = int(n_mels)fftfreqs = np.fft.rfftfreq(n = n_fft, d = 1 / sr)min_mel = 0max_mel = 45.2456mels = np.linspace(min_mel, max_mel, n_mels + 2)f_min = 0f_sp = 66.6667freqs = f_min + f_sp * melsmin_log_hz = 1000min_log_mel = (min_log_hz - f_min) / f_splogstep = np.log(6.4) / 27log_t = mels >= min_log_melfreqs[log_t] = min_log_hz * np.exp(logstep * (mels[log_t] - min_log_mel))fdiff = np.diff(freqs)ramps = freqs.reshape(-1, 1) - fftfreqs.reshape(1, -1)lower = -ramps[:-2] / np.expand_dims(fdiff[:-1], axis = 1)upper = ramps[2:] / np.expand_dims(fdiff[1:], axis = 1)weights = np.maximum(np.zeros_like(lower), np.minimum(lower, upper))enorm = 2 / (freqs[2:n_mels + 2] - freqs[:n_mels])weights *= np.expand_dims(enorm, axis = 1)weights)()
    stft = (lambda input_array, n_fft, hop_length, win_length, window, center = None, mode = staticmethod, normalized = staticmethod, onesided = (None, None, None, True, 'reflect', False, None, None), return_complex = ('input_array', np.ndarray, 'n_fft', int, 'hop_length', int, 'win_length', int, 'window', np.ndarray, 'center', bool, 'mode', str, 'normalized', bool, 'onesided', bool, 'return_complex', bool): pass# WARNING: Decompyle incomplete
)()
    
    def __call__(self = None, waveform = None, padding = None, chunk_length = (160, None)):
        '''
        Compute the log-Mel spectrogram of the provided audio.
        '''
        pass
    # WARNING: Decompyle incomplete
