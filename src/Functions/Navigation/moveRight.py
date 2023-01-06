from typing import Union
from src import BranchingNode, KeyboardMemory, Placeholder, TreeNode
from src.helpers.coalesce import coalesce
from src.helpers.firstAfterOrNone import firstAfterOrNone

def moveRight(k: KeyboardMemory) -> None:
  if isinstance(k.current, Placeholder):
    if len(k.current.nodes) > 0:
      nextNode = k.current.nodes[0]
      k.current = nextNode.placeholders[0] if isinstance(nextNode, BranchingNode) else nextNode
    elif k.current.parentNode is None:
      return
    else:
      k.current = coalesce(firstAfterOrNone(k.current.parentNode.placeholders, k.current), k.current.parentNode)
  else:
    nextNode: Union[TreeNode, None] = firstAfterOrNone(k.current.parentPlaceholder.nodes, k.current)
    if nextNode is not None:
      k.current = nextNode.placeholders[0] if isinstance(nextNode, BranchingNode) else nextNode
    else:
      ancestorNode = k.current.parentPlaceholder.parentNode
      if ancestorNode is not None:
        nextPlaceholder: Union[Placeholder, None] = firstAfterOrNone(ancestorNode.placeholders, k.current.parentPlaceholder)
        k.current = coalesce(nextPlaceholder, ancestorNode)