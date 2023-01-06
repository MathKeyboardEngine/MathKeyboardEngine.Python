from src import KeyboardMemory, DescendingBranchingNode, StandardLeafNode, DigitNode, insert, moveRight, moveDown, moveUp, moveLeft, insertWithEncapsulateCurrent, getEditModeLatex
from tests.testhelpers.UnitTestLatexConfiguration import UnitTestLatexConfiguration

def test_subscript_a_right_4():
    k = KeyboardMemory()
    insert(k, DescendingBranchingNode('', '_{', '}'))
    insert(k, StandardLeafNode('a'))
    moveRight(k)
    insert(k, DigitNode('4'))
    assert 'a_{4▦}' == getEditModeLatex(k, UnitTestLatexConfiguration())

def test_subscript_a_down_4():
    k = KeyboardMemory()
    insert(k, DescendingBranchingNode('', '_{', '}'))
    insert(k, StandardLeafNode('a'))
    moveDown(k)
    insert(k, DigitNode('4'))
    assert 'a_{4▦}' == getEditModeLatex(k, UnitTestLatexConfiguration())

def test_insertWithEncapsulateCurrent():
    k = KeyboardMemory()
    insert(k, StandardLeafNode('a'))
    insertWithEncapsulateCurrent(k, DescendingBranchingNode('', '_{', '}'))
    assert 'a_{▦}' == getEditModeLatex(k, UnitTestLatexConfiguration())

def test_subscript_a_down_4_up():
    k = KeyboardMemory()
    insert(k, DescendingBranchingNode('', '_{', '}'))
    insert(k, StandardLeafNode('a'))
    moveDown(k)
    insert(k, DigitNode('4'))
    moveUp(k)
    assert 'a▦_{4}' == getEditModeLatex(k, UnitTestLatexConfiguration())

def test_can_be_left_empty__moving_out_and_back_in():
    # Arrange
    k = KeyboardMemory()
    insert(k, DescendingBranchingNode('', '_{', '}'))
    assert '▦_{⬚}' == getEditModeLatex(k, UnitTestLatexConfiguration())
    # Act & Assert
    moveLeft(k)
    assert '▦⬚_{⬚}' == getEditModeLatex(k, UnitTestLatexConfiguration())
    moveRight(k)
    assert '▦_{⬚}' == getEditModeLatex(k, UnitTestLatexConfiguration())

def test_impossible_updown_requests_in_empty_node_should_not_throw():
    # Arrange
    k = KeyboardMemory()
    insert(k, DescendingBranchingNode('', '_{', '}'))
    assert '▦_{⬚}' == getEditModeLatex(k, UnitTestLatexConfiguration())
    # Act & Assert 1
    moveUp(k)
    assert '▦_{⬚}' == getEditModeLatex(k, UnitTestLatexConfiguration())
    # Arrange 2
    moveDown(k)
    assert '⬚_{▦}' == getEditModeLatex(k, UnitTestLatexConfiguration())
    # Act & Assert 2
    moveDown(k)
    assert '⬚_{▦}' == getEditModeLatex(k, UnitTestLatexConfiguration())

def test_impossible_updown_requests_in_filled_subscriptNode_should_not_throw():
    # Arrange
    k = KeyboardMemory()
    insert(k, DescendingBranchingNode('', '_{', '}'))
    insert(k, StandardLeafNode('a'))
    assert 'a▦_{⬚}' == getEditModeLatex(k, UnitTestLatexConfiguration())
    # Act & Assert 1
    moveUp(k)
    assert 'a▦_{⬚}' == getEditModeLatex(k, UnitTestLatexConfiguration())
    # Arrange 2
    moveDown(k)
    assert 'a_{▦}' == getEditModeLatex(k, UnitTestLatexConfiguration())
    insert(k, DigitNode('4'))
    assert 'a_{4▦}' == getEditModeLatex(k, UnitTestLatexConfiguration())
    # Act & Assert 2
    moveDown(k)
    assert 'a_{4▦}' == getEditModeLatex(k, UnitTestLatexConfiguration())