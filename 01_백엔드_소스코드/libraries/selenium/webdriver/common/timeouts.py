# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: timeouts.pyc (Python 3.11)

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from typing import TypedDict
    
    def JSONTimeouts():
        '''JSONTimeouts'''
        script: int = 'JSONTimeouts'

    JSONTimeouts = <NODE:27>(JSONTimeouts, 'JSONTimeouts', TypedDict, total = False)
else:
    JSONTimeouts = dict[(str, int)]

class _TimeoutsDescriptor:
    '''Get or set the value of the attributes listed below.

    _implicit_wait _page_load _script

    This does not set the value on the remote end.
    '''
    
    def __init__(self, name):
        self.name = name

    
    def __get__(self = None, obj = None, cls = None):
        return getattr(obj, self.name) / 1000

    
    def __set__(self = None, obj = None, value = None):
        converted_value = getattr(obj, '_convert')(value)
        setattr(obj, self.name, converted_value)



class Timeouts:
    
    def __init__(self = None, implicit_wait = None, page_load = None, script = (0, 0, 0)):
        '''Create a new Timeouts object.

        This implements https://w3c.github.io/webdriver/#timeouts.

        Args:
            implicit_wait: Number of seconds to wait when searching for elements
                before throwing an error.
            page_load: Number of seconds to wait for a page load to complete
                before throwing an error.
            script: Number of seconds to wait for an asynchronous script to
                finish execution before throwing an error.
        '''
        self._implicit_wait = self._convert(implicit_wait)
        self._page_load = self._convert(page_load)
        self._script = self._convert(script)

    implicit_wait = _TimeoutsDescriptor('_implicit_wait')
    page_load = _TimeoutsDescriptor('_page_load')
    script = _TimeoutsDescriptor('_script')
    
    def _convert(self = None, timeout = None):
        if isinstance(timeout, (int, float)):
            return int(float(timeout) * 1000)
        raise None('Timeouts can only be an int or a float')

    
    def _to_json(self = None):
        timeouts = { }
        if self._implicit_wait:
            timeouts['implicit'] = self._implicit_wait
        if self._page_load:
            timeouts['pageLoad'] = self._page_load
        if self._script:
            timeouts['script'] = self._script
        return timeouts
