from src import DigitNode, KeyboardMemory, delete_selection, get_edit_mode_latex, insert, move_left, select_left, select_right
from tests._testhelpers.UnitTestLatexConfiguration import UnitTestLatexConfiguration


def test_can_delete_a_single_TreeNode_when_the_exclusive_left_border_is_a_TreeNode():
    # Arrange
    k = KeyboardMemory()
    insert(k, DigitNode('1'))
    insert(k, DigitNode('2'))
    assert '12▦' == get_edit_mode_latex(k, UnitTestLatexConfiguration())
    select_left(k)
    assert r'1\colorbox{blue}{2}' == get_edit_mode_latex(k, UnitTestLatexConfiguration())
    # Act
    delete_selection(k)
    # Assert
    assert '1▦' == get_edit_mode_latex(k, UnitTestLatexConfiguration())


def test_can_delete_a_single_TreeNode_when_the_exclusive_left_border_is_a_Placeholder():
    # Arrange
    k = KeyboardMemory()
    insert(k, DigitNode('1'))
    assert '1▦' == get_edit_mode_latex(k, UnitTestLatexConfiguration())
    select_left(k)
    assert r'\colorbox{blue}{1}' == get_edit_mode_latex(k, UnitTestLatexConfiguration())
    # Act
    delete_selection(k)
    # Assert
    assert '▦' == get_edit_mode_latex(k, UnitTestLatexConfiguration())


def test_can_delete_multiple_TreeNodes_when_the_exclusive_left_border_is_a_TreeNode__via_selectLeft():
    # Arrange
    k = KeyboardMemory()
    insert(k, DigitNode('1'))
    insert(k, DigitNode('2'))
    insert(k, DigitNode('3'))
    assert '123▦' == get_edit_mode_latex(k, UnitTestLatexConfiguration())
    select_left(k)
    select_left(k)
    assert r'1\colorbox{blue}{23}' == get_edit_mode_latex(k, UnitTestLatexConfiguration())
    # Act
    delete_selection(k)
    # Assert
    assert '1▦' == get_edit_mode_latex(k, UnitTestLatexConfiguration())


def test_can_delete_multiple_TreeNodes_when_the_exclusive_left_border_is_a_TreeNode__via_selectRight():
    # Arrange
    k = KeyboardMemory()
    insert(k, DigitNode('1'))
    insert(k, DigitNode('2'))
    insert(k, DigitNode('3'))
    move_left(k)
    move_left(k)
    assert '1▦23' == get_edit_mode_latex(k, UnitTestLatexConfiguration())
    select_right(k)
    select_right(k)
    assert r'1\colorbox{blue}{23}' == get_edit_mode_latex(k, UnitTestLatexConfiguration())
    # Act
    delete_selection(k)
    # Assert
    assert '1▦' == get_edit_mode_latex(k, UnitTestLatexConfiguration())


def test_can_delete_multiple_TreeNodes_when_the_exclusive_left_border_is_a_Placeholder__via_selectLeft():
    # Arrange
    k = KeyboardMemory()
    insert(k, DigitNode('1'))
    insert(k, DigitNode('2'))
    assert '12▦' == get_edit_mode_latex(k, UnitTestLatexConfiguration())
    select_left(k)
    select_left(k)
    assert r'\colorbox{blue}{12}' == get_edit_mode_latex(k, UnitTestLatexConfiguration())
    # Act
    delete_selection(k)
    # Assert
    assert '▦' == get_edit_mode_latex(k, UnitTestLatexConfiguration())


def test_can_delete_multiple_TreeNodes_when_the_exclusive_left_border_is_a_Placeholder__via_selectRight():
    # Arrange
    k = KeyboardMemory()
    insert(k, DigitNode('1'))
    insert(k, DigitNode('2'))
    move_left(k)
    move_left(k)
    assert '▦12' == get_edit_mode_latex(k, UnitTestLatexConfiguration())
    select_right(k)
    select_right(k)
    assert r'\colorbox{blue}{12}' == get_edit_mode_latex(k, UnitTestLatexConfiguration())
    # Act
    delete_selection(k)
    # Assert
    assert '▦' == get_edit_mode_latex(k, UnitTestLatexConfiguration())
