# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: reflection.pyc (Python 3.11)

from __future__ import annotations
import re
from typing import Any
from typing import Callable
from typing import Dict
from typing import List
from typing import Optional
from typing import overload
from typing import Sequence
from typing import Tuple
from typing import TYPE_CHECKING
from typing import Union
from enumerated import ENUM
from enumerated import SET
from types import DATETIME
from types import TIME
from types import TIMESTAMP
from  import types as sqltypes
from  import util
from util.typing import Literal
if TYPE_CHECKING:
    from base import MySQLDialect
    from base import MySQLIdentifierPreparer
    from engine.interfaces import ReflectedColumn

class ReflectedState:
    charset: 'Optional[str]' = 'Stores raw information about a SHOW CREATE TABLE statement.'
    
    def __init__(self = None):
        self.columns = []
        self.table_options = { }
        self.table_name = None
        self.keys = []
        self.fk_constraints = []
        self.ck_constraints = []



class MySQLTableDefinitionParser:
    '''Parses the results of a SHOW CREATE TABLE statement.'''
    
    def __init__(self = None, dialect = None, preparer = None):
        self.dialect = dialect
        self.preparer = preparer
        self._prep_regexes()

    
    def parse(self = None, show_create = None, charset = None):
        state = ReflectedState()
        state.charset = charset
    # WARNING: Decompyle incomplete

    
    def _check_view(self = None, sql = None):
        return bool(self._re_is_view.match(sql))

    
    def _parse_constraints(self = None, line = None):
        '''Parse a KEY or CONSTRAINT line.

        :param line: A line of SHOW CREATE TABLE output
        '''
        m = self._re_key.match(line)
        if m:
            spec = m.groupdict()
            spec['columns'] = self._parse_keyexprs(spec['columns'])
            if spec['version_sql']:
                m2 = self._re_key_version_sql.match(spec['version_sql'])
                if m2 and m2.groupdict()['parser']:
                    spec['parser'] = m2.groupdict()['parser']
            if spec['parser']:
                spec['parser'] = self.preparer.unformat_identifiers(spec['parser'])[0]
            return ('key', spec)
        m = None._re_fk_constraint.match(line)
        if m:
            spec = m.groupdict()
            spec['table'] = self.preparer.unformat_identifiers(spec['table'])
            spec['local'] = self._parse_keyexprs(spec['local'])()
            spec['foreign'] = self._parse_keyexprs(spec['foreign'])()
            return ('fk_constraint', spec)
        m = None._re_ck_constraint.match(line)
        if m:
            spec = m.groupdict()
            return ('ck_constraint', spec)
        m = None._re_partition.match(line)
        if m:
            return ('partition', line)
        return (None, line)

    
    def _parse_table_name(self = None, line = None, state = None):
        '''Extract the table name.

        :param line: The first line of SHOW CREATE TABLE
        '''
        (regex, cleanup) = self._pr_name
        m = regex.match(line)
        if m:
            state.table_name = cleanup(m.group('name'))
            return None

    
    def _parse_table_options(self = None, line = None, state = None):
        '''Build a dictionary of all reflected table-level options.

        :param line: The final line of SHOW CREATE TABLE output.
        '''
        options = { }
        if line and line != ')':
            rest_of_line = line
            for regex, cleanup in self._pr_options:
                m = regex.search(rest_of_line)
                if not m:
                    continue
                value = m.group('val')
                directive = m.group('directive')
                if cleanup:
                    value = cleanup(value)
                options[directive.lower()] = value
                rest_of_line = regex.sub('', rest_of_line)
                for nope in ('auto_increment', 'data directory', 'index directory'):
                    options.pop(nope, None)
                    for opt, val in options.items():
                        state.table_options[f'''{self.dialect.name!s}_{opt!s}'''] = val
                        return None

    
    def _parse_partition_options(self = None, line = None, state = None):
        options = { }
        new_line = line[:]
    # WARNING: Decompyle incomplete

    
    def _parse_column(self = None, line = None, state = None):
        """Extract column details.

        Falls back to a 'minimal support' variant if full parse fails.

        :param line: Any column-bearing line from SHOW CREATE TABLE
        """
        spec = None
        m = self._re_column.match(line)
        if m:
            spec = m.groupdict()
            spec['full'] = True
        else:
            m = self._re_column_loose.match(line)
            if m:
                spec = m.groupdict()
                spec['full'] = False
        if not spec:
            util.warn('Unknown column definition %r' % line)
            return None
        if not None['full']:
            util.warn('Incomplete reflection of column definition %r' % line)
        args = spec['arg']
        type_ = spec['coltype']
        name = spec['name']
        
        try:
            col_type = self.dialect.ischema_names[type_]
        except KeyError:
            util.warn(f'''Did not recognize type \'{type_!s}\' of column \'{name!s}\'''')
            col_type = sqltypes.NullType

    # WARNING: Decompyle incomplete

    
    def _describe_to_create(self = None, table_name = None, columns = None):
        '''Re-format DESCRIBE output as a SHOW CREATE TABLE string.

        DESCRIBE is a much simpler reflection and is sufficient for
        reflecting views for runtime use.  This method formats DDL
        for columns only- keys are omitted.

        :param columns: A sequence of DESCRIBE or SHOW COLUMNS 6-tuples.
          SHOW FULL COLUMNS FROM rows must be rearranged for use with
          this function.
        '''
        pass
    # WARNING: Decompyle incomplete

    
    def _parse_keyexprs(self = None, identifiers = None):
        '''Unpack \'"col"(2),"col" ASC\'-ish strings into components.'''
        return self._re_keyexprs.findall(identifiers)()

    
    def _prep_regexes(self = None):
        '''Pre-compile regular expressions.'''
        self._pr_options = []
        _final = self.preparer.final_quote
        
        def <listcomp>(.0):
            return [ re.escape(s) for s in .0 ]

        quotes = zip(('iq', 'fq', 'esc_fq')(<listcomp>, (self.preparer.initial_quote, _final, self.preparer._escape_identifier(_final))()))
        self._pr_name = _pr_compile('^CREATE (?:\\w+ +)?TABLE +%(iq)s(?P<name>(?:%(esc_fq)s|[^%(fq)s])+)%(fq)s +\\($' % quotes, self.preparer._unescape_identifier)
        self._re_is_view = _re_compile('^CREATE(?! TABLE)(\\s.*)?\\sVIEW')
        self._re_keyexprs = _re_compile('(?:(?:%(iq)s((?:%(esc_fq)s|[^%(fq)s])+)%(fq)s)(?:\\((\\d+)\\))?(?: +(ASC|DESC))?(?=\\,|$))+' % quotes)
        self._re_csv_str = _re_compile('\\x27(?:\\x27\\x27|[^\\x27])*\\x27')
        self._re_csv_int = _re_compile('\\d+')
        self._re_column = _re_compile("  %(iq)s(?P<name>(?:%(esc_fq)s|[^%(fq)s])+)%(fq)s +(?P<coltype>\\w+)(?:\\((?P<arg>(?:\\d+|\\d+,\\d+|(?:'(?:''|[^'])*',?)+))\\))?(?: +(?P<unsigned>UNSIGNED))?(?: +(?P<zerofill>ZEROFILL))?(?: +CHARACTER SET +(?P<charset>[\\w_]+))?(?: +COLLATE +(?P<collate>[\\w_]+))?(?: +(?P<notnull>(?:NOT )?NULL))?(?: +DEFAULT +(?P<default>(?:NULL|'(?:''|[^'])*'|\\(.+?\\)|[\\-\\w\\.\\(\\)]+(?: +ON UPDATE [\\-\\w\\.\\(\\)]+)?)))?(?: +(?:GENERATED ALWAYS)? ?AS +(?P<generated>\\(.*\\))? ?(?P<persistence>VIRTUAL|STORED)?(?: +(?P<notnull_generated>(?:NOT )?NULL))?)?(?: +(?P<autoincr>AUTO_INCREMENT))?(?: +COMMENT +'(?P<comment>(?:''|[^'])*)')?(?: +COLUMN_FORMAT +(?P<colfmt>\\w+))?(?: +STORAGE +(?P<storage>\\w+))?(?: +(?P<extra>.*))?,?$" % quotes)
        self._re_column_loose = _re_compile('  %(iq)s(?P<name>(?:%(esc_fq)s|[^%(fq)s])+)%(fq)s +(?P<coltype>\\w+)(?:\\((?P<arg>(?:\\d+|\\d+,\\d+|\\x27(?:\\x27\\x27|[^\\x27])+\\x27))\\))?.*?(?P<notnull>(?:NOT )NULL)?' % quotes)
        self._re_key = _re_compile('  (?:(?P<type>\\S+) )?KEY(?: +%(iq)s(?P<name>(?:%(esc_fq)s|[^%(fq)s])+)%(fq)s)?(?: +USING +(?P<using_pre>\\S+))? +\\((?P<columns>.+?)\\)(?: +USING +(?P<using_post>\\S+))?(?: +KEY_BLOCK_SIZE *[ =]? *(?P<keyblock>\\S+))?(?: +WITH PARSER +(?P<parser>\\S+))?(?: +COMMENT +(?P<comment>(\\x27\\x27|\\x27([^\\x27])*?\\x27)+))?(?: +/\\*(?P<version_sql>.+)\\*/ *)?,?$' % quotes)
        self._re_key_version_sql = _re_compile('\\!\\d+ (?: *WITH PARSER +(?P<parser>\\S+) *)?')
        kw = quotes.copy()
        kw['on'] = 'RESTRICT|CASCADE|SET NULL|NO ACTION|SET DEFAULT'
        self._re_fk_constraint = _re_compile('  CONSTRAINT +%(iq)s(?P<name>(?:%(esc_fq)s|[^%(fq)s])+)%(fq)s +FOREIGN KEY +\\((?P<local>[^\\)]+?)\\) REFERENCES +(?P<table>%(iq)s[^%(fq)s]+%(fq)s(?:\\.%(iq)s[^%(fq)s]+%(fq)s)?) +\\((?P<foreign>(?:%(iq)s[^%(fq)s]+%(fq)s(?: *, *)?)+)\\)(?: +(?P<match>MATCH \\w+))?(?: +ON DELETE (?P<ondelete>%(on)s))?(?: +ON UPDATE (?P<onupdate>%(on)s))?' % kw)
        self._re_ck_constraint = _re_compile('  CONSTRAINT +%(iq)s(?P<name>(?:%(esc_fq)s|[^%(fq)s])+)%(fq)s +CHECK +\\((?P<sqltext>.+)\\),?' % kw)
        self._re_partition = _re_compile('(?:.*)(?:SUB)?PARTITION(?:.*)')
        for option in _options_of_type_string:
            self._add_option_string(option)
            for option in ('ENGINE', 'TYPE', 'AUTO_INCREMENT', 'AVG_ROW_LENGTH', 'CHARACTER SET', 'DEFAULT CHARSET', 'CHECKSUM', 'COLLATE', 'DELAY_KEY_WRITE', 'INSERT_METHOD', 'MAX_ROWS', 'MIN_ROWS', 'PACK_KEYS', 'ROW_FORMAT', 'KEY_BLOCK_SIZE', 'STATS_SAMPLE_PAGES'):
                self._add_option_word(option)
                for option in ('PARTITION BY', 'SUBPARTITION BY', 'PARTITIONS', 'SUBPARTITIONS', 'PARTITION', 'SUBPARTITION'):
                    self._add_partition_option_word(option)
                    self._add_option_regex('UNION', '\\([^\\)]+\\)')
                    self._add_option_regex('TABLESPACE', '.*? STORAGE DISK')
                    self._add_option_regex('RAID_TYPE', '\\w+\\s+RAID_CHUNKS\\s*\\=\\s*\\w+RAID_CHUNKSIZE\\s*=\\s*\\w+')
                    return None

    _optional_equals = '(?:\\s*(?:=\\s*)|\\s+)'
    
    def _add_option_string(self = None, directive = None):
        regex = f'''(?P<directive>{re.escape(directive)!s}){self._optional_equals!s}\'(?P<val>(?:[^\']|\'\')*?)\'(?!\')'''
        self._pr_options.append(_pr_compile(regex, cleanup_text))

    
    def _add_option_word(self = None, directive = None):
        regex = f'''(?P<directive>{re.escape(directive)!s}){self._optional_equals!s}(?P<val>\\w+)'''
        self._pr_options.append(_pr_compile(regex))

    
    def _add_partition_option_word(self = None, directive = None):
        if directive == 'PARTITION BY' or directive == 'SUBPARTITION BY':
            regex = f'''(?<!\\S)(?P<directive>{re.escape(directive)!s}){self._optional_equals!s}(?P<val>\\w+.*)'''
        elif directive == 'SUBPARTITIONS' or directive == 'PARTITIONS':
            regex = f'''(?<!\\S)(?P<directive>{re.escape(directive)!s}){self._optional_equals!s}(?P<val>\\d+)'''
        else:
            regex = f'''(?<!\\S)(?P<directive>{re.escape(directive)!s})(?!\\S)'''
        self._pr_options.append(_pr_compile(regex))

    
    def _add_option_regex(self = None, directive = None, regex = None):
        regex = f'''(?P<directive>{re.escape(directive)!s}){self._optional_equals!s}(?P<val>{regex!s})'''
        self._pr_options.append(_pr_compile(regex))


_options_of_type_string = ('COMMENT', 'DATA DIRECTORY', 'INDEX DIRECTORY', 'PASSWORD', 'CONNECTION')
_pr_compile = (lambda regex = None, cleanup = None: pass)()
_pr_compile = (lambda regex = None, cleanup = None: pass)()

def _pr_compile(regex = None, cleanup = None):
    '''Prepare a 2-tuple of compiled regex and callable.'''
    return (_re_compile(regex), cleanup)


def _re_compile(regex = None):
    '''Compile a string to regex, I and UNICODE.'''
    return re.compile(regex, re.I | re.UNICODE)


def _strip_values(values = None):
    '''Strip reflected values quotes'''
    strip_values = []
    for a in values:
        if a[0:1] == '"' or a[0:1] == "'":
            a = a[1:-1].replace(a[0] * 2, a[0])
        strip_values.append(a)
        return strip_values


def cleanup_text(raw_text = None):
    if '\\' in raw_text:
        raw_text = re.sub(_control_char_regexp, (lambda s: _control_char_map[s[0]]), raw_text)
    return raw_text.replace("''", "'")

_control_char_map = {
    '\\\\': '\\',
    '\\0': '\x00',
    '\\a': '\x07',
    '\\b': '\x08',
    '\\t': '\t',
    '\\n': '\n',
    '\\v': '\x0b',
    '\\f': '\x0c',
    '\\r': '\r' }
_control_char_regexp = '|'.join((lambda .0: pass# WARNING: Decompyle incomplete
)(_control_char_map()))
