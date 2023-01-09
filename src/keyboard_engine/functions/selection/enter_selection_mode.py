from src import KeyboardMemory
from src.keyboard_engine.functions.selection._helpers.set_selection_diff import set_selection_diff

def enter_selection_mode(k: KeyboardMemory) -> None:
  set_selection_diff(k, 0)