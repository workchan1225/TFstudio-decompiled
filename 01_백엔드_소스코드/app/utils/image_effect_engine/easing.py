# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: easing.pyc (Python 3.11)

__doc__ = '\n이징 함수 모듈\n\n부드러운 가속/감속을 위한 이징 함수 모음\nFFmpeg 표현식 제한 없이 Python 함수로 자유롭게 구현\n'
import numpy as np
from typing import Callable

def linear(t = None):
    '''선형 이징 (가속/감속 없음)'''
    return float(np.clip(t, 0, 1))


def smoothstep(t = None):
    '''
    Smoothstep 이징: t*t*(3-2*t)

    기술 리포트에서 권장하는 기본 이징 함수
    자연스러운 가속/감속 제공
    '''
    t = np.clip(t, 0, 1)
    return float(t * t * (3 - 2 * t))


def quintic_smoothstep(t = None):
    '''
    Ken Perlin의 개선된 smoothstep: 6t^5 - 15t^4 + 10t^3

    C2 연속 (가속도까지 부드러움)
    가장 부드러운 전환을 원할 때 사용
    '''
    t = np.clip(t, 0, 1)
    return float(t * t * t * (t * (6 * t - 15) + 10))


def ease_in_quad(t = None):
    '''Quadratic ease-in: t^2 (천천히 시작)'''
    t = np.clip(t, 0, 1)
    return float(t * t)


def ease_out_quad(t = None):
    '''Quadratic ease-out: 1-(1-t)^2 (천천히 끝)'''
    t = np.clip(t, 0, 1)
    return float(1 - (1 - t) * (1 - t))


def ease_in_out_quad(t = None):
    '''Quadratic ease-in-out (양쪽 부드럽게)'''
    t = np.clip(t, 0, 1)
    if t < 0.5:
        return float(2 * t * t)
    return None(1 - pow(-2 * t + 2, 2) / 2)


def ease_in_cubic(t = None):
    '''Cubic ease-in: t^3'''
    t = np.clip(t, 0, 1)
    return float(t * t * t)


def ease_out_cubic(t = None):
    '''Cubic ease-out: 1-(1-t)^3'''
    t = np.clip(t, 0, 1)
    return float(1 - pow(1 - t, 3))


def ease_in_out_cubic(t = None):
    '''Cubic ease-in-out'''
    t = np.clip(t, 0, 1)
    if t < 0.5:
        return float(4 * t * t * t)
    return None(1 - pow(-2 * t + 2, 3) / 2)


def ease_in_sine(t = None):
    '''Sine ease-in: 1 - cos(t * π/2)'''
    t = np.clip(t, 0, 1)
    return float(1 - np.cos(t * np.pi / 2))


def ease_out_sine(t = None):
    '''Sine ease-out: sin(t * π/2)'''
    t = np.clip(t, 0, 1)
    return float(np.sin(t * np.pi / 2))


def ease_in_out_sine(t = None):
    '''Sine ease-in-out: (1 - cos(π*t)) / 2'''
    t = np.clip(t, 0, 1)
    return float((1 - np.cos(np.pi * t)) / 2)


def ease_in_expo(t = None):
    '''Exponential ease-in (급격한 가속)'''
    t = np.clip(t, 0, 1)
    if t == 0:
        return 0
    return None(pow(2, 10 * t - 10))


def ease_out_expo(t = None):
    '''Exponential ease-out (급격한 감속)'''
    t = np.clip(t, 0, 1)
    if t == 1:
        return 1
    return None(1 - pow(2, -10 * t))

# WARNING: Decompyle incomplete
