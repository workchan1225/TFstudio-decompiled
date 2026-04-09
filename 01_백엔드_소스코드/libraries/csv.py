# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: csv.pyc (Python 3.11)

'''
csv.py - read/write/investigate CSV files
'''
import re
from _csv import Error, __version__, writer, reader, register_dialect, unregister_dialect, get_dialect, list_dialects, field_size_limit, QUOTE_MINIMAL, QUOTE_ALL, QUOTE_NONNUMERIC, QUOTE_NONE, __doc__
from _csv import Dialect as _Dialect
from io import StringIO
__all__ = [
    'QUOTE_MINIMAL',
    'QUOTE_ALL',
    'QUOTE_NONNUMERIC',
    'QUOTE_NONE',
    'Error',
    'Dialect',
    '__doc__',
    'excel',
    'excel_tab',
    'field_size_limit',
    'reader',
    'writer',
    'register_dialect',
    'get_dialect',
    'list_dialects',
    'Sniffer',
    'unregister_dialect',
    '__version__',
    'DictReader',
    'DictWriter',
    'unix_dialect']

class Dialect:
    '''Describe a CSV dialect.

    This must be subclassed (see csv.excel).  Valid attributes are:
    delimiter, quotechar, escapechar, doublequote, skipinitialspace,
    lineterminator, quoting.

    '''
    _name = ''
    _valid = False
    delimiter = None
    quotechar = None
    escapechar = None
    doublequote = None
    skipinitialspace = None
    lineterminator = None
    quoting = None
    
    def __init__(self):
        if self.__class__ != Dialect:
            self._valid = True
        self._validate()

    
    def _validate(self):
        
        try:
            _Dialect(self)
            return None
        except TypeError:
            e = None
            raise Error(str(e))
            e = None
            del e




class excel(Dialect):
    '''Describe the usual properties of Excel-generated CSV files.'''
    delimiter = ','
    quotechar = '"'
    doublequote = True
    skipinitialspace = False
    lineterminator = '\r\n'
    quoting = QUOTE_MINIMAL

register_dialect('excel', excel)

class excel_tab(excel):
    '''Describe the usual properties of Excel-generated TAB-delimited files.'''
    delimiter = '\t'

register_dialect('excel-tab', excel_tab)

class unix_dialect(Dialect):
    '''Describe the usual properties of Unix-generated CSV files.'''
    delimiter = ','
    quotechar = '"'
    doublequote = True
    skipinitialspace = False
    lineterminator = '\n'
    quoting = QUOTE_ALL

register_dialect('unix', unix_dialect)

class DictReader:
    
    def __init__(self, f, fieldnames, restkey, restval, dialect = (None, None, None, 'excel'), *args, **kwds):
        self._fieldnames = fieldnames
        self.restkey = restkey
        self.restval = restval
    # WARNING: Decompyle incomplete

    
    def __iter__(self):
        return self

    fieldnames = (lambda self: pass# WARNING: Decompyle incomplete
)()
    fieldnames = (lambda self, value: self._fieldnames = value)()
    
    def __next__(self):
        if self.line_num == 0:
            self.fieldnames
        row = next(self.reader)
        self.line_num = self.reader.line_num
    # WARNING: Decompyle incomplete



class DictWriter:
    
    def __init__(self, f, fieldnames, restval, extrasaction, dialect = ('', 'raise', 'excel'), *args, **kwds):
        self.fieldnames = fieldnames
        self.restval = restval
        if extrasaction.lower() not in ('raise', 'ignore'):
            raise ValueError("extrasaction (%s) must be 'raise' or 'ignore'" % extrasaction)
        self.extrasaction = extrasaction
    # WARNING: Decompyle incomplete

    
    def writeheader(self):
        header = dict(zip(self.fieldnames, self.fieldnames))
        return self.writerow(header)

    
    def _dict_to_list(self, rowdict):
        pass
    # WARNING: Decompyle incomplete

    
    def writerow(self, rowdict):
        return self.writer.writerow(self._dict_to_list(rowdict))

    
    def writerows(self, rowdicts):
        return self.writer.writerows(map(self._dict_to_list, rowdicts))



try:
    complex
except NameError:
    complex = float


class Sniffer:
    '''
    "Sniffs" the format of a CSV file (i.e. delimiter, quotechar)
    Returns a Dialect object.
    '''
    
    def __init__(self):
        self.preferred = [
            ',',
            '\t',
            ';',
            ' ',
            ':']

    
    def sniff(self, sample, delimiters = (None,)):
