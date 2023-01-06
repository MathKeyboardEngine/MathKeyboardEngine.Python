from src import KeyboardMemory, BranchingNode, Placeholder
from src.helpers.coalesce import coalesce
from src.helpers.lastOrNone import lastOrNone

def moveUp(k: KeyboardMemory) -> None:
  fromPlaceholder = k.current if isinstance(k.current, Placeholder) else k.current.parentPlaceholder
  suggestingNode: BranchingNode
  while True:
    if fromPlaceholder.parentNode is None:
      return
    suggestingNode = fromPlaceholder.parentNode
    suggestion = suggestingNode.getMoveUpSuggestion(fromPlaceholder)
    if suggestion is not None:
      k.current = coalesce(lastOrNone(suggestion.nodes), suggestion)
      return
    fromPlaceholder = suggestingNode.parentPlaceholder