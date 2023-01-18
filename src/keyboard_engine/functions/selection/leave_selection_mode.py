from src import KeyboardMemory


def leave_selection_mode(k: KeyboardMemory) -> None:
  k.selection_diff = None
  k.inclusive_selection_right_border = None
  k.inclusive_selection_left_border = None