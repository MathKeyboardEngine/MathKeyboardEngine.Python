from src import KeyboardMemory, Placeholder, TreeNode
from src.keyboard_engine.functions_temp.selection_temp.helpers.set_selection_diff import set_selection_diff
from src.helpers.coalesce import coalesce
from src.helpers.first_before_or_none import first_before_or_none

def select_right(k: KeyboardMemory) -> None:
  oldDiffWithCurrent = coalesce(k.selection_diff, 0)
  if (
    (isinstance(k.current, Placeholder) and oldDiffWithCurrent < len(k.current.nodes)) or
    (isinstance(k.current, TreeNode) and k.current.parent_placeholder.nodes.index(k.current) + oldDiffWithCurrent < len(k.current.parent_placeholder.nodes) - 1)
  ):
    set_selection_diff(k, oldDiffWithCurrent + 1)
  elif (
    isinstance(k.inclusive_selection_right_border, TreeNode) and
    k.inclusive_selection_right_border.parent_placeholder.nodes[-1] == k.inclusive_selection_right_border and
    k.inclusive_selection_right_border.parent_placeholder.parent_node is not None
  ):
    ancestorNode = k.inclusive_selection_right_border.parent_placeholder.parent_node
    k.current = coalesce(first_before_or_none(ancestorNode.parent_placeholder.nodes, ancestorNode), ancestorNode.parent_placeholder)
    set_selection_diff(k, 1)