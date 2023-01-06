from src import KeyboardMemory
from src.Functions.Selection.helpers.setSelectionDiff import setSelectionDiff

def enterSelectionMode(k: KeyboardMemory) -> None:
  setSelectionDiff(k, 0)