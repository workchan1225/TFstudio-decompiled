# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: ipaddress.pyc (Python 3.11)

'''A fast, lightweight IPv4/IPv6 manipulation library in Python.

This library is used to create/poke/manipulate IPv4 and IPv6 addresses
and networks.

'''
__version__ = '1.0'
import functools
IPV4LENGTH = 32
IPV6LENGTH = 128

class AddressValueError(ValueError):
    '''A Value Error related to the address.'''
    pass


class NetmaskValueError(ValueError):
    '''A Value Error related to the netmask.'''
    pass


def ip_address(address):
    """Take an IP string/int and return an object of the correct type.

    Args:
        address: A string or integer, the IP address.  Either IPv4 or
          IPv6 addresses may be supplied; integers less than 2**32 will
          be considered to be IPv4 by default.

    Returns:
        An IPv4Address or IPv6Address object.

    Raises:
        ValueError: if the *address* passed isn't either a v4 or a v6
          address

    """
    
    try:
        return IPv4Address(address)
    except (AddressValueError, NetmaskValueError):
        pass

    
    try:
        return IPv6Address(address)
    except (AddressValueError, NetmaskValueError):
        pass

    raise ValueError(f'''{address!r} does not appear to be an IPv4 or IPv6 address''')


def ip_network(address, strict = (True,)):
    """Take an IP string/int and return an object of the correct type.

    Args:
        address: A string or integer, the IP network.  Either IPv4 or
          IPv6 networks may be supplied; integers less than 2**32 will
          be considered to be IPv4 by default.

    Returns:
        An IPv4Network or IPv6Network object.

    Raises:
        ValueError: if the string passed isn't either a v4 or a v6
          address. Or if the network has host bits set.

    """
    
    try:
        return IPv4Network(address, strict)
    except (AddressValueError, NetmaskValueError):
        pass

    
    try:
        return IPv6Network(address, strict)
    except (AddressValueError, NetmaskValueError):
        pass

    raise ValueError(f'''{address!r} does not appear to be an IPv4 or IPv6 network''')


def ip_interface(address):
    """Take an IP string/int and return an object of the correct type.

    Args:
        address: A string or integer, the IP address.  Either IPv4 or
          IPv6 addresses may be supplied; integers less than 2**32 will
          be considered to be IPv4 by default.

    Returns:
        An IPv4Interface or IPv6Interface object.

    Raises:
        ValueError: if the string passed isn't either a v4 or a v6
          address.

    Notes:
        The IPv?Interface classes describe an Address on a particular
        Network, so they're basically a combination of both the Address
        and Network classes.

    """
    
    try:
        return IPv4Interface(address)
    except (AddressValueError, NetmaskValueError):
        pass

    
    try:
        return IPv6Interface(address)
    except (AddressValueError, NetmaskValueError):
        pass

    raise ValueError(f'''{address!r} does not appear to be an IPv4 or IPv6 interface''')


def v4_int_to_packed(address):
    '''Represent an address as 4 packed bytes in network (big-endian) order.

    Args:
        address: An integer representation of an IPv4 IP address.

    Returns:
        The integer address packed as 4 bytes in network (big-endian) order.

    Raises:
        ValueError: If the integer is negative or too large to be an
          IPv4 IP address.

    '''
    
    try:
        return address.to_bytes(4)
    except OverflowError:
        raise ValueError('Address negative or too large for IPv4')



def v6_int_to_packed(address):
    '''Represent an address as 16 packed bytes in network (big-endian) order.

    Args:
        address: An integer representation of an IPv6 IP address.

    Returns:
        The integer address packed as 16 bytes in network (big-endian) order.

    '''
    
    try:
        return address.to_bytes(16)
    except OverflowError:
        raise ValueError('Address negative or too large for IPv6')



def _split_optional_netmask(address):
    '''Helper to split the netmask and raise AddressValueError if needed'''
    addr = str(address).split('/')
    if len(addr) > 2:
        raise AddressValueError(f'''Only one \'/\' permitted in {address!r}''')
    return addr


def _find_address_range(addresses):
    '''Find a sequence of sorted deduplicated IPv#Address.

    Args:
        addresses: a list of IPv#Address objects.

    Yields:
        A tuple containing the first and last IP addresses in the sequence.

    '''
    pass
# WARNING: Decompyle incomplete


def _count_righthand_zero_bits(number, bits):
    '''Count the number of zero bits on the right hand side.

    Args:
        number: an integer.
        bits: maximum number of bits to count.

    Returns:
        The number of zero bits on the right hand side of the number.

    '''
    if number == 0:
        return bits
    return None(bits, (~number & number - 1).bit_length())


def summarize_address_range(first, last):
    """Summarize a network range given the first and last IP addresses.

    Example:
        >>> list(summarize_address_range(IPv4Address('192.0.2.0'),
        ...                              IPv4Address('192.0.2.130')))
        ...                                #doctest: +NORMALIZE_WHITESPACE
        [IPv4Network('192.0.2.0/25'), IPv4Network('192.0.2.128/31'),
         IPv4Network('192.0.2.130/32')]

    Args:
        first: the first IPv4Address or IPv6Address in the range.
        last: the last IPv4Address or IPv6Address in the range.

    Returns:
        An iterator of the summarized IPv(4|6) network objects.

    Raise:
        TypeError:
            If the first and last objects are not IP addresses.
            If the first and last objects are not the same version.
        ValueError:
            If the last object is not greater than the first.
            If the version of the first address is not 4 or 6.

    """
    pass
# WARNING: Decompyle incomplete


def _collapse_addresses_internal(addresses):
    """Loops through the addresses, collapsing concurrent netblocks.

    Example:

        ip1 = IPv4Network('192.0.2.0/26')
        ip2 = IPv4Network('192.0.2.64/26')
        ip3 = IPv4Network('192.0.2.128/26')
        ip4 = IPv4Network('192.0.2.192/26')

        _collapse_addresses_internal([ip1, ip2, ip3, ip4]) ->
          [IPv4Network('192.0.2.0/24')]

        This shouldn't be called directly; it is called via
          collapse_addresses([]).

    Args:
        addresses: A list of IPv4Network's or IPv6Network's

    Returns:
        A list of IPv4Network's or IPv6Network's depending on what we were
        passed.

    """
    pass
# WARNING: Decompyle incomplete


def collapse_addresses(addresses):
    """Collapse a list of IP objects.

    Example:
        collapse_addresses([IPv4Network('192.0.2.0/25'),
                            IPv4Network('192.0.2.128/25')]) ->
                           [IPv4Network('192.0.2.0/24')]

    Args:
        addresses: An iterator of IPv4Network or IPv6Network objects.

    Returns:
        An iterator of the collapsed IPv(4|6)Network objects.

    Raises:
        TypeError: If passed a list of mixed version objects.

    """
    addrs = []
    ips = []
    nets = []
    for ip in addresses:
        if isinstance(ip, _BaseAddress):
            if ips and ips[-1]._version != ip._version:
                raise TypeError(f'''{ip!s} and {ips[-1]!s} are not of the same version''')
            ips.append(ip)
            continue
        if ip._prefixlen == ip._max_prefixlen:
            if ips and ips[-1]._version != ip._version:
                raise TypeError(f'''{ip!s} and {ips[-1]!s} are not of the same version''')
            ips.append(ip.ip)
            continue
            except AttributeError:
                ips.append(ip.network_address)
                continue
        if nets and nets[-1]._version != ip._version:
            raise TypeError(f'''{ip!s} and {nets[-1]!s} are not of the same version''')
        nets.append(ip)
        ips = sorted(set(ips))
        if ips:
            for first, last in _find_address_range(ips):
                addrs.extend(summarize_address_range(first, last))
                return _collapse_addresses_internal(addrs + nets)


def get_mixed_type_key(obj):
    """Return a key suitable for sorting between networks and addresses.

    Address and Network objects are not sortable by default; they're
    fundamentally different so the expression

        IPv4Address('192.0.2.0') <= IPv4Network('192.0.2.0/24')

    doesn't make any sense.  There are some times however, where you may wish
    to have ipaddress sort these for you anyway. If you need to do this, you
    can use this function as the key= argument to sorted().

    Args:
      obj: either a Network or Address object.
    Returns:
      appropriate key.

    """
    if isinstance(obj, _BaseNetwork):
        return obj._get_networks_key()
    if None(obj, _BaseAddress):
        return obj._get_address_key()


class _IPAddressBase:
    '''The mother class.'''
    __slots__ = ()
    exploded = (lambda self: self._explode_shorthand_ip_string())()
    compressed = (lambda self: str(self))()
    reverse_pointer = (lambda self: self._reverse_pointer())()
    version = (lambda self: msg = '%200s has no version specified' % (type(self),)raise NotImplementedError(msg))()
    
    def _check_int_address(self, address):
        if address < 0:
            msg = '%d (< 0) is not permitted as an IPv%d address'
            raise AddressValueError(msg % (address, self._version))
        if address > self._ALL_ONES:
            msg = '%d (>= 2**%d) is not permitted as an IPv%d address'
            raise AddressValueError(msg % (address, self._max_prefixlen, self._version))

    
    def _check_packed_address(self, address, expected_len):
        address_len = len(address)
        if address_len != expected_len:
            msg = '%r (len %d != %d) is not permitted as an IPv%d address'
            raise AddressValueError(msg % (address, address_len, expected_len, self._version))

    _ip_int_from_prefix = (lambda cls, prefixlen: cls._ALL_ONES ^ cls._ALL_ONES >> prefixlen)()
    _prefix_from_ip_int = (lambda cls, ip_int: trailing_zeroes = _count_righthand_zero_bits(ip_int, cls._max_prefixlen)prefixlen = cls._max_prefixlen - trailing_zeroesleading_ones = ip_int >> trailing_zeroesall_ones = (1 << prefixlen) - 1if leading_ones != all_ones:
byteslen = cls._max_prefixlen // 8details = ip_int.to_bytes(byteslen, 'big')msg = 'Netmask pattern %r mixes zeroes & ones'raise ValueError(msg % details)prefixlen)()
    _report_invalid_netmask = (lambda cls, netmask_str: msg = '%r is not a valid netmask' % netmask_strraise NetmaskValueError(msg), None)()
    _prefix_from_prefix_string = (lambda cls, prefixlen_str: if not prefixlen_str.isascii() or prefixlen_str.isdigit():
cls._report_invalid_netmask(prefixlen_str)try:
prefixlen = int(prefixlen_str)except ValueError:
cls._report_invalid_netmask(prefixlen_str)if not  <= 0, prefixlen or 0, prefixlen <= cls._max_prefixlen:
passcls._report_invalid_netmask(prefixlen_str)prefixlen)()
    _prefix_from_ip_string = (lambda cls, ip_str: try:
ip_int = cls._ip_int_from_string(ip_str)except AddressValueError:
cls._report_invalid_netmask(ip_str)try:
cls._prefix_from_ip_int(ip_int)except ValueError:
passip_int ^= cls._ALL_ONEStry:
cls._prefix_from_ip_int(ip_int)except ValueError:
cls._report_invalid_netmask(ip_str)None)()
    _split_addr_prefix = (lambda cls, address: if isinstance(address, (bytes, int)):
(address, cls._max_prefixlen)if not None(address, tuple):
address = _split_optional_netmask(address)if len(address) > 1:
address(None[0], cls._max_prefixlen))()
    
    def __reduce__(self):
        return (self.__class__, (str(self),))


_address_fmt_re = None
_BaseAddress = <NODE:12>()
_BaseNetwork = <NODE:12>()

class _BaseConstants:
    _private_networks = []

_BaseNetwork._constants = _BaseConstants

class _BaseV4:
    '''Base IPv4 object.

    The following methods are used by IPv4 objects in both single IP
    addresses and networks.

    '''
    __slots__ = ()
    _version = 4
    _ALL_ONES = 2 ** IPV4LENGTH - 1
    _max_prefixlen = IPV4LENGTH
    _netmask_cache = { }
    
    def _explode_shorthand_ip_string(self):
        return str(self)

    _make_netmask = (lambda cls, arg:
