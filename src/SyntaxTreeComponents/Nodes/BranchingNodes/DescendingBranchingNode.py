from typing import Union
from src import Placeholder, StandardBranchingNode

class DescendingBranchingNode(StandardBranchingNode):
  def getMoveDownSuggestion(self, fromPlaceholder: Placeholder) -> Union[Placeholder, None]:
    currentPlaceholderIndex = self.placeholders.index(fromPlaceholder)
    if currentPlaceholderIndex < len(self.placeholders) - 1:
      return self.placeholders[currentPlaceholderIndex + 1]
    else:
      return None

  def getMoveUpSuggestion(self, fromPlaceholder: Placeholder) -> Union[Placeholder, None]:
    currentPlaceholderIndex = self.placeholders.index(fromPlaceholder)
    if currentPlaceholderIndex > 0:
      return self.placeholders[currentPlaceholderIndex - 1]
    else:
      return None