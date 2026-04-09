# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: itunes.pyc (Python 3.11)

from util import FeedParserDict

class Namespace(object):
    supported_namespaces = {
        'http://www.itunes.com/DTDs/PodCast-1.0.dtd': 'itunes',
        'http://example.com/DTDs/PodCast-1.0.dtd': 'itunes' }
    
    def _start_itunes_author(self, attrs_d):
        self._start_author(attrs_d)

    
    def _end_itunes_author(self):
        self._end_author()

    
    def _end_itunes_category(self):
        self._end_category()

    
    def _start_itunes_name(self, attrs_d):
        self._start_name(attrs_d)

    
    def _end_itunes_name(self):
        self._end_name()

    
    def _start_itunes_email(self, attrs_d):
        self._start_email(attrs_d)

    
    def _end_itunes_email(self):
        self._end_email()

    
    def _start_itunes_subtitle(self, attrs_d):
        self._start_subtitle(attrs_d)

    
    def _end_itunes_subtitle(self):
        self._end_subtitle()

    
    def _start_itunes_summary(self, attrs_d):
        self._start_summary(attrs_d)

    
    def _end_itunes_summary(self):
        self._end_summary()

    
    def _start_itunes_owner(self, attrs_d):
        self.inpublisher = 1
        self.push('publisher', 0)

    
    def _end_itunes_owner(self):
        self.pop('publisher')
        self.inpublisher = 0
        self._sync_author_detail('publisher')

    
    def _end_itunes_keywords(self):
        for term in self.pop('itunes_keywords').split(','):
            if term.strip():
                self._add_tag(term.strip(), 'http://www.itunes.com/', None)
            return None

    
    def _start_itunes_category(self, attrs_d):
        self._add_tag(attrs_d.get('text'), 'http://www.itunes.com/', None)
        self.push('category', 1)

    
    def _start_itunes_image(self, attrs_d):
        self.push('itunes_image', 0)
        if attrs_d.get('href'):
            self._get_context()['image'] = FeedParserDict({
                'href': attrs_d.get('href') })
            return None
        if None.get('url'):
            self._get_context()['image'] = FeedParserDict({
                'href': attrs_d.get('url') })
            return None

    _start_itunes_link = _start_itunes_image
    
    def _end_itunes_block(self):
