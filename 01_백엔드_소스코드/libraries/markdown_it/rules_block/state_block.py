# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: state_block.pyc (Python 3.11)

from __future__ import annotations
from typing import TYPE_CHECKING, Literal
from common.utils import isStrSpace
from ruler import StateBase
from token import Token
from utils import EnvType
if TYPE_CHECKING:
    from markdown_it.main import MarkdownIt

class StateBlock(StateBase):
    
    def __init__(self, src = None, md = None, env = None, tokens = ('src', 'str', 'md', 'MarkdownIt', 'env', 'EnvType', 'tokens', 'list[Token]', 'return', 'None')):
        self.src = src
        self.md = md
        self.env = env
        self.tokens = tokens
        self.bMarks = []
        self.eMarks = []
        self.tShift = []
        self.sCount = []
        self.bsCount = []
        self.blkIndent = 0
        self.line = 0
        self.lineMax = 0
        self.tight = False
        self.ddIndent = -1
        self.listIndent = -1
        self.parentType = 'root'
        self.level = 0
        self.result = ''
        indent_found = False
        start = 0
        pos = 0
        indent = 0
        offset = 0
        length = len(self.src)
        for pos, character in enumerate(self.src):
            if not indent_found:
                if isStrSpace(character):
                    indent += 1
                    if character == '\t':
                        offset += 4 - offset % 4
                    else:
                        offset += 1
                    continue
                indent_found = True
            if character == '\n' or pos == length - 1:
                if character != '\n':
                    pos += 1
                self.bMarks.append(start)
                self.eMarks.append(pos)
                self.tShift.append(indent)
                self.sCount.append(offset)
                self.bsCount.append(0)
                indent_found = False
                indent = 0
                offset = 0
                start = pos + 1
            self.bMarks.append(length)
            self.eMarks.append(length)
            self.tShift.append(0)
            self.sCount.append(0)
            self.bsCount.append(0)
            self.lineMax = len(self.bMarks) - 1
            self._code_enabled = 'code' in self.md['block'].ruler.get_active_rules()
            return None

    
    def __repr__(self = None):
        return f'''{self.__class__.__name__}(line={self.line},level={self.level},tokens={len(self.tokens)})'''

    
    def push(self = None, ttype = None, tag = None, nesting = ('ttype', 'str', 'tag', 'str', 'nesting', 'Literal[-1, 0, 1]', 'return', 'Token')):
        '''Push new token to "stream".'''
        token = Token(ttype, tag, nesting)
        token.block = True
        if nesting < 0:
            pass
        self.level = self, self.level -= 1, .level
        if nesting > 0:
            pass
        self.tokens.append(token)
        return token

    
    def isEmpty(self = None, line = None):
        '''.'''
        return self.bMarks[line] + self.tShift[line] >= self.eMarks[line]

    
    def skipEmptyLines(self = None, from_pos = None):
        '''.'''
        pass
    # WARNING: Decompyle incomplete

    
    def skipSpaces(self = None, pos = None):
        '''Skip spaces from given position.'''
        
        try:
            current = self.src[pos]
        except IndexError:
            pass
        except:
            if not isStrSpace(current):
                pass
            else:
                pos += 1

        return pos

    
    def skipSpacesBack(self = None, pos = None, minimum = None):
        '''Skip spaces from given position in reverse.'''
        if pos <= minimum:
            return pos
    # WARNING: Decompyle incomplete

    
    def skipChars(self = None, pos = None, code = None):
        '''Skip character code from given position.'''
        
        try:
            current = self.srcCharCode[pos]
        except IndexError:
            pass
        except:
            if current != code:
                pass
            else:
                pos += 1

        return pos

    
    def skipCharsStr(self = None, pos = None, ch = None):
        '''Skip character string from given position.'''
        
        try:
            current = self.src[pos]
        except IndexError:
            pass
        except:
            if current != ch:
                pass
            else:
                pos += 1

        return pos

    
    def skipCharsBack(self = None, pos = None, code = None, minimum = ('pos', 'int', 'code', 'int', 'minimum', 'int', 'return', 'int')):
        '''Skip character code reverse from given position - 1.'''
        if pos <= minimum:
            return pos
    # WARNING: Decompyle incomplete

    
    def skipCharsStrBack(self = None, pos = None, ch = None, minimum = ('pos', 'int', 'ch', 'str', 'minimum', 'int', 'return', 'int')):
        '''Skip character string reverse from given position - 1.'''
        if pos <= minimum:
            return pos
    # WARNING: Decompyle incomplete

    
    def getLines(self, begin = None, end = None, indent = None, keepLastLF = ('begin', 'int', 'end', 'int', 'indent', 'int', 'keepLastLF', 'bool', 'return', 'str')):
        '''Cut lines range from source.'''
        line = begin
        if begin >= end:
            return ''
        queue = [
            None] * (end - begin)
        i = 1
    # WARNING: Decompyle incomplete

    
    def is_code_block(self = None, line = None):
        '''Check if line is a code block,
        i.e. the code block rule is enabled and text is indented by more than 3 spaces.
        '''
        if self._code_enabled:
            pass
        return self.sCount[line] - self.blkIndent >= 4
