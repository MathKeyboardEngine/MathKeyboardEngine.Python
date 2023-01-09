from src import KeyboardMemory, BranchingNode, insert, moveRight, PartOfNumberWithDigits, RoundBracketsNode, TreeNode
from src.KeyboardEngine.Functions.helpers.encapsulate import encapsulate
from src.KeyboardEngine.Functions.helpers.encapsulateAllPartsOfNumberWithDigitsLeftOfIndex import encapsulateAllPartsOfNumberWithDigitsLeftOfIndex
from src.helpers.coalesce import coalesce
from src.helpers.firstAfterOrNone import firstAfterOrNone

def insertWithEncapsulateCurrent(k: KeyboardMemory, newNode: BranchingNode, deleteOuterRoundBracketsIfAny : bool = False) -> None:
  encapsulatingPlaceholder = newNode.placeholders[0]
  if isinstance(k.current, TreeNode):
    siblingNodes = k.current.parentPlaceholder.nodes
    currentIndex = siblingNodes.index(k.current)
    siblingNodes[currentIndex] = newNode
    newNode.parentPlaceholder = k.current.parentPlaceholder
    if isinstance(k.current, RoundBracketsNode) and deleteOuterRoundBracketsIfAny:
      encapsulate(k.current.placeholders[0].nodes, encapsulatingPlaceholder)
      k.current = coalesce(firstAfterOrNone(newNode.placeholders, encapsulatingPlaceholder), newNode)
    elif isinstance(k.current, PartOfNumberWithDigits):
      encapsulatingPlaceholder.nodes.append(k.current)
      k.current.parentPlaceholder = encapsulatingPlaceholder
      encapsulateAllPartsOfNumberWithDigitsLeftOfIndex(currentIndex, siblingNodes, encapsulatingPlaceholder)
      moveRight(k)
    else:
      encapsulatingPlaceholder.nodes.append(k.current)
      k.current.parentPlaceholder = encapsulatingPlaceholder
      moveRight(k)
  else:
    insert(k, newNode)