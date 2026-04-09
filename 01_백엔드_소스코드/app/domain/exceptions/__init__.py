# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: __init__.pyc (Python 3.11)

'''
Domain Exceptions

Custom exceptions for domain layer validation and business rule violations.
These exceptions are framework-agnostic and can be used throughout the domain layer.
'''

class DomainError(Exception):
    pass
# WARNING: Decompyle incomplete


class ValidationError(DomainError):
    pass
# WARNING: Decompyle incomplete


class InvalidStateTransitionError(DomainError):
    pass
# WARNING: Decompyle incomplete


class EntityNotFoundError(DomainError):
    pass
# WARNING: Decompyle incomplete
