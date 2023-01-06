from src import KeyboardMemory, DescendingBranchingNode, DigitNode, insert, getEditModeLatex,moveRight, moveUp, moveDown
from tests.testhelpers.UnitTestLatexConfiguration import UnitTestLatexConfiguration

def test_basic_test():
    k = KeyboardMemory()
    insert(k, DescendingBranchingNode(r'\sqrt[', ']{', '}'))
    assert r'\sqrt[▦]{⬚}' == getEditModeLatex(k, UnitTestLatexConfiguration())
    insert(k, DigitNode('3'))
    moveRight(k)
    assert r'\sqrt[3]{▦}' == getEditModeLatex(k, UnitTestLatexConfiguration())
    insert(k, DigitNode('2'))
    insert(k, DigitNode('7'))
    assert r'\sqrt[3]{27▦}' == getEditModeLatex(k, UnitTestLatexConfiguration())

def test_updown_including_impossible_updown_requests():
    k = KeyboardMemory()
    insert(k, DescendingBranchingNode(r'\sqrt[', ']{', '}'))
    moveDown(k)
    assert r'\sqrt[⬚]{▦}' == getEditModeLatex(k, UnitTestLatexConfiguration())
    moveDown(k)
    assert r'\sqrt[⬚]{▦}' == getEditModeLatex(k, UnitTestLatexConfiguration())

    moveUp(k)
    assert r'\sqrt[▦]{⬚}' == getEditModeLatex(k, UnitTestLatexConfiguration())
    moveUp(k)
    assert r'\sqrt[▦]{⬚}' == getEditModeLatex(k, UnitTestLatexConfiguration())