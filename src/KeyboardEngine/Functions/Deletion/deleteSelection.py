from src import KeyboardMemory
from src.KeyboardEngine.Functions.Selection.helpers.popSelection import popSelection

def deleteSelection(k: KeyboardMemory) -> None:
  popSelection(k)