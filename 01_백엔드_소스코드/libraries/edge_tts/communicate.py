# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: communicate.pyc (Python 3.11)

'''Communicate with the service. Only the Communicate class should be used by
end-users. The other classes and functions are for internal use only.'''
import asyncio
import concurrent.futures as concurrent
import json
import ssl
import time
import uuid
from contextlib import nullcontext
from io import TextIOWrapper
from queue import Queue
from typing import AsyncGenerator, ContextManager, Dict, Generator, List, Optional, Tuple, Union
from xml.sax.saxutils import escape, unescape
import aiohttp
import certifi
from typing_extensions import Literal
from constants import DEFAULT_VOICE, SEC_MS_GEC_VERSION, WSS_HEADERS, WSS_URL
from data_classes import TTSConfig
from drm import DRM
from exceptions import NoAudioReceived, UnexpectedResponse, UnknownResponse, WebSocketError
from typing import CommunicateState, TTSChunk

def get_headers_and_data(data = None, header_length = None):
    '''
    Returns the headers and data from the given data.

    Args:
        data (bytes): The data to be parsed.
        header_length (int): The length of the header.

    Returns:
        tuple: The headers and data to be used in the request.
    '''
    if not isinstance(data, bytes):
        raise TypeError('data must be bytes')
    headers = { }
    for line in data[:header_length].split(b'\r\n'):
        (key, value) = line.split(b':', 1)
        headers[key] = value
        return (headers, data[header_length + 2:])


def remove_incompatible_characters(string = None):
    '''
    The service does not support a couple character ranges.
    Most important being the vertical tab character which is
    commonly present in OCR-ed PDFs. Not doing this will
    result in an error from the service.

    Args:
        string (str or bytes): The string to be cleaned.

    Returns:
        str: The cleaned string.
    '''
    if isinstance(string, bytes):
        string = string.decode('utf-8')
    if not isinstance(string, str):
        raise TypeError('string must be str or bytes')
    chars = list(string)
    for idx, char in enumerate(chars):
        code = ord(char)
        if not  <= 0, code or 0, code <= 8:
            pass
        
        if not  <= 11, code or 11, code <= 12:
            pass
        
        if  <= 14, code or 14, code <= 31:
            pass
        
        return ''.join(chars)


def connect_id():
    '''
    Returns a UUID without dashes.

    Returns:
        str: A UUID without dashes.
    '''
    return uuid.uuid4().hex


def _find_last_newline_or_space_within_limit(text = None, limit = None):
    '''
    Finds the index of the rightmost preferred split character (newline or space)
    within the initial `limit` bytes of the text.

    This helps find a natural word or sentence boundary for splitting, prioritizing
    newlines over spaces.

    Args:
        text (bytes): The byte string to search within.
        limit (int): The maximum index (exclusive) to search up to.

    Returns:
        int: The index of the last found newline or space within the limit,
             or -1 if neither is found in that range.
    '''
    split_at = text.rfind(b'\n', 0, limit)
    if split_at < 0:
        split_at = text.rfind(b' ', 0, limit)
    return split_at


def _find_safe_utf8_split_point(text_segment = None):
    '''
    Finds the rightmost possible byte index such that the
    segment `text_segment[:index]` is a valid UTF-8 sequence.

    This prevents splitting in the middle of a multi-byte UTF-8 character.

    Args:
        text_segment (bytes): The byte segment being considered for splitting.

    Returns:
        int: The index of the safe split point. Returns 0 if no valid split
             point is found (e.g., if the first byte is part of a multi-byte
             sequence longer than the limit allows).
    '''
    split_at = len(text_segment)
# WARNING: Decompyle incomplete


def _adjust_split_point_for_xml_entity(text = None, split_at = None):
    '''
    Adjusts a proposed split point backward to prevent splitting inside an XML entity.

    For example, if `text` is `b"this &amp; that"` and `split_at` falls between
    `&` and `;`, this function moves `split_at` to the index before `&`.

    Args:
        text (bytes): The text segment being considered.
        split_at (int): The proposed split point index, determined by whitespace
                        or UTF-8 safety.

    Returns:
        int: The adjusted split point index. It will be moved to the \'&\'
             if an unterminated entity is detected right before the original `split_at`.
             Otherwise, the original `split_at` is returned.
    '''
    pass
# WARNING: Decompyle incomplete


def split_text_by_byte_length(text = None, byte_length = None):
    """
    Splits text into chunks, each not exceeding a maximum byte length.

    This function prioritizes splitting at natural boundaries (newlines, spaces)
    while ensuring that:
    1. No chunk exceeds `byte_length` bytes.
    2. Chunks do not end with an incomplete UTF-8 multi-byte character.
    3. Chunks do not split XML entities (like `&amp;`) in the middle.

    Args:
        text (str or bytes): The input text. If str, it's encoded to UTF-8.
        byte_length (int): The maximum allowed byte length for any yielded chunk.
                           Must be positive.

    Yields:
        bytes: Text chunks (UTF-8 encoded, stripped of leading/trailing whitespace)
               that conform to the byte length and integrity constraints.

    Raises:
        TypeError: If `text` is not str or bytes.
        ValueError: If `byte_length` is not positive, or if a split point
                    cannot be determined (e.g., due to extremely small byte_length
                    relative to character/entity sizes).
    """
    pass
# WARNING: Decompyle incomplete


def mkssml(tc = None, escaped_text = None):
    '''
    Creates a SSML string from the given parameters.

    Args:
        tc (TTSConfig): The TTS configuration.
        escaped_text (str or bytes): The escaped text. If bytes, it must be UTF-8 encoded.

    Returns:
        str: The SSML string.
    '''
    if isinstance(escaped_text, bytes):
        escaped_text = escaped_text.decode('utf-8')
    return f'''<speak version=\'1.0\' xmlns=\'http://www.w3.org/2001/10/synthesis\' xml:lang=\'en-US\'><voice name=\'{tc.voice}\'><prosody pitch=\'{tc.pitch}\' rate=\'{tc.rate}\' volume=\'{tc.volume}\'>{escaped_text}</prosody></voice></speak>'''


def date_to_string():
    '''
    Return Javascript-style date string.

    Returns:
        str: Javascript-style date string.
    '''
    return time.strftime('%a %b %d %Y %H:%M:%S GMT+0000 (Coordinated Universal Time)', time.gmtime())


def ssml_headers_plus_data(request_id = None, timestamp = None, ssml = None):
    '''
    Returns the headers and data to be used in the request.

    Returns:
        str: The headers and data to be used in the request.
    '''
    return f'''X-RequestId:{request_id}\r\nContent-Type:application/ssml+xml\r\nX-Timestamp:{timestamp}Z\r\nPath:ssml\r\n\r\n{ssml}'''


class Communicate:
    '''
    Communicate with the service.
    '''
    
    def __init__(self = None, text = None, voice = None, *, rate, volume, pitch, boundary, connector, proxy, connect_timeout, receive_timeout):
        self.tts_config = TTSConfig(voice, rate, volume, pitch, boundary)
        if not isinstance(text, str):
            raise TypeError('text must be str')
        self.texts = split_text_by_byte_length(escape(remove_incompatible_characters(text)), 4096)
    # WARNING: Decompyle incomplete

    
    def __parse_metadata(self = None, data = None):
        for meta_obj in json.loads(data)['Metadata']:
            meta_type = meta_obj['Type']
            if meta_type in ('WordBoundary', 'SentenceBoundary'):
                current_offset = meta_obj['Data']['Offset'] + self.state['offset_compensation']
                current_duration = meta_obj['Data']['Duration']
                
                return None, {
                    'type': meta_type,
                    'offset': current_offset,
                    'duration': current_duration,
                    'text': unescape(meta_obj['Data']['text']['Text']) }
            if None in ('SessionEnd',):
                continue
            raise UnknownResponse(f'''Unknown metadata type: {meta_type}''')
            raise UnexpectedResponse('No WordBoundary metadata found')

    
    def __stream(self = None):
        pass
    # WARNING: Decompyle incomplete

    
    def stream(self = None):
        '''
        Streams audio and metadata from the service.

        Raises:
            NoAudioReceived: If no audio is received from the service.
            UnexpectedResponse: If the response from the service is unexpected.
            UnknownResponse: If the response from the service is unknown.
            WebSocketError: If there is an error with the websocket.
        '''
        pass
    # WARNING: Decompyle incomplete

    
    async def save(self = None, audio_fname = None, metadata_fname = None):
        '''
        Save the audio and metadata to the specified files.
        '''
        pass
    # WARNING: Decompyle incomplete

    
    def stream_sync(self = None):
        '''Synchronous interface for async stream method'''
        pass
    # WARNING: Decompyle incomplete

    
    def save_sync(self = None, audio_fname = None, metadata_fname = None):
        '''Synchronous interface for async save method.'''
        executor = concurrent.futures.ThreadPoolExecutor()
        future = executor.submit(asyncio.run, self.save(audio_fname, metadata_fname))
        future.result()
        None(None, None)
        return None
        with None:
            if not None:
                pass
