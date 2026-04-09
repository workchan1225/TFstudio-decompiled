# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: fft.pyc (Python 3.11)

from __future__ import annotations
from typing import Union, Sequence, Literal
import torch
import torch.fft as torch
from torch.fft import *
from _typing import Array

def fftn(x = None, *, s, axes, norm, **kwargs):
    pass
# WARNING: Decompyle incomplete


def ifftn(x = None, *, s, axes, norm, **kwargs):
    pass
# WARNING: Decompyle incomplete


def rfftn(x = None, *, s, axes, norm, **kwargs):
    pass
# WARNING: Decompyle incomplete


def irfftn(x = None, *, s, axes, norm, **kwargs):
    pass
# WARNING: Decompyle incomplete


def fftshift(x = None, *, axes, **kwargs):
    pass
# WARNING: Decompyle incomplete


def ifftshift(x = None, *, axes, **kwargs):
    pass
# WARNING: Decompyle incomplete

__all__ = torch.fft.__all__ + [
    'fftn',
    'ifftn',
    'rfftn',
    'irfftn',
    'fftshift',
    'ifftshift']
_all_ignore = [
    'torch']
