# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: websocket_connection.pyc (Python 3.11)

import json
import logging
from ssl import CERT_NONE
from threading import Thread
from time import sleep
from websocket import WebSocketApp
from selenium.common import WebDriverException
logger = logging.getLogger(__name__)

class WebSocketConnection:
    _max_log_message_size = 9999
    
    def __init__(self, url, timeout, interval):
        pass
    # WARNING: Decompyle incomplete

    
    def close(self):
        self._ws_thread.join(timeout = self.response_wait_timeout)
        self._ws.close()
        self._started = False
        self._ws = None

    
    def execute(self, command):
        pass
    # WARNING: Decompyle incomplete

    
    def add_callback(self, event, callback):
        pass
    # WARNING: Decompyle incomplete

    on = add_callback
    
    def remove_callback(self, event, callback_id):
        event_name = event.event_class
        if event_name in self.callbacks:
            for callback in self.callbacks[event_name]:
                if id(callback) == callback_id:
                    self.callbacks[event_name].remove(callback)
                    return None
                return None
                return None

    
    def _serialize_command(self, command):
        return next(command)

    
    def _deserialize_result(self, result, command):
        
        try:
            _ = command.send(result)
            raise WebDriverException("The command's generator function did not exit when expected!")
        except StopIteration:
            exit = None
            del exit
            return None
            None = 
            del exit


    
    def _start_ws(self):
        pass
    # WARNING: Decompyle incomplete

    
    def _process_message(self, message):
        message = json.loads(message)
        logger.debug(f'''<- {message}'''[:self._max_log_message_size])
        if 'id' in message:
            self._messages[message['id']] = message
        if 'method' in message:
            params = message['params']
            for callback in self.callbacks.get(message['method'], []):
                Thread(target = callback, args = (params,), daemon = True).start()
                return None
                return None

    
    def _wait_until(self, condition):
        timeout = self.response_wait_timeout
        interval = self.response_wait_interval
    # WARNING: Decompyle incomplete
