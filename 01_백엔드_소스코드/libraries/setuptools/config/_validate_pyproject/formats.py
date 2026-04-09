# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: formats.pyc (Python 3.11)

import logging
import os
import re
import string
import typing
from itertools import chain as _chain
_logger = logging.getLogger(__name__)
VERSION_PATTERN = '\n    v?\n    (?:\n        (?:(?P<epoch>[0-9]+)!)?                           # epoch\n        (?P<release>[0-9]+(?:\\.[0-9]+)*)                  # release segment\n        (?P<pre>                                          # pre-release\n            [-_\\.]?\n            (?P<pre_l>(a|b|c|rc|alpha|beta|pre|preview))\n            [-_\\.]?\n            (?P<pre_n>[0-9]+)?\n        )?\n        (?P<post>                                         # post release\n            (?:-(?P<post_n1>[0-9]+))\n            |\n            (?:\n                [-_\\.]?\n                (?P<post_l>post|rev|r)\n                [-_\\.]?\n                (?P<post_n2>[0-9]+)?\n            )\n        )?\n        (?P<dev>                                          # dev release\n            [-_\\.]?\n            (?P<dev_l>dev)\n            [-_\\.]?\n            (?P<dev_n>[0-9]+)?\n        )?\n    )\n    (?:\\+(?P<local>[a-z0-9]+(?:[-_\\.][a-z0-9]+)*))?       # local version\n'
VERSION_REGEX = re.compile('^\\s*' + VERSION_PATTERN + '\\s*$', re.X | re.I)

def pep440(version = None):
    return VERSION_REGEX.match(version) is not None

PEP508_IDENTIFIER_PATTERN = '([A-Z0-9]|[A-Z0-9][A-Z0-9._-]*[A-Z0-9])'
PEP508_IDENTIFIER_REGEX = re.compile(f'''^{PEP508_IDENTIFIER_PATTERN}$''', re.I)

def pep508_identifier(name = None):
    return PEP508_IDENTIFIER_REGEX.match(name) is not None


try:
    from packaging import requirements as _req
    
    try:
        pass
    except ImportError:
        from setuptools._vendor.packaging import requirements as _req
        
        try:
            pass
        try:
            
            def pep508(value = None):
                
                try:
                    _req.Requirement(value)
                    return True
                except _req.InvalidRequirement:
                    return False


        except ImportError:
            _logger.warning('Could not find an installation of `packaging`. Requirements, dependencies and versions might not be validated. To enforce validation, please install `packaging`.')
            
            def pep508(value = None):
                return True


        
        def pep508_versionspec(value = None):
            '''Expression that can be used to specify/lock versions (including ranges)'''
            pass
        # WARNING: Decompyle incomplete

        
        def pep517_backend_reference(value = None):
            (module, _, obj) = value.partition(':')
            identifiers = _chain(module.split('.'), obj.split('.'))()
            return (lambda .0: pass# WARNING: Decompyle incomplete
)(identifiers())

        
        def _download_classifiers():
            import ssl
            Message = Message
            import email.message
            urlopen = urlopen
            import urllib.request
            url = 'https://pypi.org/pypi?:action=list_classifiers'
            context = ssl.create_default_context()
            response = urlopen(url, context = context)
            headers = Message()
            headers['content_type'] = response.getheader('content-type', 'text/plain')
            None(None, None)
            return 
            with None:
                if not None, response.read().decode(headers.get_param('charset', 'utf-8')):
                    pass

        
        class _TroveClassifier:
            """The ``trove_classifiers`` package is the official way of validating classifiers,
    however this package might not be always available.
    As a workaround we can still download a list from PyPI.
    We also don't want to be over strict about it, so simply skipping silently is an
    option (classifiers will be validated anyway during the upload to PyPI).
    """
            
            def __init__(self):
                self.downloaded = None
                self._skip_download = False
                self.__name__ = 'trove_classifier'

            
            def _disable_download(self):
                self._skip_download = True

            
            def __call__(self = None, value = None):
                if self.downloaded is False or self._skip_download is True:
                    return True
                if None.getenv('NO_NETWORK') or os.getenv('VALIDATE_PYPROJECT_NO_NETWORK'):
                    self.downloaded = False
                    msg = 'Install ``trove-classifiers`` to ensure proper validation. Skipping download of classifiers list from PyPI (NO_NETWORK).'
                    _logger.debug(msg)
                    return True
            # WARNING: Decompyle incomplete


        
        try:
            from trove_classifiers import classifiers as _trove_classifiers
            
            def trove_classifier(value = None):
                if not value in _trove_classifiers:
                    pass
                return value.lower().startswith('private ::')

        except ImportError:
            trove_classifier = _TroveClassifier()

        
        def url(value = None):
            urlparse = urlparse
            import urllib.parse
            
            try:
                parts = urlparse(value)
                if not parts.scheme:
                    _logger.warning(f'''For maximum compatibility please make sure to include a `scheme` prefix in your URL (e.g. \'http://\'). Given value: {value}''')
                    if not value.startswith('/') and value.startswith('\\') and '@' in value:
                        parts = urlparse(f'''http://{value}''')
                if parts.scheme:
                    return bool(parts.netloc)
                except Exception:
                    bool
                    return False


        ENTRYPOINT_PATTERN = '[^\\[\\s=]([^=]*[^\\s=])?'
        ENTRYPOINT_REGEX = re.compile(f'''^{ENTRYPOINT_PATTERN}$''', re.I)
        RECOMMEDED_ENTRYPOINT_PATTERN = '[\\w.-]+'
        RECOMMEDED_ENTRYPOINT_REGEX = re.compile(f'''^{RECOMMEDED_ENTRYPOINT_PATTERN}$''', re.I)
        ENTRYPOINT_GROUP_PATTERN = '\\w+(\\.\\w+)*'
        ENTRYPOINT_GROUP_REGEX = re.compile(f'''^{ENTRYPOINT_GROUP_PATTERN}$''', re.I)
        
        def python_identifier(value = None):
            return value.isidentifier()

        
        def python_qualified_identifier(value = None):
            if value.startswith('.') or value.endswith('.'):
                return False
            return (lambda .0: pass# WARNING: Decompyle incomplete
)(value.split('.')())

        
        def python_module_name(value = None):
            return python_qualified_identifier(value)

        
        def python_entrypoint_group(value = None):
            return ENTRYPOINT_GROUP_REGEX.match(value) is not None

        
        def python_entrypoint_name(value = None):
            if not ENTRYPOINT_REGEX.match(value):
                return False
            if not None.match(value):
                msg = f'''Entry point `{value}` does not follow recommended pattern: '''
                msg += RECOMMEDED_ENTRYPOINT_PATTERN
                _logger.warning(msg)
            return True

        
        def python_entrypoint_reference(value = None):
