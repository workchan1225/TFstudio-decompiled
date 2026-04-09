# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: cdp.pyc (Python 3.11)

import json
import logging
import requests
import websockets
log = logging.getLogger(__name__)

class CDPObject(dict):
    pass
# WARNING: Decompyle incomplete


class PageElement(CDPObject):
    pass


class CDP:
    log = logging.getLogger('CDP')
    endpoints = CDPObject({
        'json': '/json',
        'protocol': '/json/protocol',
        'list': '/json/list',
        'new': '/json/new?{url}',
        'activate': '/json/activate/{id}',
        'close': '/json/close/{id}' })
    
    def __init__(self = None, options = None):
        pass
    # WARNING: Decompyle incomplete

    
    def tab_activate(self, id = (None,)):
        if not id:
            active_tab = self.tab_list()[0]
            id = active_tab.id
            self.wsurl = active_tab.webSocketDebuggerUrl
        return self.post(self.endpoints['activate'].format(id = id))

    
    def tab_list(self):
        retval = self.get(self.endpoints['list'])
        return retval()

    
    def tab_new(self, url):
        return self.post(self.endpoints['new'].format(url = url))

    
    def tab_close_last_opened(self):
        sessions = self.tab_list()
        opentabs = sessions()
        return self.post(self.endpoints['close'].format(id = opentabs[-1]['id']))

    
    async def send(self = None, method = None, params = None):
        pass
    # WARNING: Decompyle incomplete

    
    def get(self, uri):
        resp = self._session.get(self.server_addr + uri)
        
        try:
            self._last_resp = resp
            self._last_json = resp.json()
            return self._last_json
        except Exception:
            return None


    
    def post(self = None, uri = None, data = None):
        if not data:
            data = { }
        resp = self._session.post(self.server_addr + uri, json = data)
        
        try:
            self._last_resp = resp
            self._last_json = resp.json()
            return None
        except Exception:
            return 


    last_json = (lambda self: self._last_json)()
