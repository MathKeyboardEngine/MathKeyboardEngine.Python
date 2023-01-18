from src import KeyboardMemory


def in_selection_mode(k: KeyboardMemory) -> bool:
    return k.selection_diff is not None
