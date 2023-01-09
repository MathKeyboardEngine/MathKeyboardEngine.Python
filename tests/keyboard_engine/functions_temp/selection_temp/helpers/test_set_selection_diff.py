import pytest
from src import KeyboardMemory, insert, DigitNode, select_left, get_edit_mode_latex
from tests.testhelpers.UnitTestLatexConfiguration import UnitTestLatexConfiguration
from src.keyboard_engine.functions_temp.selection_temp.helpers.set_selection_diff import set_selection_diff

def test_throws_at_nonsensical_request():
    # Arrange
    k = KeyboardMemory()
    insert(k, DigitNode('1'))
    select_left(k)
    assert r'\colorbox{blue}{1}' == get_edit_mode_latex(k, UnitTestLatexConfiguration())
    # Act & assert
    with pytest.raises(Exception) as ex:
      set_selection_diff(k, k.selection_diff - 1) # Trying to go even more to the left.
    assert 'The TreeNode at index 0 of the current Placeholder is as far as you can go left if current is a TreeNode.' == str(ex.value)
