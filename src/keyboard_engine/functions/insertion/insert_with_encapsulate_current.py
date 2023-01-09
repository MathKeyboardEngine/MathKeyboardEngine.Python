from src import KeyboardMemory, BranchingNode, insert, move_right, PartOfNumberWithDigits, RoundBracketsNode, TreeNode
from src.keyboard_engine.functions._helpers.encapsulate import encapsulate
from src.keyboard_engine.functions._helpers.encapsulate_all_parts_of_number_with_digits_left_of_index import encapsulate_all_parts_of_number_with_digits_left_of_index
from src._helpers.coalesce import coalesce
from src._helpers.first_after_or_none import first_after_or_none

def insert_with_encapsulate_current(k: KeyboardMemory, new_node: BranchingNode, delete_outer_round_brackets_if_any : bool = False) -> None:
  encapsulating_placeholder = new_node.placeholders[0]
  if isinstance(k.current, TreeNode):
    sibling_nodes = k.current.parent_placeholder.nodes
    current_index = sibling_nodes.index(k.current)
    sibling_nodes[current_index] = new_node
    new_node.parent_placeholder = k.current.parent_placeholder
    if isinstance(k.current, RoundBracketsNode) and delete_outer_round_brackets_if_any:
      encapsulate(k.current.placeholders[0].nodes, encapsulating_placeholder)
      k.current = coalesce(first_after_or_none(new_node.placeholders, encapsulating_placeholder), new_node)
    elif isinstance(k.current, PartOfNumberWithDigits):
      encapsulating_placeholder.nodes.append(k.current)
      k.current.parent_placeholder = encapsulating_placeholder
      encapsulate_all_parts_of_number_with_digits_left_of_index(current_index, sibling_nodes, encapsulating_placeholder)
      move_right(k)
    else:
      encapsulating_placeholder.nodes.append(k.current)
      k.current.parent_placeholder = encapsulating_placeholder
      move_right(k)
  else:
    insert(k, new_node)