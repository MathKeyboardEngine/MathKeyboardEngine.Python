from src import KeyboardMemory, DigitNode, insert, StandardBranchingNode, get_edit_mode_latex, move_right, move_left, delete_current
from tests.testhelpers.UnitTestLatexConfiguration import UnitTestLatexConfiguration

def test_sqrt_3_right_left_left_left_right():
    k = KeyboardMemory()
    insert(k, StandardBranchingNode(r'\sqrt{', '}'))
    assert r'\sqrt{▦}' == get_edit_mode_latex(k, UnitTestLatexConfiguration())
    insert(k, DigitNode('3'))
    move_right(k)
    assert r'\sqrt{3}▦' == get_edit_mode_latex(k, UnitTestLatexConfiguration())
    move_left(k)
    assert r'\sqrt{3▦}' == get_edit_mode_latex(k, UnitTestLatexConfiguration())
    move_left(k)
    assert r'\sqrt{▦3}' == get_edit_mode_latex(k, UnitTestLatexConfiguration())
    move_left(k)
    assert r'▦\sqrt{3}' == get_edit_mode_latex(k, UnitTestLatexConfiguration())
    move_right(k)
    assert r'\sqrt{▦3}' == get_edit_mode_latex(k, UnitTestLatexConfiguration())

def test_sqrt_right_left_left_right():
    k = KeyboardMemory()
    insert(k, StandardBranchingNode(r'\sqrt{', '}'))
    assert r'\sqrt{▦}' == get_edit_mode_latex(k, UnitTestLatexConfiguration())
    move_right(k)
    assert r'\sqrt{⬚}▦' == get_edit_mode_latex(k, UnitTestLatexConfiguration())
    move_left(k)
    assert r'\sqrt{▦}' == get_edit_mode_latex(k, UnitTestLatexConfiguration())
    move_left(k)
    assert r'▦\sqrt{⬚}' == get_edit_mode_latex(k, UnitTestLatexConfiguration())
    move_right(k)
    assert r'\sqrt{▦}' == get_edit_mode_latex(k, UnitTestLatexConfiguration())

def test_sqrt_del():
    k = KeyboardMemory()
    insert(k, StandardBranchingNode(r'\sqrt{', '}'))
    assert r'\sqrt{▦}' == get_edit_mode_latex(k, UnitTestLatexConfiguration())
    delete_current(k)
    assert '▦' == get_edit_mode_latex(k, UnitTestLatexConfiguration())