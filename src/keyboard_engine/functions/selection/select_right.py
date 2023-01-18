from src import KeyboardMemory, Placeholder, TreeNode
from src._helpers.coalesce import coalesce
from src._helpers.first_before_or_none import first_before_or_none
from src.keyboard_engine.functions.selection._helpers.set_selection_diff import set_selection_diff


def select_right(k: KeyboardMemory) -> None:
  old_diff_with_current = coalesce(k.selection_diff, 0)
  if (
    (isinstance(k.current, Placeholder) and old_diff_with_current < len(k.current.nodes)) or
    (isinstance(k.current, TreeNode) and k.current.parent_placeholder.nodes.index(k.current) + old_diff_with_current < len(k.current.parent_placeholder.nodes) - 1)
  ):
    set_selection_diff(k, old_diff_with_current + 1)
  elif (
    isinstance(k.inclusive_selection_right_border, TreeNode) and
    k.inclusive_selection_right_border.parent_placeholder.nodes[-1] == k.inclusive_selection_right_border and
    k.inclusive_selection_right_border.parent_placeholder.parent_node is not None
  ):
    ancestor_node = k.inclusive_selection_right_border.parent_placeholder.parent_node
    k.current = coalesce(first_before_or_none(ancestor_node.parent_placeholder.nodes, ancestor_node), ancestor_node.parent_placeholder)
    set_selection_diff(k, 1)