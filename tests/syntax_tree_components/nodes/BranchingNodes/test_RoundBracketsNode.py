from src import KeyboardMemory, insert, RoundBracketsNode, get_edit_mode_latex
from tests._testhelpers.UnitTestLatexConfiguration import UnitTestLatexConfiguration

def test_Default_round_brackets():
    k = KeyboardMemory()
    insert(k, RoundBracketsNode())
    assert r'\left(▦\right)' == get_edit_mode_latex(k, UnitTestLatexConfiguration())

def test_can_be_overridden():
    k = KeyboardMemory()
    insert(k, RoundBracketsNode('(', ')'))
    assert '(▦)' == get_edit_mode_latex(k, UnitTestLatexConfiguration())