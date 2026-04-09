# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: psc.pyc (Python 3.11)

import datetime
import re
from  import util

class Namespace(object):
    pass
# WARNING: Decompyle incomplete

format_ = re.compile('^((\\d{2}):)?(\\d{2}):(\\d{2})(\\.(\\d{3}))?$')

def _parse_psc_chapter_start(start):
    m = format_.match(start)
# WARNING: Decompyle incomplete
