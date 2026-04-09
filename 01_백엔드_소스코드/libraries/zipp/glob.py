# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: glob.pyc (Python 3.11)

import os
import re
from compat.py313 import legacy_end_marker
_default_seps = os.sep + str(os.altsep) * bool(os.altsep)

class Translator:
    seps: str = "\n    >>> Translator('xyz')\n    Traceback (most recent call last):\n    ...\n    AssertionError: Invalid separators\n\n    >>> Translator('')\n    Traceback (most recent call last):\n    ...\n    AssertionError: Invalid separators\n    "
    
    def __init__(self = None, seps = None):
        pass
    # WARNING: Decompyle incomplete

    
    def translate(self, pattern):
        '''
        Given a glob pattern, produce a regex that matches it.
        '''
        return self.extend(self.match_dirs(self.translate_core(pattern)))

    extend = (lambda self, pattern: f'''(?s:{pattern})\\z''')()
    
    def match_dirs(self, pattern):
        '''
        Ensure that zipfile.Path directory names are matched.

        zipfile.Path directory names always end in a slash.
        '''
        return f'''{pattern}[/]?'''

    
    def translate_core(self, pattern):
        """
        Given a glob pattern, produce a regex that matches it.

        >>> t = Translator()
        >>> t.translate_core('*.txt').replace('\\\\\\\\', '')
        '[^/]*\\\\.txt'
        >>> t.translate_core('a?txt')
        'a[^/]txt'
        >>> t.translate_core('**/*').replace('\\\\\\\\', '')
        '.*/[^/][^/]*'
        """
        self.restrict_rglob(pattern)
        return ''.join(map(self.replace, separate(self.star_not_empty(pattern))))

    
    def replace(self, match):
        '''
        Perform the replacements for a match from :func:`separate`.
        '''
        if not match.group('set'):
            pass
        return re.escape(match.group(0)).replace('\\*\\*', '.*').replace('\\*', f'''[^{re.escape(self.seps)}]*''').replace('\\?', '[^/]')

    
    def restrict_rglob(self, pattern):
        """
        Raise ValueError if ** appears in anything but a full path segment.

        >>> Translator().translate('**foo')
        Traceback (most recent call last):
        ...
        ValueError: ** must appear alone in a path segment
        """
        seps_pattern = f'''[{re.escape(self.seps)}]+'''
        segments = re.split(seps_pattern, pattern)
        if (lambda .0: pass# WARNING: Decompyle incomplete
)(segments()):
            raise ValueError('** must appear alone in a path segment')

    
    def star_not_empty(self, pattern):
        '''
        Ensure that * will not match an empty segment.
        '''
        
        def handle_segment(match):
            segment = match.group(0)
            return '?*' if segment == '*' else segment

        not_seps_pattern = f'''[^{re.escape(self.seps)}]+'''
        return re.sub(not_seps_pattern, handle_segment, pattern)



def separate(pattern):
    """
    Separate out character sets to avoid translating their contents.

    >>> [m.group(0) for m in separate('*.txt')]
    ['*.txt']
    >>> [m.group(0) for m in separate('a[?]txt')]
    ['a', '[?]', 'txt']
    """
    return re.finditer('([^\\[]+)|(?P<set>[\\[].*?[\\]])|([\\[][^\\]]*$)', pattern)
