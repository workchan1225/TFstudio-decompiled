# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: zoom.pyc (Python 3.11)

'''
줌 효과 (Zoom In / Zoom Out)

서브픽셀 정밀도의 부드러운 줌 효과
다양한 해상도(그록 영상 포함) 호환성 고려
'''
import random
from typing import Tuple
import numpy as np
from base import BaseEffect
ZOOM_FOCUS_POSITIONS = [
    'center',
    'top',
    'bottom',
    'left',
    'right',
    'top_left',
    'top_right',
    'bottom_left',
    'bottom_right']
FOCUS_RATIOS = {
    'center': (0.5, 0.5),
    'top': (0.5, 0.3),
    'bottom': (0.5, 0.7),
    'left': (0.3, 0.5),
    'right': (0.7, 0.5),
    'top_left': (0.3, 0.3),
    'top_right': (0.7, 0.3),
    'bottom_left': (0.3, 0.7),
    'bottom_right': (0.7, 0.7) }

class ZoomInEffect(BaseEffect):
    pass
# WARNING: Decompyle incomplete


class ZoomOutEffect(BaseEffect):
    pass
# WARNING: Decompyle incomplete
