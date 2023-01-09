from src import KeyboardMemory
from src.keyboard_engine.functions_temp.selection_temp.helpers.pop_selection import pop_selection

def delete_selection(k: KeyboardMemory) -> None:
  pop_selection(k)