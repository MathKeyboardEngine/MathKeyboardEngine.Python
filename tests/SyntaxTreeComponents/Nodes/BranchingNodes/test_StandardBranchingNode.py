from src import KeyboardMemory, DigitNode, insert, StandardBranchingNode, getEditModeLatex, moveRight, moveLeft, deleteCurrent
from tests.testhelpers.UnitTestLatexConfiguration import UnitTestLatexConfiguration

def test_sqrt_3_right_left_left_left_right():
    k = KeyboardMemory()
    insert(k, StandardBranchingNode(r'\sqrt{', '}'))
    assert r'\sqrt{▦}' == getEditModeLatex(k, UnitTestLatexConfiguration())
    insert(k, DigitNode('3'))
    moveRight(k)
    assert r'\sqrt{3}▦' == getEditModeLatex(k, UnitTestLatexConfiguration())
    moveLeft(k)
    assert r'\sqrt{3▦}' == getEditModeLatex(k, UnitTestLatexConfiguration())
    moveLeft(k)
    assert r'\sqrt{▦3}' == getEditModeLatex(k, UnitTestLatexConfiguration())
    moveLeft(k)
    assert r'▦\sqrt{3}' == getEditModeLatex(k, UnitTestLatexConfiguration())
    moveRight(k)
    assert r'\sqrt{▦3}' == getEditModeLatex(k, UnitTestLatexConfiguration())

def test_sqrt_right_left_left_right():
    k = KeyboardMemory()
    insert(k, StandardBranchingNode(r'\sqrt{', '}'))
    assert r'\sqrt{▦}' == getEditModeLatex(k, UnitTestLatexConfiguration())
    moveRight(k)
    assert r'\sqrt{⬚}▦' == getEditModeLatex(k, UnitTestLatexConfiguration())
    moveLeft(k)
    assert r'\sqrt{▦}' == getEditModeLatex(k, UnitTestLatexConfiguration())
    moveLeft(k)
    assert r'▦\sqrt{⬚}' == getEditModeLatex(k, UnitTestLatexConfiguration())
    moveRight(k)
    assert r'\sqrt{▦}' == getEditModeLatex(k, UnitTestLatexConfiguration())

def test_sqrt_del():
    k = KeyboardMemory()
    insert(k, StandardBranchingNode(r'\sqrt{', '}'))
    assert r'\sqrt{▦}' == getEditModeLatex(k, UnitTestLatexConfiguration())
    deleteCurrent(k)
    assert '▦' == getEditModeLatex(k, UnitTestLatexConfiguration())