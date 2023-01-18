from src import DescendingBranchingNode, DigitNode, KeyboardMemory, enter_selection_mode, get_edit_mode_latex, insert, insert_with_encapsulate_selection, select_left
from tests._testhelpers.UnitTestLatexConfiguration import UnitTestLatexConfiguration


def test_when_a_single_TreeNode_is_selected_and_the_exclusive_left_border_is_a_TreeNode():
    # Arrange
    k = KeyboardMemory()
    insert(k, DigitNode('1'))
    insert(k, DigitNode('2'))
    assert '12▦' == get_edit_mode_latex(k, UnitTestLatexConfiguration())
    select_left(k)
    assert r'1\colorbox{blue}{2}' == get_edit_mode_latex(k, UnitTestLatexConfiguration())
    # Act
    insert_with_encapsulate_selection(k, DescendingBranchingNode(r'\frac{', '}{', '}'))
    # Assert
    assert r'1\frac{2}{▦}' == get_edit_mode_latex(k, UnitTestLatexConfiguration())


def test_when_a_single_TreeNode_is_selected_and_the_exclusive_left_border_is_a_Placeholder():
    # Arrange
    k = KeyboardMemory()
    insert(k, DigitNode('1'))
    assert '1▦' == get_edit_mode_latex(k, UnitTestLatexConfiguration())
    select_left(k)
    assert r'\colorbox{blue}{1}' == get_edit_mode_latex(k, UnitTestLatexConfiguration())
    # Act
    insert_with_encapsulate_selection(k, DescendingBranchingNode(r'\frac{', '}{', '}'))
    # Assert
    assert r'\frac{1}{▦}' == get_edit_mode_latex(k, UnitTestLatexConfiguration())


def test_when_multiple_TreeNodes_are_selected_and_the_exclusive_left_border_is_a_TreeNode():
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
    insert_with_encapsulate_selection(k, DescendingBranchingNode(r'\frac{', '}{', '}'))
    # Assert
    assert r'1\frac{23}{▦}' == get_edit_mode_latex(k, UnitTestLatexConfiguration())


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
    insert_with_encapsulate_selection(k, DescendingBranchingNode(r'\frac{', '}{', '}'))
    # Assert
    assert r'\frac{12}{▦}' == get_edit_mode_latex(k, UnitTestLatexConfiguration())


def test_does_a_regular_insert_when_inSelectionMode_but_nothing_is_selected():
    # Arrange
    k = KeyboardMemory()
    insert(k, DigitNode('1'))
    insert(k, DigitNode('2'))
    enter_selection_mode(k)
    assert '12▦' == get_edit_mode_latex(k, UnitTestLatexConfiguration())
    # Act
    insert_with_encapsulate_selection(k, DescendingBranchingNode(r'\frac{', '}{', '}'))
    # Assert
    assert r'12\frac{▦}{⬚}' == get_edit_mode_latex(k, UnitTestLatexConfiguration())
