# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: reasoning.pyc (Python 3.11)

from typing import Optional
from typing_extensions import Literal
from _models import BaseModel
from reasoning_effort import ReasoningEffort
__all__ = [
    'Reasoning']

class Reasoning(BaseModel):
    '''**gpt-5 and o-series models only**

    Configuration options for
    [reasoning models](https://platform.openai.com/docs/guides/reasoning).
    '''
    effort: Optional[ReasoningEffort] = None
    generate_summary: Optional[Literal[('auto', 'concise', 'detailed')]] = None
    summary: Optional[Literal[('auto', 'concise', 'detailed')]] = None
