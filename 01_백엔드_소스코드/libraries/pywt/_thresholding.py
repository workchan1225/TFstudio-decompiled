# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: _thresholding.pyc (Python 3.11)

'''
The thresholding helper module implements the most popular signal thresholding
functions.
'''
import numpy as np
__all__ = [
    'threshold',
    'threshold_firm']

def soft(data, value, substitute = (0,)):
