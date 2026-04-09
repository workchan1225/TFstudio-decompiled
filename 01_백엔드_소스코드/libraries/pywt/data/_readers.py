# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: _readers.pyc (Python 3.11)

import functools
import importlib.resources as importlib
import os
import numpy as np
_DATADIR = importlib.resources.files('pywt.data')
ascent = (lambda : f = importlib.resources.as_file(_DATADIR.joinpath('ascent.npz'))ascent = np.load(f)['data']None(None, None))()
aero = (lambda : f = importlib.resources.as_file(_DATADIR.joinpath('aero.npz'))aero = np.load(f)['data']None(None, None))()
camera = (lambda : f = importlib.resources.as_file(_DATADIR.joinpath('camera.npz'))camera = np.load(f)['data']None(None, None))()
ecg = (lambda : f = importlib.resources.as_file(_DATADIR.joinpath('ecg.npz'))ecg = np.load(f)['data']None(None, None))()
nino = (lambda : f = importlib.resources.as_file(_DATADIR.joinpath('sst_nino3.npz'))sst_csv = np.load(f)['data']None(None, None))()
