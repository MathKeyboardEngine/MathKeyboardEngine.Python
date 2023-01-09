from src import KeyboardMemory, DescendingBranchingNode, DigitNode, insert, get_edit_mode_latex,move_right, move_up, move_down
from tests._testhelpers.UnitTestLatexConfiguration import UnitTestLatexConfiguration

def test_basic_test():
    k = KeyboardMemory()
    insert(k, DescendingBranchingNode(r'\sqrt[', ']{', '}'))
    assert r'\sqrt[▦]{⬚}' == get_edit_mode_latex(k, UnitTestLatexConfiguration())
    insert(k, DigitNode('3'))
    move_right(k)
    assert r'\sqrt[3]{▦}' == get_edit_mode_latex(k, UnitTestLatexConfiguration())
    insert(k, DigitNode('2'))
    insert(k, DigitNode('7'))
    assert r'\sqrt[3]{27▦}' == get_edit_mode_latex(k, UnitTestLatexConfiguration())

def test_updown_including_impossible_updown_requests():
    k = KeyboardMemory()
    insert(k, DescendingBranchingNode(r'\sqrt[', ']{', '}'))
    move_down(k)
    assert r'\sqrt[⬚]{▦}' == get_edit_mode_latex(k, UnitTestLatexConfiguration())
    move_down(k)
    assert r'\sqrt[⬚]{▦}' == get_edit_mode_latex(k, UnitTestLatexConfiguration())

    move_up(k)
    assert r'\sqrt[▦]{⬚}' == get_edit_mode_latex(k, UnitTestLatexConfiguration())
    move_up(k)
    assert r'\sqrt[▦]{⬚}' == get_edit_mode_latex(k, UnitTestLatexConfiguration())