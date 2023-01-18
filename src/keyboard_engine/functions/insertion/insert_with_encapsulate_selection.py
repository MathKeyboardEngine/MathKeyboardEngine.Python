from src import BranchingNode, KeyboardMemory, insert, move_right
from src.keyboard_engine.functions._helpers.encapsulate import encapsulate
from src.keyboard_engine.functions.selection._helpers.pop_selection import pop_selection


def insert_with_encapsulate_selection(k: KeyboardMemory, new_node: BranchingNode) -> None:
    selection = pop_selection(k)
    insert(k, new_node)
    if len(selection) > 0:
        encapsulating_placeholder = new_node.placeholders[0]
        encapsulate(selection, encapsulating_placeholder)
        k.current = selection[-1]
        move_right(k)
