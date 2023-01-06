from src import KeyboardMemory, insert, RoundBracketsNode, getEditModeLatex
from tests.testhelpers.UnitTestLatexConfiguration import UnitTestLatexConfiguration

def test_Default_round_brackets():
    k = KeyboardMemory()
    insert(k, RoundBracketsNode())
    assert r'\left(▦\right)' == getEditModeLatex(k, UnitTestLatexConfiguration())

def test_can_be_overridden():
    k = KeyboardMemory()
    insert(k, RoundBracketsNode('(', ')'))
    assert '(▦)' == getEditModeLatex(k, UnitTestLatexConfiguration())