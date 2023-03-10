import pytest

from src import DigitNode, KeyboardMemory, get_edit_mode_latex, insert, select_left
from src.keyboard_engine.functions.selection._helpers.set_selection_diff import set_selection_diff
from tests._testhelpers.UnitTestLatexConfiguration import UnitTestLatexConfiguration


def test_throws_at_nonsensical_request():
    # Arrange
    k = KeyboardMemory()
    insert(k, DigitNode('1'))
    select_left(k)
    assert r'\colorbox{blue}{1}' == get_edit_mode_latex(k, UnitTestLatexConfiguration())
    # Act & assert
    with pytest.raises(Exception) as ex:
        set_selection_diff(k, k.selection_diff - 1)   # Trying to go even more to the left.
    assert 'The TreeNode at index 0 of the current Placeholder is as far as you can go left if current is a TreeNode.' == str(ex.value)
