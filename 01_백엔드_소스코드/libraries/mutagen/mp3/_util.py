# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: _util.pyc (Python 3.11)

'''
http://www.codeproject.com/Articles/8295/MPEG-Audio-Frame-Header
http://wiki.hydrogenaud.io/index.php?title=MP3
'''
from __future__ import division
from functools import partial
from io import BytesIO
from typing import List
from mutagen._util import cdata, BitReader, iterbytes

class LAMEError(Exception):
    pass


class LAMEHeader(object):
    '''http://gabriel.mp3-tech.org/mp3infotag.html'''
    vbr_method = 0
    lowpass_filter = 0
    quality = -1
    vbr_quality = -1
    track_peak = None
    track_gain_origin = 0
    track_gain_adjustment = None
    album_gain_origin = 0
    album_gain_adjustment = None
    encoding_flags = 0
    ath_type = -1
    bitrate = -1
    encoder_delay_start = 0
    encoder_padding_end = 0
    source_sample_frequency_enum = -1
    unwise_setting_used = False
    stereo_mode = 0
    noise_shaping = 0
    mp3_gain = 0
    surround_info = 0
    preset_used = 0
    music_length = 0
    music_crc = -1
    header_crc = -1
    
    def __init__(self, xing, fileobj):
        '''Raises LAMEError if parsing fails'''
        payload = fileobj.read(27)
        if len(payload) != 27:
            raise LAMEError('Not enough data')
        r = BitReader(BytesIO(payload))
        revision = r.bits(4)
        if revision != 0:
            raise LAMEError('unsupported header revision %d' % revision)
        self.vbr_method = r.bits(4)
        self.lowpass_filter = r.bits(8) * 100
        self.quality = (100 - xing.vbr_scale) % 10
        self.vbr_quality = (100 - xing.vbr_scale) // 10
        track_peak_data = r.bytes(4)
        if track_peak_data == b'\x00\x00\x00\x00':
            self.track_peak = None
        else:
            self.track_peak = cdata.uint32_be(track_peak_data) / 8388608
        track_gain_type = r.bits(3)
        self.track_gain_origin = r.bits(3)
        sign = r.bits(1)
        gain_adj = r.bits(9) / 10
        if sign:
            gain_adj *= -1
        if track_gain_type == 1:
            self.track_gain_adjustment = gain_adj
        else:
            self.track_gain_adjustment = None
    # WARNING: Decompyle incomplete

    
    def guess_settings(self, major, minor):
