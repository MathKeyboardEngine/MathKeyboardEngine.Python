from src import KeyboardMemory
from src.KeyboardEngine.Functions.Selection.helpers.setSelectionDiff import setSelectionDiff

def enterSelectionMode(k: KeyboardMemory) -> None:
  setSelectionDiff(k, 0)