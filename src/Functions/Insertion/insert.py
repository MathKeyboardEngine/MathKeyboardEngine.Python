from src import KeyboardMemory, Placeholder, TreeNode, moveRight

def insert(k: KeyboardMemory, newNode: TreeNode):
  if isinstance(k.current, Placeholder):
    k.current.nodes.insert(0, newNode)
    newNode.parentPlaceholder = k.current
  else:
    parent: Placeholder = k.current.parentPlaceholder
    indexOfCurrent = parent.nodes.index(k.current)
    parent.nodes[indexOfCurrent + 1: indexOfCurrent + 1] = [newNode]
    newNode.parentPlaceholder = parent
  moveRight(k)