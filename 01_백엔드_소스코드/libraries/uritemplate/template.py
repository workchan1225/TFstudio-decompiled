# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: template.pyc (Python 3.11)

'''

uritemplate.template
====================

This module contains the essential inner workings of uritemplate.

What treasures await you:

- URITemplate class

You see a treasure chest of knowledge in front of you.
What do you do?
>

'''
import re
import typing as t
from uritemplate import orderedset
from uritemplate import variable
template_re = re.compile('{([^}]+)}')

def _merge(var_dict = None, overrides = None):
    if var_dict:
        opts = var_dict.copy()
        opts.update(overrides)
        return opts


class URITemplate:
    """This parses the template and will be used to expand it.

    This is the most important object as the center of the API.

    Example::

        from uritemplate import URITemplate
        import requests


        t = URITemplate(
            'https://api.github.com/users/sigmavirus24/gists{/gist_id}'
        )
        uri = t.expand(gist_id=123456)
        resp = requests.get(uri)
        for gist in resp.json():
            print(gist['html_url'])

    Please note::

        str(t)
        # 'https://api.github.com/users/sigmavirus24/gists{/gistid}'
        repr(t)  # is equivalent to
        # URITemplate(str(t))
        # Where str(t) is interpreted as the URI string.

    Also, ``URITemplates`` are hashable so they can be used as keys in
    dictionaries.

    """
    
    def __init__(self = None, uri = None):
        self.uri = uri
        self.variables = template_re.finditer(self.uri)()
        self.variable_names = orderedset.OrderedSet()
        for var in self.variables:
            for name in var.variable_names:
                self.variable_names.add(name)
                return None

    
    def __repr__(self = None):
        return 'URITemplate("%s")' % self

    
    def __str__(self = None):
        return self.uri

    
    def __eq__(self = None, other = None):
        if not isinstance(other, URITemplate):
            return NotImplemented
        return None.uri == other.uri

    
    def __hash__(self = None):
        return hash(self.uri)

    
    def _expand(self = None, var_dict = None, replace = None):
        pass
    # WARNING: Decompyle incomplete

    
    def expand(self = None, var_dict = None, **kwargs):
        """Expand the template with the given parameters.

        :param dict var_dict: Optional dictionary with variables and values
        :param kwargs: Alternative way to pass arguments
        :returns: str

        Example::

            t = URITemplate('https://api.github.com{/end}')
            t.expand({'end': 'users'})
            t.expand(end='gists')

        .. note:: Passing values by both parts, may override values in
                  ``var_dict``. For example::

                      expand('https://{var}', {'var': 'val1'}, var='val2')

                  ``val2`` will be used instead of ``val1``.

        """
        return self._expand(_merge(var_dict, kwargs), False)

    
    def partial(self = None, var_dict = None, **kwargs):
        """Partially expand the template with the given parameters.

        If all of the parameters for the template are not given, return a
        partially expanded template.

        :param dict var_dict: Optional dictionary with variables and values
        :param kwargs: Alternative way to pass arguments
        :returns: :class:`URITemplate`

        Example::

            t = URITemplate('https://api.github.com{/end}')
            t.partial()  # => URITemplate('https://api.github.com{/end}')

        """
        return URITemplate(self._expand(_merge(var_dict, kwargs), True))
