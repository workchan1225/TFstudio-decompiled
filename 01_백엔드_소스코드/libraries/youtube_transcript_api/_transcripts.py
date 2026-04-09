# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: _transcripts.pyc (Python 3.11)

from dataclasses import dataclass, asdict
from enum import Enum
from itertools import chain
from html import unescape
from typing import List, Dict, Iterator, Iterable, Pattern, Optional
from defusedxml import ElementTree
import re
from requests import HTTPError, Session, Response
from proxies import ProxyConfig
from _settings import WATCH_URL, INNERTUBE_CONTEXT, INNERTUBE_API_URL
from _errors import VideoUnavailable, YouTubeRequestFailed, NoTranscriptFound, TranscriptsDisabled, NotTranslatable, TranslationLanguageNotAvailable, FailedToCreateConsentCookie, InvalidVideoId, IpBlocked, RequestBlocked, AgeRestricted, VideoUnplayable, YouTubeDataUnparsable, PoTokenRequired
FetchedTranscriptSnippet = <NODE:12>()
FetchedTranscript = <NODE:12>()
_TranslationLanguage = <NODE:12>()

class _PlayabilityStatus(Enum, str):
    OK = 'OK'
    ERROR = 'ERROR'
    LOGIN_REQUIRED = 'LOGIN_REQUIRED'


class _PlayabilityFailedReason(Enum, str):
    BOT_DETECTED = 'Sign in to confirm you’re not a bot'
    AGE_RESTRICTED = 'This video may be inappropriate for some users.'
    VIDEO_UNAVAILABLE = 'This video is unavailable'


def _raise_http_errors(response = dataclass, video_id = None):
    
    try:
        if response.status_code == 429:
            raise IpBlocked(video_id)
        response.raise_for_status()
        return response
    except HTTPError:
        error = None
        raise YouTubeRequestFailed(video_id, error)
        error = None
        del error



class Transcript:
    
    def __init__(self, http_client, video_id, url, language = None, language_code = None, is_generated = None, translation_languages = ('http_client', Session, 'video_id', str, 'url', str, 'language', str, 'language_code', str, 'is_generated', bool, 'translation_languages', List[_TranslationLanguage])):
        """
        You probably don't want to initialize this directly. Usually you'll access Transcript objects using a
        TranscriptList.
        """
        self._http_client = http_client
        self.video_id = video_id
        self._url = url
        self.language = language
        self.language_code = language_code
        self.is_generated = is_generated
        self.translation_languages = translation_languages
        self._translation_languages_dict = translation_languages()

    
    def fetch(self = None, preserve_formatting = None):
        '''
        Loads the actual transcript data.
        :param preserve_formatting: whether to keep select HTML text formatting
        '''
        if '&exp=xpe' in self._url:
            raise PoTokenRequired(self.video_id)
        response = self._http_client.get(self._url)
        snippets = _TranscriptParser(preserve_formatting = preserve_formatting).parse(_raise_http_errors(response, self.video_id).text)
        return FetchedTranscript(snippets = snippets, video_id = self.video_id, language = self.language, language_code = self.language_code, is_generated = self.is_generated)

    
    def __str__(self = None):
        return '{language_code} ("{language}"){translation_description}'.format(language = self.language, language_code = self.language_code, translation_description = '[TRANSLATABLE]' if self.is_translatable else '')

    is_translatable = (lambda self = None: len(self.translation_languages) > 0)()
    
    def translate(self = None, language_code = None):
        if not self.is_translatable:
            raise NotTranslatable(self.video_id)
        if language_code not in self._translation_languages_dict:
            raise TranslationLanguageNotAvailable(self.video_id)
        return Transcript(self._http_client, self.video_id, '{url}&tlang={language_code}'.format(url = self._url, language_code = language_code), self._translation_languages_dict[language_code], language_code, True, [])



class TranscriptList:
    '''
    This object represents a list of transcripts. It can be iterated over to list all transcripts which are available
    for a given YouTube video. Also, it provides functionality to search for a transcript in a given language.
    '''
    
    def __init__(self, video_id = None, manually_created_transcripts = None, generated_transcripts = None, translation_languages = ('video_id', str, 'manually_created_transcripts', Dict[(str, Transcript)], 'generated_transcripts', Dict[(str, Transcript)], 'translation_languages', List[_TranslationLanguage])):
        '''
        The constructor is only for internal use. Use the static build method instead.

        :param video_id: the id of the video this TranscriptList is for
        :param manually_created_transcripts: dict mapping language codes to the manually created transcripts
        :param generated_transcripts: dict mapping language codes to the generated transcripts
        :param translation_languages: list of languages which can be used for translatable languages
        '''
        self.video_id = video_id
        self._manually_created_transcripts = manually_created_transcripts
        self._generated_transcripts = generated_transcripts
        self._translation_languages = translation_languages

    build = (lambda http_client = None, video_id = None, captions_json = staticmethod: translation_languages = captions_json.get('translationLanguages', [])()manually_created_transcripts = { }generated_transcripts = { }for caption in captions_json['captionTracks']:
transcript_dict[caption['languageCode']] = Transcript(http_client, video_id, caption['baseUrl'].replace('&fmt=srv3', ''), caption['name']['runs'][0]['text'], caption['languageCode'], caption.get('kind', '') == 'asr', translation_languages if caption.get('isTranslatable', False) else [])TranscriptList(video_id, manually_created_transcripts, generated_transcripts, translation_languages))()
    
    def __iter__(self = None):
        return chain(self._manually_created_transcripts.values(), self._generated_transcripts.values())

    
    def find_transcript(self = None, language_codes = None):
        """
        Finds a transcript for a given language code. Manually created transcripts are returned first and only if none
        are found, generated transcripts are used. If you only want generated transcripts use
        `find_manually_created_transcript` instead.

        :param language_codes: A list of language codes in a descending priority. For example, if this is set to
        ['de', 'en'] it will first try to fetch the german transcript (de) and then fetch the english transcript (en) if
        it fails to do so.
        :return: the found Transcript
        """
        return self._find_transcript(language_codes, [
            self._manually_created_transcripts,
            self._generated_transcripts])

    
    def find_generated_transcript(self = None, language_codes = None):
        """
        Finds an automatically generated transcript for a given language code.

        :param language_codes: A list of language codes in a descending priority. For example, if this is set to
        ['de', 'en'] it will first try to fetch the german transcript (de) and then fetch the english transcript (en) if
        it fails to do so.
        :return: the found Transcript
        """
        return self._find_transcript(language_codes, [
            self._generated_transcripts])

    
    def find_manually_created_transcript(self = None, language_codes = None):
        """
        Finds a manually created transcript for a given language code.

        :param language_codes: A list of language codes in a descending priority. For example, if this is set to
        ['de', 'en'] it will first try to fetch the german transcript (de) and then fetch the english transcript (en) if
        it fails to do so.
        :return: the found Transcript
        """
        return self._find_transcript(language_codes, [
            self._manually_created_transcripts])

    
    def _find_transcript(self = None, language_codes = None, transcript_dicts = None):
        for language_code in language_codes:
            for transcript_dict in transcript_dicts:
                if language_code in transcript_dict:
                    
                    
                    return None, None, transcript_dict[language_code]
                raise NoTranscriptFound(self.video_id, language_codes, self)

    
    def __str__(self = None):
        return (lambda .0: pass# WARNING: Decompyle incomplete
)(self._manually_created_transcripts.values()())(video_id = self._get_language_description, available_manually_created_transcript_languages = (lambda .0: pass# WARNING: Decompyle incomplete
)(self._generated_transcripts.values()()), available_generated_transcripts = self._get_language_description, available_translation_languages = (lambda .0: pass# WARNING: Decompyle incomplete
)(self._translation_languages()))

    
    def _get_language_description(self = None, transcript_strings = None):
        description = (lambda .0: pass# WARNING: Decompyle incomplete
)(transcript_strings())
        return description if description else 'None'



class TranscriptListFetcher:
    
    def __init__(self = None, http_client = None, proxy_config = None):
        self._http_client = http_client
        self._proxy_config = proxy_config

    
    def fetch(self = None, video_id = None):
        return TranscriptList.build(self._http_client, video_id, self._fetch_captions_json(video_id))

    
    def _fetch_captions_json(self = None, video_id = None, try_number = None):
        pass
    # WARNING: Decompyle incomplete

    
    def _extract_innertube_api_key(self = None, html = None, video_id = None):
        pattern = '"INNERTUBE_API_KEY":\\s*"([a-zA-Z0-9_-]+)"'
        match = re.search(pattern, html)
        if match and len(match.groups()) == 1:
            return match.group(1)
        if None in html:
            raise IpBlocked(video_id)
        raise YouTubeDataUnparsable(video_id)

    
    def _extract_captions_json(self = None, innertube_data = None, video_id = None):
        self._assert_playability(innertube_data.get('playabilityStatus'), video_id)
        captions_json = innertube_data.get('captions', { }).get('playerCaptionsTracklistRenderer')
    # WARNING: Decompyle incomplete

    
    def _assert_playability(self = None, playability_status_data = None, video_id = None):
        playability_status = playability_status_data.get('status')
    # WARNING: Decompyle incomplete

    
    def _create_consent_cookie(self = None, html = None, video_id = None):
        match = re.search('name="v" value="(.*?)"', html)
    # WARNING: Decompyle incomplete

    
    def _fetch_video_html(self = None, video_id = None):
        html = self._fetch_html(video_id)
        if 'action="https://consent.youtube.com/s"' in html:
            self._create_consent_cookie(html, video_id)
            html = self._fetch_html(video_id)
            if 'action="https://consent.youtube.com/s"' in html:
                raise FailedToCreateConsentCookie(video_id)
        return html

    
    def _fetch_html(self = None, video_id = None):
        response = self._http_client.get(WATCH_URL.format(video_id = video_id))
        return unescape(_raise_http_errors(response, video_id).text)

    
    def _fetch_innertube_data(self = None, video_id = None, api_key = None):
        response = self._http_client.post(INNERTUBE_API_URL.format(api_key = api_key), json = {
            'context': INNERTUBE_CONTEXT,
            'videoId': video_id })
        data = _raise_http_errors(response, video_id).json()
        return data



class _TranscriptParser:
    _FORMATTING_TAGS = [
        'strong',
        'em',
        'b',
        'i',
        'mark',
        'small',
        'del',
        'ins',
        'sub',
        'sup']
    
    def __init__(self = None, preserve_formatting = None):
        self._html_regex = self._get_html_regex(preserve_formatting)

    
    def _get_html_regex(self = None, preserve_formatting = None):
        if preserve_formatting:
            formats_regex = '|'.join(self._FORMATTING_TAGS)
            formats_regex = '<\\/?(?!\\/?(' + formats_regex + ')\\b).*?\\b>'
            html_regex = re.compile(formats_regex, re.IGNORECASE)
        else:
            html_regex = re.compile('<[^>]*>', re.IGNORECASE)
        return html_regex

    
    def parse(self = None, raw_data = None):
        pass
    # WARNING: Decompyle incomplete
