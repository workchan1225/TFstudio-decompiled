# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: translation_create_response.pyc (Python 3.11)

from typing import Union
from typing_extensions import TypeAlias
from translation import Translation
from translation_verbose import TranslationVerbose
__all__ = [
    'TranslationCreateResponse']
TranslationCreateResponse: TypeAlias = Union[(Translation, TranslationVerbose)]
