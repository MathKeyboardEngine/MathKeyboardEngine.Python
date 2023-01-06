from src import deleteCurrent, KeyboardMemory, moveLeft, moveUp, DescendingBranchingNode, getEditModeLatex, insert, insertWithEncapsulateCurrent, DigitNode, moveRight, moveDown
from tests.testhelpers.UnitTestLatexConfiguration import UnitTestLatexConfiguration

def test_frac_left_right_right_right():
    k = KeyboardMemory()
    insert(k, DescendingBranchingNode(r'\frac{', '}{', '}'))
    moveLeft(k)
    assert r'▦\frac{⬚}{⬚}' == getEditModeLatex(k, UnitTestLatexConfiguration())
    moveRight(k)
    assert r'\frac{▦}{⬚}' == getEditModeLatex(k, UnitTestLatexConfiguration())
    moveRight(k)
    assert r'\frac{⬚}{▦}' == getEditModeLatex(k, UnitTestLatexConfiguration())
    moveRight(k)
    assert r'\frac{⬚}{⬚}▦' == getEditModeLatex(k, UnitTestLatexConfiguration())

def test_frac_3_right_4():
    k = KeyboardMemory()
    insert(k, DescendingBranchingNode(r'\frac{', '}{', '}'))
    insert(k, DigitNode('3'))
    moveRight(k)
    insert(k, DigitNode('4'))
    assert r'\frac{3}{4▦}' == getEditModeLatex(k, UnitTestLatexConfiguration())

def test_frac_3_down_4():
    k = KeyboardMemory()
    insert(k, DescendingBranchingNode(r'\frac{', '}{', '}'))
    insert(k, DigitNode('3'))
    moveDown(k)
    insert(k, DigitNode('4'))
    assert r'\frac{3}{4▦}' == getEditModeLatex(k, UnitTestLatexConfiguration())

def test_3_encapsulated_the_numerator_of_a_fraction():
    k = KeyboardMemory()
    insert(k, DigitNode('3'))
    insertWithEncapsulateCurrent(k, DescendingBranchingNode(r'\frac{', '}{', '}'))
    assert r'\frac{3}{▦}' == getEditModeLatex(k, UnitTestLatexConfiguration())

def test_delete_empty_frac_from_numerator():
    k = KeyboardMemory()
    insert(k, DescendingBranchingNode(r'\frac{', '}{', '}'))
    assert r'\frac{▦}{⬚}' == getEditModeLatex(k, UnitTestLatexConfiguration())
    deleteCurrent(k)
    assert '▦' == getEditModeLatex(k, UnitTestLatexConfiguration())

def test_delete_empty_frac_from_denominator():
    k = KeyboardMemory()
    insert(k, DescendingBranchingNode(r'\frac{', '}{', '}'))
    moveDown(k)
    assert r'\frac{⬚}{▦}' == getEditModeLatex(k, UnitTestLatexConfiguration())
    deleteCurrent(k)
    assert '▦' == getEditModeLatex(k, UnitTestLatexConfiguration())

def test_delete_empty_frac_from_the_right():
    k = KeyboardMemory()
    insert(k, DescendingBranchingNode(r'\frac{', '}{', '}'))
    moveDown(k)
    moveRight(k)
    assert r'\frac{⬚}{⬚}▦' == getEditModeLatex(k, UnitTestLatexConfiguration())
    deleteCurrent(k)
    assert '▦' == getEditModeLatex(k, UnitTestLatexConfiguration())

def test_deleting_frac_from_denominator_releases_non_empty_numerator():
    k = KeyboardMemory()
    insert(k, DescendingBranchingNode(r'\frac{', '}{', '}'))
    insert(k, DigitNode('1'))
    insert(k, DigitNode('2'))
    moveDown(k)
    insert(k, DigitNode('3'))
    moveRight(k)
    assert r'\frac{12}{3}▦' == getEditModeLatex(k, UnitTestLatexConfiguration())

    deleteCurrent(k)
    assert r'\frac{12}{▦}' == getEditModeLatex(k, UnitTestLatexConfiguration())
    deleteCurrent(k)
    assert '12▦' == getEditModeLatex(k, UnitTestLatexConfiguration())

def test_moveUp_in_filled_fraction():
    k = KeyboardMemory()
    insert(k, DescendingBranchingNode(r'\frac{', '}{', '}'))
    insert(k, DigitNode('1'))
    insert(k, DigitNode('2'))
    moveDown(k)
    insert(k, DigitNode('3'))
    assert r'\frac{12}{3▦}' == getEditModeLatex(k, UnitTestLatexConfiguration())

    moveUp(k)
    assert r'\frac{12▦}{3}' == getEditModeLatex(k, UnitTestLatexConfiguration())

def test_impossible_updown_requests_in_filled_fraction_should_not_throw():
    k = KeyboardMemory()
    insert(k, DescendingBranchingNode(r'\frac{', '}{', '}'))
    insert(k, DigitNode('1'))
    assert r'\frac{1▦}{⬚}' == getEditModeLatex(k, UnitTestLatexConfiguration())
    moveUp(k)
    assert r'\frac{1▦}{⬚}' == getEditModeLatex(k, UnitTestLatexConfiguration())

    moveDown(k)
    insert(k, DigitNode('2'))
    assert r'\frac{1}{2▦}' == getEditModeLatex(k, UnitTestLatexConfiguration())
    moveDown(k)
    assert r'\frac{1}{2▦}' == getEditModeLatex(k, UnitTestLatexConfiguration())

def test_impossible_updown_requests_in_empty_fraction_should_not_throw():
    k = KeyboardMemory()
    insert(k, DescendingBranchingNode(r'\frac{', '}{', '}'))
    moveDown(k)
    assert r'\frac{⬚}{▦}' == getEditModeLatex(k, UnitTestLatexConfiguration())
    moveDown(k)
    assert r'\frac{⬚}{▦}' == getEditModeLatex(k, UnitTestLatexConfiguration())
    moveUp(k)
    assert r'\frac{▦}{⬚}' == getEditModeLatex(k, UnitTestLatexConfiguration())
    moveUp(k)
    assert r'\frac{▦}{⬚}' == getEditModeLatex(k, UnitTestLatexConfiguration())