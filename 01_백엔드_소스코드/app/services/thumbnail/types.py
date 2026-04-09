# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: types.pyc (Python 3.11)

'''
Thumbnail Pipeline Types
5단계 파이프라인에서 사용하는 공통 타입 정의
'''
from dataclasses import dataclass, field
from typing import Dict, List, Optional, Any, Literal
from enum import Enum

class PipelineStep(Enum, str):
    '''파이프라인 단계'''
    ANALYZE = 'analyze'
    INPUT = 'input'
    PROMPT = 'prompt'
    OPTIMIZE = 'optimize'
    GENERATE = 'generate'

TextPosition = <NODE:12>()
FontProperties = <NODE:12>()
ColorInfo = <NODE:12>()
TextEffects = <NODE:12>()
TextAlignment = <NODE:12>()
TextElement = <NODE:12>()
StyleAnalysis = <NODE:12>()
ColorPalette = <NODE:12>()
LayoutInfo = <NODE:12>()
ImageDimensions = <NODE:12>()
LayoutAnalysisDetail = <NODE:12>()
VisualGrammar = <NODE:12>()
MidjourneyParams = <NODE:12>()
NegativeSpace = <NODE:12>()
TextStyleGuide = <NODE:12>()
ReferenceAnalysisResult = <NODE:12>()
SubjectImage = <NODE:12>()
FloatingText = <NODE:12>()
AdditionalText = <NODE:12>()
StylePreferences = <NODE:12>()
UserContentInput = <NODE:12>()
PromptElements = <NODE:12>()
GeneratedPrompt = <NODE:12>()
OptimizationAnalysis = <NODE:12>()
OptimizationIteration = <NODE:12>()
OptimizationResult = <NODE:12>()
QualityMetrics = <NODE:12>()
ThumbnailAnalysis = <NODE:12>()
GeneratedThumbnail = <NODE:12>()
GenerationResult = <NODE:12>()
PipelineProgress = <NODE:12>()
PipelineResult = <NODE:12>()

def to_dict(obj = dataclass):
    '''데이터클래스를 딕셔너리로 변환'''
    pass
# WARNING: Decompyle incomplete


def from_dict(data = dataclass, cls = dataclass):
    '''딕셔너리를 데이터클래스로 변환'''
    if not hasattr(cls, '__dataclass_fields__'):
        return data
    field_values = None
# WARNING: Decompyle incomplete
