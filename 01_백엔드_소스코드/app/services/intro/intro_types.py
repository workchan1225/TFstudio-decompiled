# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: intro_types.pyc (Python 3.11)

'''
Intro Types - 인트로/후킹 타입 정의
'''
from dataclasses import dataclass, field
from typing import Optional, List
from enum import Enum

class IntroType(Enum, str):
    HIGHLIGHT_QUESTION = 'highlight_question'
    HIGHLIGHT_TEASER = 'highlight_teaser'
    HOOK_TEXT_ONLY = 'hook_text_only'
    CUSTOM = 'custom'


class IntroEffect(Enum, str):
    FAST_ZOOM = 'fast_zoom'
    GLITCH = 'glitch'
    FLASH_CUT = 'flash_cut'
    FADE_DRAMATIC = 'fade_dramatic'
    NONE = 'none'

HighlightResult = <NODE:12>()
IntroImage = <NODE:12>()
IntroData = <NODE:12>()
IntroTTSSettings = <NODE:12>()
