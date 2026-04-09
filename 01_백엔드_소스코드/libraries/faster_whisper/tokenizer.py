# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: tokenizer.pyc (Python 3.11)

import string
from functools import cached_property
from typing import List, Optional, Tuple
import tokenizers

class Tokenizer:
    '''Simple wrapper around a tokenizers.Tokenizer.'''
    
    def __init__(self = None, tokenizer = None, multilingual = None, task = (None, None), language = ('tokenizer', tokenizers.Tokenizer, 'multilingual', bool, 'task', Optional[str], 'language', Optional[str])):
        self.tokenizer = tokenizer
        if multilingual:
            if task not in _TASKS:
                raise ValueError(f'''\'{task!s}\' is not a valid task (accepted tasks: {', '.join(_TASKS)!s})''')
            if language not in _LANGUAGE_CODES:
                raise ValueError(f'''\'{language!s}\' is not a valid language code (accepted language codes: {', '.join(_LANGUAGE_CODES)!s})''')
            self.task = self.tokenizer.token_to_id('<|%s|>' % task)
            self.language = self.tokenizer.token_to_id('<|%s|>' % language)
            self.language_code = language
            return None
        self.task = None
        self.language = None
        self.language_code = 'en'

    transcribe = (lambda self = None: self.tokenizer.token_to_id('<|transcribe|>'))()
    translate = (lambda self = None: self.tokenizer.token_to_id('<|translate|>'))()
    sot = (lambda self = None: self.tokenizer.token_to_id('<|startoftranscript|>'))()
    sot_lm = (lambda self = None: self.tokenizer.token_to_id('<|startoflm|>'))()
    sot_prev = (lambda self = None: self.tokenizer.token_to_id('<|startofprev|>'))()
    eot = (lambda self = None: self.tokenizer.token_to_id('<|endoftext|>'))()
    no_timestamps = (lambda self = None: self.tokenizer.token_to_id('<|notimestamps|>'))()
    no_speech = (lambda self = None:
