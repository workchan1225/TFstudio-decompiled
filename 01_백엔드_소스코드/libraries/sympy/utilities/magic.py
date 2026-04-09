# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: magic.pyc (Python 3.11)

'''Functions that involve magic. '''

def pollute(names, objects):
    '''Pollute the global namespace with symbols -> objects mapping. '''
    currentframe = currentframe
    import inspect
    frame = currentframe().f_back.f_back
    
    try:
        for name, obj in zip(names, objects):
            frame.f_globals[name] = obj
            del frame
            return None
            del frame
