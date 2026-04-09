# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: prompting.pyc (Python 3.11)

'''
Prompt section assembly helpers for Script Generation V2.
'''
from __future__ import annotations
from dataclasses import dataclass
from typing import List, Tuple
from app.services.ai.response_parser import TextCleaner
PromptSection = <NODE:12>()

class PromptSpec:
    
    def __init__(self = None, sections = None, max_prompt_chars = None):
        self.sections = sections
        self.max_prompt_chars = max_prompt_chars
        self._cleaner = TextCleaner()

    
    def render(self = None):
        included = []
        rendered_parts = []
        clamped = []
        current_length = 0
        for section in sorted(self.sections, key = (lambda item: item.priority), reverse = True):
            if not section.content:
                content = ''.strip()
                if not content:
                    continue
            if section.max_chars and len(content) > section.max_chars:
                content = self._cleaner.truncate_safely(content, section.max_chars)
                clamped.append(section.name)
            separator = '\n\n' if rendered_parts else ''
            projected = current_length + len(separator) + len(content)
            if projected > self.max_prompt_chars:
                remaining = self.max_prompt_chars - current_length - len(separator)
                if not remaining <= 120 and section.required:
                    clamped.append(section.name)
                    continue
                if remaining > 120:
                    content = self._cleaner.truncate_safely(content, remaining)
                    clamped.append(section.name)
                
            else:
                rendered_parts.append(content)
                included.append(section.name)
                current_length = len('\n\n'.join(rendered_parts))
            return ('\n\n'.join(rendered_parts), included, clamped)
