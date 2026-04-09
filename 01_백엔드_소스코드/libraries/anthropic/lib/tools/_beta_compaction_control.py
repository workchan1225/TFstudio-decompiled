# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: _beta_compaction_control.pyc (Python 3.11)

from typing import TypedDict
from typing_extensions import Required
DEFAULT_SUMMARY_PROMPT = "You have been working on the task described above but have not yet completed it. Write a continuation summary that will allow you (or another instance of yourself) to resume work efficiently in a future context window where the conversation history will be replaced with this summary. Your summary should be structured, concise, and actionable. Include:\n1. Task Overview\nThe user's core request and success criteria\nAny clarifications or constraints they specified\n2. Current State\nWhat has been completed so far\nFiles created, modified, or analyzed (with paths if relevant)\nKey outputs or artifacts produced\n3. Important Discoveries\nTechnical constraints or requirements uncovered\nDecisions made and their rationale\nErrors encountered and how they were resolved\nWhat approaches were tried that didn't work (and why)\n4. Next Steps\nSpecific actions needed to complete the task\nAny blockers or open questions to resolve\nPriority order if multiple steps remain\n5. Context to Preserve\nUser preferences or style requirements\nDomain-specific details that aren't obvious\nAny promises made to the user\nBe concise but complete—err on the side of including information that would prevent duplicate work or repeated mistakes. Write in a way that enables immediate resumption of the task.\nWrap your summary in <summary></summary> tags."
DEFAULT_THRESHOLD = 100000

def CompactionControl():
    '''CompactionControl'''
    enabled: Required[bool] = 'CompactionControl'

CompactionControl = <NODE:27>(CompactionControl, 'CompactionControl', TypedDict, total = False)
