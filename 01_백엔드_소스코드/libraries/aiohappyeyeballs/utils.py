# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: utils.pyc (Python 3.11)

'''Utility functions for aiohappyeyeballs.'''
import ipaddress
import socket
from typing import Dict, List, Optional, Tuple, Union
from types import AddrInfoType

def addr_to_addr_infos(addr = None):
    '''Convert an address tuple to a list of addr_info tuples.'''
    pass
# WARNING: Decompyle incomplete


def pop_addr_infos_interleave(addr_infos = None, interleave = None):
    '''
    Pop addr_info from the list of addr_infos by family up to interleave times.

    The interleave parameter is used to know how many addr_infos for
    each family should be popped of the top of the list.
    '''
    seen = { }
# WARNING: Decompyle incomplete


def _addr_tuple_to_ip_address(addr = None):
    '''Convert an address tuple to an IPv4Address.'''
    pass
# WARNING: Decompyle incomplete


def remove_addr_infos(addr_infos = None, addr = None):
    '''
    Remove an address from the list of addr_infos.

    The addr value is typically the return value of
    sock.getpeername().
    '''
    bad_addrs_infos = []
    for addr_info in addr_infos:
        if addr_info[-1] == addr:
            bad_addrs_infos.append(addr_info)
        if bad_addrs_infos:
            for bad_addr_info in bad_addrs_infos:
                addr_infos.remove(bad_addr_info)
                return None
                match_addr = _addr_tuple_to_ip_address(addr)
                for addr_info in addr_infos:
                    if match_addr == _addr_tuple_to_ip_address(addr_info[-1]):
                        bad_addrs_infos.append(addr_info)
                    if bad_addrs_infos:
                        for bad_addr_info in bad_addrs_infos:
                            addr_infos.remove(bad_addr_info)
                            return None
                            raise ValueError(f'''Address {addr} not found in addr_infos''')
