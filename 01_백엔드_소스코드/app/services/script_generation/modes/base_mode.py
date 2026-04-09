# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: base_mode.pyc (Python 3.11)

'''
Base Mode Abstract Class

모든 생성 모드의 추상 기본 클래스
'''
from abc import ABC, abstractmethod
from typing import List, Any
from types import TitleConfig, GeneratedTitle, SynopsisConfig, GeneratedSynopsis, ScriptConfig, GeneratedScript

class BaseMode(ABC):
    '''
    생성 모드 추상 기본 클래스

    모든 생성 모드(StandardMode, ReferenceMode 등)가 구현해야 하는
    인터페이스를 정의합니다.
    '''
    
    def __init__(self = None, genai = None, model = None):
        '''
        Args:
            genai: Google Generative AI 인스턴스
            model: Gemini 모델 인스턴스
        '''
        self.genai = genai
        self.model = model

    generate_titles = (lambda self = None, config = None: pass)()
    generate_synopses = (lambda self = None, config = None: pass)()
    generate_script = (lambda self = None, config = None: pass)()
    
    def get_mode_name(self = None):
        '''모드 이름 반환'''
        return self.__class__.__name__
