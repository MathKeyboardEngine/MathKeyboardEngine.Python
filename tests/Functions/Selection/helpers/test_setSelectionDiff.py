import pytest
from src import KeyboardMemory, insert, DigitNode, selectLeft, getEditModeLatex
from tests.testhelpers.UnitTestLatexConfiguration import UnitTestLatexConfiguration
from src.Functions.Selection.helpers.setSelectionDiff import setSelectionDiff

def test_throws_at_nonsensical_request():
    # Arrange
    k = KeyboardMemory()
    insert(k, DigitNode('1'))
    selectLeft(k)
    assert r'\colorbox{blue}{1}' == getEditModeLatex(k, UnitTestLatexConfiguration())
    # Act & assert
    with pytest.raises(Exception) as ex:
      setSelectionDiff(k, k.selectionDiff - 1) # Trying to go even more to the left.
    assert 'The TreeNode at index 0 of the current Placeholder is as far as you can go left if current is a TreeNode.' == str(ex.value)
