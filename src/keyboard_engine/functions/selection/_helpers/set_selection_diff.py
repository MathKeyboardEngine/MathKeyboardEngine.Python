from src import KeyboardMemory, Placeholder

def set_selection_diff(k: KeyboardMemory, diff_with_current: int) -> None:
  k.selection_diff = diff_with_current
  if diff_with_current == 0:
    k.inclusive_selection_left_border = None
    k.inclusive_selection_right_border = None
  elif isinstance(k.current, Placeholder):
    k.inclusive_selection_left_border = k.current
    k.inclusive_selection_right_border = k.current.nodes[diff_with_current - 1]
  else:
    nodes = k.current.parent_placeholder.nodes
    index_of_current = nodes.index(k.current)
    if diff_with_current > 0:
      k.inclusive_selection_left_border = nodes[index_of_current + 1]
      k.inclusive_selection_right_border = nodes[index_of_current + diff_with_current]
    else:
      index_of_new_inclusive_selection_left_border = index_of_current + diff_with_current + 1
      if index_of_new_inclusive_selection_left_border < 0:
        raise Exception('The TreeNode at index 0 of the current Placeholder is as far as you can go left if current is a TreeNode.')
      k.inclusive_selection_left_border = nodes[index_of_new_inclusive_selection_left_border]
      k.inclusive_selection_right_border = k.current