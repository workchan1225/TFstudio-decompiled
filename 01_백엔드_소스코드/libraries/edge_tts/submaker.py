# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: submaker.pyc (Python 3.11)

'''SubMaker module is used to generate subtitles from WordBoundary and SentenceBoundary events.'''
from datetime import timedelta
from typing import List, Optional
from srt_composer import Subtitle, compose
from typing import TTSChunk

class SubMaker:
    '''
    SubMaker is used to generate subtitles from WordBoundary and SentenceBoundary messages.
    '''
    
    def __init__(self = None):
        self.cues = []
        self.type = None

    
    def feed(self = None, msg = None):
        '''
        Feed a WordBoundary or SentenceBoundary message to the SubMaker object.

        Args:
            msg (dict): The WordBoundary or SentenceBoundary message.

        Returns:
            None
        '''
        if msg['type'] not in ('WordBoundary', 'SentenceBoundary'):
            raise ValueError("Invalid message type, expected 'WordBoundary' or 'SentenceBoundary'.")
    # WARNING: Decompyle incomplete

    
    def get_srt(self = None):
        '''
        Get the SRT formatted subtitles from the SubMaker object.

        Returns:
            str: The SRT formatted subtitles.
        '''
        return compose(self.cues)

    
    def __str__(self = None):
        return self.get_srt()
