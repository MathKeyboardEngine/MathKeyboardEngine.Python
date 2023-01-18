from typing import Union

from src import BranchingNode, KeyboardMemory, PartOfNumberWithDigits, Placeholder, TreeNode
from src._helpers.coalesce import coalesce
from src._helpers.first_before_or_none import first_before_or_none
from src._helpers.last_or_none import last_or_none
from src.keyboard_engine.functions._helpers.encapsulate_all_parts_of_number_with_digits_left_of_index import encapsulate_all_parts_of_number_with_digits_left_of_index
from src.keyboard_engine.functions._helpers.get_first_non_empty_on_left_of import get_first_non_empty_on_left_of


def delete_current(k: KeyboardMemory) -> None:
  if isinstance(k.current, Placeholder):
    if k.current.parent_node is None or len(k.current.nodes) > 0:
      return
    else:
      non_empty_placeholder_on_left: Union[Placeholder, None] = get_first_non_empty_on_left_of(k.current.parent_node.placeholders, k.current)
      if non_empty_placeholder_on_left:
        if len(k.current.parent_node.placeholders) == 2 and k.current == k.current.parent_node.placeholders[1] and len(k.current.nodes) == 0:
          delete_outer_branching_node_but_not_its_contents(k, non_empty_placeholder_on_left)
        else:
          non_empty_placeholder_on_left.nodes.pop()
          k.current = coalesce(last_or_none(non_empty_placeholder_on_left.nodes), non_empty_placeholder_on_left)
      elif all(len(ph.nodes) == 0 for ph in k.current.parent_node.placeholders):
        ancestor_placeholder = k.current.parent_node.parent_placeholder
        previous_node = first_before_or_none(ancestor_placeholder.nodes, k.current.parent_node)
        ancestor_placeholder.nodes.remove(k.current.parent_node)
        k.current = coalesce(previous_node, ancestor_placeholder)
      elif k.current.parent_node.placeholders[0] == k.current and len(k.current.nodes) == 0 and any(len(ph.nodes) != 0 for ph in k.current.parent_node.placeholders):
        previous_node = first_before_or_none(k.current.parent_node.parent_placeholder.nodes, k.current.parent_node)
        if previous_node is not None:
          encapsulate_previous_into(previous_node, k.current)
          k.current = k.current.nodes[-1]
        else:
          non_empty_sibling_placeholders = list(filter(lambda p: len(p.nodes) != 0, k.current.parent_node.placeholders))
          if len(non_empty_sibling_placeholders) == 1:
            nodes = non_empty_sibling_placeholders[0].nodes
            ancestor_placeholder = k.current.parent_node.parent_placeholder
            index_of_parent_node = ancestor_placeholder.nodes.index(k.current.parent_node)
            for node in nodes:
              node.parent_placeholder = ancestor_placeholder
            ancestor_placeholder.nodes[index_of_parent_node: index_of_parent_node + 1] = nodes
            k.current = nodes[-1]
  else:
    if isinstance(k.current, BranchingNode) and len(k.current.placeholders[0].nodes) > 0 and all(len(ph.nodes) == 0 for ph in k.current.placeholders[1:]):
      delete_outer_branching_node_but_not_its_contents(k, k.current.placeholders[0])
    elif isinstance(k.current, BranchingNode) and any(len(ph.nodes) > 0 for ph in k.current.placeholders):
      k.current = [node for ph in k.current.placeholders for node in ph.nodes][-1]
      delete_current(k)
    else:
      previous_node: Union[TreeNode, None] = first_before_or_none(k.current.parent_placeholder.nodes, k.current)
      k.current.parent_placeholder.nodes.remove(k.current)
      k.current = coalesce(previous_node, k.current.parent_placeholder)

def encapsulate_previous_into(previous_node: TreeNode, target_placeholder: Placeholder):
  target_placeholder.parent_node.parent_placeholder.nodes.remove(previous_node)
  target_placeholder.nodes.append(previous_node)
  previous_node_old_parent_placeholder = previous_node.parent_placeholder
  previous_node.parent_placeholder = target_placeholder
  if isinstance(previous_node, PartOfNumberWithDigits):
    encapsulate_all_parts_of_number_with_digits_left_of_index(len(previous_node_old_parent_placeholder.nodes) - 1, previous_node_old_parent_placeholder.nodes, target_placeholder)

def delete_outer_branching_node_but_not_its_contents(k: KeyboardMemory, non_empty_placeholder: Placeholder):
  outer_branchingnode = non_empty_placeholder.parent_node
  index_of_outer_branchingnode = outer_branchingnode.parent_placeholder.nodes.index(outer_branchingnode)
  outer_branchingnode.parent_placeholder.nodes[index_of_outer_branchingnode: index_of_outer_branchingnode + 1] = non_empty_placeholder.nodes
  for node in non_empty_placeholder.nodes:
    node.parent_placeholder = outer_branchingnode.parent_placeholder
  k.current = non_empty_placeholder.nodes[-1]