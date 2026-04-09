# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: headerregistry.pyc (Python 3.11)

__doc__ = 'Representing and manipulating email headers via custom objects.\n\nThis module provides an implementation of the HeaderRegistry API.\nThe implementation is designed to flexibly follow RFC5322 rules.\n'
from types import MappingProxyType
from email import utils
from email import errors
from email import _header_value_parser as parser

class Address:
    
    def __init__(self, display_name, username, domain, addr_spec = ('', '', '', None)):
        """Create an object representing a full email address.

        An address can have a 'display_name', a 'username', and a 'domain'.  In
        addition to specifying the username and domain separately, they may be
        specified together by using the addr_spec keyword *instead of* the
        username and domain keywords.  If an addr_spec string is specified it
        must be properly quoted according to RFC 5322 rules; an error will be
        raised if it is not.

        An Address object has display_name, username, domain, and addr_spec
        attributes, all of which are read-only.  The addr_spec and the string
        value of the object are both quoted according to RFC5322 rules, but
        without any Content Transfer Encoding.

        """
        inputs = ''.join(filter(None, (display_name, username, domain, addr_spec)))
        if '\r' in inputs or '\n' in inputs:
            raise ValueError('invalid arguments; address parts cannot contain CR or LF')
    # WARNING: Decompyle incomplete

    display_name = (lambda self: self._display_name)()
    username = (lambda self: self._username)()
    domain = (lambda self: self._domain)()
    addr_spec = (lambda self: lp = self.usernameif not parser.DOT_ATOM_ENDS.isdisjoint(lp):
lp = parser.quote_string(lp)if self.domain:
lp + '@' + self.domainif not None:
'<>')()
    
    def __repr__(self):
        return '{}(display_name={!r}, username={!r}, domain={!r})'.format(self.__class__.__name__, self.display_name, self.username, self.domain)

    
    def __str__(self):
        disp = self.display_name
        if not parser.SPECIALS.isdisjoint(disp):
            disp = parser.quote_string(disp)
        if disp:
            addr_spec = '' if self.addr_spec == '<>' else self.addr_spec
            return '{} <{}>'.format(disp, addr_spec)
        return None.addr_spec

    
    def __eq__(self, other):
