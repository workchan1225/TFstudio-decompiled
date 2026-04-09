# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: abstract_event_listener.pyc (Python 3.11)


class AbstractEventListener:
    '''Event listener must subclass and implement this fully or partially.'''
    
    def before_navigate_to(self = None, url = None, driver = None):
        pass

    
    def after_navigate_to(self = None, url = None, driver = None):
        pass

    
    def before_navigate_back(self = None, driver = None):
        pass

    
    def after_navigate_back(self = None, driver = None):
        pass

    
    def before_navigate_forward(self = None, driver = None):
        pass

    
    def after_navigate_forward(self = None, driver = None):
        pass

    
    def before_find(self = None, by = None, value = None, driver = ('return', None)):
        pass

    
    def after_find(self = None, by = None, value = None, driver = ('return', None)):
        pass

    
    def before_click(self = None, element = None, driver = None):
        pass

    
    def after_click(self = None, element = None, driver = None):
        pass

    
    def before_change_value_of(self = None, element = None, driver = None):
        pass

    
    def after_change_value_of(self = None, element = None, driver = None):
        pass

    
    def before_execute_script(self = None, script = None, driver = None):
        pass

    
    def after_execute_script(self = None, script = None, driver = None):
        pass

    
    def before_close(self = None, driver = None):
        pass

    
    def after_close(self = None, driver = None):
        pass

    
    def before_quit(self = None, driver = None):
        pass

    
    def after_quit(self = None, driver = None):
        pass

    
    def on_exception(self = None, exception = None, driver = None):
        pass
