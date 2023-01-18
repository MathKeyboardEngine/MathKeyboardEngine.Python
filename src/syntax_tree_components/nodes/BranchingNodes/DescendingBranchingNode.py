from typing import Union

from src import Placeholder, StandardBranchingNode


class DescendingBranchingNode(StandardBranchingNode):
  def get_move_down_suggestion(self, from_placeholder: Placeholder) -> Union[Placeholder, None]:
    current_placeholder_index = self.placeholders.index(from_placeholder)
    if current_placeholder_index < len(self.placeholders) - 1:
      return self.placeholders[current_placeholder_index + 1]
    else:
      return None

  def get_move_up_suggestion(self, from_placeholder: Placeholder) -> Union[Placeholder, None]:
    current_placeholder_index = self.placeholders.index(from_placeholder)
    if current_placeholder_index > 0:
      return self.placeholders[current_placeholder_index - 1]
    else:
      return None