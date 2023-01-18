from src import DigitNode, KeyboardMemory, StandardBranchingNode, StandardLeafNode, get_edit_mode_latex, in_selection_mode, insert, move_left, move_right, select_left, select_right
from tests._testhelpers.UnitTestLatexConfiguration import UnitTestLatexConfiguration


def test_can_select_a_single_TreeNode_and_the_selection_is_correctly_displayed__case__the_exclusive_left_border_is_a_TreeNode():
    # Arrange
    k = KeyboardMemory()
    insert(k, DigitNode('1'))
    insert(k, DigitNode('2'))
    move_left(k)
    assert '1▦2' == get_edit_mode_latex(k, UnitTestLatexConfiguration())
    # Act
    select_right(k)
    # Assert
    assert r'1\colorbox{blue}{2}' == get_edit_mode_latex(k, UnitTestLatexConfiguration())

def test_can_select_a_single_TreeNode_and_the_selection_is_correctly_displayed__case__the_exclusive_left_border_is_a_Placeholder():
    # Arrange
    k = KeyboardMemory()
    insert(k, DigitNode('1'))
    move_left(k)
    assert '▦1' == get_edit_mode_latex(k, UnitTestLatexConfiguration())
    # Act
    select_right(k)
    # Assert
    assert r'\colorbox{blue}{1}' == get_edit_mode_latex(k, UnitTestLatexConfiguration())

def test_can_select_multiple_TreeNodes_and_the_selection_is_correctly_displayed__case__the_exclusive_left_border_is_a_TreeNode():
    # Arrange
    k = KeyboardMemory()
    insert(k, DigitNode('1'))
    insert(k, DigitNode('2'))
    insert(k, DigitNode('3'))
    move_left(k)
    move_left(k)
    assert '1▦23' == get_edit_mode_latex(k, UnitTestLatexConfiguration())
    # Act
    select_right(k)
    select_right(k)
    # Assert
    assert r'1\colorbox{blue}{23}' == get_edit_mode_latex(k, UnitTestLatexConfiguration())

def test_can_select_multiple_TreeNodes_and_the_selection_is_correctly_displayed__case__the_exclusive_left_border_is_a_Placeholder():
    # Arrange
    k = KeyboardMemory()
    insert(k, DigitNode('1'))
    insert(k, DigitNode('2'))
    move_left(k)
    move_left(k)
    assert '▦12' == get_edit_mode_latex(k, UnitTestLatexConfiguration())
    # Act
    select_right(k)
    select_right(k)
    # Assert
    assert r'\colorbox{blue}{12}' == get_edit_mode_latex(k, UnitTestLatexConfiguration())

def test_stays_in_selection_mode_after_deselecting():
    # Arrange
    k = KeyboardMemory()
    insert(k, DigitNode('1'))
    select_left(k)
    assert r'\colorbox{blue}{1}' == get_edit_mode_latex(k, UnitTestLatexConfiguration())
    # Act
    select_right(k)
    # Assert
    assert '1▦' == get_edit_mode_latex(k, UnitTestLatexConfiguration())
    assert in_selection_mode(k)

def test_does_nothing_if_all_on_the_right_available_TreeNodes_are_selected__case__the_exclusive_left_border_is_a_Placeholder_and_the_syntaxTreeRoot():
    # Arrange
    k = KeyboardMemory()
    insert(k, DigitNode('1'))
    move_left(k)
    assert '▦1' == get_edit_mode_latex(k, UnitTestLatexConfiguration())
    select_right(k)
    assert r'\colorbox{blue}{1}' == get_edit_mode_latex(k, UnitTestLatexConfiguration())
    # Act
    select_right(k)
    # Assert
    assert r'\colorbox{blue}{1}' == get_edit_mode_latex(k, UnitTestLatexConfiguration())

def test_does_nothing_if_all_on_the_right_available_TreeNodes_are_selected_and_the_exclusive_left_border_is_a_TreeNode_and_the_parentPlaceholder_is_the_syntaxTreeRoot():
    # Arrange
    k = KeyboardMemory()
    insert(k, DigitNode('1'))
    insert(k, DigitNode('2'))
    move_left(k)
    assert '1▦2' == get_edit_mode_latex(k, UnitTestLatexConfiguration())
    select_right(k)
    assert r'1\colorbox{blue}{2}' == get_edit_mode_latex(k, UnitTestLatexConfiguration())
    # Act
    select_right(k)
    # Assert
    assert r'1\colorbox{blue}{2}' == get_edit_mode_latex(k, UnitTestLatexConfiguration())

def test_can_break_out_of_the_current_Placeholder__case__set_a_Placeholder_as_current():
    # Arrange
    k = KeyboardMemory()
    insert(k, StandardBranchingNode(r'\sqrt{', '}'))
    insert(k, DigitNode('2'))
    move_right(k)
    insert(k, StandardLeafNode('+'))
    insert(k, StandardLeafNode('a'))
    move_left(k)
    move_left(k)
    move_left(k)
    move_left(k)
    assert r'\sqrt{▦2}+a' == get_edit_mode_latex(k, UnitTestLatexConfiguration())
    select_right(k)
    assert r'\sqrt{\colorbox{blue}{2}}+a' == get_edit_mode_latex(k, UnitTestLatexConfiguration())
    # Act & Assert
    select_right(k)
    assert r'\colorbox{blue}{\sqrt{2}}+a' == get_edit_mode_latex(k, UnitTestLatexConfiguration())
    select_right(k)
    assert r'\colorbox{blue}{\sqrt{2}+}a' == get_edit_mode_latex(k, UnitTestLatexConfiguration())
    select_right(k)
    assert r'\colorbox{blue}{\sqrt{2}+a}' == get_edit_mode_latex(k, UnitTestLatexConfiguration())

def test_can_break_out_of_the_current_Placeholder__case__set_a_TreeNode_as_current():
    # Arrange
    k = KeyboardMemory()
    insert(k, DigitNode('3'))
    insert(k, StandardBranchingNode(r'\sqrt{', '}'))
    insert(k, DigitNode('2'))
    move_right(k)
    insert(k, StandardLeafNode('+'))
    insert(k, StandardLeafNode('a'))
    move_left(k)
    move_left(k)
    move_left(k)
    move_left(k)
    assert r'3\sqrt{▦2}+a' == get_edit_mode_latex(k, UnitTestLatexConfiguration())
    select_right(k)
    assert r'3\sqrt{\colorbox{blue}{2}}+a' == get_edit_mode_latex(k, UnitTestLatexConfiguration())
    # Act & Assert
    select_right(k)
    assert r'3\colorbox{blue}{\sqrt{2}}+a' == get_edit_mode_latex(k, UnitTestLatexConfiguration())
    select_right(k)
    assert r'3\colorbox{blue}{\sqrt{2}+}a' == get_edit_mode_latex(k, UnitTestLatexConfiguration())
    select_right(k)
    assert r'3\colorbox{blue}{\sqrt{2}+a}' == get_edit_mode_latex(k, UnitTestLatexConfiguration())