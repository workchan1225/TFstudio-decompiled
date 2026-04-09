# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: networks.pyc (Python 3.11)

import re
from ipaddress import IPv4Address, IPv4Interface, IPv4Network, IPv6Address, IPv6Interface, IPv6Network, _BaseAddress, _BaseNetwork
from typing import TYPE_CHECKING, Any, Collection, Dict, Generator, List, Match, Optional, Pattern, Set, Tuple, Type, Union, cast, no_type_check
from pydantic.v1 import errors
from pydantic.v1.utils import Representation, update_not_none
from pydantic.v1.validators import constr_length_validator, str_validator
NetworkType = Union[(str, bytes, int, Tuple[(Union[(str, bytes, int)], Union[(str, int)])])]
__all__ = [
    'AnyUrl',
    'AnyHttpUrl',
    'FileUrl',
    'HttpUrl',
    'stricturl',
    'EmailStr',
    'NameEmail',
    'IPvAnyAddress',
    'IPvAnyInterface',
    'IPvAnyNetwork',
    'PostgresDsn',
    'CockroachDsn',
    'AmqpDsn',
    'RedisDsn',
    'MongoDsn',
    'KafkaDsn',
    'validate_email']
_url_regex_cache = None
_multi_host_url_regex_cache = None
_ascii_domain_regex_cache = None
_int_domain_regex_cache = None
_host_regex_cache = None
_host_regex = '(?:(?P<ipv4>(?:\\d{1,3}\\.){3}\\d{1,3})(?=$|[/:#?])|(?P<ipv6>\\[[A-F0-9]*:[A-F0-9:]+\\])(?=$|[/:#?])|(?P<domain>[^\\s/:?#]+))?(?::(?P<port>\\d+))?'
_scheme_regex = '(?:(?P<scheme>[a-z][a-z0-9+\\-.]+)://)?'
_user_info_regex = '(?:(?P<user>[^\\s:/]*)(?::(?P<password>[^\\s/]*))?@)?'
_path_regex = '(?P<path>/[^\\s?#]*)?'
_query_regex = '(?:\\?(?P<query>[^\\s#]*))?'
_fragment_regex = '(?:#(?P<fragment>[^\\s#]*))?'

def url_regex():
    pass
# WARNING: Decompyle incomplete


def multi_host_url_regex():
    '''
    Compiled multi host url regex.

    Additionally to `url_regex` it allows to match multiple hosts.
    E.g. host1.db.net,host2.db.net
    '''
    pass
# WARNING: Decompyle incomplete


def ascii_domain_regex():
    pass
# WARNING: Decompyle incomplete


def int_domain_regex():
    pass
# WARNING: Decompyle incomplete


def host_regex():
    pass
# WARNING: Decompyle incomplete


class AnyUrl(str):
    pass
# WARNING: Decompyle incomplete


class AnyHttpUrl(AnyUrl):
    allowed_schemes = {
        'http',
        'https'}
    __slots__ = ()


class HttpUrl(AnyHttpUrl):
    tld_required = True
    max_length = 2083
    hidden_parts = {
        'port'}
    get_default_parts = (lambda parts = None: {
'port': '80' if parts['scheme'] == 'http' else '443' })()


class FileUrl(AnyUrl):
    allowed_schemes = {
        'file'}
    host_required = False
    __slots__ = ()


class MultiHostDsn(AnyUrl):
    pass
# WARNING: Decompyle incomplete


class PostgresDsn(MultiHostDsn):
    allowed_schemes = {
        'postgresql+pg8000',
        'postgresql+asyncpg',
        'postgresql+psycopg',
        'postgresql+psycopg2',
        'postgresql+pygresql',
        'postgresql+psycopg2cffi',
        'postgresql+py-postgresql',
        'postgres',
        'postgresql'}
    user_required = True
    __slots__ = ()


class CockroachDsn(AnyUrl):
    allowed_schemes = {
        'cockroachdb+asyncpg',
        'cockroachdb+psycopg2',
        'cockroachdb'}
    user_required = True


class AmqpDsn(AnyUrl):
    allowed_schemes = {
        'amqp',
        'amqps'}
    host_required = False


class RedisDsn(AnyUrl):
    __slots__ = ()
    allowed_schemes = {
        'redis',
        'rediss'}
    host_required = False
    get_default_parts = (lambda parts = None: {
'domain': 'localhost' if not parts['ipv4'] and parts['ipv6'] else '',
'port': '6379',
'path': '/0' })()


class MongoDsn(AnyUrl):
    allowed_schemes = {
        'mongodb'}
    get_default_parts = (lambda parts = None: {
'port': '27017' })()


class KafkaDsn(AnyUrl):
    allowed_schemes = {
        'kafka'}
    get_default_parts = (lambda parts = None: {
'domain': 'localhost',
'port': '9092' })()


def stricturl(*, strip_whitespace, min_length, max_length, tld_required, host_required, allowed_schemes):
    namespace = dict(strip_whitespace = strip_whitespace, min_length = min_length, max_length = max_length, tld_required = tld_required, host_required = host_required, allowed_schemes = allowed_schemes)
    return type('UrlValue', (AnyUrl,), namespace)


def import_email_validator():
    global email_validator
    
    try:
        import email_validator
        return None
    except ImportError:
        e = None
        raise ImportError('email-validator is not installed, run `pip install pydantic[email]`'), e
        e = None
        del e



class EmailStr(str):
    __modify_schema__ = (lambda cls = None, field_schema = None: field_schema.update(type = 'string', format = 'email'))()
    __get_validators__ = (lambda cls = None: pass# WARNING: Decompyle incomplete
)()
    validate = (lambda cls = None, value = None: validate_email(value)[1])()


class NameEmail(Representation):
    __slots__ = ('name', 'email')
    
    def __init__(self = None, name = None, email = None):
        self.name = name
        self.email = email

    
    def __eq__(self = None, other = None):
        if isinstance(other, NameEmail):
            pass
        return (self.name, self.email) == (other.name, other.email)

    __modify_schema__ = (lambda cls = None, field_schema = None: field_schema.update(type = 'string', format = 'name-email'))()
    __get_validators__ = (lambda cls = None: pass# WARNING: Decompyle incomplete
)()
    validate = (lambda cls = None, value = None: if value.__class__ == cls:
valuevalue = None(value)# WARNING: Decompyle incomplete
)()
    
    def __str__(self = None):
        return f'''{self.name} <{self.email}>'''



class IPvAnyAddress(_BaseAddress):
    __slots__ = ()
    __modify_schema__ = (lambda cls = None, field_schema = None: field_schema.update(type = 'string', format = 'ipvanyaddress'))()
    __get_validators__ = (lambda cls = None: pass# WARNING: Decompyle incomplete
)()
    validate = (lambda cls = None, value = None: try:
IPv4Address(value)except ValueError:
passtry:
IPv6Address(value)except ValueError:
raise errors.IPvAnyAddressError())()


class IPvAnyInterface(_BaseAddress):
    __slots__ = ()
    __modify_schema__ = (lambda cls = None, field_schema = None: field_schema.update(type = 'string', format = 'ipvanyinterface'))()
    __get_validators__ = (lambda cls = None: pass# WARNING: Decompyle incomplete
)()
    validate = (lambda cls = None, value = None: try:
IPv4Interface(value)except ValueError:
passtry:
IPv6Interface(value)except ValueError:
raise errors.IPvAnyInterfaceError())()


class IPvAnyNetwork(_BaseNetwork):
    __modify_schema__ = (lambda cls = None, field_schema = None: field_schema.update(type = 'string', format = 'ipvanynetwork'))()
    __get_validators__ = (lambda cls = None: pass# WARNING: Decompyle incomplete
)()
    validate = (lambda cls = None, value = None: try:
IPv4Network(value)except ValueError:
passtry:
IPv6Network(value)except ValueError:
raise errors.IPvAnyNetworkError())()

pretty_email_regex = re.compile('([\\w ]*?) *<(.*)> *')
MAX_EMAIL_LENGTH = 2048

def validate_email(value = None):
    '''
    Email address validation using https://pypi.org/project/email-validator/
    Notes:
    * raw ip address (literal) domain parts are not allowed.
    * "John Doe <local_part@domain.com>" style "pretty" email addresses are processed
    * spaces are striped from the beginning and end of addresses but no error is raised
    '''
    pass
# WARNING: Decompyle incomplete
