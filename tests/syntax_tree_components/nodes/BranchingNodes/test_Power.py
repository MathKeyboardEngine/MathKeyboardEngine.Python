from src import KeyboardMemory, insert, AscendingBranchingNode, DigitNode, insert_with_encapsulate_current, move_down, move_left, move_right, move_up, get_edit_mode_latex
from tests._testhelpers.UnitTestLatexConfiguration import UnitTestLatexConfiguration

def test_pow_3_right_4():
    k = KeyboardMemory()
    insert(k, AscendingBranchingNode('', '^{', '}'))
    insert(k, DigitNode('3'))
    move_right(k)
    insert(k, DigitNode('4'))
    assert '3^{4▦}' == get_edit_mode_latex(k, UnitTestLatexConfiguration())

def test_pow_3_up_4():
    k = KeyboardMemory()
    insert(k, AscendingBranchingNode('', '^{', '}'))
    insert(k, DigitNode('3'))
    move_up(k)
    insert(k, DigitNode('4'))
    assert '3^{4▦}' == get_edit_mode_latex(k, UnitTestLatexConfiguration())

def test_3_encapsulated_by_the_base_of_a_power():
    k = KeyboardMemory()
    insert(k, DigitNode('3'))
    insert_with_encapsulate_current(k, AscendingBranchingNode('', '^{', '}'))
    assert '3^{▦}' == get_edit_mode_latex(k, UnitTestLatexConfiguration())

def test_pow_3_up_down():
    k = KeyboardMemory()
    insert(k, AscendingBranchingNode('', '^{', '}'))
    insert(k, DigitNode('3'))
    move_up(k)
    insert(k, DigitNode('4'))
    move_down(k)
    assert '3▦^{4}' == get_edit_mode_latex(k, UnitTestLatexConfiguration())

def test_pow_can_be_lef_empty__moving_out_and_back_in():
    k = KeyboardMemory()
    insert(k, AscendingBranchingNode('', '^{', '}'))
    assert '▦^{⬚}' == get_edit_mode_latex(k, UnitTestLatexConfiguration())
    move_left(k)
    assert '▦⬚^{⬚}' == get_edit_mode_latex(k, UnitTestLatexConfiguration())
    move_right(k)
    assert '▦^{⬚}' == get_edit_mode_latex(k, UnitTestLatexConfiguration())

def test_impossible_updown_requests_in_empty_power_should_not_throw():
    # Arrange
    k = KeyboardMemory()
    insert(k, AscendingBranchingNode('', '^{', '}'))
    assert '▦^{⬚}' == get_edit_mode_latex(k, UnitTestLatexConfiguration())
    # Act & Assert
    move_down(k)
    assert '▦^{⬚}' == get_edit_mode_latex(k, UnitTestLatexConfiguration())
    move_up(k)
    assert '⬚^{▦}' == get_edit_mode_latex(k, UnitTestLatexConfiguration())
    move_up(k)
    assert '⬚^{▦}' == get_edit_mode_latex(k, UnitTestLatexConfiguration())

def test_impossible_updown_requests_in_filled_power_should_not_throw():
    k = KeyboardMemory()
    insert(k, AscendingBranchingNode('', '^{', '}'))
    insert(k, DigitNode('3'))
    assert '3▦^{⬚}' == get_edit_mode_latex(k, UnitTestLatexConfiguration())
    move_down(k)
    assert '3▦^{⬚}' == get_edit_mode_latex(k, UnitTestLatexConfiguration())
    move_up(k)
    assert '3^{▦}' == get_edit_mode_latex(k, UnitTestLatexConfiguration())
    insert(k, DigitNode('4'))
    assert '3^{4▦}' == get_edit_mode_latex(k, UnitTestLatexConfiguration())
    move_up(k)
    assert '3^{4▦}' == get_edit_mode_latex(k, UnitTestLatexConfiguration())