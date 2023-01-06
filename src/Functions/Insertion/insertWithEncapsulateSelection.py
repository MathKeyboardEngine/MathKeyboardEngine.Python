from src import BranchingNode, insert, KeyboardMemory, moveRight
from src.Functions.helpers.encapsulate import encapsulate
from src.Functions.Selection.helpers.popSelection import popSelection

def insertWithEncapsulateSelection(k: KeyboardMemory, newNode: BranchingNode) -> None:
  selection = popSelection(k)
  insert(k, newNode)
  if len(selection) > 0:
    encapsulatingPlaceholder = newNode.placeholders[0]
    encapsulate(selection, encapsulatingPlaceholder)
    k.current = selection[-1]
    moveRight(k)