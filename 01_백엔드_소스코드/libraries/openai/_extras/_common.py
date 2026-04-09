# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: _common.pyc (Python 3.11)

from _exceptions import OpenAIError
INSTRUCTIONS = '\n\nOpenAI error:\n\n    missing `{library}`\n\nThis feature requires additional dependencies:\n\n    $ pip install openai[{extra}]\n\n'

def format_instructions(*, library, extra):
    return INSTRUCTIONS.format(library = library, extra = extra)


class MissingDependencyError(OpenAIError):
    pass
