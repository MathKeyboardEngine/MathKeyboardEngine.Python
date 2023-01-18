from typing import Union

from src import Placeholder, TreeNode


class KeyboardMemory:
    def __init__(self) -> None:
        self.syntax_tree_root: Placeholder = Placeholder()
        self.current: Union[TreeNode, Placeholder] = self.syntax_tree_root
        self.selection_diff: Union[int, None] = None
        self.inclusive_selection_right_border: Union[TreeNode, None] = None
        self.inclusive_selection_left_border: Union[TreeNode, Placeholder, None] = None
