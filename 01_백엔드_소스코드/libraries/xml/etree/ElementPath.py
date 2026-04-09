# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: ElementPath.pyc (Python 3.11)

import re
xpath_tokenizer_re = re.compile('(\'[^\']*\'|\\"[^\\"]*\\"|::|//?|\\.\\.|\\(\\)|!=|[/.*:\\[\\]\\(\\)@=])|((?:\\{[^}]+\\})?[^/\\[\\]\\(\\)@!=\\s]+)|\\s+')

def xpath_tokenizer(pattern, namespaces = (None,)):
    pass
# WARNING: Decompyle incomplete


def get_parent_map(context):
    parent_map = context.parent_map
# WARNING: Decompyle incomplete


def _is_wildcard_tag(tag):
