# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: provider_factory.pyc (Python 3.11)

'''
AI Provider Factory

Factory pattern for creating AI service instances based on provider name.
Centralizes provider instantiation and makes it easy to add new providers.
'''
from base_ai_service import BaseAIService
import logging
logger = logging.getLogger(__name__)

def get_ai_service(provider = None, api_key = None):
    """
    Create AI service instance using Factory pattern.

    Args:
        provider: Provider identifier ('google')
        api_key: Optional API key. If None, retrieves from Settings.

    Returns:
        BaseAIService implementation (GoogleProvider)

    Raises:
        ValueError: If provider is not supported

    Examples:
        >>> service = get_ai_service('google')
        >>> topics = service.generate_topics('AI 영상 주제', count=3)
    """
    GoogleProvider = GoogleProvider
    import google_provider
    providers = {
        'google': GoogleProvider }
    provider_lower = provider.lower().strip()
    provider_class = providers.get(provider_lower)
    if not provider_class:
        supported = ', '.join(providers.keys())
        raise ValueError(f'''Unsupported AI provider: \'{provider}\'. Supported providers: {supported}''')
    logger.info(f'''Creating {provider_lower} service instance''')
    return provider_class(api_key)


def get_available_providers():
    """
    Get list of available AI providers.

    Returns:
        List of provider names

    Examples:
        >>> providers = get_available_providers()
        >>> print(providers)  # ['google']
    """
    return [
        'google']


def validate_provider(provider = None):
    """
    Check if provider is supported.

    Args:
        provider: Provider name to validate

    Returns:
        True if provider is supported, False otherwise

    Examples:
        >>> validate_provider('google')
        True
        >>> validate_provider('unknown')
        False
    """
    return provider.lower().strip() in get_available_providers()
