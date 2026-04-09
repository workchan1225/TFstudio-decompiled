# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: srt_composer.pyc (Python 3.11)

'''A tiny library for composing SRT files.

Based on https://github.com/cdown/srt with parsing, subtitle modifying
functionality and Python 2 support removed. This is because of
https://github.com/rany2/edge-tts/issues/383.

Typing support was added, and more Python 3 features were used.

Copyright (c) 2014-2023 Christopher Down
Copyright (c) 2025- rany <rany@riseup.net>

This file is licensed under the MIT License (MIT).
See the LICENSE-MIT file for details.
'''
import functools
import logging
import re
from datetime import timedelta
from typing import Generator, List, Union
LOG = logging.getLogger(__name__)
MULTI_WS_REGEX = re.compile('\\n\\n+')
ZERO_TIMEDELTA = timedelta(0)
SUBTITLE_SKIP_CONDITIONS = (('No content', (lambda sub: not sub.content.strip())), ('Start time < 0 seconds', (lambda sub: sub.start < ZERO_TIMEDELTA)), ('Subtitle start time >= end time', (lambda sub: sub.start >= sub.end)))
SECONDS_IN_HOUR = 3600
SECONDS_IN_MINUTE = 60
HOURS_IN_DAY = 24
MICROSECONDS_IN_MILLISECOND = 1000
Subtitle = <NODE:12>()

def make_legal_content(content = None):
    """
    Remove illegal content from a content block. Illegal content includes:

    * Blank lines
    * Starting or ending with a blank line

    .. doctest::

        >>> make_legal_content('\\nfoo\\n\\nbar\\n')
        'foo\\nbar'

    :param str content: The content to make legal
    :returns: The legalised content
    :rtype: srt
    """
    if content and content[0] != '\n' and '\n\n' not in content:
        return content
    legal_content = None.sub('\n', content.strip('\n'))
    LOG.info('Legalised content %r to %r', content, legal_content)
    return legal_content


def timedelta_to_srt_timestamp(timedelta_timestamp = None):
    """
    Convert a :py:class:`~datetime.timedelta` to an SRT timestamp.

    .. doctest::

        >>> import datetime
        >>> delta = datetime.timedelta(hours=1, minutes=23, seconds=4)
        >>> timedelta_to_srt_timestamp(delta)
        '01:23:04,000'

    :param datetime.timedelta timedelta_timestamp: A datetime to convert to an
                                                   SRT timestamp
    :returns: The timestamp in SRT format
    :rtype: str
    """
    (hrs, secs_remainder) = divmod(timedelta_timestamp.seconds, SECONDS_IN_HOUR)
    hrs += timedelta_timestamp.days * HOURS_IN_DAY
    (mins, secs) = divmod(secs_remainder, SECONDS_IN_MINUTE)
    msecs = timedelta_timestamp.microseconds // MICROSECONDS_IN_MILLISECOND
    return f'''{int(hrs):02}:{int(mins):02}:{int(secs):02},{int(msecs):03}'''


def sort_and_reindex(subtitles = None, start_index = None, in_place = None, skip = (1, False, True)):
    '''
    Reorder subtitles to be sorted by start time order, and rewrite the indexes
    to be in that same order. This ensures that the SRT file will play in an
    expected fashion after, for example, times were changed in some subtitles
    and they may need to be resorted.

    If skip=True, subtitles will also be skipped if they are considered not to
    be useful. Currently, the conditions to be considered "not useful" are as
    follows:

    - Content is empty, or only whitespace
    - The start time is negative
    - The start time is equal to or later than the end time

    .. doctest::

        >>> from datetime import timedelta
        >>> one = timedelta(seconds=1)
        >>> two = timedelta(seconds=2)
        >>> three = timedelta(seconds=3)
        >>> subs = [
        ...     Subtitle(index=999, start=one, end=two, content=\'1\'),
        ...     Subtitle(index=0, start=two, end=three, content=\'2\'),
        ... ]
        >>> list(sort_and_reindex(subs))  # doctest: +ELLIPSIS
        [Subtitle(...index=1...), Subtitle(...index=2...)]

    :param subtitles: :py:class:`Subtitle` objects in any order
    :param int start_index: The index to start from
    :param bool in_place: Whether to modify subs in-place for performance
                          (version <=1.0.0 behaviour)
    :param bool skip: Whether to skip subtitles considered not useful (see
                      above for rules)
    :returns: The sorted subtitles
    :rtype: :term:`generator` of :py:class:`Subtitle` objects
    '''
    pass
# WARNING: Decompyle incomplete


def _should_skip_sub(subtitle = None):
    '''
    Check if a subtitle should be skipped based on the rules in
    SUBTITLE_SKIP_CONDITIONS.

    :param subtitle: A :py:class:`Subtitle` to check whether to skip
    :raises _ShouldSkipException: If the subtitle should be skipped
    '''
    for info_msg, sub_skipper in SUBTITLE_SKIP_CONDITIONS:
        if sub_skipper(subtitle):
            raise _ShouldSkipException(info_msg)
        return None


def compose(subtitles = None, reindex = None, start_index = None, eol = (True, 1, None, False), in_place = ('subtitles', Union[(Generator[(Subtitle, None, None)], List[Subtitle])], 'reindex', bool, 'start_index', int, 'eol', Union[(str, None)], 'in_place', bool, 'return', str)):
    '''
    Convert an iterator of :py:class:`Subtitle` objects to a string of joined
    SRT blocks.

    .. doctest::

        >>> from datetime import timedelta
        >>> start = timedelta(seconds=1)
        >>> end = timedelta(seconds=2)
        >>> subs = [
        ...     Subtitle(index=1, start=start, end=end, content=\'x\'),
        ...     Subtitle(index=2, start=start, end=end, content=\'y\'),
        ... ]
        >>> compose(subs)  # doctest: +ELLIPSIS
        \'1\\n00:00:01,000 --> 00:00:02,000\\nx\\n\\n2\\n00:00:01,000 --> ...\'

    :param subtitles: The subtitles to convert to SRT blocks
    :type subtitles: :term:`iterator` of :py:class:`Subtitle` objects
    :param bool reindex: Whether to reindex subtitles based on start time
    :param int start_index: If reindexing, the index to start reindexing from
    :param str eol: The end of line string to use (default "\\\\n")
    :returns: A single SRT formatted string, with each input
              :py:class:`Subtitle` represented as an SRT block
    :param bool in_place: Whether to reindex subs in-place for performance
                          (version <=1.0.0 behaviour)
    :rtype: str
    '''
    pass
# WARNING: Decompyle incomplete


class _ShouldSkipException(Exception):
    '''
    Raised when a subtitle should be skipped.
    '''
    pass
