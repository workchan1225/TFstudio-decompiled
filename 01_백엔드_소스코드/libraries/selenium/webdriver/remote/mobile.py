# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: mobile.pyc (Python 3.11)

from selenium.webdriver.remote.command import Command

class _ConnectionType:
    
    def __init__(self, mask):
        self.mask = mask

    airplane_mode = (lambda self: self.mask % 2 == 1)()
    wifi = (lambda self: self.mask / 2 % 2 == 1)()
    data = (lambda self: self.mask / 4 > 0)()


class Mobile:
    ConnectionType = _ConnectionType
    ALL_NETWORK = ConnectionType(6)
    WIFI_NETWORK = ConnectionType(2)
    DATA_NETWORK = ConnectionType(4)
    AIRPLANE_MODE = ConnectionType(1)
    
    def __init__(self, driver):
        import weakref
        self._driver = weakref.proxy(driver)

    network_connection = (lambda self: self.ConnectionType(self._driver.execute(Command.GET_NETWORK_CONNECTION)['value']))()
    
    def set_network_connection(self, network):
        '''Set the network connection for the remote device.

        Example of setting airplane mode::

            driver.mobile.set_network_connection(driver.mobile.AIRPLANE_MODE)
        '''
        mode = network.mask if isinstance(network, self.ConnectionType) else network
        return self.ConnectionType(self._driver.execute(Command.SET_NETWORK_CONNECTION, {
            'name': 'network_connection',
            'parameters': {
                'type': mode } })['value'])

    context = (lambda self: self._driver.execute(Command.CURRENT_CONTEXT_HANDLE))()
    context = (lambda self = property, new_context = property: self._driver.execute(Command.SWITCH_TO_CONTEXT, {
'name': new_context }))()
    contexts = (lambda self: self._driver.execute(Command.CONTEXT_HANDLES))()
