import pytest
from src import KeyboardMemory, insert, DigitNode, get_edit_mode_latex, select_left, insert_with_ecapsulate_selection_and_previous, AscendingBranchingNode, StandardBranchingNode, StandardLeafNode, enter_selection_mode, DescendingBranchingNode 
from tests._testhelpers.UnitTestLatexConfiguration import UnitTestLatexConfiguration

def test_when_a_single_TreeNode_is_selected_and_the_exclusive_left_border_is_a_TreeNode():
    # Arrange
    k = KeyboardMemory()
    insert(k, DigitNode('2'))
    insert(k, DigitNode('3'))
    assert '23▦' == get_edit_mode_latex(k, UnitTestLatexConfiguration())
    select_left(k)
    assert r'2\colorbox{blue}{3}' == get_edit_mode_latex(k, UnitTestLatexConfiguration())
    # Act
    insert_with_ecapsulate_selection_and_previous(k, AscendingBranchingNode('', '^{', '}'))
    # Assert
    assert '2^{3▦}' == get_edit_mode_latex(k, UnitTestLatexConfiguration())

def test_when_a_single_TreeNode_is_selected_and_the_exclusive_left_border_is_a_Placeholder():
    # Arrange
    k = KeyboardMemory()
    insert(k, DigitNode('2'))
    assert '2▦' == get_edit_mode_latex(k, UnitTestLatexConfiguration())
    select_left(k)
    assert r'\colorbox{blue}{2}' == get_edit_mode_latex(k, UnitTestLatexConfiguration())
    # Act
    insert_with_ecapsulate_selection_and_previous(k, AscendingBranchingNode('', '^{', '}'))
    # Assert
    assert '⬚^{2▦}' == get_edit_mode_latex(k, UnitTestLatexConfiguration())

def test_when_multiple_TreeNodes_are_selected_and_the_exclusive_left_border_is_a_TreeNode():
    # Arrange
    k = KeyboardMemory()
    insert(k, DigitNode('2'))
    insert(k, DigitNode('1'))
    insert(k, DigitNode('0'))
    assert '210▦' == get_edit_mode_latex(k, UnitTestLatexConfiguration())
    select_left(k)
    select_left(k)
    assert r'2\colorbox{blue}{10}' == get_edit_mode_latex(k, UnitTestLatexConfiguration())
    # Act
    insert_with_ecapsulate_selection_and_previous(k, AscendingBranchingNode('', '^{', '}'))
    # Assert
    assert '2^{10▦}' == get_edit_mode_latex(k, UnitTestLatexConfiguration())

def test_when_multiple_TreeNodes_are_selected_and_the_exclusive_left_border_is_a_Placeholder():
    # Arrange
    k = KeyboardMemory()
    insert(k, DigitNode('1'))
    insert(k, DigitNode('2'))
    assert '12▦' == get_edit_mode_latex(k, UnitTestLatexConfiguration())
    select_left(k)
    select_left(k)
    assert r'\colorbox{blue}{12}' == get_edit_mode_latex(k, UnitTestLatexConfiguration())
    # Act
    insert_with_ecapsulate_selection_and_previous(k, AscendingBranchingNode('', '^{', '}'))
    # Assert
    assert '⬚^{12▦}' == get_edit_mode_latex(k, UnitTestLatexConfiguration())

def test_invokes_insertWithEncapsulateCurrent_if_inSelectionMode_but_nothing_selected():
    # Arrange
    k = KeyboardMemory()
    insert(k, DigitNode('1'))
    insert(k, StandardLeafNode('+'))
    insert(k, DigitNode('1'))
    insert(k, DigitNode('2'))
    enter_selection_mode(k)
    assert '1+12▦' == get_edit_mode_latex(k, UnitTestLatexConfiguration())
    # Act
    insert_with_ecapsulate_selection_and_previous(k, DescendingBranchingNode(r'\frac{', '}{', '}'))
    # Assert
    assert r'1+\frac{12}{▦}' == get_edit_mode_latex(k, UnitTestLatexConfiguration())

def test_throws_on_inserting_BranchingNode_with_single_Placeholder():
    with pytest.raises(Exception) as ex:
        k = KeyboardMemory()
        insert_with_ecapsulate_selection_and_previous(k, StandardBranchingNode('[', ']'))
    assert 'Expected 2 placeholders.' == str(ex.value)
