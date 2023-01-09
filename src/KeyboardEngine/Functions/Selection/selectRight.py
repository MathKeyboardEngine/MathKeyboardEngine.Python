from src import KeyboardMemory, Placeholder, TreeNode
from src.KeyboardEngine.Functions.Selection.helpers.setSelectionDiff import setSelectionDiff
from src.helpers.coalesce import coalesce
from src.helpers.firstBeforeOrNone import firstBeforeOrNone

def selectRight(k: KeyboardMemory) -> None:
  oldDiffWithCurrent = coalesce(k.selectionDiff, 0)
  if (
    (isinstance(k.current, Placeholder) and oldDiffWithCurrent < len(k.current.nodes)) or
    (isinstance(k.current, TreeNode) and k.current.parentPlaceholder.nodes.index(k.current) + oldDiffWithCurrent < len(k.current.parentPlaceholder.nodes) - 1)
  ):
    setSelectionDiff(k, oldDiffWithCurrent + 1)
  elif (
    isinstance(k.inclusiveSelectionRightBorder, TreeNode) and
    k.inclusiveSelectionRightBorder.parentPlaceholder.nodes[-1] == k.inclusiveSelectionRightBorder and
    k.inclusiveSelectionRightBorder.parentPlaceholder.parentNode is not None
  ):
    ancestorNode = k.inclusiveSelectionRightBorder.parentPlaceholder.parentNode
    k.current = coalesce(firstBeforeOrNone(ancestorNode.parentPlaceholder.nodes, ancestorNode), ancestorNode.parentPlaceholder)
    setSelectionDiff(k, 1)