# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: computer_screenshot_content.pyc (Python 3.11)

from typing import Optional
from typing_extensions import Literal
from _models import BaseModel
__all__ = [
    'ComputerScreenshotContent']

class ComputerScreenshotContent(BaseModel):
    '''A screenshot of a computer.'''
    file_id: Optional[str] = None
    type: Literal['computer_screenshot'] = None
