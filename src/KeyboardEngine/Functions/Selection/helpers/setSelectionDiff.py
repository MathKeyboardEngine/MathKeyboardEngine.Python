from src import KeyboardMemory, Placeholder

def setSelectionDiff(k: KeyboardMemory, diffWithCurrent: int) -> None:
  k.selectionDiff = diffWithCurrent
  if diffWithCurrent == 0:
    k.inclusiveSelectionLeftBorder = None
    k.inclusiveSelectionRightBorder = None
  elif isinstance(k.current, Placeholder):
    k.inclusiveSelectionLeftBorder = k.current
    k.inclusiveSelectionRightBorder = k.current.nodes[diffWithCurrent - 1]
  else:
    nodes = k.current.parentPlaceholder.nodes
    indexOfCurrent = nodes.index(k.current)
    if diffWithCurrent > 0:
      k.inclusiveSelectionLeftBorder = nodes[indexOfCurrent + 1]
      k.inclusiveSelectionRightBorder = nodes[indexOfCurrent + diffWithCurrent]
    else:
      indexOfNewInclusiveSelectionLeftBorder = indexOfCurrent + diffWithCurrent + 1
      if indexOfNewInclusiveSelectionLeftBorder < 0:
        raise Exception('The TreeNode at index 0 of the current Placeholder is as far as you can go left if current is a TreeNode.')
      k.inclusiveSelectionLeftBorder = nodes[indexOfNewInclusiveSelectionLeftBorder]
      k.inclusiveSelectionRightBorder = k.current