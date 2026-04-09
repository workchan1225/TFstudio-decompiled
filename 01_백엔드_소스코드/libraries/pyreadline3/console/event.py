# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: event.pyc (Python 3.11)


class Event(object):
    '''Represent events from the console.'''
    
    def __init__(self, console, input):
        pass

    
    def __repr__(self):
        '''Display an event for debugging.'''
        if self.type in ('KeyPress', 'KeyRelease'):
            chr = self.char
            if ord(chr) < ord('A'):
                chr = '?'
            s = "%s char='%s'%d keysym='%s' keycode=%d:%x state=%x keyinfo=%s" % (self.type, chr, ord(self.char), self.keysym, self.keycode, self.keycode, self.state, self.keyinfo)
        elif self.type in ('Motion', 'Button'):
            s = '%s x=%d y=%d state=%x' % (self.type, self.x, self.y, self.state)
        elif self.type == 'Configure':
            s = '%s w=%d h=%d' % (self.type, self.width, self.height)
        elif self.type in ('FocusIn', 'FocusOut'):
            s = self.type
        elif self.type == 'Menu':
            s = '%s state=%x' % (self.type, self.state)
        else:
            s = 'unknown event type'
        return s
