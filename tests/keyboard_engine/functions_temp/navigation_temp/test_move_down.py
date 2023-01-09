from src import KeyboardMemory, insert, DigitNode, insert_with_encapsulate_current, AscendingBranchingNode, RoundBracketsNode, get_edit_mode_latex, move_down
from tests.testhelpers.UnitTestLatexConfiguration import UnitTestLatexConfiguration

def test_can_move_the_cursor_down_via_an_ancestor_if_the_current_BranchingNode_does_not_support_updown_navigation():
    # Arrange
    k = KeyboardMemory()
    insert(k, DigitNode('2'))
    insert_with_encapsulate_current(k, AscendingBranchingNode('', '^{', '}'))
    insert(k, RoundBracketsNode('(', ')'))
    assert '2^{(▦)}' == get_edit_mode_latex(k, UnitTestLatexConfiguration())
    # Act
    move_down(k)
    # Assert
    assert '2▦^{(⬚)}' == get_edit_mode_latex(k, UnitTestLatexConfiguration())