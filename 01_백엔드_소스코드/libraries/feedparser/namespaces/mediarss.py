# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: mediarss.pyc (Python 3.11)

from util import FeedParserDict

class Namespace(object):
    supported_namespaces = {
        'http://search.yahoo.com/mrss/': 'media',
        'http://search.yahoo.com/mrss': 'media' }
    
    def _start_media_category(self, attrs_d):
        attrs_d.setdefault('scheme', 'http://search.yahoo.com/mrss/category_schema')
        self._start_category(attrs_d)

    
    def _end_media_category(self):
        self._end_category()

    
    def _end_media_keywords(self):
        for term in self.pop('media_keywords').split(','):
            if term.strip():
                self._add_tag(term.strip(), None, None)
            return None

    
    def _start_media_title(self, attrs_d):
        self._start_title(attrs_d)

    
    def _end_media_title(self):
        title_depth = self.title_depth
        self._end_title()
        self.title_depth = title_depth

    
    def _start_media_group(self, attrs_d):
        pass

    
    def _start_media_rating(self, attrs_d):
        context = self._get_context()
        context.setdefault('media_rating', attrs_d)
        self.push('rating', 1)

    
    def _end_media_rating(self):
        rating = self.pop('rating')
    # WARNING: Decompyle incomplete

    
    def _start_media_credit(self, attrs_d):
        context = self._get_context()
        context.setdefault('media_credit', [])
        context['media_credit'].append(attrs_d)
        self.push('credit', 1)

    
    def _end_media_credit(self):
        credit = self.pop('credit')
    # WARNING: Decompyle incomplete

    
    def _start_media_description(self, attrs_d):
        self._start_description(attrs_d)

    
    def _end_media_description(self):
        self._end_description()

    
    def _start_media_restriction(self, attrs_d):
        context = self._get_context()
        context.setdefault('media_restriction', attrs_d)
        self.push('restriction', 1)

    
    def _end_media_restriction(self):
        restriction = self.pop('restriction')
    # WARNING: Decompyle incomplete

    
    def _start_media_license(self, attrs_d):
        context = self._get_context()
        context.setdefault('media_license', attrs_d)
        self.push('license', 1)

    
    def _end_media_license(self):
        license_ = self.pop('license')
    # WARNING: Decompyle incomplete

    
    def _start_media_content(self, attrs_d):
        context = self._get_context()
        context.setdefault('media_content', [])
        context['media_content'].append(attrs_d)

    
    def _start_media_thumbnail(self, attrs_d):
        context = self._get_context()
        context.setdefault('media_thumbnail', [])
        self.push('url', 1)
        context['media_thumbnail'].append(attrs_d)

    
    def _end_media_thumbnail(self):
        url = self.pop('url')
        context = self._get_context()
    # WARNING: Decompyle incomplete

    
    def _start_media_player(self, attrs_d):
        self.push('media_player', 0)
        self._get_context()['media_player'] = FeedParserDict(attrs_d)

    
    def _end_media_player(self):
        value = self.pop('media_player')
        context = self._get_context()
        context['media_player']['content'] = value
