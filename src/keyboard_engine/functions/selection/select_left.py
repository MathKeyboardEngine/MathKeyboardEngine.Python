from src import KeyboardMemory, Placeholder, TreeNode
from src._helpers.coalesce import coalesce
from src.keyboard_engine.functions.selection._helpers.set_selection_diff import set_selection_diff

def select_left(k: KeyboardMemory) -> None:
  oldDiffWithCurrent = coalesce(k.selection_diff, 0)
  if (
    (isinstance(k.current, TreeNode) and k.current.parent_placeholder.nodes.index(k.current) + oldDiffWithCurrent >= 0) or 
    (isinstance(k.current, Placeholder) and oldDiffWithCurrent > 0)
  ):
    set_selection_diff(k, oldDiffWithCurrent - 1)
  elif (
    isinstance(k.inclusive_selection_left_border, TreeNode) and 
    k.inclusive_selection_left_border.parent_placeholder.nodes.index(k.inclusive_selection_left_border) == 0 and
    k.inclusive_selection_left_border.parent_placeholder.parent_node is not None
  ):
    k.current = k.inclusive_selection_left_border.parent_placeholder.parent_node
    set_selection_diff(k, -1)