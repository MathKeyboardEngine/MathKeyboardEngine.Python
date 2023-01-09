from typing import Union
from src import BranchingNode, KeyboardMemory, Placeholder, TreeNode
from src._helpers.coalesce import coalesce
from src._helpers.first_after_or_none import first_after_or_none

def move_right(k: KeyboardMemory) -> None:
  if isinstance(k.current, Placeholder):
    if len(k.current.nodes) > 0:
      next_node = k.current.nodes[0]
      k.current = next_node.placeholders[0] if isinstance(next_node, BranchingNode) else next_node
    elif k.current.parent_node is None:
      return
    else:
      k.current = coalesce(first_after_or_none(k.current.parent_node.placeholders, k.current), k.current.parent_node)
  else:
    next_node: Union[TreeNode, None] = first_after_or_none(k.current.parent_placeholder.nodes, k.current)
    if next_node is not None:
      k.current = next_node.placeholders[0] if isinstance(next_node, BranchingNode) else next_node
    else:
      ancestor_node = k.current.parent_placeholder.parent_node
      if ancestor_node is not None:
        next_placeholder: Union[Placeholder, None] = first_after_or_none(ancestor_node.placeholders, k.current.parent_placeholder)
        k.current = coalesce(next_placeholder, ancestor_node)