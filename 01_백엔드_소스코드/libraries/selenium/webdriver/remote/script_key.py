# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: script_key.pyc (Python 3.11)

import uuid

class ScriptKey:
    
    def __init__(self, id = (None,)):
        if not id:
            pass
        self._id = uuid.uuid4()

    id = (lambda self: self._id)()
    
    def __eq__(self, other):
        return self._id == other

    
    def __repr__(self = None):
        return f'''ScriptKey(id={self.id})'''
