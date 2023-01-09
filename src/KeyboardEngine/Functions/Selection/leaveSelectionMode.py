from src import KeyboardMemory

def leaveSelectionMode(k: KeyboardMemory) -> None:
  k.selectionDiff = None
  k.inclusiveSelectionRightBorder = None
  k.inclusiveSelectionLeftBorder = None