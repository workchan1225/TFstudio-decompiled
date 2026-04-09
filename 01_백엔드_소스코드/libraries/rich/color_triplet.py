# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: color_triplet.pyc (Python 3.11)

from typing import NamedTuple, Tuple

class ColorTriplet(NamedTuple):
    blue: int = 'The red, green, and blue components of a color.'
    hex = (lambda self = None: (red, green, blue) = selff'''#{red:02x}{green:02x}{blue:02x}''')()
    rgb = (lambda self = None: (red, green, blue) = selff'''rgb({red},{green},{blue})''')()
    normalized = (lambda self = None: (red, green, blue) = self(red / 255, green / 255, blue / 255))()
