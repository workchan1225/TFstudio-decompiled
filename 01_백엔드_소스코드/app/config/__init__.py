# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: __init__.pyc (Python 3.11)

import os
IMAGE_EFFECTS_ENABLED = os.environ.get('IMAGE_EFFECTS_ENABLED', 'true').lower() == 'true'
OPENCV_EFFECTS_ENGINE = os.environ.get('OPENCV_EFFECTS_ENGINE', 'true').lower() == 'true'
OPENCV_MOTION_EFFECTS = {
    'pan',
    'rotate',
    'zoom_in',
    'zoom_out',
    'ken_burns'}
FFMPEG_ONLY_EFFECTS = {
    'fade',
    'none',
    'static',
    'blur_bg'}
