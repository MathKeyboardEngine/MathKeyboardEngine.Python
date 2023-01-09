from src import KeyboardMemory, Placeholder

def set_selection_diff(k: KeyboardMemory, diffWithCurrent: int) -> None:
  k.selection_diff = diffWithCurrent
  if diffWithCurrent == 0:
    k.inclusive_selection_left_border = None
    k.inclusive_selection_right_border = None
  elif isinstance(k.current, Placeholder):
    k.inclusive_selection_left_border = k.current
    k.inclusive_selection_right_border = k.current.nodes[diffWithCurrent - 1]
  else:
    nodes = k.current.parent_placeholder.nodes
    indexOfCurrent = nodes.index(k.current)
    if diffWithCurrent > 0:
      k.inclusive_selection_left_border = nodes[indexOfCurrent + 1]
      k.inclusive_selection_right_border = nodes[indexOfCurrent + diffWithCurrent]
    else:
      indexOfNewInclusiveSelectionLeftBorder = indexOfCurrent + diffWithCurrent + 1
      if indexOfNewInclusiveSelectionLeftBorder < 0:
        raise Exception('The TreeNode at index 0 of the current Placeholder is as far as you can go left if current is a TreeNode.')
      k.inclusive_selection_left_border = nodes[indexOfNewInclusiveSelectionLeftBorder]
      k.inclusive_selection_right_border = k.current