# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: networks.pyc (Python 3.11)

'''The networks module contains types for common network-related fields.'''
from __future__ import annotations as _annotations
import dataclasses as _dataclasses
import re
from dataclasses import fields
from functools import lru_cache
from importlib.metadata import version
from ipaddress import IPv4Address, IPv4Interface, IPv4Network, IPv6Address, IPv6Interface, IPv6Network
from typing import TYPE_CHECKING, Annotated, Any, ClassVar
from pydantic_core import MultiHostHost, PydanticCustomError, PydanticSerializationUnexpectedValue, SchemaSerializer, core_schema
from pydantic_core import MultiHostUrl as _CoreMultiHostUrl
from pydantic_core import Url as _CoreUrl
from typing_extensions import Self, TypeAlias
from pydantic.errors import PydanticUserError
from _internal import _repr, _schema_generation_shared
from _migration import getattr_migration
from annotated_handlers import GetCoreSchemaHandler
from json_schema import JsonSchemaValue
from type_adapter import TypeAdapter
if TYPE_CHECKING:
    import email_validator
    NetworkType: 'TypeAlias' = 'str | bytes | int | tuple[str | bytes | int, str | int]'
else:
    email_validator = None
__all__ = [
    'AnyUrl',
    'AnyHttpUrl',
    'FileUrl',
    'FtpUrl',
    'HttpUrl',
    'WebsocketUrl',
    'AnyWebsocketUrl',
    'UrlConstraints',
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
    'NatsDsn',
    'validate_email',
    'MySQLDsn',
    'MariaDBDsn',
    'ClickHouseDsn',
    'SnowflakeDsn']
UrlConstraints = <NODE:12>()

class _BaseUrl:
    _url: '_CoreUrl' = UrlConstraints()
    
    def __init__(self = None, url = None):
        self._url = _build_type_adapter(self.__class__).validate_python(url)._url

    scheme = (lambda self = None: self._url.scheme)()
    username = (lambda self = None: self._url.username)()
    password = (lambda self = None: self._url.password)()
    host = (lambda self = None: self._url.host)()
    
    def unicode_host(self = None):
        '''The host part of the URL as a unicode string, or `None`.

        e.g. `host` in `https://user:pass@host:port/path?query#fragment`

        If the URL must be punycode encoded, this is the decoded host, e.g if the input URL is `https://£££.com`,
        `unicode_host()` will be `£££.com`
        '''
        return self._url.unicode_host()

    port = (lambda self = None: self._url.port)()
    path = (lambda self = None: self._url.path)()
    query = (lambda self = None: self._url.query)()
    
    def query_params(self = None):
        """The query part of the URL as a list of key-value pairs.

        e.g. `[('foo', 'bar')]` in `https://user:pass@host:port/path?foo=bar#fragment`
        """
        return self._url.query_params()

    fragment = (lambda self = None: self._url.fragment)()
    
    def unicode_string(self = None):
        '''The URL as a unicode string, unlike `__str__()` this will not punycode encode the host.

        If the URL must be punycode encoded, this is the decoded string, e.g if the input URL is `https://£££.com`,
        `unicode_string()` will be `https://£££.com`
        '''
        return self._url.unicode_string()

    
    def encoded_string(self = None):
        """The URL's encoded string representation via __str__().

        This returns the punycode-encoded host version of the URL as a string.
        """
        return str(self)

    
    def __str__(self = None):
        '''The URL as a string, this will punycode encode the host if required.'''
        return str(self._url)

    
    def __repr__(self = None):
        return f'''{self.__class__.__name__}({str(self._url)!r})'''

    
    def __deepcopy__(self = None, memo = None):
        return self.__class__(self._url)

    
    def __eq__(self = None, other = None):
        if self.__class__ is other.__class__:
            pass
        return self._url == other._url

    
    def __lt__(self = None, other = None):
        if self.__class__ is other.__class__:
            pass
        return self._url < other._url

    
    def __gt__(self = None, other = None):
        if self.__class__ is other.__class__:
            pass
        return self._url > other._url

    
    def __le__(self = None, other = None):
        if self.__class__ is other.__class__:
            pass
        return self._url <= other._url

    
    def __ge__(self = None, other = None):
        if self.__class__ is other.__class__:
            pass
        return self._url >= other._url

    
    def __hash__(self = None):
        return hash(self._url)

    
    def __len__(self = None):
        return len(str(self._url))

    build = (lambda cls = None, *, scheme: cls(_CoreUrl.build(scheme = scheme, username = username, password = password, host = host, port = port, path = path, query = query, fragment = fragment)))()
    serialize_url = (lambda cls = None, url = None, info = classmethod: if not isinstance(url, cls):
raise PydanticSerializationUnexpectedValue(f'''Expected `{cls}` but got `{type(url)}` with value `\'{url}\'` - serialized value may not be as expected.''')if info.mode == 'json':
str(url))()
    __get_pydantic_core_schema__ = (lambda cls = None, source = None, handler = classmethod: pass# WARNING: Decompyle incomplete
)()
    __get_pydantic_json_schema__ = (lambda cls = None, core_schema = None, handler = classmethod: inner_schema = core_schema['schema'] if core_schema['type'] == 'function-wrap' else core_schemahandler(inner_schema))()
    __pydantic_serializer__ = SchemaSerializer(core_schema.any_schema(serialization = core_schema.to_string_ser_schema()))


class _BaseMultiHostUrl:
    _url: '_CoreMultiHostUrl' = UrlConstraints()
    
    def __init__(self = None, url = None):
        self._url = _build_type_adapter(self.__class__).validate_python(url)._url

    scheme = (lambda self = None: self._url.scheme)()
    path = (lambda self = None: self._url.path)()
    query = (lambda self = None: self._url.query)()
    
    def query_params(self = None):
        """The query part of the URL as a list of key-value pairs.

        e.g. `[('foo', 'bar')]` in `https://foo.com,bar.com/path?foo=bar#fragment`
        """
        return self._url.query_params()

    fragment = (lambda self = None: self._url.fragment)()
    
    def hosts(self = None):
        '''The hosts of the `MultiHostUrl` as [`MultiHostHost`][pydantic_core.MultiHostHost] typed dicts.

        ```python
        from pydantic_core import MultiHostUrl

        mhu = MultiHostUrl(\'https://foo.com:123,foo:bar@bar.com/path\')
        print(mhu.hosts())
        """
        [
            {\'username\': None, \'password\': None, \'host\': \'foo.com\', \'port\': 123},
            {\'username\': \'foo\', \'password\': \'bar\', \'host\': \'bar.com\', \'port\': 443}
        ]
        ```
        Returns:
            A list of dicts, each representing a host.
        '''
        return self._url.hosts()

    
    def encoded_string(self = None):
        """The URL's encoded string representation via __str__().

        This returns the punycode-encoded host version of the URL as a string.
        """
        return str(self)

    
    def unicode_string(self = None):
        '''The URL as a unicode string, unlike `__str__()` this will not punycode encode the hosts.'''
        return self._url.unicode_string()

    
    def __str__(self = None):
        '''The URL as a string, this will punycode encode the host if required.'''
        return str(self._url)

    
    def __repr__(self = None):
        return f'''{self.__class__.__name__}({str(self._url)!r})'''

    
    def __deepcopy__(self = None, memo = None):
        return self.__class__(self._url)

    
    def __eq__(self = None, other = None):
        if self.__class__ is other.__class__:
            pass
        return self._url == other._url

    
    def __hash__(self = None):
        return hash(self._url)

    
    def __len__(self = None):
        return len(str(self._url))

    build = (lambda cls = None, *, scheme: cls(_CoreMultiHostUrl.build(scheme = scheme, hosts = hosts, username = username, password = password, host = host, port = port, path = path, query = query, fragment = fragment)))()
    serialize_url = (lambda cls = None, url = None, info = classmethod: if not isinstance(url, cls):
raise PydanticSerializationUnexpectedValue(f'''Expected `{cls}` but got `{type(url)}` with value `\'{url}\'` - serialized value may not be as expected.''')if info.mode == 'json':
str(url))()
    __get_pydantic_core_schema__ = (lambda cls = None, source = None, handler = classmethod: pass# WARNING: Decompyle incomplete
)()
    __get_pydantic_json_schema__ = (lambda cls = None, core_schema = None, handler = classmethod: inner_schema = core_schema['schema'] if core_schema['type'] == 'function-wrap' else core_schemahandler(inner_schema))()
    __pydantic_serializer__ = SchemaSerializer(core_schema.any_schema(serialization = core_schema.to_string_ser_schema()))

_build_type_adapter = (lambda cls = None: TypeAdapter(cls))()

class AnyUrl(_BaseUrl):
    '''Base type for all URLs.

    * Any scheme allowed
    * Top-level domain (TLD) not required
    * Host not required

    Assuming an input URL of `http://samuel:pass@example.com:8000/the/path/?query=here#fragment=is;this=bit`,
    the types export the following properties:

    - `scheme`: the URL scheme (`http`), always set.
    - `host`: the URL host (`example.com`).
    - `username`: optional username if included (`samuel`).
    - `password`: optional password if included (`pass`).
    - `port`: optional port (`8000`).
    - `path`: optional path (`/the/path/`).
    - `query`: optional URL query (for example, `GET` arguments or "search string", such as `query=here`).
    - `fragment`: optional fragment (`fragment=is;this=bit`).
    '''
    pass


class AnyHttpUrl(AnyUrl):
    '''A type that will accept any http or https URL.

    * TLD not required
    * Host not required
    '''
    _constraints = UrlConstraints(allowed_schemes = [
        'http',
        'https'])


class HttpUrl(AnyUrl):
    '''A type that will accept any http or https URL.

    * TLD not required
    * Host not required
    * Max length 2083

    ```python
    from pydantic import BaseModel, HttpUrl, ValidationError

    class MyModel(BaseModel):
        url: HttpUrl

    m = MyModel(url=\'http://www.example.com\')  # (1)!
    print(m.url)
    #> http://www.example.com/

    try:
        MyModel(url=\'ftp://invalid.url\')
    except ValidationError as e:
        print(e)
        \'\'\'
        1 validation error for MyModel
        url
          URL scheme should be \'http\' or \'https\' [type=url_scheme, input_value=\'ftp://invalid.url\', input_type=str]
        \'\'\'

    try:
        MyModel(url=\'not a url\')
    except ValidationError as e:
        print(e)
        \'\'\'
        1 validation error for MyModel
        url
          Input should be a valid URL, relative URL without a base [type=url_parsing, input_value=\'not a url\', input_type=str]
        \'\'\'
    ```

    1. Note: mypy would prefer `m = MyModel(url=HttpUrl(\'http://www.example.com\'))`, but Pydantic will convert the string to an HttpUrl instance anyway.

    "International domains" (e.g. a URL where the host or TLD includes non-ascii characters) will be encoded via
    [punycode](https://en.wikipedia.org/wiki/Punycode) (see
    [this article](https://www.xudongz.com/blog/2017/idn-phishing/) for a good description of why this is important):

    ```python
    from pydantic import BaseModel, HttpUrl

    class MyModel(BaseModel):
        url: HttpUrl

    m1 = MyModel(url=\'http://puny£code.com\')
    print(m1.url)
    #> http://xn--punycode-eja.com/
    m2 = MyModel(url=\'https://www.аррӏе.com/\')
    print(m2.url)
    #> https://www.xn--80ak6aa92e.com/
    m3 = MyModel(url=\'https://www.example.珠宝/\')
    print(m3.url)
    #> https://www.example.xn--pbt977c/
    ```


    !!! warning "Underscores in Hostnames"
        In Pydantic, underscores are allowed in all parts of a domain except the TLD.
        Technically this might be wrong - in theory the hostname cannot have underscores, but subdomains can.

        To explain this; consider the following two cases:

        - `exam_ple.co.uk`: the hostname is `exam_ple`, which should not be allowed since it contains an underscore.
        - `foo_bar.example.com` the hostname is `example`, which should be allowed since the underscore is in the subdomain.

        Without having an exhaustive list of TLDs, it would be impossible to differentiate between these two. Therefore
        underscores are allowed, but you can always do further validation in a validator if desired.

        Also, Chrome, Firefox, and Safari all currently accept `http://exam_ple.com` as a URL, so we\'re in good
        (or at least big) company.
    '''
    _constraints = UrlConstraints(max_length = 2083, allowed_schemes = [
        'http',
        'https'])


class AnyWebsocketUrl(AnyUrl):
    '''A type that will accept any ws or wss URL.

    * TLD not required
    * Host not required
    '''
    _constraints = UrlConstraints(allowed_schemes = [
        'ws',
        'wss'])


class WebsocketUrl(AnyUrl):
    '''A type that will accept any ws or wss URL.

    * TLD not required
    * Host not required
    * Max length 2083
    '''
    _constraints = UrlConstraints(max_length = 2083, allowed_schemes = [
        'ws',
        'wss'])


class FileUrl(AnyUrl):
    '''A type that will accept any file URL.

    * Host not required
    '''
    _constraints = UrlConstraints(allowed_schemes = [
        'file'])


class FtpUrl(AnyUrl):
    '''A type that will accept ftp URL.

    * TLD not required
    * Host not required
    '''
    _constraints = UrlConstraints(allowed_schemes = [
        'ftp'])


class PostgresDsn(_BaseMultiHostUrl):
    """A type that will accept any Postgres DSN.

    * User info required
    * TLD not required
    * Host required
    * Supports multiple hosts

    If further validation is required, these properties can be used by validators to enforce specific behaviour:

    ```python
    from pydantic import (
        BaseModel,
        HttpUrl,
        PostgresDsn,
        ValidationError,
        field_validator,
    )

    class MyModel(BaseModel):
        url: HttpUrl

    m = MyModel(url='http://www.example.com')

    # the repr() method for a url will display all properties of the url
    print(repr(m.url))
    #> HttpUrl('http://www.example.com/')
    print(m.url.scheme)
    #> http
    print(m.url.host)
    #> www.example.com
    print(m.url.port)
    #> 80

    class MyDatabaseModel(BaseModel):
        db: PostgresDsn

        @field_validator('db')
        def check_db_name(cls, v):
            assert v.path and len(v.path) > 1, 'database must be provided'
            return v

    m = MyDatabaseModel(db='postgres://user:pass@localhost:5432/foobar')
    print(m.db)
    #> postgres://user:pass@localhost:5432/foobar

    try:
        MyDatabaseModel(db='postgres://user:pass@localhost:5432')
    except ValidationError as e:
        print(e)
        '''
        1 validation error for MyDatabaseModel
        db
          Assertion failed, database must be provided
        assert (None)
         +  where None = PostgresDsn('postgres://user:pass@localhost:5432').path [type=assertion_error, input_value='postgres://user:pass@localhost:5432', input_type=str]
        '''
    ```
    """
    _constraints = UrlConstraints(host_required = True, allowed_schemes = [
        'postgres',
        'postgresql',
        'postgresql+asyncpg',
        'postgresql+pg8000',
        'postgresql+psycopg',
        'postgresql+psycopg2',
        'postgresql+psycopg2cffi',
        'postgresql+py-postgresql',
        'postgresql+pygresql'])
    host = (lambda self = None: self._url.host)()


class CockroachDsn(AnyUrl):
    '''A type that will accept any Cockroach DSN.

    * User info required
    * TLD not required
    * Host required
    '''
    _constraints = UrlConstraints(host_required = True, allowed_schemes = [
        'cockroachdb',
        'cockroachdb+psycopg2',
        'cockroachdb+asyncpg'])
    host = (lambda self = None: self._url.host)()


class AmqpDsn(AnyUrl):
    '''A type that will accept any AMQP DSN.

    * User info required
    * TLD not required
    * Host not required
    '''
    _constraints = UrlConstraints(allowed_schemes = [
        'amqp',
        'amqps'])


class RedisDsn(AnyUrl):
    '''A type that will accept any Redis DSN.

    * User info required
    * TLD not required
    * Host required (e.g., `rediss://:pass@localhost`)
    '''
    _constraints = UrlConstraints(allowed_schemes = [
        'redis',
        'rediss'], default_host = 'localhost', default_port = 6379, default_path = '/0', host_required = True)
    host = (lambda self = None: self._url.host)()


class MongoDsn(_BaseMultiHostUrl):
    """A type that will accept any MongoDB DSN.

    * User info not required
    * Database name not required
    * Port not required
    * User info may be passed without user part (e.g., `mongodb://mongodb0.example.com:27017`).

    !!! warning
        If a port isn't specified, the default MongoDB port `27017` will be used. If this behavior is
        undesirable, you can use the following:

        ```python
        from typing import Annotated

        from pydantic import UrlConstraints
        from pydantic_core import MultiHostUrl

        MongoDsnNoDefaultPort = Annotated[
            MultiHostUrl,
            UrlConstraints(allowed_schemes=['mongodb', 'mongodb+srv']),
        ]
        ```
    """
    _constraints = UrlConstraints(allowed_schemes = [
        'mongodb',
        'mongodb+srv'], default_port = 27017)


class KafkaDsn(AnyUrl):
    '''A type that will accept any Kafka DSN.

    * User info required
    * TLD not required
    * Host not required
    '''
    _constraints = UrlConstraints(allowed_schemes = [
        'kafka'], default_host = 'localhost', default_port = 9092)


class NatsDsn(_BaseMultiHostUrl):
    '''A type that will accept any NATS DSN.

    NATS is a connective technology built for the ever increasingly hyper-connected world.
    It is a single technology that enables applications to securely communicate across
    any combination of cloud vendors, on-premise, edge, web and mobile, and devices.
    More: https://nats.io
    '''
    _constraints = UrlConstraints(allowed_schemes = [
        'nats',
        'tls',
        'ws',
        'wss'], default_host = 'localhost', default_port = 4222)


class MySQLDsn(AnyUrl):
    '''A type that will accept any MySQL DSN.

    * User info required
    * TLD not required
    * Host not required
    '''
    _constraints = UrlConstraints(allowed_schemes = [
        'mysql',
        'mysql+mysqlconnector',
        'mysql+aiomysql',
        'mysql+asyncmy',
        'mysql+mysqldb',
        'mysql+pymysql',
        'mysql+cymysql',
        'mysql+pyodbc'], default_port = 3306, host_required = True)


class MariaDBDsn(AnyUrl):
    '''A type that will accept any MariaDB DSN.

    * User info required
    * TLD not required
    * Host not required
    '''
    _constraints = UrlConstraints(allowed_schemes = [
        'mariadb',
        'mariadb+mariadbconnector',
        'mariadb+pymysql'], default_port = 3306)


class ClickHouseDsn(AnyUrl):
    '''A type that will accept any ClickHouse DSN.

    * User info required
    * TLD not required
    * Host not required
    '''
    _constraints = UrlConstraints(allowed_schemes = [
        'clickhouse+native',
        'clickhouse+asynch',
        'clickhouse+http',
        'clickhouse',
        'clickhouses',
        'clickhousedb'], default_host = 'localhost', default_port = 9000)


class SnowflakeDsn(AnyUrl):
    '''A type that will accept any Snowflake DSN.

    * User info required
    * TLD not required
    * Host required
    '''
    _constraints = UrlConstraints(allowed_schemes = [
        'snowflake'], host_required = True)
    host = (lambda self = None: self._url.host)()


def import_email_validator():
    global email_validator
    
    try:
        import email_validator
    except ImportError:
        e = None
        raise ImportError("email-validator is not installed, run `pip install 'pydantic[email]'`"), e
        e = None
        del e

    if not version('email-validator').partition('.')[0] == '2':
        raise ImportError('email-validator version >= 2.0 required, run pip install -U email-validator')


class NameEmail(_repr.Representation):
    """
    Info:
        To use this type, you need to install the optional
        [`email-validator`](https://github.com/JoshData/python-email-validator) package:

        ```bash
        pip install email-validator
        ```

    Validate a name and email address combination, as specified by
    [RFC 5322](https://datatracker.ietf.org/doc/html/rfc5322#section-3.4).

    The `NameEmail` has two properties: `name` and `email`.
    In case the `name` is not provided, it's inferred from the email address.

    ```python
    from pydantic import BaseModel, NameEmail

    class User(BaseModel):
        email: NameEmail

    user = User(email='Fred Bloggs <fred.bloggs@example.com>')
    print(user.email)
    #> Fred Bloggs <fred.bloggs@example.com>
    print(user.email.name)
    #> Fred Bloggs

    user = User(email='fred.bloggs@example.com')
    print(user.email)
    #> fred.bloggs <fred.bloggs@example.com>
    print(user.email.name)
    #> fred.bloggs
    ```
    """
    __slots__ = ('name', 'email')
    
    def __init__(self = None, name = None, email = None):
        self.name = name
        self.email = email

    
    def __eq__(self = None, other = None):
        if isinstance(other, NameEmail):
            pass
        return (self.name, self.email) == (other.name, other.email)

    __get_pydantic_json_schema__ = (lambda cls = None, core_schema = None, handler = classmethod: field_schema = handler(core_schema)field_schema.update(type = 'string', format = 'name-email')field_schema)()
    __get_pydantic_core_schema__ = (lambda cls = None, _source = None, _handler = classmethod: import_email_validator()core_schema.no_info_after_validator_function(cls._validate, core_schema.json_or_python_schema(json_schema = core_schema.str_schema(), python_schema = core_schema.union_schema([
core_schema.is_instance_schema(cls),
core_schema.str_schema()], custom_error_type = 'name_email_type', custom_error_message = 'Input is not a valid NameEmail'), serialization = core_schema.to_string_ser_schema())))()
    _validate = (lambda cls = None, input_value = None: if isinstance(input_value, str):
(name, email) = validate_email(input_value)cls(name, email))()
    
    def __str__(self = None):
        if '@' in self.name:
            return f'''"{self.name}" <{self.email}>'''
        return f'''{None.name} <{self.email}>'''


IPvAnyAddressType: 'TypeAlias' = 'IPv4Address | IPv6Address'
IPvAnyInterfaceType: 'TypeAlias' = 'IPv4Interface | IPv6Interface'
IPvAnyNetworkType: 'TypeAlias' = 'IPv4Network | IPv6Network'

def _build_pretty_email_regex():
    name_chars = "[\\w!#$%&\\'*+\\-/=?^_`{|}~]"
    unquoted_name_group = f'''((?:{name_chars}+\\s+)*{name_chars}+)'''
    quoted_name_group = '"((?:[^"]|\\")+)"'
    email_group = '<(.+)>'
    return re.compile(f'''\\s*(?:{unquoted_name_group}|{quoted_name_group})?\\s*{email_group}\\s*''')

pretty_email_regex = _build_pretty_email_regex()
MAX_EMAIL_LENGTH = 2048

def validate_email(value = None):
    '''Email address validation using [email-validator](https://pypi.org/project/email-validator/).

    Returns:
        A tuple containing the local part of the email (or the name for "pretty" email addresses)
            and the normalized email.

    Raises:
        PydanticCustomError: If the email is invalid.

    Note:
        Note that:

        * Raw IP address (literal) domain parts are not allowed.
        * `"John Doe <local_part@domain.com>"` style "pretty" email addresses are processed.
        * Spaces are striped from the beginning and end of addresses, but no error is raised.
    '''
    pass
# WARNING: Decompyle incomplete

__getattr__ = getattr_migration(__name__)
