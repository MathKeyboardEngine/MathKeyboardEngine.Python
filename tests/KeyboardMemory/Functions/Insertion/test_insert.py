from src import KeyboardMemory, DigitNode, insert, getEditModeLatex, moveLeft
from tests.testhelpers.UnitTestLatexConfiguration import UnitTestLatexConfiguration

def test_instert_prepends_if_current_is_a_Placeholder():
    # Arrange
    k = KeyboardMemory()
    digitNode1 = DigitNode('1')
    insert(k, digitNode1)
    assert '1▦' == getEditModeLatex(k, UnitTestLatexConfiguration())
    moveLeft(k)
    assert k.current == digitNode1.parentPlaceholder
    assert '▦1' == getEditModeLatex(k, UnitTestLatexConfiguration())
    # Act
    insert(k, DigitNode('2'))
    # Assert
    assert '2▦1' == getEditModeLatex(k, UnitTestLatexConfiguration())

def test_inserts_at_the_right_of_a_TreeNode_if_current_is_a_TreeNode():
    # Arrange
    k = KeyboardMemory()
    digitNode1 = DigitNode('1')
    insert(k, digitNode1)
    assert k.current == digitNode1
    assert '1▦' == getEditModeLatex(k, UnitTestLatexConfiguration())
    # Act 1
    insert(k, DigitNode('2'))
    # Assert 1
    assert '12▦' == getEditModeLatex(k, UnitTestLatexConfiguration())
    # Arrange 2
    moveLeft(k)
    assert k.current == digitNode1
    assert '1▦2' == getEditModeLatex(k, UnitTestLatexConfiguration())
    # Act 2
    insert(k, DigitNode('3'))
    # Assert 2
    assert '13▦2' == getEditModeLatex(k, UnitTestLatexConfiguration())

def test_sets_the_parentPlaceholder():
    # Arrange
    k = KeyboardMemory()
    node = DigitNode('1')
    assert node.parentPlaceholder is None
    # Act
    insert(k, node)
    # Assert
    assert node.parentPlaceholder is not None

def test_sets_current():
    # Arrange
    k = KeyboardMemory()
    originalCurrent = k.current
    # Act
    d = DigitNode('1')
    insert(k, d)
    # Assert
    assert originalCurrent != k.current
    assert d == k.current