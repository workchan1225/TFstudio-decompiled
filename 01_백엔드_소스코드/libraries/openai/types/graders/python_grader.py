# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: python_grader.pyc (Python 3.11)

from typing import Optional
from typing_extensions import Literal
from _models import BaseModel
__all__ = [
    'PythonGrader']

class PythonGrader(BaseModel):
    type: Literal['python'] = 'A PythonGrader object that runs a python script on the input.'
    image_tag: Optional[str] = None
