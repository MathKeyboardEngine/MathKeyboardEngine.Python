from src import DescendingBranchingNode, DigitNode, KeyboardMemory, StandardLeafNode, get_edit_mode_latex, insert, insert_with_encapsulate_current, move_down, move_left, move_right, move_up
from tests._testhelpers.UnitTestLatexConfiguration import UnitTestLatexConfiguration


def test_subscript_a_right_4():
    k = KeyboardMemory()
    insert(k, DescendingBranchingNode('', '_{', '}'))
    insert(k, StandardLeafNode('a'))
    move_right(k)
    insert(k, DigitNode('4'))
    assert 'a_{4▦}' == get_edit_mode_latex(k, UnitTestLatexConfiguration())

def test_subscript_a_down_4():
    k = KeyboardMemory()
    insert(k, DescendingBranchingNode('', '_{', '}'))
    insert(k, StandardLeafNode('a'))
    move_down(k)
    insert(k, DigitNode('4'))
    assert 'a_{4▦}' == get_edit_mode_latex(k, UnitTestLatexConfiguration())

def test_insertWithEncapsulateCurrent():
    k = KeyboardMemory()
    insert(k, StandardLeafNode('a'))
    insert_with_encapsulate_current(k, DescendingBranchingNode('', '_{', '}'))
    assert 'a_{▦}' == get_edit_mode_latex(k, UnitTestLatexConfiguration())

def test_subscript_a_down_4_up():
    k = KeyboardMemory()
    insert(k, DescendingBranchingNode('', '_{', '}'))
    insert(k, StandardLeafNode('a'))
    move_down(k)
    insert(k, DigitNode('4'))
    move_up(k)
    assert 'a▦_{4}' == get_edit_mode_latex(k, UnitTestLatexConfiguration())

def test_can_be_left_empty__moving_out_and_back_in():
    # Arrange
    k = KeyboardMemory()
    insert(k, DescendingBranchingNode('', '_{', '}'))
    assert '▦_{⬚}' == get_edit_mode_latex(k, UnitTestLatexConfiguration())
    # Act & Assert
    move_left(k)
    assert '▦⬚_{⬚}' == get_edit_mode_latex(k, UnitTestLatexConfiguration())
    move_right(k)
    assert '▦_{⬚}' == get_edit_mode_latex(k, UnitTestLatexConfiguration())

def test_impossible_updown_requests_in_empty_node_should_not_throw():
    # Arrange
    k = KeyboardMemory()
    insert(k, DescendingBranchingNode('', '_{', '}'))
    assert '▦_{⬚}' == get_edit_mode_latex(k, UnitTestLatexConfiguration())
    # Act & Assert 1
    move_up(k)
    assert '▦_{⬚}' == get_edit_mode_latex(k, UnitTestLatexConfiguration())
    # Arrange 2
    move_down(k)
    assert '⬚_{▦}' == get_edit_mode_latex(k, UnitTestLatexConfiguration())
    # Act & Assert 2
    move_down(k)
    assert '⬚_{▦}' == get_edit_mode_latex(k, UnitTestLatexConfiguration())

def test_impossible_updown_requests_in_filled_subscriptNode_should_not_throw():
    # Arrange
    k = KeyboardMemory()
    insert(k, DescendingBranchingNode('', '_{', '}'))
    insert(k, StandardLeafNode('a'))
    assert 'a▦_{⬚}' == get_edit_mode_latex(k, UnitTestLatexConfiguration())
    # Act & Assert 1
    move_up(k)
    assert 'a▦_{⬚}' == get_edit_mode_latex(k, UnitTestLatexConfiguration())
    # Arrange 2
    move_down(k)
    assert 'a_{▦}' == get_edit_mode_latex(k, UnitTestLatexConfiguration())
    insert(k, DigitNode('4'))
    assert 'a_{4▦}' == get_edit_mode_latex(k, UnitTestLatexConfiguration())
    # Act & Assert 2
    move_down(k)
    assert 'a_{4▦}' == get_edit_mode_latex(k, UnitTestLatexConfiguration())