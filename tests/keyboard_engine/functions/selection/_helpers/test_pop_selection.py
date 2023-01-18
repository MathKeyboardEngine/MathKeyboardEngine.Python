import pytest

from src import KeyboardMemory, enter_selection_mode
from src.keyboard_engine.functions.selection._helpers.pop_selection import pop_selection


def test_throws_if_not_inSelectionMode():
  with pytest.raises(Exception) as ex:
    k = KeyboardMemory()
    pop_selection(k)
  assert 'Enter selection mode before calling this method.' == str(ex.value)

def test_returns_an_empty_array_when_inSelectionMode_but_nothing_is_selected():
    k = KeyboardMemory()
    enter_selection_mode(k)
    assert 0 == len(pop_selection(k))