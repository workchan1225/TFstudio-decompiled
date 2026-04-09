# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: __init__.pyc (Python 3.11)

'''
Domain Interfaces (Ports)

Abstract interfaces that define contracts for external dependencies.
These interfaces follow the Dependency Inversion Principle (DIP).

The domain layer defines these interfaces, and the infrastructure layer implements them.
'''
from abc import ABC, abstractmethod
from typing import Optional, List
from app.domain.entities import Project, Character, Media

class IProjectRepository(ABC):
    '''
    Repository interface for Project entity.

    This interface defines the contract for project persistence operations.
    The actual implementation will be in the infrastructure layer.
    '''
    get_by_id = (lambda self = None, project_id = None: pass)()
    get_all = (lambda self = None: pass)()
    save = (lambda self = None, project = None, commit = abstractmethod: pass)()
    delete = (lambda self = None, project_id = None: pass)()
    exists = (lambda self = None, project_id = None: pass)()
    exists_by_title = (lambda self = None, title = None: pass)()


class IMediaRepository(ABC):
    '''
    Repository interface for Media entity.
    '''
    get_by_id = (lambda self = None, media_id = None: pass)()
    get_by_project_id = (lambda self = None, project_id = None: pass)()
    get_all = (lambda self = None: pass)()
    save = (lambda self = None, media = None: pass)()
    delete = (lambda self = None, media_id = None: pass)()


class IAIService(ABC):
    '''
    Interface for AI content generation services.
    '''
    generate_topic = (lambda self = None, prompt = None: pass)()
    generate_outline = (lambda self = None, topic = None: pass)()
    generate_script = (lambda self = None, outline = None: pass)()


class ITTSService(ABC):
    '''
    Interface for Text-to-Speech services.
    '''
    generate_audio = (lambda self = None, text = None, voice_id = abstractmethod: pass)()
    get_available_voices = (lambda self = None: pass)()


class IVideoService(ABC):
    '''
    Interface for video generation services.
    '''
    generate_video = (lambda self = None, project_id = None: pass)()
    get_video_status = (lambda self = None, project_id = None: pass)()
