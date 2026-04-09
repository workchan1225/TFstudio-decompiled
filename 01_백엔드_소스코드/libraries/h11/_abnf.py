# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: _abnf.pyc (Python 3.11)

OWS = '[ \\t]*'
token = "[-!#$%&'*+.^_`|~0-9a-zA-Z]+"
field_name = token
vchar = '[\\x21-\\x7e]'
vchar_or_obs_text = '[^\\x00\\s]'
field_vchar = vchar_or_obs_text
# WARNING: Decompyle incomplete
