# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: _errors.pyc (Python 3.11)

from pathlib import Path
from typing import Iterable, Optional, List
from requests import HTTPError
from _settings import WATCH_URL
from proxies import ProxyConfig, GenericProxyConfig, WebshareProxyConfig

class YouTubeTranscriptApiException(Exception):
    pass


class CookieError(YouTubeTranscriptApiException):
    pass


class CookiePathInvalid(CookieError):
    pass
# WARNING: Decompyle incomplete


class CookieInvalid(CookieError):
    pass
# WARNING: Decompyle incomplete


class CouldNotRetrieveTranscript(YouTubeTranscriptApiException):
    pass
# WARNING: Decompyle incomplete


class YouTubeDataUnparsable(CouldNotRetrieveTranscript):
    CAUSE_MESSAGE = 'The data required to fetch the transcript is not parsable. This should not happen, please open an issue (make sure to include the video ID)!'


class YouTubeRequestFailed(CouldNotRetrieveTranscript):
    pass
# WARNING: Decompyle incomplete


class VideoUnplayable(CouldNotRetrieveTranscript):
    pass
# WARNING: Decompyle incomplete


class VideoUnavailable(CouldNotRetrieveTranscript):
    CAUSE_MESSAGE = 'The video is no longer available'


class InvalidVideoId(CouldNotRetrieveTranscript):
    CAUSE_MESSAGE = 'You provided an invalid video id. Make sure you are using the video id and NOT the url!\n\nDo NOT run: `YouTubeTranscriptApi().fetch("https://www.youtube.com/watch?v=1234")`\nInstead run: `YouTubeTranscriptApi().fetch("1234")`'


class RequestBlocked(CouldNotRetrieveTranscript):
    pass
# WARNING: Decompyle incomplete


class IpBlocked(RequestBlocked):
    CAUSE_MESSAGE = f'''{RequestBlocked.BASE_CAUSE_MESSAGE}Ways to work around this are explained in the "Working around IP bans" section of the README (https://github.com/jdepoix/youtube-transcript-api?tab=readme-ov-file#working-around-ip-bans-requestblocked-or-ipblocked-exception).\n'''


class TranscriptsDisabled(CouldNotRetrieveTranscript):
    CAUSE_MESSAGE = 'Subtitles are disabled for this video'


class AgeRestricted(CouldNotRetrieveTranscript):
    CAUSE_MESSAGE = "This video is age-restricted. Therefore, you are unable to retrieve transcripts for it without authenticating yourself.\n\nUnfortunately, Cookie Authentication is temporarily unsupported in youtube-transcript-api, as recent changes in YouTube's API broke the previous implementation. I will do my best to re-implement it as soon as possible."


class NotTranslatable(CouldNotRetrieveTranscript):
    CAUSE_MESSAGE = 'The requested language is not translatable'


class TranslationLanguageNotAvailable(CouldNotRetrieveTranscript):
    CAUSE_MESSAGE = 'The requested translation language is not available'


class FailedToCreateConsentCookie(CouldNotRetrieveTranscript):
    CAUSE_MESSAGE = 'Failed to automatically give consent to saving cookies'


class NoTranscriptFound(CouldNotRetrieveTranscript):
    pass
# WARNING: Decompyle incomplete


class PoTokenRequired(CouldNotRetrieveTranscript):
    CAUSE_MESSAGE = 'The requested video cannot be retrieved without a PO Token. If this happens, please open a GitHub issue!'
