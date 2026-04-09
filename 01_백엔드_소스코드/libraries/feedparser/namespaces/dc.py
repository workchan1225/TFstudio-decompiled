# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: dc.pyc (Python 3.11)

from datetimes import _parse_date
from util import FeedParserDict

class Namespace(object):
    supported_namespaces = {
        'http://purl.org/dc/elements/1.1/': 'dc',
        'http://purl.org/dc/terms/': 'dcterms' }
    
    def _end_dc_author(self):
        self._end_author()

    
    def _end_dc_creator(self):
        self._end_author()

    
    def _end_dc_date(self):
        self._end_updated()

    
    def _end_dc_description(self):
        self._end_description()

    
    def _end_dc_language(self):
        self._end_language()

    
    def _end_dc_publisher(self):
        self._end_webmaster()

    
    def _end_dc_rights(self):
        self._end_rights()

    
    def _end_dc_subject(self):
        self._end_category()

    
    def _end_dc_title(self):
        self._end_title()

    
    def _end_dcterms_created(self):
        self._end_created()

    
    def _end_dcterms_issued(self):
        self._end_published()

    
    def _end_dcterms_modified(self):
        self._end_updated()

    
    def _start_dc_author(self, attrs_d):
        self._start_author(attrs_d)

    
    def _start_dc_creator(self, attrs_d):
        self._start_author(attrs_d)

    
    def _start_dc_date(self, attrs_d):
        self._start_updated(attrs_d)

    
    def _start_dc_description(self, attrs_d):
        self._start_description(attrs_d)

    
    def _start_dc_language(self, attrs_d):
        self._start_language(attrs_d)

    
    def _start_dc_publisher(self, attrs_d):
        self._start_webmaster(attrs_d)

    
    def _start_dc_rights(self, attrs_d):
        self._start_rights(attrs_d)

    
    def _start_dc_subject(self, attrs_d):
        self._start_category(attrs_d)

    
    def _start_dc_title(self, attrs_d):
        self._start_title(attrs_d)

    
    def _start_dcterms_created(self, attrs_d):
        self._start_created(attrs_d)

    
    def _start_dcterms_issued(self, attrs_d):
        self._start_published(attrs_d)

    
    def _start_dcterms_modified(self, attrs_d):
        self._start_updated(attrs_d)

    
    def _start_dcterms_valid(self, attrs_d):
        self.push('validity', 1)

    
    def _end_dcterms_valid(self):
        for validity_detail in self.pop('validity').split(';'):
            if '=' in validity_detail:
                (key, value) = validity_detail.split('=', 1)
                if key == 'start':
                    self._save('validity_start', value, overwrite = True)
                    self._save('validity_start_parsed', _parse_date(value), overwrite = True)
                    continue
                if key == 'end':
                    self._save('validity_end', value, overwrite = True)
                    self._save('validity_end_parsed', _parse_date(value), overwrite = True)
            return None

    
    def _start_dc_contributor(self, attrs_d):
        self.incontributor = 1
        context = self._get_context()
        context.setdefault('contributors', [])
        context['contributors'].append(FeedParserDict())
        self.push('name', 0)

    
    def _end_dc_contributor(self):
        self._end_name()
        self.incontributor = 0
