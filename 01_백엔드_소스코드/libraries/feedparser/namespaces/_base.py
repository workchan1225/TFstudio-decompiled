# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: _base.pyc (Python 3.11)

import copy
from datetimes import _parse_date
from urls import make_safe_absolute_uri
from util import FeedParserDict

class Namespace(object):
    '''Support for the Atom, RSS, RDF, and CDF feed formats.

    The feed formats all share common elements, some of which have conflicting
    interpretations. For simplicity, all of the base feed format support is
    collected here.
    '''
    supported_namespaces = {
        '': '',
        'http://backend.userland.com/rss': '',
        'http://blogs.law.harvard.edu/tech/rss': '',
        'http://purl.org/rss/1.0/': '',
        'http://my.netscape.com/rdf/simple/0.9/': '',
        'http://example.com/newformat#': '',
        'http://example.com/necho': '',
        'http://purl.org/echo/': '',
        'uri/of/echo/namespace#': '',
        'http://purl.org/pie/': '',
        'http://purl.org/atom/ns#': '',
        'http://www.w3.org/2005/Atom': '',
        'http://purl.org/rss/1.0/modules/rss091#': '' }
    
    def _start_rss(self, attrs_d):
        versionmap = {
            '0.91': 'rss091u',
            '0.92': 'rss092',
            '0.93': 'rss093',
            '0.94': 'rss094' }
        if not self.version or self.version.startswith('rss'):
            attr_version = attrs_d.get('version', '')
            version = versionmap.get(attr_version)
            if version:
                self.version = version
                return None
            if None.startswith('2.'):
                self.version = 'rss20'
                return None
            self.version = None
            return None

    
    def _start_channel(self, attrs_d):
        self.infeed = 1
        self._cdf_common(attrs_d)

    
    def _cdf_common(self, attrs_d):
        if 'lastmod' in attrs_d:
            self._start_modified({ })
            self.elementstack[-1][-1] = attrs_d['lastmod']
            self._end_modified()
        if 'href' in attrs_d:
            self._start_link({ })
            self.elementstack[-1][-1] = attrs_d['href']
            self._end_link()
            return None

    
    def _start_feed(self, attrs_d):
        self.infeed = 1
        versionmap = {
            '0.1': 'atom01',
            '0.2': 'atom02',
            '0.3': 'atom03' }
        if not self.version:
            attr_version = attrs_d.get('version')
            version = versionmap.get(attr_version)
            if version:
                self.version = version
                return None
            self.version = None
            return None

    
    def _end_channel(self):
        self.infeed = 0

    _end_feed = _end_channel
    
    def _start_image(self, attrs_d):
        context = self._get_context()
        if not self.inentry:
            context.setdefault('image', FeedParserDict())
        self.inimage = 1
        self.title_depth = -1
        self.push('image', 0)

    
    def _end_image(self):
        self.pop('image')
        self.inimage = 0

    
    def _start_textinput(self, attrs_d):
        context = self._get_context()
        context.setdefault('textinput', FeedParserDict())
        self.intextinput = 1
        self.title_depth = -1
        self.push('textinput', 0)

    _start_textInput = _start_textinput
    
    def _end_textinput(self):
        self.pop('textinput')
        self.intextinput = 0

    _end_textInput = _end_textinput
    
    def _start_author(self, attrs_d):
        self.inauthor = 1
        self.push('author', 1)
        context = self._get_context()
        context.setdefault('authors', [])
        context['authors'].append(FeedParserDict())

    _start_managingeditor = _start_author
    
    def _end_author(self):
        self.pop('author')
        self.inauthor = 0
        self._sync_author_detail()

    _end_managingeditor = _end_author
    
    def _start_contributor(self, attrs_d):
        self.incontributor = 1
        context = self._get_context()
        context.setdefault('contributors', [])
        context['contributors'].append(FeedParserDict())
        self.push('contributor', 0)

    
    def _end_contributor(self):
        self.pop('contributor')
        self.incontributor = 0

    
    def _start_name(self, attrs_d):
        self.push('name', 0)

    
    def _end_name(self):
        value = self.pop('name')
        if self.inpublisher:
            self._save_author('name', value, 'publisher')
            return None
        if None.inauthor:
            self._save_author('name', value)
            return None
        if None.incontributor:
            self._save_contributor('name', value)
            return None
        if None.intextinput:
            context = self._get_context()
            context['name'] = value
            return None

    
    def _start_width(self, attrs_d):
        self.push('width', 0)

    
    def _end_width(self):
        value = self.pop('width')
        
        try:
            value = int(value)
        except ValueError:
            value = 0

        if self.inimage:
            context = self._get_context()
            context['width'] = value
            return None

    
    def _start_height(self, attrs_d):
        self.push('height', 0)

    
    def _end_height(self):
        value = self.pop('height')
        
        try:
            value = int(value)
        except ValueError:
            value = 0

        if self.inimage:
            context = self._get_context()
            context['height'] = value
            return None

    
    def _start_url(self, attrs_d):
        self.push('href', 1)

    _start_homepage = _start_url
    _start_uri = _start_url
    
    def _end_url(self):
        value = self.pop('href')
        if self.inauthor:
            self._save_author('href', value)
            return None
        if None.incontributor:
            self._save_contributor('href', value)
            return None

    _end_homepage = _end_url
    _end_uri = _end_url
    
    def _start_email(self, attrs_d):
        self.push('email', 0)

    
    def _end_email(self):
        value = self.pop('email')
        if self.inpublisher:
            self._save_author('email', value, 'publisher')
            return None
        if None.inauthor:
            self._save_author('email', value)
            return None
        if None.incontributor:
            self._save_contributor('email', value)
            return None

    
    def _start_subtitle(self, attrs_d):
        self.push_content('subtitle', attrs_d, 'text/plain', 1)

    _start_tagline = _start_subtitle
    
    def _end_subtitle(self):
        self.pop_content('subtitle')

    _end_tagline = _end_subtitle
    
    def _start_rights(self, attrs_d):
        self.push_content('rights', attrs_d, 'text/plain', 1)

    _start_copyright = _start_rights
    
    def _end_rights(self):
        self.pop_content('rights')

    _end_copyright = _end_rights
    
    def _start_item(self, attrs_d):
        self.entries.append(FeedParserDict())
        self.push('item', 0)
        self.inentry = 1
        self.guidislink = 0
        self.title_depth = -1
        id = self._get_attribute(attrs_d, 'rdf:about')
        if id:
            context = self._get_context()
            context['id'] = id
        self._cdf_common(attrs_d)

    _start_entry = _start_item
    
    def _end_item(self):
        self.pop('item')
        self.inentry = 0
        self.hasContent = 0

    _end_entry = _end_item
    
    def _start_language(self, attrs_d):
        self.push('language', 1)

    
    def _end_language(self):
        self.lang = self.pop('language')

    
    def _start_webmaster(self, attrs_d):
        self.push('publisher', 1)

    
    def _end_webmaster(self):
        self.pop('publisher')
        self._sync_author_detail('publisher')

    
    def _start_published(self, attrs_d):
        self.push('published', 1)

    _start_issued = _start_published
    _start_pubdate = _start_published
    
    def _end_published(self):
        value = self.pop('published')
        self._save('published_parsed', _parse_date(value), overwrite = True)

    _end_issued = _end_published
    _end_pubdate = _end_published
    
    def _start_updated(self, attrs_d):
        self.push('updated', 1)

    _start_modified = _start_updated
    _start_lastbuilddate = _start_updated
    
    def _end_updated(self):
        value = self.pop('updated')
        parsed_value = _parse_date(value)
        self._save('updated_parsed', parsed_value, overwrite = True)

    _end_modified = _end_updated
    _end_lastbuilddate = _end_updated
    
    def _start_created(self, attrs_d):
        self.push('created', 1)

    
    def _end_created(self):
        value = self.pop('created')
        self._save('created_parsed', _parse_date(value), overwrite = True)

    
    def _start_expirationdate(self, attrs_d):
        self.push('expired', 1)

    
    def _end_expirationdate(self):
        self._save('expired_parsed', _parse_date(self.pop('expired')), overwrite = True)

    
    def _start_category(self, attrs_d):
        term = attrs_d.get('term')
        scheme = attrs_d.get('scheme', attrs_d.get('domain'))
        label = attrs_d.get('label')
        self._add_tag(term, scheme, label)
        self.push('category', 1)

    _start_keywords = _start_category
    
    def _end_category(self):
        value = self.pop('category')
        if not value:
            return None
        context = None._get_context()
        tags = context['tags']
        if not value and len(tags) and tags[-1]['term']:
            tags[-1]['term'] = value
            return None
        None._add_tag(value, None, None)

    _end_keywords = _end_category
    
    def _start_cloud(self, attrs_d):
        self._get_context()['cloud'] = FeedParserDict(attrs_d)

    
    def _start_link(self, attrs_d):
        attrs_d.setdefault('rel', 'alternate')
        if attrs_d['rel'] == 'self':
            attrs_d.setdefault('type', 'application/atom+xml')
        else:
            attrs_d.setdefault('type', 'text/html')
        context = self._get_context()
        attrs_d = self._enforce_href(attrs_d)
        if 'href' in attrs_d:
            attrs_d['href'] = self.resolve_uri(attrs_d['href'])
        if not self.infeed:
            if not self.inentry:
                expecting_text = self.insource
                context.setdefault('links', [])
                if not self.inentry or self.inimage:
                    context['links'].append(FeedParserDict(attrs_d))
        if 'href' in attrs_d:
            if attrs_d.get('rel') == 'alternate' or self.map_content_type(attrs_d.get('type')) in self.html_types:
                context['link'] = attrs_d['href']
                return None
            return None
        return None
        self.push('link', expecting_text)

    
    def _end_link(self):
        self.pop('link')

    
    def _start_guid(self, attrs_d):
        self.guidislink = attrs_d.get('ispermalink', 'true') == 'true'
        self.push('id', 1)

    _start_id = _start_guid
    
    def _end_guid(self):
