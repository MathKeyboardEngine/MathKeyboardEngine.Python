from src import KeyboardMemory, insert, AscendingBranchingNode, DigitNode, insertWithEncapsulateCurrent, moveDown, moveLeft, moveRight, moveUp, getEditModeLatex
from tests.testhelpers.UnitTestLatexConfiguration import UnitTestLatexConfiguration

def test_pow_3_right_4():
    k = KeyboardMemory()
    insert(k, AscendingBranchingNode('', '^{', '}'))
    insert(k, DigitNode('3'))
    moveRight(k)
    insert(k, DigitNode('4'))
    assert '3^{4▦}' == getEditModeLatex(k, UnitTestLatexConfiguration())

def test_pow_3_up_4():
    k = KeyboardMemory()
    insert(k, AscendingBranchingNode('', '^{', '}'))
    insert(k, DigitNode('3'))
    moveUp(k)
    insert(k, DigitNode('4'))
    assert '3^{4▦}' == getEditModeLatex(k, UnitTestLatexConfiguration())

def test_3_encapsulated_by_the_base_of_a_power():
    k = KeyboardMemory()
    insert(k, DigitNode('3'))
    insertWithEncapsulateCurrent(k, AscendingBranchingNode('', '^{', '}'))
    assert '3^{▦}' == getEditModeLatex(k, UnitTestLatexConfiguration())

def test_pow_3_up_down():
    k = KeyboardMemory()
    insert(k, AscendingBranchingNode('', '^{', '}'))
    insert(k, DigitNode('3'))
    moveUp(k)
    insert(k, DigitNode('4'))
    moveDown(k)
    assert '3▦^{4}' == getEditModeLatex(k, UnitTestLatexConfiguration())

def test_pow_can_be_lef_empty__moving_out_and_back_in():
    k = KeyboardMemory()
    insert(k, AscendingBranchingNode('', '^{', '}'))
    assert '▦^{⬚}' == getEditModeLatex(k, UnitTestLatexConfiguration())
    moveLeft(k)
    assert '▦⬚^{⬚}' == getEditModeLatex(k, UnitTestLatexConfiguration())
    moveRight(k)
    assert '▦^{⬚}' == getEditModeLatex(k, UnitTestLatexConfiguration())

def test_impossible_updown_requests_in_empty_power_should_not_throw():
    # Arrange
    k = KeyboardMemory()
    insert(k, AscendingBranchingNode('', '^{', '}'))
    assert '▦^{⬚}' == getEditModeLatex(k, UnitTestLatexConfiguration())
    # Act & Assert
    moveDown(k)
    assert '▦^{⬚}' == getEditModeLatex(k, UnitTestLatexConfiguration())
    moveUp(k)
    assert '⬚^{▦}' == getEditModeLatex(k, UnitTestLatexConfiguration())
    moveUp(k)
    assert '⬚^{▦}' == getEditModeLatex(k, UnitTestLatexConfiguration())

def test_impossible_updown_requests_in_filled_power_should_not_throw():
    k = KeyboardMemory()
    insert(k, AscendingBranchingNode('', '^{', '}'))
    insert(k, DigitNode('3'))
    assert '3▦^{⬚}' == getEditModeLatex(k, UnitTestLatexConfiguration())
    moveDown(k)
    assert '3▦^{⬚}' == getEditModeLatex(k, UnitTestLatexConfiguration())
    moveUp(k)
    assert '3^{▦}' == getEditModeLatex(k, UnitTestLatexConfiguration())
    insert(k, DigitNode('4'))
    assert '3^{4▦}' == getEditModeLatex(k, UnitTestLatexConfiguration())
    moveUp(k)
    assert '3^{4▦}' == getEditModeLatex(k, UnitTestLatexConfiguration())