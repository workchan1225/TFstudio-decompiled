# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: base_ai_service.pyc (Python 3.11)

'''
Base AI Service - Abstract base class for all AI providers

Provides common interface and shared logic for OpenAI, Claude, and Google Gemini services.
'''
from abc import ABC, abstractmethod
from app.models.settings import Settings
import logging
from app.services.google_auth_service import get_google_api_key_or_runtime_token
logger = logging.getLogger(__name__)

class BaseAIService(ABC):
    """
    Abstract base class for AI service providers.

    Implements common functionality:
    - API key management from Settings
    - API key validation
    - Provider name abstraction

    Subclasses must implement:
    - _get_provider_name(): Return provider identifier ('openai', 'claude', 'google')
    - All abstract generation methods
    """
    
    def __init__(self = None, api_key = None):
        '''
        Initialize AI service with API key.

        Args:
            api_key: API key string. If None, retrieves from Settings based on provider name.

        Raises:
            ValueError: If API key not found in Settings or invalid
        '''
        pass
    # WARNING: Decompyle incomplete

    _get_provider_name = (lambda self = None: pass)()
    
    def _get_api_key_from_settings(self = None):
        '''
        Retrieve API key from Settings database.

        This centralizes API key management - all keys are stored in Settings model,
        not environment variables.

        Returns:
            API key string

        Raises:
            ValueError: If API key not found in Settings
        '''
        settings = Settings.get_or_create()
        provider = self._get_provider_name()
        if provider == 'google':
            api_key = get_google_api_key_or_runtime_token(settings = settings)
        else:
            api_key = settings.get_api_key(provider)
        if not api_key:
            raise ValueError('Google 인증 설정이 필요합니다. 설정 페이지에서 API Key 또는 Vertex AI를 구성해주세요.' if provider == 'google' else f'''{provider} API key not found in Settings. Please configure API key in Settings page.''')
        logger.debug(f'''Retrieved API key for {provider} from Settings''')
        return api_key

    
    def _validate_api_key(self):
        '''
        Validate API key exists and is non-empty.

        Raises:
            ValueError: If API key is missing or empty
        '''
        if not self.api_key:
            raise ValueError(f'''API key required for {self._get_provider_name()}''')
        if not isinstance(self.api_key, str) or self.api_key.strip():
            raise ValueError(f'''Invalid API key format for {self._get_provider_name()}''')

    generate_topics = (lambda self = None, prompt = None, count = abstractmethod: pass)()
    generate_outline = (lambda self = None, topic = None: pass)()
    generate_script = (lambda self = None, outline = None, duration_minutes = abstractmethod: pass)()
    generate_titles = (lambda self, topic, genre, language = None, tone = None, count = abstractmethod, content_type = (10, None, None), subgenre = ('topic', str, 'genre', str, 'language', str, 'tone', str, 'count', int, 'content_type', str, 'subgenre', str, 'return', list[dict]): pass)()
    generate_synopses = (lambda self, title, genre, language = None, tone = None, count = abstractmethod, content_type = (5, None, None), subgenre = ('title', str, 'genre', str, 'language', str, 'tone', str, 'count', int, 'content_type', str, 'subgenre', str, 'return', list[str]): pass)()
    expand_script = (lambda self, script = None, language = None, target_multiplier = abstractmethod, focus_areas = ('script', str, 'language', str, 'target_multiplier', float, 'focus_areas', list[str], 'return', str): pass)()
    
    def generate_image(self = None, prompt = None, **kwargs):
        """
        Generate image from prompt (if provider supports it).

        Args:
            prompt: Image generation prompt
            **kwargs: Provider-specific parameters (size, quality, etc.)

        Returns:
            Image URL or path

        Raises:
            NotImplementedError: If provider doesn't support image generation
        """
        raise NotImplementedError(f'''{self._get_provider_name()} does not support image generation''')

    
    def generate_youtube_metadata(self = None, script = None, **kwargs):
        """
        Generate YouTube metadata (title, description, tags, thumbnail text).

        Args:
            script: Video script
            **kwargs: Provider-specific parameters

        Returns:
            Dict with 'titles', 'description', 'tags', 'thumbnailText' keys

        Raises:
            NotImplementedError: If provider doesn't support metadata generation
        """
        raise NotImplementedError(f'''{self._get_provider_name()} does not support YouTube metadata generation''')

    
    def expand_script_from_synopsis(self, synopsis, current_script = None, language = None, target_length = None, focus_areas = ('synopsis', str, 'current_script', str, 'language', str, 'target_length', int, 'focus_areas', list[str], 'return', str), **kwargs):
        """
        Expand script from synopsis (provider-specific advanced feature).

        Args:
            synopsis: Story synopsis
            current_script: Current script for reference
            language: Language
            target_length: Target character count
            focus_areas: Areas to focus on
            **kwargs: Provider-specific parameters

        Returns:
            Expanded script text

        Raises:
            NotImplementedError: If provider doesn't support this feature
        """
        raise NotImplementedError(f'''{self._get_provider_name()} does not support synopsis-based script expansion''')
