# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: _fft.pyc (Python 3.11)

from __future__ import annotations
from collections.abc import Sequence
from typing import Literal, TypeAlias
from _typing import Array, Device, DType, Namespace
_Norm: 'TypeAlias' = Literal[('backward', 'ortho', 'forward')]

def fft(x = None, xp = None, *, n, axis, norm):
    res = xp.fft.fft(x, n = n, axis = axis, norm = norm)
    if x.dtype in (xp.float32, xp.complex64):
        return res.astype(xp.complex64)


def ifft(x = None, xp = None, *, n, axis, norm):
    res = xp.fft.ifft(x, n = n, axis = axis, norm = norm)
    if x.dtype in (xp.float32, xp.complex64):
        return res.astype(xp.complex64)


def fftn(x = None, xp = None, *, s, axes, norm):
    res = xp.fft.fftn(x, s = s, axes = axes, norm = norm)
    if x.dtype in (xp.float32, xp.complex64):
        return res.astype(xp.complex64)


def ifftn(x = None, xp = None, *, s, axes, norm):
    res = xp.fft.ifftn(x, s = s, axes = axes, norm = norm)
    if x.dtype in (xp.float32, xp.complex64):
        return res.astype(xp.complex64)


def rfft(x = None, xp = None, *, n, axis, norm):
    res = xp.fft.rfft(x, n = n, axis = axis, norm = norm)
    if x.dtype == xp.float32:
        return res.astype(xp.complex64)


def irfft(x = None, xp = None, *, n, axis, norm):
    res = xp.fft.irfft(x, n = n, axis = axis, norm = norm)
    if x.dtype == xp.complex64:
        return res.astype(xp.float32)


def rfftn(x = None, xp = None, *, s, axes, norm):
    res = xp.fft.rfftn(x, s = s, axes = axes, norm = norm)
    if x.dtype == xp.float32:
        return res.astype(xp.complex64)


def irfftn(x = None, xp = None, *, s, axes, norm):
    res = xp.fft.irfftn(x, s = s, axes = axes, norm = norm)
    if x.dtype == xp.complex64:
        return res.astype(xp.float32)


def hfft(x = None, xp = None, *, n, axis, norm):
    res = xp.fft.hfft(x, n = n, axis = axis, norm = norm)
    if x.dtype in (xp.float32, xp.complex64):
        return res.astype(xp.float32)


def ihfft(x = None, xp = None, *, n, axis, norm):
    res = xp.fft.ihfft(x, n = n, axis = axis, norm = norm)
    if x.dtype in (xp.float32, xp.complex64):
        return res.astype(xp.complex64)


def fftfreq(n = None, xp = None, *, d, dtype, device):
    if device not in ('cpu', None):
        raise ValueError(f'''Unsupported device {device!r}''')
    res = xp.fft.fftfreq(n, d = d)
# WARNING: Decompyle incomplete


def rfftfreq(n = None, xp = None, *, d, dtype, device):
    if device not in ('cpu', None):
        raise ValueError(f'''Unsupported device {device!r}''')
    res = xp.fft.rfftfreq(n, d = d)
# WARNING: Decompyle incomplete


def fftshift(x = None, xp = None, *, axes):
    return xp.fft.fftshift(x, axes = axes)


def ifftshift(x = None, xp = None, *, axes):
    return xp.fft.ifftshift(x, axes = axes)

__all__ = [
    'fft',
    'ifft',
    'fftn',
    'ifftn',
    'rfft',
    'irfft',
    'rfftn',
    'irfftn',
    'hfft',
    'ihfft',
    'fftfreq',
    'rfftfreq',
    'fftshift',
    'ifftshift']

def __dir__():
    return __all__
