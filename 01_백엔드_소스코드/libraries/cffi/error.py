# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: error.pyc (Python 3.11)


class FFIError(Exception):
    __module__ = 'cffi'


class CDefError(Exception):
    __module__ = 'cffi'
    
    def __str__(self):
        
        try:
            current_decl = self.args[1]
            filename = current_decl.coord.file
            linenum = current_decl.coord.line
            prefix = '%s:%d: ' % (filename, linenum)
        except (AttributeError, TypeError, IndexError):
            prefix = ''

        return f'''{prefix!s}{self.args[0]!s}'''



class VerificationError(Exception):
    ''' An error raised when verification fails
    '''
    __module__ = 'cffi'


class VerificationMissing(Exception):
    ''' An error raised when incomplete structures are passed into
    cdef, but no verification has been done
    '''
    __module__ = 'cffi'


class PkgConfigError(Exception):
    ''' An error raised for missing modules in pkg-config
    '''
    __module__ = 'cffi'
