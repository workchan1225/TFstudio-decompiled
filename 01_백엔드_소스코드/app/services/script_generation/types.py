# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: types.pyc (Python 3.11)

'''
Script Generation Types

대본 생성 관련 타입 정의
'''
from dataclasses import dataclass, field
from typing import List, Dict, Optional, Any
from enum import Enum

class ContentFormat(Enum, str):
    '''콘텐츠 포맷'''
    LONGFORM = 'longform'
    SHORTS = 'shorts'
    REFERENCE = 'reference'


class PatternIntensity(Enum, str):
    '''패턴 적용 강도'''
    STRICT = 'strict'
    MODERATE = 'moderate'
    LOOSE = 'loose'


class ShortsDuration(Enum, str):
    '''쇼츠 길이'''
    ONE_MIN = '1min'
    TWO_MIN = '2min'
    THREE_MIN = '3min'

TitleConfig = <NODE:12>()
GeneratedTitle = <NODE:12>()
SynopsisConfig = <NODE:12>()
GeneratedSynopsis = <NODE:12>()
ScriptConfig = <NODE:12>()
ScriptChapter = <NODE:12>()
GeneratedScript = <NODE:12>()
TranscriptSegment = <NODE:12>()
VideoInfo = <NODE:12>()
StructuralSection = <NODE:12>()
StructuralPattern = <NODE:12>()
TensionPoint = <NODE:12>()
EmotionalBeat = <NODE:12>()
RetentionHook = <NODE:12>()
PsychologicalPattern = <NODE:12>()
NarrativeSection = <NODE:12>()
NarrativeStructure = <NODE:12>()
KeyPoint = <NODE:12>()
DetectedTone = <NODE:12>()
RetentionAnalysis = <NODE:12>()
HookTimingAnalysis = <NODE:12>()
ContentCategory = <NODE:12>()
TitleOptimization = <NODE:12>()
PaceAnalysis = <NODE:12>()
YouTubeReferenceAnalysis = <NODE:12>()
ExtractTranscriptResult = <NODE:12>()
AnalyzePatternResult = <NODE:12>()
