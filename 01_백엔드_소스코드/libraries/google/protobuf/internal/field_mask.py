# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: field_mask.pyc (Python 3.11)

'''Contains FieldMask class.'''
from google.protobuf.descriptor import FieldDescriptor

class FieldMask(object):
    '''Class for FieldMask message type.'''
    __slots__ = ()
    
    def ToJsonString(self):
        '''Converts FieldMask to string according to proto3 JSON spec.'''
        camelcase_paths = []
        for path in self.paths:
            camelcase_paths.append(_SnakeCaseToCamelCase(path))
            return ','.join(camelcase_paths)

    
    def FromJsonString(self, value):
        '''Converts string to FieldMask according to proto3 JSON spec.'''
        if not isinstance(value, str):
            raise ValueError('FieldMask JSON value not a string: {!r}'.format(value))
        self.Clear()
        if value:
            for path in value.split(','):
                self.paths.append(_CamelCaseToSnakeCase(path))
                return None
                return None

    
    def IsValidForDescriptor(self, message_descriptor):
        '''Checks whether the FieldMask is valid for Message Descriptor.'''
        for path in self.paths:
            if not _IsValidPath(message_descriptor, path):
                return False
            return True

    
    def AllFieldsFromDescriptor(self, message_descriptor):
        '''Gets all direct fields of Message Descriptor to FieldMask.'''
        self.Clear()
        for field in message_descriptor.fields:
            self.paths.append(field.name)
            return None

    
    def CanonicalFormFromMask(self, mask):
        '''Converts a FieldMask to the canonical form.

    Removes paths that are covered by another path. For example,
    "foo.bar" is covered by "foo" and will be removed if "foo"
    is also in the FieldMask. Then sorts all paths in alphabetical order.

    Args:
      mask: The original FieldMask to be converted.
    '''
        tree = _FieldMaskTree(mask)
        tree.ToFieldMask(self)

    
    def Union(self, mask1, mask2):
        '''Merges mask1 and mask2 into this FieldMask.'''
        _CheckFieldMaskMessage(mask1)
        _CheckFieldMaskMessage(mask2)
        tree = _FieldMaskTree(mask1)
        tree.MergeFromFieldMask(mask2)
        tree.ToFieldMask(self)

    
    def Intersect(self, mask1, mask2):
        '''Intersects mask1 and mask2 into this FieldMask.'''
        _CheckFieldMaskMessage(mask1)
        _CheckFieldMaskMessage(mask2)
        tree = _FieldMaskTree(mask1)
        intersection = _FieldMaskTree()
        for path in mask2.paths:
            tree.IntersectPath(path, intersection)
            intersection.ToFieldMask(self)
            return None

    
    def MergeMessage(self, source, destination, replace_message_field, replace_repeated_field = (False, False)):
        '''Merges fields specified in FieldMask from source to destination.

    Args:
      source: Source message.
      destination: The destination message to be merged into.
      replace_message_field: Replace message field if True. Merge message
          field if False.
      replace_repeated_field: Replace repeated field if True. Append
          elements of repeated field if False.
    '''
        tree = _FieldMaskTree(self)
        tree.MergeMessage(source, destination, replace_message_field, replace_repeated_field)



def _IsValidPath(message_descriptor, path):
    '''Checks whether the path is valid for Message Descriptor.'''
    parts = path.split('.')
    last = parts.pop()
# WARNING: Decompyle incomplete


def _CheckFieldMaskMessage(message):
    '''Raises ValueError if message is not a FieldMask.'''
    message_descriptor = message.DESCRIPTOR
    if message_descriptor.name != 'FieldMask' or message_descriptor.file.name != 'google/protobuf/field_mask.proto':
        raise ValueError('Message {0} is not a FieldMask.'.format(message_descriptor.full_name))


def _SnakeCaseToCamelCase(path_name):
    '''Converts a path name from snake_case to camelCase.'''
    result = []
    after_underscore = False
    for c in path_name:
        if c.isupper():
            raise ValueError('Fail to print FieldMask to Json string: Path name {0} must not contain uppercase letters.'.format(path_name))
        if after_underscore:
            if c.islower():
                result.append(c.upper())
                after_underscore = False
                continue
            raise ValueError('Fail to print FieldMask to Json string: The character after a "_" must be a lowercase letter in path name {0}.'.format(path_name))
        if c == '_':
            after_underscore = True
            continue
        result += c
        if after_underscore:
            raise ValueError('Fail to print FieldMask to Json string: Trailing "_" in path name {0}.'.format(path_name))
        return ''.join(result)


def _CamelCaseToSnakeCase(path_name):
    '''Converts a field name from camelCase to snake_case.'''
    result = []
    for c in path_name:
        if c == '_':
            raise ValueError('Fail to parse FieldMask: Path name {0} must not contain "_"s.'.format(path_name))
        if c.isupper():
            result += '_'
            result += c.lower()
            continue
        result += c
        return ''.join(result)


class _FieldMaskTree(object):
    '''Represents a FieldMask in a tree structure.

  For example, given a FieldMask "foo.bar,foo.baz,bar.baz",
  the FieldMaskTree will be:
      [_root] -+- foo -+- bar
            |       |
            |       +- baz
            |
            +- bar --- baz
  In the tree, each leaf node represents a field path.
  '''
    __slots__ = ('_root',)
    
    def __init__(self, field_mask = (None,)):
        '''Initializes the tree by FieldMask.'''
        self._root = { }
        if field_mask:
            self.MergeFromFieldMask(field_mask)
            return None

    
    def MergeFromFieldMask(self, field_mask):
        '''Merges a FieldMask to the tree.'''
        for path in field_mask.paths:
            self.AddPath(path)
            return None

    
    def AddPath(self, path):
        """Adds a field path into the tree.

    If the field path to add is a sub-path of an existing field path
    in the tree (i.e., a leaf node), it means the tree already matches
    the given path so nothing will be added to the tree. If the path
    matches an existing non-leaf node in the tree, that non-leaf node
    will be turned into a leaf node with all its children removed because
    the path matches all the node's children. Otherwise, a new path will
    be added.

    Args:
      path: The field path to add.
    """
        node = self._root
        for name in path.split('.'):
            if name not in node:
                node[name] = { }
            elif not node[name]:
                return None
            node = node[name]
            node.clear()
            return None

    
    def ToFieldMask(self, field_mask):
        '''Converts the tree to a FieldMask.'''
        field_mask.Clear()
        _AddFieldPaths(self._root, '', field_mask)

    
    def IntersectPath(self, path, intersection):
        '''Calculates the intersection part of a field path with this tree.

    Args:
      path: The field path to calculates.
      intersection: The out tree to record the intersection part.
    '''
        node = self._root
        for name in path.split('.'):
            if name not in node:
                return None
            if not None[name]:
                intersection.AddPath(path)
                return None
            node = None[name]
            intersection.AddLeafNodes(path, node)
            return None

    
    def AddLeafNodes(self, prefix, node):
        '''Adds leaf nodes begin with prefix to this tree.'''
        if not node:
            self.AddPath(prefix)
        for name in node:
            child_path = prefix + '.' + name
            self.AddLeafNodes(child_path, node[name])
            return None

    
    def MergeMessage(self, source, destination, replace_message, replace_repeated):
        '''Merge all fields specified by this tree from source to destination.'''
        _MergeMessage(self._root, source, destination, replace_message, replace_repeated)



def _StrConvert(value):
    '''Converts value to str if it is not.'''
    if not isinstance(value, str):
        return value.encode('utf-8')


def _MergeMessage(node, source, destination, replace_message, replace_repeated):
    '''Merge all fields specified by a sub-tree from source to destination.'''
    source_descriptor = source.DESCRIPTOR
# WARNING: Decompyle incomplete


def _AddFieldPaths(node, prefix, field_mask):
    '''Adds the field paths descended from node to field_mask.'''
    if node and prefix:
        field_mask.paths.append(prefix)
        return None
    for name in None(node):
        if prefix:
            child_path = prefix + '.' + name
        else:
            child_path = name
        _AddFieldPaths(node[name], child_path, field_mask)
        return None
