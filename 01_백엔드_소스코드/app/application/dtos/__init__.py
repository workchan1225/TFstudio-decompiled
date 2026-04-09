# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: __init__.pyc (Python 3.11)

'''
Application DTOs (Data Transfer Objects)

DTOs for transferring data between layers.
These are used for use case inputs (Requests) and outputs (Responses).
'''
from dataclasses import dataclass, field
from typing import Optional, List, Dict, Any
from datetime import datetime
from script_dtos import ValidationLevel, ValidationMessage, CharacterDTO, ScriptChapterDTO, GenerateScriptRequestDTO, GenerateScriptResponseDTO, ExpandScriptRequestDTO, ValidateScriptRequestDTO, ValidateScriptResponseDTO, ToneConsistencyResult, RatioAnalysisResult, VALID_TONES, VALID_CONTENT_FORMATS, VALID_SPEAKER_TAG_MODES, VALID_CREATIVE_MODES, DRAMA_GENRES, INFO_GENRES, DOCU_GENRES
CreateProjectRequest = <NODE:12>()
GetProjectRequest = <NODE:12>()
UpdateProjectRequest = <NODE:12>()
DeleteProjectRequest = <NODE:12>()
SetTopicRequest = <NODE:12>()
SetScriptRequest = <NODE:12>()
ProjectResponse = <NODE:12>()
ProjectListResponse = <NODE:12>()
DeleteProjectResponse = <NODE:12>()
GenerateTopicRequest = <NODE:12>()
GenerateTopicResponse = <NODE:12>()
GenerateOutlineRequest = <NODE:12>()
GenerateOutlineResponse = <NODE:12>()
GenerateScriptRequest = <NODE:12>()
GenerateScriptResponse = <NODE:12>()
