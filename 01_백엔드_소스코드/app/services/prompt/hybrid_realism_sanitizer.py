# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: hybrid_realism_sanitizer.pyc (Python 3.11)

import re
_REALISM_CUE_PATTERN = re.compile('\\b(?:photoreal(?:istic)?|photo[-\\s]?realistic|hyper[-\\s]?realistic|real\\s+photograph|real\\s+photo|realistic\\s+photograph(?:y)?|cinematic\\s+realism|cinematic\\s+photograph(?:y)?|(?:8k|4k)\\s+photo(?:graph)?|polished\\s+digital|realistic\\s+(?:image|imagery|render(?:ing)?|skin|face|human|person|portrait|people))\\b', flags = re.IGNORECASE)
_NEGATION_PATTERN = re.compile("\\b(?:no|not|avoid|without|never|exclude|forbid|ban)\\b|do\\s+not|don't|dont", flags = re.IGNORECASE)
_BACKGROUND_SCOPE_PATTERN = re.compile('\\b(?:background|environment|backdrop|scenery|setting|location|plate|live[-\\s]?action|camera|lens|cinematography|documentary)\\b', flags = re.IGNORECASE)
_CLAUSE_PATTERN = re.compile('[^,;\\n]+(?:[,;\\n]+)?', flags = re.MULTILINE)

def _is_conflicting_global_realism_clause(clause = None):
