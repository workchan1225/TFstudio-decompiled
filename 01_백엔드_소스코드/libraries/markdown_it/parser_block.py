# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: parser_block.pyc (Python 3.11)

'''Block-level tokenizer.'''
from __future__ import annotations
from collections.abc import Callable
import logging
from typing import TYPE_CHECKING
from  import rules_block
from ruler import Ruler
from rules_block.state_block import StateBlock
from token import Token
from utils import EnvType
if TYPE_CHECKING:
    from markdown_it import MarkdownIt
LOGGER = logging.getLogger(__name__)
RuleFuncBlockType = Callable[([
    StateBlock,
    int,
    int,
    bool], bool)]
_rules: 'list[tuple[str, RuleFuncBlockType, list[str]]]' = [
    ('table', rules_block.table, [
        'paragraph',
        'reference']),
    ('code', rules_block.code, []),
    ('fence', rules_block.fence, [
        'paragraph',
        'reference',
        'blockquote',
        'list']),
    ('blockquote', rules_block.blockquote, [
        'paragraph',
        'reference',
        'blockquote',
        'list']),
    ('hr', rules_block.hr, [
        'paragraph',
        'reference',
        'blockquote',
        'list']),
    ('list', rules_block.list_block, [
        'paragraph',
        'reference',
        'blockquote']),
    ('reference', rules_block.reference, []),
    ('html_block', rules_block.html_block, [
        'paragraph',
        'reference',
        'blockquote']),
    ('heading', rules_block.heading, [
        'paragraph',
        'reference',
        'blockquote']),
    ('lheading', rules_block.lheading, []),
    ('paragraph', rules_block.paragraph, [])]

class ParserBlock:
    '''
    ParserBlock#ruler -> Ruler

    [[Ruler]] instance. Keep configuration of block rules.
    '''
    
    def __init__(self = None):
        self.ruler = Ruler[RuleFuncBlockType]()
        for name, rule, alt in _rules:
            self.ruler.push(name, rule, {
                'alt': alt })
            return None

    
    def tokenize(self = None, state = None, startLine = None, endLine = ('state', 'StateBlock', 'startLine', 'int', 'endLine', 'int', 'return', 'None')):
        '''Generate tokens for input range.'''
        rules = self.ruler.getRules('')
        line = startLine
        maxNesting = state.md.options.maxNesting
        hasEmptyLines = False
    # WARNING: Decompyle incomplete

    
    def parse(self, src = None, md = None, env = None, outTokens = ('src', 'str', 'md', 'MarkdownIt', 'env', 'EnvType', 'outTokens', 'list[Token]', 'return', 'list[Token] | None')):
        '''Process input string and push block tokens into `outTokens`.'''
        if not src:
            return None
        state = None(src, md, env, outTokens)
        self.tokenize(state, state.line, state.lineMax)
        return state.tokens
