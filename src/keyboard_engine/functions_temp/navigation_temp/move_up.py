from src import KeyboardMemory, BranchingNode, Placeholder
from src.helpers.coalesce import coalesce
from src.helpers.last_or_none import last_or_none

def move_up(k: KeyboardMemory) -> None:
  from_placeholder = k.current if isinstance(k.current, Placeholder) else k.current.parent_placeholder
  suggesting_node: BranchingNode
  while True:
    if from_placeholder.parent_node is None:
      return
    suggesting_node = from_placeholder.parent_node
    suggestion = suggesting_node.get_move_up_suggestion(from_placeholder)
    if suggestion is not None:
      k.current = coalesce(last_or_none(suggestion.nodes), suggestion)
      return
    from_placeholder = suggesting_node.parent_placeholder