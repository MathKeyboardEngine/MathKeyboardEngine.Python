from src import BranchingNode, insertWithEncapsulateCurrent, KeyboardMemory
from src.KeyboardEngine.Functions.helpers.encapsulate import encapsulate
from src.KeyboardEngine.Functions.Selection.helpers.popSelection import popSelection
from src.helpers.coalesce import coalesce
from src.helpers.lastOrNone import lastOrNone

def insertWithEncapsulateSelectionAndPrevious(k: KeyboardMemory, newNode: BranchingNode) -> None:
  if len(newNode.placeholders) < 2:
    raise Exception('Expected 2 placeholders.')
  selection = popSelection(k)
  secondPlaceholder = newNode.placeholders[1]
  encapsulate(selection, secondPlaceholder)
  insertWithEncapsulateCurrent(k, newNode)
  k.current = coalesce(lastOrNone(selection), secondPlaceholder)