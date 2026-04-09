# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: common.pyc (Python 3.11)

from core import *
from helpers import delimited_list, any_open_tag, any_close_tag
from datetime import datetime

class pyparsing_common:
    """Here are some common low-level expressions that may be useful in
    jump-starting parser development:

    - numeric forms (:class:`integers<integer>`, :class:`reals<real>`,
      :class:`scientific notation<sci_real>`)
    - common :class:`programming identifiers<identifier>`
    - network addresses (:class:`MAC<mac_address>`,
      :class:`IPv4<ipv4_address>`, :class:`IPv6<ipv6_address>`)
    - ISO8601 :class:`dates<iso8601_date>` and
      :class:`datetime<iso8601_datetime>`
    - :class:`UUID<uuid>`
    - :class:`comma-separated list<comma_separated_list>`
    - :class:`url`

    Parse actions:

    - :class:`convertToInteger`
    - :class:`convertToFloat`
    - :class:`convertToDate`
    - :class:`convertToDatetime`
    - :class:`stripHTMLTags`
    - :class:`upcaseTokens`
    - :class:`downcaseTokens`

    Example::

        pyparsing_common.number.runTests('''
            # any int or real number, returned as the appropriate type
            100
            -100
            +100
            3.14159
            6.02e23
            1e-12
            ''')

        pyparsing_common.fnumber.runTests('''
            # any int or real number, returned as float
            100
            -100
            +100
            3.14159
            6.02e23
            1e-12
            ''')

        pyparsing_common.hex_integer.runTests('''
            # hex numbers
            100
            FF
            ''')

        pyparsing_common.fraction.runTests('''
            # fractions
            1/2
            -3/4
            ''')

        pyparsing_common.mixed_integer.runTests('''
            # mixed fractions
            1
            1/2
            -3/4
            1-3/4
            ''')

        import uuid
        pyparsing_common.uuid.setParseAction(tokenMap(uuid.UUID))
        pyparsing_common.uuid.runTests('''
            # uuid
            12345678-1234-5678-1234-567812345678
            ''')

    prints::

        # any int or real number, returned as the appropriate type
        100
        [100]

        -100
        [-100]

        +100
        [100]

        3.14159
        [3.14159]

        6.02e23
        [6.02e+23]

        1e-12
        [1e-12]

        # any int or real number, returned as float
        100
        [100.0]

        -100
        [-100.0]

        +100
        [100.0]

        3.14159
        [3.14159]

        6.02e23
        [6.02e+23]

        1e-12
        [1e-12]

        # hex numbers
        100
        [256]

        FF
        [255]

        # fractions
        1/2
        [0.5]

        -3/4
        [-0.75]

        # mixed fractions
        1
        [1]

        1/2
        [0.5]

        -3/4
        [-0.75]

        1-3/4
        [1.75]

        # uuid
        12345678-1234-5678-1234-567812345678
        [UUID('12345678-1234-5678-1234-567812345678')]
    """
    convert_to_integer = token_map(int)
    convert_to_float = token_map(float)
    integer = Word(nums).set_name('integer').set_parse_action(convert_to_integer)
    hex_integer = Word(hexnums).set_name('hex integer').set_parse_action(token_map(int, 16))
    signed_integer = Regex('[+-]?\\d+').set_name('signed integer').set_parse_action(convert_to_integer)
    fraction = (signed_integer().set_parse_action(convert_to_float) + '/' + signed_integer().set_parse_action(convert_to_float)).set_name('fraction')
    fraction.add_parse_action((lambda tt: tt[0] / tt[-1]))
    mixed_integer = (fraction | signed_integer + Opt(Opt('-').suppress() + fraction)).set_name('fraction or mixed integer-fraction')
    mixed_integer.add_parse_action(sum)
    real = Regex('[+-]?(?:\\d+\\.\\d*|\\.\\d+)').set_name('real number').set_parse_action(convert_to_float)
    sci_real = Regex('[+-]?(?:\\d+(?:[eE][+-]?\\d+)|(?:\\d+\\.\\d*|\\.\\d+)(?:[eE][+-]?\\d+)?)').set_name('real number with scientific notation').set_parse_action(convert_to_float)
    number = (sci_real | real | signed_integer).setName('number').streamline()
    fnumber = Regex('[+-]?\\d+\\.?\\d*([eE][+-]?\\d+)?').set_name('fnumber').set_parse_action(convert_to_float)
    identifier = Word(identchars, identbodychars).set_name('identifier')
    ipv4_address = Regex('(25[0-5]|2[0-4][0-9]|1?[0-9]{1,2})(\\.(25[0-5]|2[0-4][0-9]|1?[0-9]{1,2})){3}').set_name('IPv4 address')
    _ipv6_part = Regex('[0-9a-fA-F]{1,4}').set_name('hex_integer')
    _full_ipv6_address = (_ipv6_part + (':' + _ipv6_part) * 7).set_name('full IPv6 address')
    _short_ipv6_address = (Opt(_ipv6_part + (':' + _ipv6_part) * (0, 6)) + '::' + Opt(_ipv6_part + (':' + _ipv6_part) * (0, 6))).set_name('short IPv6 address')
    _short_ipv6_address.add_condition((lambda t: (lambda .0: pass# WARNING: Decompyle incomplete
)(t()) < 8
))
    _mixed_ipv6_address = ('::ffff:' + ipv4_address).set_name('mixed IPv6 address')
    ipv6_address = Combine((_full_ipv6_address | _mixed_ipv6_address | _short_ipv6_address).set_name('IPv6 address')).set_name('IPv6 address')
    mac_address = Regex('[0-9a-fA-F]{2}([:.-])[0-9a-fA-F]{2}(?:\\1[0-9a-fA-F]{2}){4}').set_name('MAC address')
    convert_to_date = (lambda fmt = None: pass# WARNING: Decompyle incomplete
)()
    convert_to_datetime = (lambda fmt = None: pass# WARNING: Decompyle incomplete
)()
    iso8601_date = Regex('(?P<year>\\d{4})(?:-(?P<month>\\d\\d)(?:-(?P<day>\\d\\d))?)?').set_name('ISO8601 date')
    iso8601_datetime = Regex('(?P<year>\\d{4})-(?P<month>\\d\\d)-(?P<day>\\d\\d)[T ](?P<hour>\\d\\d):(?P<minute>\\d\\d)(:(?P<second>\\d\\d(\\.\\d*)?)?)?(?P<tz>Z|[+-]\\d\\d:?\\d\\d)?').set_name('ISO8601 datetime')
    uuid = Regex('[0-9a-fA-F]{8}(-[0-9a-fA-F]{4}){3}-[0-9a-fA-F]{12}').set_name('UUID')
    _html_stripper = any_open_tag.suppress() | any_close_tag.suppress()
    strip_html_tags = (lambda s = None, l = None, tokens = staticmethod: pyparsing_common._html_stripper.transform_string(tokens[0]))()
    _commasepitem = Combine(OneOrMore(~Literal(',') + ~LineEnd() + Word(printables, exclude_chars = ',') + Opt(White(' \t') + ~FollowedBy(LineEnd() | ',')))).streamline().set_name('commaItem')
    comma_separated_list = delimited_list(Opt(quoted_string.copy() | _commasepitem, default = '')).set_name('comma separated list')
    upcase_tokens = staticmethod(token_map((lambda t: t.upper())))
    downcase_tokens = staticmethod(token_map((lambda t: t.lower())))
    url = Regex('^(?:(?:(?P<scheme>https?|ftp):)?\\/\\/)(?:(?P<auth>\\S+(?::\\S*)?)@)?(?P<host>(?!(?:10|127)(?:\\.\\d{1,3}){3})(?!(?:169\\.254|192\\.168)(?:\\.\\d{1,3}){2})(?!172\\.(?:1[6-9]|2\\d|3[0-1])(?:\\.\\d{1,3}){2})(?:[1-9]\\d?|1\\d\\d|2[01]\\d|22[0-3])(?:\\.(?:1?\\d{1,2}|2[0-4]\\d|25[0-5])){2}(?:\\.(?:[1-9]\\d?|1\\d\\d|2[0-4]\\d|25[0-4]))|(?:(?:[a-z0-9\\u00a1-\\uffff][a-z0-9\\u00a1-\\uffff_-]{0,62})?[a-z0-9\\u00a1-\\uffff]\\.)+(?:[a-z\\u00a1-\\uffff]{2,}\\.?))(:(?P<port>\\d{2,5}))?(?P<path>\\/[^?# ]*)?(\\?(?P<query>[^#]*))?(#(?P<fragment>\\S*))?$').set_name('url')
    convertToInteger = convert_to_integer
    convertToFloat = convert_to_float
    convertToDate = convert_to_date
    convertToDatetime = convert_to_datetime
    stripHTMLTags = strip_html_tags
    upcaseTokens = upcase_tokens
    downcaseTokens = downcase_tokens

_builtin_exprs = vars(pyparsing_common).values()()
