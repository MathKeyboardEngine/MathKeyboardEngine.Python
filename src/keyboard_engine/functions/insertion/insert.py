from typing import List, Union

from src import KeyboardMemory, Placeholder, TreeNode, move_right


def insert(k: KeyboardMemory, toInsert: Union[TreeNode, List[TreeNode]]):
    if isinstance(toInsert, List):
        for node in toInsert:
            insert(k, node)
            k.current = node
    else:
        if isinstance(k.current, Placeholder):
            k.current.nodes.insert(0, toInsert)
            toInsert.parent_placeholder = k.current
        else:
            parent: Placeholder = k.current.parent_placeholder
            index_of_current = parent.nodes.index(k.current)
            parent.nodes[index_of_current + 1 : index_of_current + 1] = [toInsert]
            toInsert.parent_placeholder = parent
        move_right(k)
