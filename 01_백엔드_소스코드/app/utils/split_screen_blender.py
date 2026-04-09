# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: split_screen_blender.pyc (Python 3.11)

'''
Split Screen Detection and Gradient Blending Utility

Detects split screen images (vertical/horizontal divisions) and applies
gradient blending to create smooth transitions instead of hard lines.

v1.0.0: Initial implementation for handling AI-generated split screen images
v1.1.0: Added lighting normalization for gradual brightness differences
v1.2.0: Increased contrast threshold (7.0 → 30.0) to prevent false positive detection
'''
import numpy as np
from PIL import Image, ImageFilter
from typing import Dict, Tuple, Optional
import logging
logger = logging.getLogger(__name__)

def _local_half_contrast(arr = None, direction = None, position = None, window = (24,)):
    '''Estimate brightness contrast across a candidate split line.'''
    (height, width) = arr.shape
    if direction == 'vertical':
        left_end = max(0, position - 2)
        left_start = max(0, left_end - window)
        right_start = min(width, position + 2)
        right_end = min(width, right_start + window)
        if left_end - left_start < 4 or right_end - right_start < 4:
            return 0
        left_mean = None(np.mean(arr[(:, left_start:left_end)]))
        right_mean = float(np.mean(arr[(:, right_start:right_end)]))
        return abs(left_mean - right_mean)
    top_end = None(0, position - 2)
    top_start = max(0, top_end - window)
    bottom_start = min(height, position + 2)
    bottom_end = min(height, bottom_start + window)
    if top_end - top_start < 4 or bottom_end - bottom_start < 4:
        return 0
    top_mean = None(np.mean(arr[(top_start:top_end, :)]))
    bottom_mean = float(np.mean(arr[(bottom_start:bottom_end, :)]))
    return abs(top_mean - bottom_mean)


def detect_split_line(image = None, threshold = None):
