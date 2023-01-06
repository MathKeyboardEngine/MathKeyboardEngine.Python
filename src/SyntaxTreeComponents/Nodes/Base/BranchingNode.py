from typing import List, Union
from src import Placeholder, TreeNode

class BranchingNode(TreeNode):
  def __init__(self, leftToRight : List[Placeholder]) -> None:
    super().__init__()
    self.placeholders = leftToRight
    for ph in self.placeholders:
      ph.parentNode = self

  def getMoveDownSuggestion(self, fromPlaceholder: Placeholder) -> Union[Placeholder, None]:
    return None
  
  def getMoveUpSuggestion(self, fromPlaceholder: Placeholder) -> Union[Placeholder, None]:
    return None