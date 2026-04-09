# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: __init__.pyc (Python 3.11)

"""A collection of models which don't fit in the generic classes :class:`ctranslate2.Translator`
and :class:`ctranslate2.Generator`.
"""

try:
    from ctranslate2._ext import Wav2Vec2, Wav2Vec2Bert, Whisper, WhisperGenerationResult, WhisperGenerationResultAsync
    return None
except ImportError:
    e = None
    if 'No module named' in str(e):
        pass
    else:
        raise 
    e = None
    del e
    return None
    e = None
    del e
