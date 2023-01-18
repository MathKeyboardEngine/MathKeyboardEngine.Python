from src import KeyboardMemory, Placeholder, TreeNode, move_right


def insert(k: KeyboardMemory, new_node: TreeNode):
    if isinstance(k.current, Placeholder):
        k.current.nodes.insert(0, new_node)
        new_node.parent_placeholder = k.current
    else:
        parent: Placeholder = k.current.parent_placeholder
        index_of_current = parent.nodes.index(k.current)
        parent.nodes[index_of_current + 1 : index_of_current + 1] = [new_node]
        new_node.parent_placeholder = parent
    move_right(k)
