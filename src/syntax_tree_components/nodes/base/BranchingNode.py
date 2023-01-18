from typing import List, Union

from src import Placeholder, TreeNode


class BranchingNode(TreeNode):
    def __init__(self, left_to_right: List[Placeholder]) -> None:
        super().__init__()
        self.placeholders = left_to_right
        for ph in self.placeholders:
            ph.parent_node = self

    def get_move_down_suggestion(self, from_placeholder: Placeholder) -> Union[Placeholder, None]:
        return None

    def get_move_up_suggestion(self, from_placeholder: Placeholder) -> Union[Placeholder, None]:
        return None
