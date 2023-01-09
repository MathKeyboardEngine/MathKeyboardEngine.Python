from src import delete_current, KeyboardMemory, move_left, move_up, DescendingBranchingNode, get_edit_mode_latex, insert, insert_with_encapsulate_current, DigitNode, move_right, move_down
from tests.testhelpers.UnitTestLatexConfiguration import UnitTestLatexConfiguration

def test_frac_left_right_right_right():
    k = KeyboardMemory()
    insert(k, DescendingBranchingNode(r'\frac{', '}{', '}'))
    move_left(k)
    assert r'▦\frac{⬚}{⬚}' == get_edit_mode_latex(k, UnitTestLatexConfiguration())
    move_right(k)
    assert r'\frac{▦}{⬚}' == get_edit_mode_latex(k, UnitTestLatexConfiguration())
    move_right(k)
    assert r'\frac{⬚}{▦}' == get_edit_mode_latex(k, UnitTestLatexConfiguration())
    move_right(k)
    assert r'\frac{⬚}{⬚}▦' == get_edit_mode_latex(k, UnitTestLatexConfiguration())

def test_frac_3_right_4():
    k = KeyboardMemory()
    insert(k, DescendingBranchingNode(r'\frac{', '}{', '}'))
    insert(k, DigitNode('3'))
    move_right(k)
    insert(k, DigitNode('4'))
    assert r'\frac{3}{4▦}' == get_edit_mode_latex(k, UnitTestLatexConfiguration())

def test_frac_3_down_4():
    k = KeyboardMemory()
    insert(k, DescendingBranchingNode(r'\frac{', '}{', '}'))
    insert(k, DigitNode('3'))
    move_down(k)
    insert(k, DigitNode('4'))
    assert r'\frac{3}{4▦}' == get_edit_mode_latex(k, UnitTestLatexConfiguration())

def test_3_encapsulated_the_numerator_of_a_fraction():
    k = KeyboardMemory()
    insert(k, DigitNode('3'))
    insert_with_encapsulate_current(k, DescendingBranchingNode(r'\frac{', '}{', '}'))
    assert r'\frac{3}{▦}' == get_edit_mode_latex(k, UnitTestLatexConfiguration())

def test_delete_empty_frac_from_numerator():
    k = KeyboardMemory()
    insert(k, DescendingBranchingNode(r'\frac{', '}{', '}'))
    assert r'\frac{▦}{⬚}' == get_edit_mode_latex(k, UnitTestLatexConfiguration())
    delete_current(k)
    assert '▦' == get_edit_mode_latex(k, UnitTestLatexConfiguration())

def test_delete_empty_frac_from_denominator():
    k = KeyboardMemory()
    insert(k, DescendingBranchingNode(r'\frac{', '}{', '}'))
    move_down(k)
    assert r'\frac{⬚}{▦}' == get_edit_mode_latex(k, UnitTestLatexConfiguration())
    delete_current(k)
    assert '▦' == get_edit_mode_latex(k, UnitTestLatexConfiguration())

def test_delete_empty_frac_from_the_right():
    k = KeyboardMemory()
    insert(k, DescendingBranchingNode(r'\frac{', '}{', '}'))
    move_down(k)
    move_right(k)
    assert r'\frac{⬚}{⬚}▦' == get_edit_mode_latex(k, UnitTestLatexConfiguration())
    delete_current(k)
    assert '▦' == get_edit_mode_latex(k, UnitTestLatexConfiguration())

def test_deleting_frac_from_denominator_releases_non_empty_numerator():
    k = KeyboardMemory()
    insert(k, DescendingBranchingNode(r'\frac{', '}{', '}'))
    insert(k, DigitNode('1'))
    insert(k, DigitNode('2'))
    move_down(k)
    insert(k, DigitNode('3'))
    move_right(k)
    assert r'\frac{12}{3}▦' == get_edit_mode_latex(k, UnitTestLatexConfiguration())

    delete_current(k)
    assert r'\frac{12}{▦}' == get_edit_mode_latex(k, UnitTestLatexConfiguration())
    delete_current(k)
    assert '12▦' == get_edit_mode_latex(k, UnitTestLatexConfiguration())

def test_moveUp_in_filled_fraction():
    k = KeyboardMemory()
    insert(k, DescendingBranchingNode(r'\frac{', '}{', '}'))
    insert(k, DigitNode('1'))
    insert(k, DigitNode('2'))
    move_down(k)
    insert(k, DigitNode('3'))
    assert r'\frac{12}{3▦}' == get_edit_mode_latex(k, UnitTestLatexConfiguration())

    move_up(k)
    assert r'\frac{12▦}{3}' == get_edit_mode_latex(k, UnitTestLatexConfiguration())

def test_impossible_updown_requests_in_filled_fraction_should_not_throw():
    k = KeyboardMemory()
    insert(k, DescendingBranchingNode(r'\frac{', '}{', '}'))
    insert(k, DigitNode('1'))
    assert r'\frac{1▦}{⬚}' == get_edit_mode_latex(k, UnitTestLatexConfiguration())
    move_up(k)
    assert r'\frac{1▦}{⬚}' == get_edit_mode_latex(k, UnitTestLatexConfiguration())

    move_down(k)
    insert(k, DigitNode('2'))
    assert r'\frac{1}{2▦}' == get_edit_mode_latex(k, UnitTestLatexConfiguration())
    move_down(k)
    assert r'\frac{1}{2▦}' == get_edit_mode_latex(k, UnitTestLatexConfiguration())

def test_impossible_updown_requests_in_empty_fraction_should_not_throw():
    k = KeyboardMemory()
    insert(k, DescendingBranchingNode(r'\frac{', '}{', '}'))
    move_down(k)
    assert r'\frac{⬚}{▦}' == get_edit_mode_latex(k, UnitTestLatexConfiguration())
    move_down(k)
    assert r'\frac{⬚}{▦}' == get_edit_mode_latex(k, UnitTestLatexConfiguration())
    move_up(k)
    assert r'\frac{▦}{⬚}' == get_edit_mode_latex(k, UnitTestLatexConfiguration())
    move_up(k)
    assert r'\frac{▦}{⬚}' == get_edit_mode_latex(k, UnitTestLatexConfiguration())