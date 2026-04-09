# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: truncate.pyc (Python 3.11)

'''Utilities for truncating assertion output.

Current default behaviour is to truncate assertion explanations at
terminal lines, unless running with an assertions verbosity level of at least 2 or running on CI.
'''
from __future__ import annotations
from _pytest.compat import running_on_ci
from _pytest.config import Config
from _pytest.nodes import Item
DEFAULT_MAX_LINES = 8
DEFAULT_MAX_CHARS = DEFAULT_MAX_LINES * 80
USAGE_MSG = "use '-vv' to show"

def truncate_if_required(explanation = None, item = None):
    '''Truncate this assertion explanation if the given test item is eligible.'''
    (should_truncate, max_lines, max_chars) = _get_truncation_parameters(item)
    if should_truncate:
        return _truncate_explanation(explanation, max_lines = max_lines, max_chars = max_chars)


def _get_truncation_parameters(item = None):
    '''Return the truncation parameters related to the given item, as (should truncate, max lines, max chars).'''
    max_lines = item.config.getini('truncation_limit_lines')
# WARNING: Decompyle incomplete


def _truncate_explanation(input_lines = None, max_lines = None, max_chars = None):
    '''Truncate given list of strings that makes up the assertion explanation.

    Truncates to either max_lines, or max_chars - whichever the input reaches
    first, taking the truncation explanation into account. The remaining lines
    will be replaced by a usage message.
    '''
    input_char_count = len(''.join(input_lines))
    tolerable_max_chars = max_chars + 70
    tolerable_max_lines = max_lines + 2
    if len(input_lines) <= tolerable_max_lines and input_char_count <= tolerable_max_chars:
        return input_lines
    if None > 0:
        truncated_explanation = input_lines[:max_lines]
    else:
        truncated_explanation = input_lines
    truncated_char = True
    if len(''.join(truncated_explanation)) > tolerable_max_chars and max_chars > 0:
        truncated_explanation = _truncate_by_char_count(truncated_explanation, max_chars)
    else:
        truncated_char = False
    if truncated_explanation == input_lines:
        return truncated_explanation
    truncated_line_count = None(input_lines) - len(truncated_explanation)
    if truncated_explanation[-1]:
        truncated_explanation[-1] = truncated_explanation[-1] + '...'
        if truncated_char:
            truncated_line_count += 1
        else:
            truncated_explanation[-1] = '...'
    return None[''][f'''...Full output truncated ({truncated_line_count} line{'' if truncated_line_count == 1 else 's'} hidden), {USAGE_MSG}''']


def _truncate_by_char_count(input_lines = None, max_chars = None):
    iterated_char_count = 0
    for iterated_index, input_line in enumerate(input_lines):
        if iterated_char_count + len(input_line) > max_chars:
            pass
        else:
            iterated_char_count += len(input_line)
        truncated_result = input_lines[:iterated_index]
        final_line = input_lines[iterated_index]
        if final_line:
            final_line_truncate_point = max_chars - iterated_char_count
            final_line = final_line[:final_line_truncate_point]
    truncated_result.append(final_line)
    return truncated_result
