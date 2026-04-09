# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: teal.pyc (Python 3.11)

'''
    pygments.lexers.teal
    ~~~~~~~~~~~~~~~~~~~~

    Lexer for TEAL.

    :copyright: Copyright 2006-2025 by the Pygments team, see AUTHORS.
    :license: BSD, see LICENSE for details.
'''
from pygments.lexer import RegexLexer, bygroups, include, words
from pygments.token import Comment, Name, Number, String, Text, Keyword, Whitespace
__all__ = [
    'TealLexer']

class TealLexer(RegexLexer):
    '''
    For the Transaction Execution Approval Language (TEAL)

    For more information about the grammar, see:
    https://github.com/algorand/go-algorand/blob/master/data/transactions/logic/assembler.go
    '''
    name = 'teal'
    url = 'https://developer.algorand.org/docs/reference/teal/specification/'
    aliases = [
        'teal']
    filenames = [
        '*.teal']
    version_added = '2.9'
    keywords = words({
        'Fee',
        'NoOp',
        'Note',
        'TxID',
        'Type',
        'Lease',
        'OptIn',
        'Round',
        'Amount',
        'Sender',
        'VotePK',
        'RekeyTo',
        'Accounts',
        'AssetURL',
        'CloseOut',
        'Receiver',
        'TypeEnum',
        'VoteLast',
        'AssetName',
        'GroupSize',
        'LastValid',
        'MinTxnFee',
        'VoteFirst',
        'XferAsset',
        'AssetTotal',
        'ClearState',
        'FirstValid',
        'GroupIndex',
        'MaxTxnLife',
        'MinBalance',
        'NumAppArgs',
        'AssetAmount',
        'AssetFreeze',
        'AssetFrozen',
        'AssetSender',
        'ConfigAsset',
        'FreezeAsset',
        'NumAccounts',
        'SelectionPK',
        'ZeroAddress',
        'AssetBalance',
        'AssetCloseTo',
        'AssetManager',
        'AssetReserve',
        'OnCompletion',
        'ApplicationID',
        'AssetClawback',
        'AssetDecimals',
        'AssetReceiver',
        'AssetUnitName',
        'ConfigAssetURL',
        'FirstValidTime',
        'ApplicationArgs',
        'ApprovalProgram',
        'ConfigAssetName',
        'LatestTimestamp',
        'LogicSigVersion',
        'VoteKeyDilution',
        'CloseRemainderTo',
        'ConfigAssetTotal',
        'AssetMetadataHash',
        'ClearStateProgram',
        'ConfigAssetFreeze',
        'DeleteApplication',
        'FreezeAssetFrozen',
        'UpdateApplication',
        'AssetDefaultFrozen',
        'ConfigAssetManager',
        'ConfigAssetReserve',
        'FreezeAssetAccount',
        'ConfigAssetClawback',
        'ConfigAssetDecimals',
        'ConfigAssetUnitName',
        'CurrentApplicationID',
        'ConfigAssetMetadataHash',
        'ConfigAssetDefaultFrozen'}, suffix = '\\b')
    identifier = '[^ \\t\\n]+(?=\\/\\/)|[^ \\t\\n]+'
    newline = '\\r?\\n'
    tokens = {
        'root': [
            include('whitespace'),
            ('^#pragma .*' + newline, Comment.Directive),
            ('(' + identifier + ':' + ')' + '([ \t].*)', bygroups(Name.Label, Comment.Single)),
            (identifier, Name.Function, 'function-args')],
        'function-args': [
            include('whitespace'),
            ('"', String, 'string'),
            ('(b(?:ase)?(?:32|64) ?)(\\(?[a-zA-Z0-9+/=]+\\)?)', bygroups(String.Affix, String.Other)),
            ('[A-Z2-7]{58}', Number),
            ('0x[\\da-fA-F]+', Number.Hex),
            ('\\d+', Number.Integer),
            (keywords, Keyword),
            (identifier, Name.Attributes),
            (newline, Text, '#pop')],
        'string': [
            ('\\\\(?:["nrt\\\\]|x\\d\\d)', String.Escape),
            ('[^\\\\\\"\\n]+', String),
            ('"', String, '#pop')],
        'whitespace': [
            ('[ \\t]+', Whitespace),
            ('//[^\\n]+', Comment.Single)] }
