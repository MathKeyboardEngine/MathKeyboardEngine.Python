from src import KeyboardMemory

def inSelectionMode(k: KeyboardMemory) -> bool:
  return k.selectionDiff is not None