# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: message.pyc (Python 3.11)

from typing import List, Union
from typing_extensions import Literal, Annotated, TypeAlias
from _utils import PropertyInfo
from _models import BaseModel
from text_content import TextContent
from summary_text_content import SummaryTextContent
from computer_screenshot_content import ComputerScreenshotContent
from responses.response_input_file import ResponseInputFile
from responses.response_input_text import ResponseInputText
from responses.response_input_image import ResponseInputImage
from responses.response_output_text import ResponseOutputText
from responses.response_output_refusal import ResponseOutputRefusal
__all__ = [
    'Message',
    'Content',
    'ContentReasoningText']

class ContentReasoningText(BaseModel):
    type: Literal['reasoning_text'] = 'Reasoning text from the model.'

Content: TypeAlias = Annotated[(Union[(ResponseInputText, ResponseOutputText, TextContent, SummaryTextContent, ContentReasoningText, ResponseOutputRefusal, ResponseInputImage, ComputerScreenshotContent, ResponseInputFile)], PropertyInfo(discriminator = 'type'))]

class Message(BaseModel):
    type: Literal['message'] = 'A message to or from the model.'
