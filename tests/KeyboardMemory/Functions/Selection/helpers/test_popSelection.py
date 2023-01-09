import pytest
from src import KeyboardMemory, enterSelectionMode
from src.KeyboardEngine.Functions.Selection.helpers.popSelection import popSelection

def test_throws_if_not_inSelectionMode():
  with pytest.raises(Exception) as ex:
    k = KeyboardMemory()
    popSelection(k)
  assert 'Enter selection mode before calling this method.' == str(ex.value)

def test_returns_an_empty_array_when_inSelectionMode_but_nothing_is_selected():
    k = KeyboardMemory()
    enterSelectionMode(k)
    assert 0 == len(popSelection(k))