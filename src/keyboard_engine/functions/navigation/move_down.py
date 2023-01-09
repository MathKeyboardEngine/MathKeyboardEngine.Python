from src import BranchingNode, KeyboardMemory, Placeholder
from src._helpers.coalesce import coalesce
from src._helpers.last_or_none import last_or_none

def move_down(k: KeyboardMemory) -> None:
  from_placeholder = k.current if isinstance(k.current, Placeholder) else k.current.parent_placeholder
  suggesting_node: BranchingNode
  while True:
    if from_placeholder.parent_node is None:
      return
    suggesting_node = from_placeholder.parent_node
    suggestion = suggesting_node.get_move_down_suggestion(from_placeholder)
    if suggestion is not None:
      k.current = coalesce(last_or_none(suggestion.nodes), suggestion)
      return
    from_placeholder = suggesting_node.parent_placeholder