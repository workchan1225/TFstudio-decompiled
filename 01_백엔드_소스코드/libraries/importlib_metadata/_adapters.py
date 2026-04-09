# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: _adapters.pyc (Python 3.11)

import email.message as email
import email.policy as email
import re
import textwrap
from _text import FoldedCase

class RawPolicy(email.policy.EmailPolicy):
    
    def fold(self, name, value):
        folded = self.linesep.join(textwrap.indent(value, prefix = '        ', predicate = (lambda line: True)).lstrip().splitlines())
        return f'''{name}: {folded}{self.linesep}'''



class Message(email.message.Message):
    pass
# WARNING: Decompyle incomplete
