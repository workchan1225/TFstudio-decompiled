# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: script_dtos.pyc (Python 3.11)

'''
Script DTOs (Data Transfer Objects)

대본 생성 관련 API 요청/응답 표준화.
설정 검증 및 조합 경고 시스템 포함.
'''
from dataclasses import dataclass, field
from typing import Optional, List, Dict, Any
from enum import Enum

class ValidationLevel(Enum):
    '''검증 결과 레벨'''
    ERROR = 'error'
    WARNING = 'warning'
    INFO = 'info'

ValidationMessage = <NODE:12>()
CharacterDTO = <NODE:12>()
ScriptChapterDTO = <NODE:12>()
VALID_TONES = [
    '설명체',
    '친근체',
    '소설체',
    '극적체',
    '담담체',
    '유머체',
    '감성체',
    '다큐체',
    '다채로운 문체']
VALID_CONTENT_FORMATS = [
    '',
    'longform',
    'shorts']
VALID_SHORTS_DURATIONS = [
    '1min',
    '2min',
    '3min']
VALID_SPEAKER_TAG_MODES = [
    'with_tags',
    'without_tags']
VALID_CREATIVE_MODES = [
    'strict',
    'balanced',
    'creative']
DRAMA_GENRES = [
    'DRAMATIC',
    'REVENGE',
    'TOUCHING',
    'CONFESSION',
    'MYSTERY',
    'THRILLER',
    'SF_FANTASY',
    'HISTORICAL',
    'HEART_WARMING',
    'JOSEON_FOLKTALE',
    'LIFE_LESSONS',
    'LIFE_CHALLENGE',
    'CONSPIRACY',
    'NATIONAL_PRIDE']
INFO_GENRES = [
    'LIFE_KNOWLEDGE',
    'OFFICE_SURVIVAL',
    'MONEY_SENSE',
    'RELATIONSHIP_EQ',
    'PSYCHOLOGY',
    'LIFE_CHOICES',
    'KNOWLEDGE_BITE']
DOCU_GENRES = [
    'TRUE_STORY',
    'DOCUMENTARY',
    'NEWS_REPORT',
    'REVIEW_ANALYSIS',
    'VARIETY',
    'HYBRID']
GenerateScriptRequestDTO = <NODE:12>()
GenerateScriptResponseDTO = <NODE:12>()
ExpandScriptRequestDTO = <NODE:12>()
ValidateScriptRequestDTO = <NODE:12>()
ToneConsistencyResult = <NODE:12>()
RatioAnalysisResult = <NODE:12>()
ValidateScriptResponseDTO = <NODE:12>()
