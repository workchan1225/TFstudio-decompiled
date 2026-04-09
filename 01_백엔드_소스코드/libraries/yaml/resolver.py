# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: resolver.pyc (Python 3.11)

__all__ = [
    'BaseResolver',
    'Resolver']
from error import *
from nodes import *
import re

class ResolverError(YAMLError):
    pass


class BaseResolver:
    DEFAULT_SCALAR_TAG = 'tag:yaml.org,2002:str'
    DEFAULT_SEQUENCE_TAG = 'tag:yaml.org,2002:seq'
    DEFAULT_MAPPING_TAG = 'tag:yaml.org,2002:map'
    yaml_implicit_resolvers = { }
    yaml_path_resolvers = { }
    
    def __init__(self):
        self.resolver_exact_paths = []
        self.resolver_prefix_paths = []

    add_implicit_resolver = (lambda cls, tag, regexp, first: pass# WARNING: Decompyle incomplete
)()
    add_path_resolver = (lambda cls, tag, path, kind = (None,): if 'yaml_path_resolvers' not in cls.__dict__:
cls.yaml_path_resolvers = cls.yaml_path_resolvers.copy()new_path = []# WARNING: Decompyle incomplete
)()
    
    def descend_resolver(self, current_node, current_index):
        if not self.yaml_path_resolvers:
            return None
        exact_paths = None
        prefix_paths = []
        if current_node:
            depth = len(self.resolver_prefix_paths)
            for path, kind in self.resolver_prefix_paths[-1]:
                if self.check_resolver_prefix(depth, path, kind, current_node, current_index):
                    if len(path) > depth:
                        prefix_paths.append((path, kind))
                        continue
                    exact_paths[kind] = self.yaml_path_resolvers[(path, kind)]
        for path, kind in self.yaml_path_resolvers:
            if not path:
                exact_paths[kind] = self.yaml_path_resolvers[(path, kind)]
                continue
            prefix_paths.append((path, kind))
            self.resolver_exact_paths.append(exact_paths)
            self.resolver_prefix_paths.append(prefix_paths)
            return None

    
    def ascend_resolver(self):
        if not self.yaml_path_resolvers:
            return None
        None.resolver_exact_paths.pop()
        self.resolver_prefix_paths.pop()

    
    def check_resolver_prefix(self, depth, path, kind, current_node, current_index):
        (node_check, index_check) = path[depth - 1]
        if isinstance(node_check, str):
            if current_node.tag != node_check:
                return None
    # WARNING: Decompyle incomplete

    
    def resolve(self, kind, value, implicit):
