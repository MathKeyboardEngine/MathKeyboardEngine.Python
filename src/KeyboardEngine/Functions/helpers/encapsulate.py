from typing import List
from src import Placeholder, TreeNode

def encapsulate(nodes: List[TreeNode], encapsulatingPlaceholder: Placeholder) -> None:
  for node in nodes:
    node.parentPlaceholder = encapsulatingPlaceholder
    encapsulatingPlaceholder.nodes.append(node)
