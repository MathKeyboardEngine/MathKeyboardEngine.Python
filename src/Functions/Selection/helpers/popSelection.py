from typing import List
from src import KeyboardMemory, leaveSelectionMode, Placeholder, TreeNode
from src.helpers.firstBeforeOrNone import firstBeforeOrNone
from src.helpers.coalesce import coalesce

def popSelection(k: KeyboardMemory) -> List[TreeNode]:
  if k.selectionDiff is None:
    raise Exception('Enter selection mode before calling this method.')
  if k.selectionDiff == 0:
    leaveSelectionMode(k)
    return []
  diff = k.selectionDiff
  if isinstance(k.current, Placeholder):
    leaveSelectionMode(k)
    return [k.current.nodes.pop(0) for i in range(diff)]
  else:
    siblings = k.current.parentPlaceholder.nodes
    indexOfLeftBorder = siblings.index(k.inclusiveSelectionLeftBorder)
    k.current = coalesce(firstBeforeOrNone(siblings, k.inclusiveSelectionLeftBorder), k.current.parentPlaceholder)
    leaveSelectionMode(k)
    return [siblings.pop(indexOfLeftBorder) for i in range(abs(diff))]