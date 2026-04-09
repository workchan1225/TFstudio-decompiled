# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: __init__.pyc (Python 3.11)

'''
Domain Entities

Core business entities that have identity and lifecycle.
These are framework-agnostic and contain business logic.
'''
from dataclasses import dataclass, field
from datetime import datetime
from typing import Optional, Dict, Any, List
from app.domain.enums import ProjectType, ProjectStatus, TTSMethod, MediaType, YouTubeUploadStatus
from app.domain.value_objects import AudioUrl, VideoSettings, DependencyMetadata, SubtitleLayer, BGMTrack
from app.domain.exceptions import ValidationError, InvalidStateTransitionError
Character = <NODE:12>()
Media = <NODE:12>()
Project = <NODE:12>()
