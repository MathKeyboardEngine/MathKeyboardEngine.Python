from typing import List
from src import TreeNode, PartOfNumberWithDigits, Placeholder

def encapsulate_all_parts_of_number_with_digits_left_of_index(exclusive_right_index: int, sibling_nodes: List[TreeNode], to_placeholder: Placeholder) -> None:
  for i in range(exclusive_right_index - 1, -1, -1):
    sibling_node = sibling_nodes[i]
    if isinstance(sibling_node, PartOfNumberWithDigits):
      sibling_nodes.remove(sibling_node)
      to_placeholder.nodes.insert(0, sibling_node)
      sibling_node.parent_placeholder = to_placeholder
    else:
      break
