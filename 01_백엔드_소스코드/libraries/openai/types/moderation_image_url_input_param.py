# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: moderation_image_url_input_param.pyc (Python 3.11)

from __future__ import annotations
from typing_extensions import Literal, Required, TypedDict
__all__ = [
    'ModerationImageURLInputParam',
    'ImageURL']

def ImageURL():
    '''ImageURL'''
    url: 'Required[str]' = 'Contains either an image URL or a data URL for a base64 encoded image.'

ImageURL = <NODE:27>(ImageURL, 'ImageURL', TypedDict, total = False)

def ModerationImageURLInputParam():
    '''ModerationImageURLInputParam'''
    type: "Required[Literal['image_url']]" = 'An object describing an image to classify.'

ModerationImageURLInputParam = <NODE:27>(ModerationImageURLInputParam, 'ModerationImageURLInputParam', TypedDict, total = False)
