from typing import Union
from src import BranchingNode, KeyboardMemory, PartOfNumberWithDigits, Placeholder, TreeNode
from src.KeyboardEngine.Functions.helpers.encapsulateAllPartsOfNumberWithDigitsLeftOfIndex import encapsulateAllPartsOfNumberWithDigitsLeftOfIndex
from src.KeyboardEngine.Functions.helpers.getFirstNonEmptyOnLeftOf import getFirstNonEmptyOnLeftOf
from src.helpers.lastOrNone import lastOrNone
from src.helpers.firstBeforeOrNone import firstBeforeOrNone
from src.helpers.coalesce import coalesce

def deleteCurrent(k: KeyboardMemory) -> None:
  if isinstance(k.current, Placeholder):
    if k.current.parentNode is None or len(k.current.nodes) > 0:
      return
    else:
      nonEmptyPlaceholderOnLeft: Union[Placeholder, None] = getFirstNonEmptyOnLeftOf(k.current.parentNode.placeholders, k.current)
      if nonEmptyPlaceholderOnLeft:
        if len(k.current.parentNode.placeholders) == 2 and k.current == k.current.parentNode.placeholders[1] and len(k.current.nodes) == 0:
          deleteOuterBranchingNodeButNotItsContents(k, nonEmptyPlaceholderOnLeft)
        else:
          nonEmptyPlaceholderOnLeft.nodes.pop()
          k.current = coalesce(lastOrNone(nonEmptyPlaceholderOnLeft.nodes), nonEmptyPlaceholderOnLeft)
      elif all(len(ph.nodes) == 0 for ph in k.current.parentNode.placeholders):
        ancestorPlaceholder = k.current.parentNode.parentPlaceholder
        previousNode = firstBeforeOrNone(ancestorPlaceholder.nodes, k.current.parentNode)
        ancestorPlaceholder.nodes.remove(k.current.parentNode)
        k.current = coalesce(previousNode, ancestorPlaceholder)
      elif k.current.parentNode.placeholders[0] == k.current and len(k.current.nodes) == 0 and any(len(ph.nodes) != 0 for ph in k.current.parentNode.placeholders):
        previousNode = firstBeforeOrNone(k.current.parentNode.parentPlaceholder.nodes, k.current.parentNode)
        if previousNode is not None:
          encapsulatePreviousInto(previousNode, k.current)
          k.current = k.current.nodes[-1]
        else:
          nonEmptySiblingPlaceholders = list(filter(lambda p: len(p.nodes) != 0, k.current.parentNode.placeholders))
          if len(nonEmptySiblingPlaceholders) == 1:
            nodes = nonEmptySiblingPlaceholders[0].nodes
            ancestorPlaceholder = k.current.parentNode.parentPlaceholder
            indexOfParentNode = ancestorPlaceholder.nodes.index(k.current.parentNode)
            for node in nodes:
              node.parentPlaceholder = ancestorPlaceholder
            ancestorPlaceholder.nodes[indexOfParentNode: indexOfParentNode + 1] = nodes
            k.current = nodes[-1]
  else:
    if isinstance(k.current, BranchingNode) and len(k.current.placeholders[0].nodes) > 0 and all(len(ph.nodes) == 0 for ph in k.current.placeholders[1:]):
      deleteOuterBranchingNodeButNotItsContents(k, k.current.placeholders[0])
    elif isinstance(k.current, BranchingNode) and any(len(ph.nodes) > 0 for ph in k.current.placeholders):
      k.current = [node for ph in k.current.placeholders for node in ph.nodes][-1]
      deleteCurrent(k)
    else:
      previousNode: Union[TreeNode, None] = firstBeforeOrNone(k.current.parentPlaceholder.nodes, k.current)
      k.current.parentPlaceholder.nodes.remove(k.current)
      k.current = coalesce(previousNode, k.current.parentPlaceholder)

def encapsulatePreviousInto(previousNode: TreeNode, targetPlaceholder: Placeholder):
  targetPlaceholder.parentNode.parentPlaceholder.nodes.remove(previousNode)
  targetPlaceholder.nodes.append(previousNode)
  previousNodeOldParentPlaceholder = previousNode.parentPlaceholder
  previousNode.parentPlaceholder = targetPlaceholder
  if isinstance(previousNode, PartOfNumberWithDigits):
    encapsulateAllPartsOfNumberWithDigitsLeftOfIndex(len(previousNodeOldParentPlaceholder.nodes) - 1, previousNodeOldParentPlaceholder.nodes, targetPlaceholder)

def deleteOuterBranchingNodeButNotItsContents(k: KeyboardMemory, nonEmptyPlaceholder: Placeholder):
  outerBranchingNode = nonEmptyPlaceholder.parentNode
  indexOfOuterBranchingNode = outerBranchingNode.parentPlaceholder.nodes.index(outerBranchingNode)
  outerBranchingNode.parentPlaceholder.nodes[indexOfOuterBranchingNode: indexOfOuterBranchingNode + 1] = nonEmptyPlaceholder.nodes
  for node in nonEmptyPlaceholder.nodes:
    node.parentPlaceholder = outerBranchingNode.parentPlaceholder
  k.current = nonEmptyPlaceholder.nodes[-1]