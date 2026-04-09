# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: cc.pyc (Python 3.11)

from util import FeedParserDict

class Namespace(object):
    supported_namespaces = {
        'http://creativecommons.org/ns#license': 'cc',
        'http://web.resource.org/cc/': 'cc',
        'http://cyber.law.harvard.edu/rss/creativeCommonsRssModule.html': 'creativecommons',
        'http://backend.userland.com/creativeCommonsRssModule': 'creativecommons' }
    
    def _start_cc_license(self, attrs_d):
        context = self._get_context()
        value = self._get_attribute(attrs_d, 'rdf:resource')
        attrs_d = FeedParserDict()
        attrs_d['rel'] = 'license'
        if value:
            attrs_d['href'] = value
        context.setdefault('links', []).append(attrs_d)

    
    def _start_creativecommons_license(self, attrs_d):
        self.push('license', 1)

    _start_creativeCommons_license = _start_creativecommons_license
    
    def _end_creativecommons_license(self):
        value = self.pop('license')
        context = self._get_context()
        attrs_d = FeedParserDict()
        attrs_d['rel'] = 'license'
        if value:
            attrs_d['href'] = value
        context.setdefault('links', []).append(attrs_d)
        del context['license']

    _end_creativeCommons_license = _end_creativecommons_license
