from src import KeyboardMemory, DigitNode, insert, get_edit_mode_latex, move_left
from tests.testhelpers.UnitTestLatexConfiguration import UnitTestLatexConfiguration

def test_instert_prepends_if_current_is_a_Placeholder():
    # Arrange
    k = KeyboardMemory()
    node1 = DigitNode('1')
    insert(k, node1)
    assert '1▦' == get_edit_mode_latex(k, UnitTestLatexConfiguration())
    move_left(k)
    assert k.current == node1.parent_placeholder
    assert '▦1' == get_edit_mode_latex(k, UnitTestLatexConfiguration())
    # Act
    insert(k, DigitNode('2'))
    # Assert
    assert '2▦1' == get_edit_mode_latex(k, UnitTestLatexConfiguration())

def test_inserts_at_the_right_of_a_TreeNode_if_current_is_a_TreeNode():
    # Arrange
    k = KeyboardMemory()
    node1 = DigitNode('1')
    insert(k, node1)
    assert k.current == node1
    assert '1▦' == get_edit_mode_latex(k, UnitTestLatexConfiguration())
    # Act 1
    insert(k, DigitNode('2'))
    # Assert 1
    assert '12▦' == get_edit_mode_latex(k, UnitTestLatexConfiguration())
    # Arrange 2
    move_left(k)
    assert k.current == node1
    assert '1▦2' == get_edit_mode_latex(k, UnitTestLatexConfiguration())
    # Act 2
    insert(k, DigitNode('3'))
    # Assert 2
    assert '13▦2' == get_edit_mode_latex(k, UnitTestLatexConfiguration())

def test_sets_the_parentPlaceholder():
    # Arrange
    k = KeyboardMemory()
    node = DigitNode('1')
    assert node.parent_placeholder is None
    # Act
    insert(k, node)
    # Assert
    assert node.parent_placeholder is not None

def test_sets_current():
    # Arrange
    k = KeyboardMemory()
    original_current = k.current
    # Act
    d = DigitNode('1')
    insert(k, d)
    # Assert
    assert original_current != k.current
    assert d == k.current