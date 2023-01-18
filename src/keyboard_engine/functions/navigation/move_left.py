from typing import Union

from src import BranchingNode, KeyboardMemory, Placeholder, TreeNode
from src._helpers.coalesce import coalesce
from src._helpers.first_before_or_none import first_before_or_none
from src._helpers.last_or_none import last_or_none


def move_left(k: KeyboardMemory) -> None:
  if isinstance(k.current, Placeholder):
    if k.current.parent_node is None:
      return
    previous_placeholder: Union[Placeholder, None] = first_before_or_none(k.current.parent_node.placeholders, k.current)
    if previous_placeholder is not None:
      k.current = coalesce(last_or_none(previous_placeholder.nodes), previous_placeholder)
    else:
      ancestor_placeholder = k.current.parent_node.parent_placeholder
      node_previous_to_parent_of_current: Union[TreeNode, None] = first_before_or_none(ancestor_placeholder.nodes, k.current.parent_node)
      k.current = coalesce(node_previous_to_parent_of_current, ancestor_placeholder)
  else:
    if isinstance(k.current, BranchingNode):
      placeholder = k.current.placeholders[-1]
      k.current = coalesce(last_or_none(placeholder.nodes), placeholder)
    else:
      k.current = coalesce(first_before_or_none(k.current.parent_placeholder.nodes, k.current), k.current.parent_placeholder)