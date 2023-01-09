from src import KeyboardMemory, insert, DigitNode, insertWithEncapsulateCurrent, AscendingBranchingNode, RoundBracketsNode, getEditModeLatex, moveDown
from tests.testhelpers.UnitTestLatexConfiguration import UnitTestLatexConfiguration

def test_can_move_the_cursor_down_via_an_ancestor_if_the_current_BranchingNode_does_not_support_updown_navigation():
    # Arrange
    k = KeyboardMemory()
    insert(k, DigitNode('2'))
    insertWithEncapsulateCurrent(k, AscendingBranchingNode('', '^{', '}'))
    insert(k, RoundBracketsNode('(', ')'))
    assert '2^{(▦)}' == getEditModeLatex(k, UnitTestLatexConfiguration())
    # Act
    moveDown(k)
    # Assert
    assert '2▦^{(⬚)}' == getEditModeLatex(k, UnitTestLatexConfiguration())