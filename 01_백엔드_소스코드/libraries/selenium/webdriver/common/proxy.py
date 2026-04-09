# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: proxy.pyc (Python 3.11)

'''The Proxy implementation.'''

class ProxyTypeFactory:
    '''Factory for proxy types.'''
    make = (lambda ff_value, string: {
'ff_value': ff_value,
'string': string })()


class ProxyType:
    """Set of possible types of proxy.

    Each proxy type has 2 properties: 'ff_value' is value of Firefox
    profile preference, 'string' is id of proxy type.
    """
    DIRECT = ProxyTypeFactory.make(0, 'DIRECT')
    MANUAL = ProxyTypeFactory.make(1, 'MANUAL')
    PAC = ProxyTypeFactory.make(2, 'PAC')
    RESERVED_1 = ProxyTypeFactory.make(3, 'RESERVED1')
    AUTODETECT = ProxyTypeFactory.make(4, 'AUTODETECT')
    SYSTEM = ProxyTypeFactory.make(5, 'SYSTEM')
    UNSPECIFIED = ProxyTypeFactory.make(6, 'UNSPECIFIED')
    load = (lambda cls, value: if isinstance(value, dict) and 'string' in value:
value = value['string']value = str(value).upper()for attr in dir(cls):
attr_value = getattr(cls, attr)if isinstance(attr_value, dict) and 'string' in attr_value and attr_value['string'] == value:
None, attr_valueraise Exception(f'''No proxy type is found for {value}'''))()


class _ProxyTypeDescriptor:
    
    def __init__(self, name, p_type):
        self.name = name
        self.p_type = p_type

    
    def __get__(self, obj, cls):
        return getattr(obj, self.name)

    
    def __set__(self, obj, value):
        if not self.name == 'autodetect' and isinstance(value, bool):
            raise ValueError('Autodetect proxy value needs to be a boolean')
        getattr(obj, '_verify_proxy_type_compatibility')(self.p_type)
        setattr(obj, 'proxyType', self.p_type)
        setattr(obj, self.name, value)



class Proxy:
    '''Proxy configuration containing proxy type and necessary proxy settings.'''
    proxyType = ProxyType.UNSPECIFIED
    autodetect = False
    httpProxy = ''
    noProxy = ''
    proxyAutoconfigUrl = ''
    sslProxy = ''
    socksProxy = ''
    socksUsername = ''
    socksPassword = ''
    socksVersion = None
    auto_detect = _ProxyTypeDescriptor('autodetect', ProxyType.AUTODETECT)
    http_proxy = _ProxyTypeDescriptor('httpProxy', ProxyType.MANUAL)
    no_proxy = _ProxyTypeDescriptor('noProxy', ProxyType.MANUAL)
    proxy_autoconfig_url = _ProxyTypeDescriptor('proxyAutoconfigUrl', ProxyType.PAC)
    ssl_proxy = _ProxyTypeDescriptor('sslProxy', ProxyType.MANUAL)
    socks_proxy = _ProxyTypeDescriptor('socksProxy', ProxyType.MANUAL)
    socks_username = _ProxyTypeDescriptor('socksUsername', ProxyType.MANUAL)
    socks_password = _ProxyTypeDescriptor('socksPassword', ProxyType.MANUAL)
    socks_version = _ProxyTypeDescriptor('socksVersion', ProxyType.MANUAL)
    
    def __init__(self = None, raw = None):
        '''Creates a new Proxy.

        Args:
            raw: Raw proxy data. If None, default class values are used.
        '''
        pass
    # WARNING: Decompyle incomplete

    proxy_type = (lambda self: self.proxyType)()
    proxy_type = (lambda self = None, value = property: self._verify_proxy_type_compatibility(value)self.proxyType = value)()
    
    def _verify_proxy_type_compatibility(self, compatible_proxy):
        if self.proxyType not in (ProxyType.UNSPECIFIED, compatible_proxy):
            raise ValueError(f'''Specified proxy type ({compatible_proxy}) not compatible with current setting ({self.proxyType})''')

    
    def to_capabilities(self):
        proxy_caps = {
            'proxyType': self.proxyType['string'].lower() }
        proxies = [
            'autodetect',
            'httpProxy',
            'proxyAutoconfigUrl',
            'sslProxy',
            'noProxy',
            'socksProxy',
            'socksUsername',
            'socksPassword',
            'socksVersion']
        for proxy in proxies:
            attr_value = getattr(self, proxy)
            if attr_value:
                proxy_caps[proxy] = attr_value
            return proxy_caps

    
    def to_bidi_dict(self = None):
        '''Convert proxy settings to BiDi format.

        Returns:
            Proxy configuration in BiDi format.
        '''
        proxy_type = self.proxyType['string'].lower()
        result = {
            'proxyType': proxy_type }
    # WARNING: Decompyle incomplete
