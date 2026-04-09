# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: __init__.pyc (Python 3.11)

'''
AI Service Module

Provides unified interface for different AI providers (OpenAI, Claude, Google Gemini).
Uses Strategy pattern with Factory for provider instantiation.
'''
from base_ai_service import BaseAIService
from provider_factory import get_ai_service
__all__ = [
    'BaseAIService',
    'get_ai_service']
