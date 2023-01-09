from src import KeyboardMemory, insert, DigitNode, get_edit_mode_latex, select_left, move_left, enter_selection_mode, select_right, in_selection_mode, insert_with_encapsulate_current, AscendingBranchingNode, StandardLeafNode
from tests.testhelpers.UnitTestLatexConfiguration import UnitTestLatexConfiguration

def test_can_select_a_single_TreeNode_and_the_selection_is_correctly_displayed__case__the_exclusive_left_border_is_a_TreeNode():
    # Arrange
    k = KeyboardMemory()
    insert(k, DigitNode('1'))
    insert(k, DigitNode('2'))
    assert '12▦' == get_edit_mode_latex(k, UnitTestLatexConfiguration())
    # Act
    select_left(k)
    # Assert
    assert r'1\colorbox{blue}{2}' == get_edit_mode_latex(k, UnitTestLatexConfiguration())

def test_can_select_a_single_TreeNode_and_the_selection_is_correctly_displayed__case__the_exclusive_left_border_is_a_Placeholder():
    # Arrange
    k = KeyboardMemory()
    insert(k, DigitNode('1'))
    assert '1▦' == get_edit_mode_latex(k, UnitTestLatexConfiguration())
    # Act
    select_left(k)
    # Assert
    assert r'\colorbox{blue}{1}' == get_edit_mode_latex(k, UnitTestLatexConfiguration())

def test_can_select_multiple_TreeNodes_and_the_selection_is_correctly_displayed__case__the_exclusive_left_border_is_a_TreeNode():
    # Arrange
    k = KeyboardMemory()
    insert(k, DigitNode('1'))
    insert(k, DigitNode('2'))
    insert(k, DigitNode('3'))
    assert '123▦' == get_edit_mode_latex(k, UnitTestLatexConfiguration())
    # Act
    select_left(k)
    select_left(k)
    # Assert
    assert r'1\colorbox{blue}{23}' == get_edit_mode_latex(k, UnitTestLatexConfiguration())

def test_can_select_multiple_TreeNodes_and_the_selection_is_correctly_displayed__case__the_exclusive_left_border_is_a_Placeholder():
    # Arrange
    k = KeyboardMemory()
    insert(k, DigitNode('1'))
    insert(k, DigitNode('2'))
    assert '12▦' == get_edit_mode_latex(k, UnitTestLatexConfiguration())
    # Act
    select_left(k)
    select_left(k)
    # Assert
    assert r'\colorbox{blue}{12}' == get_edit_mode_latex(k, UnitTestLatexConfiguration())

def test_does_nothing_if_current_is_the_syntaxTreeRoot_and_no_selectRight_has_been_done():
    # Arrange
    k = KeyboardMemory()
    insert(k, DigitNode('1'))
    move_left(k)
    assert '▦1' == get_edit_mode_latex(k, UnitTestLatexConfiguration())
    enter_selection_mode(k)
    # Act
    select_left(k)
    # Assert
    assert '▦1' == get_edit_mode_latex(k, UnitTestLatexConfiguration())

def test_does_nothing_if_all_on_the_left_available_TreeNodes_are_selected():
    # Arrange
    k = KeyboardMemory()
    insert(k, DigitNode('1'))
    select_left(k)
    assert r'\colorbox{blue}{1}' == get_edit_mode_latex(k, UnitTestLatexConfiguration())
    # Act
    select_left(k)
    # Assert
    assert r'\colorbox{blue}{1}' == get_edit_mode_latex(k, UnitTestLatexConfiguration())

def test_stays_in_selection_mode_after_deselecting():
    # Arrange
    k = KeyboardMemory()
    insert(k, DigitNode('1'))
    move_left(k)
    select_right(k)
    assert r'\colorbox{blue}{1}' == get_edit_mode_latex(k, UnitTestLatexConfiguration())
    # Act
    select_left(k)
    # Assert
    assert '▦1' == get_edit_mode_latex(k, UnitTestLatexConfiguration())
    assert in_selection_mode(k)

def test_can_break_out_of_the_current_Placeholder():
    # Arrange
    k = KeyboardMemory()
    insert(k, DigitNode('2'))
    insert_with_encapsulate_current(k, AscendingBranchingNode('', '^{', '}'))
    insert(k, StandardLeafNode('x'))
    assert r'2^{x▦}' == get_edit_mode_latex(k, UnitTestLatexConfiguration())
    select_left(k)
    assert r'2^{\colorbox{blue}{x}}' == get_edit_mode_latex(k, UnitTestLatexConfiguration())
    # Act
    select_left(k)
    # Assert
    assert r'\colorbox{blue}{2^{x}}' == get_edit_mode_latex(k, UnitTestLatexConfiguration())