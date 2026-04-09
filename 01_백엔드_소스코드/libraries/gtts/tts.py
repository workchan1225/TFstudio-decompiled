# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: tts.pyc (Python 3.11)

import base64
import json
import logging
import re
import urllib
import requests
from gtts.lang import _fallback_deprecated_lang, tts_langs
from gtts.tokenizer import Tokenizer, pre_processors, tokenizer_cases
from gtts.utils import _clean_tokens, _minimize, _translate_url
__all__ = [
    'gTTS',
    'gTTSError']
log = logging.getLogger(__name__)
log.addHandler(logging.NullHandler())

class Speed:
    '''Read Speed

    The Google TTS Translate API supports two speeds:
        Slow: True
        Normal: None
    '''
    SLOW = True
    NORMAL = None


class gTTS:
    """gTTS -- Google Text-to-Speech.

    An interface to Google Translate's Text-to-Speech API.

    Args:
        text (string): The text to be read.
        tld (string): Top-level domain for the Google Translate host,
            i.e `https://translate.google.<tld>`. Different Google domains
            can produce different localized 'accents' for a given
            language. This is also useful when ``google.com`` might be blocked
            within a network but a local or different Google host
            (e.g. ``google.com.hk``) is not. Default is ``com``.
        lang (string, optional): The language (IETF language tag) to
            read the text in. Default is ``en``.
        slow (bool, optional): Reads text more slowly. Defaults to ``False``.
        lang_check (bool, optional): Strictly enforce an existing ``lang``,
            to catch a language error early. If set to ``True``,
            a ``ValueError`` is raised if ``lang`` doesn't exist.
            Setting ``lang_check`` to ``False`` skips Web requests
            (to validate language) and therefore speeds up instantiation.
            Default is ``True``.
        pre_processor_funcs (list): A list of zero or more functions that are
            called to transform (pre-process) text before tokenizing. Those
            functions must take a string and return a string. Defaults to::

                [
                    pre_processors.tone_marks,
                    pre_processors.end_of_line,
                    pre_processors.abbreviations,
                    pre_processors.word_sub
                ]

        tokenizer_func (callable): A function that takes in a string and
            returns a list of string (tokens). Defaults to::

                Tokenizer([
                    tokenizer_cases.tone_marks,
                    tokenizer_cases.period_comma,
                    tokenizer_cases.colon,
                    tokenizer_cases.other_punctuation
                ]).run

        timeout (float or tuple, optional): Seconds to wait for the server to
            send data before giving up, as a float, or a ``(connect timeout,
            read timeout)`` tuple. ``None`` will wait forever (default).

    See Also:
        :doc:`Pre-processing and tokenizing <tokenizer>`

    Raises:
        AssertionError: When ``text`` is ``None`` or empty; when there's nothing
            left to speak after pre-processing, tokenizing and cleaning.
        ValueError: When ``lang_check`` is ``True`` and ``lang`` is not supported.
        RuntimeError: When ``lang_check`` is ``True`` but there's an error loading
            the languages dictionary.

    """
    GOOGLE_TTS_MAX_CHARS = 100
    GOOGLE_TTS_HEADERS = {
        'Referer': 'http://translate.google.com/',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.106 Safari/537.36',
        'Content-Type': 'application/x-www-form-urlencoded;charset=utf-8' }
    GOOGLE_TTS_RPC = 'jQ1olc'
    
    def __init__(self, text, tld, lang, slow, lang_check, pre_processor_funcs, tokenizer_func, timeout = ('com', 'en', False, True, [
        pre_processors.tone_marks,
        pre_processors.end_of_line,
        pre_processors.abbreviations,
        pre_processors.word_sub], Tokenizer([
        tokenizer_cases.tone_marks,
        tokenizer_cases.period_comma,
        tokenizer_cases.colon,
        tokenizer_cases.other_punctuation]).run, None)):
        pass
    # WARNING: Decompyle incomplete

    
    def _tokenize(self, text):
        text = text.strip()
        for pp in self.pre_processor_funcs:
            log.debug('pre-processing: %s', pp)
            text = pp(text)
            if len(text) <= self.GOOGLE_TTS_MAX_CHARS:
                return _clean_tokens([
                    text])
            None.debug('tokenizing: %s', self.tokenizer_func)
            tokens = self.tokenizer_func(text)
            tokens = _clean_tokens(tokens)
            min_tokens = []
            for t in tokens:
                min_tokens += _minimize(t, ' ', self.GOOGLE_TTS_MAX_CHARS)
                tokens = min_tokens()
                return tokens

    
    def _prepare_requests(self):
        '''Created the TTS API the request(s) without sending them.

        Returns:
            list: ``requests.PreparedRequests_``. <https://2.python-requests.org/en/master/api/#requests.PreparedRequest>`_``.
        '''
        translate_url = _translate_url(tld = self.tld, path = '_/TranslateWebserverUi/data/batchexecute')
        text_parts = self._tokenize(self.text)
        log.debug('text_parts: %s', str(text_parts))
        log.debug('text_parts: %i', len(text_parts))
    # WARNING: Decompyle incomplete

    
    def _package_rpc(self, text):
        parameter = [
            text,
            self.lang,
            self.speed,
            'null']
        escaped_parameter = json.dumps(parameter, separators = (',', ':'))
        rpc = [
            [
                [
                    self.GOOGLE_TTS_RPC,
                    escaped_parameter,
                    None,
                    'generic']]]
        espaced_rpc = json.dumps(rpc, separators = (',', ':'))
        return 'f.req={}&'.format(urllib.parse.quote(espaced_rpc))

    
    def get_bodies(self):
        '''Get TTS API request bodies(s) that would be sent to the TTS API.

        Returns:
            list: A list of TTS API request bodies to make.
        '''
        return self._prepare_requests()()

    
    def stream(self):
        """Do the TTS API request(s) and stream bytes

        Raises:
            :class:`gTTSError`: When there's an error with the API request.

        """
        pass
    # WARNING: Decompyle incomplete

    
    def write_to_fp(self, fp):
        """Do the TTS API request(s) and write bytes to a file-like object.

        Args:
            fp (file object): Any file-like object to write the ``mp3`` to.

        Raises:
            :class:`gTTSError`: When there's an error with the API request.
            TypeError: When ``fp`` is not a file-like object that takes bytes.

        """
        
        try:
            for idx, decoded in enumerate(self.stream()):
                fp.write(decoded)
                log.debug('part-%i written to %s', idx, fp)
                return None
                except (AttributeError, TypeError):
                    e = None
                    raise TypeError("'fp' is not a file-like object or it does not take bytes: %s" % str(e))
                    e = None
                    del e


    
    def save(self, savefile):
        """Do the TTS API request and write result to file.

        Args:
            savefile (string): The path and file name to save the ``mp3`` to.

        Raises:
            :class:`gTTSError`: When there's an error with the API request.

        """
        f = open(str(savefile), 'wb')
        self.write_to_fp(f)
        f.flush()
        log.debug('Saved to %s', savefile)
        None(None, None)
        return None
        with None:
            if not None:
                pass



class gTTSError(Exception):
    pass
# WARNING: Decompyle incomplete
