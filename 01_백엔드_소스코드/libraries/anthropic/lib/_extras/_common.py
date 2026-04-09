# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: _common.pyc (Python 3.11)

from _exceptions import AnthropicError
INSTRUCTIONS = '\n\nAnthropic error: missing required dependency `{library}`.\n\n    $ pip install anthropic[{extra}]\n'

class MissingDependencyError(AnthropicError):
    pass
# WARNING: Decompyle incomplete
