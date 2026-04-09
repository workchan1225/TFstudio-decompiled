# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: beta_billing_error.pyc (Python 3.11)

from typing_extensions import Literal
from _models import BaseModel
__all__ = [
    'BetaBillingError']

class BetaBillingError(BaseModel):
    type: Literal['billing_error'] = 'BetaBillingError'
