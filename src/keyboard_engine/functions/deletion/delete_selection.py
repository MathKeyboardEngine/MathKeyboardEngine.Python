from src import KeyboardMemory
from src.keyboard_engine.functions.selection._helpers.pop_selection import pop_selection


def delete_selection(k: KeyboardMemory) -> None:
    pop_selection(k)
