from src import KeyboardMemory, insert, DigitNode, getEditModeLatex, selectLeft, moveLeft, enterSelectionMode, selectRight, inSelectionMode, insertWithEncapsulateCurrent, AscendingBranchingNode, StandardLeafNode
from tests.testhelpers.UnitTestLatexConfiguration import UnitTestLatexConfiguration

def test_can_select_a_single_TreeNode_and_the_selection_is_correctly_displayed__case__the_exclusive_left_border_is_a_TreeNode():
    # Arrange
    k = KeyboardMemory()
    insert(k, DigitNode('1'))
    insert(k, DigitNode('2'))
    assert '12▦' == getEditModeLatex(k, UnitTestLatexConfiguration())
    # Act
    selectLeft(k)
    # Assert
    assert r'1\colorbox{blue}{2}' == getEditModeLatex(k, UnitTestLatexConfiguration())

def test_can_select_a_single_TreeNode_and_the_selection_is_correctly_displayed__case__the_exclusive_left_border_is_a_Placeholder():
    # Arrange
    k = KeyboardMemory()
    insert(k, DigitNode('1'))
    assert '1▦' == getEditModeLatex(k, UnitTestLatexConfiguration())
    # Act
    selectLeft(k)
    # Assert
    assert r'\colorbox{blue}{1}' == getEditModeLatex(k, UnitTestLatexConfiguration())

def test_can_select_multiple_TreeNodes_and_the_selection_is_correctly_displayed__case__the_exclusive_left_border_is_a_TreeNode():
    # Arrange
    k = KeyboardMemory()
    insert(k, DigitNode('1'))
    insert(k, DigitNode('2'))
    insert(k, DigitNode('3'))
    assert '123▦' == getEditModeLatex(k, UnitTestLatexConfiguration())
    # Act
    selectLeft(k)
    selectLeft(k)
    # Assert
    assert r'1\colorbox{blue}{23}' == getEditModeLatex(k, UnitTestLatexConfiguration())

def test_can_select_multiple_TreeNodes_and_the_selection_is_correctly_displayed__case__the_exclusive_left_border_is_a_Placeholder():
    # Arrange
    k = KeyboardMemory()
    insert(k, DigitNode('1'))
    insert(k, DigitNode('2'))
    assert '12▦' == getEditModeLatex(k, UnitTestLatexConfiguration())
    # Act
    selectLeft(k)
    selectLeft(k)
    # Assert
    assert r'\colorbox{blue}{12}' == getEditModeLatex(k, UnitTestLatexConfiguration())

def test_does_nothing_if_current_is_the_syntaxTreeRoot_and_no_selectRight_has_been_done():
    # Arrange
    k = KeyboardMemory()
    insert(k, DigitNode('1'))
    moveLeft(k)
    assert '▦1' == getEditModeLatex(k, UnitTestLatexConfiguration())
    enterSelectionMode(k)
    # Act
    selectLeft(k)
    # Assert
    assert '▦1' == getEditModeLatex(k, UnitTestLatexConfiguration())

def test_does_nothing_if_all_on_the_left_available_TreeNodes_are_selected():
    # Arrange
    k = KeyboardMemory()
    insert(k, DigitNode('1'))
    selectLeft(k)
    assert r'\colorbox{blue}{1}' == getEditModeLatex(k, UnitTestLatexConfiguration())
    # Act
    selectLeft(k)
    # Assert
    assert r'\colorbox{blue}{1}' == getEditModeLatex(k, UnitTestLatexConfiguration())

def test_stays_in_selection_mode_after_deselecting():
    # Arrange
    k = KeyboardMemory()
    insert(k, DigitNode('1'))
    moveLeft(k)
    selectRight(k)
    assert r'\colorbox{blue}{1}' == getEditModeLatex(k, UnitTestLatexConfiguration())
    # Act
    selectLeft(k)
    # Assert
    assert '▦1' == getEditModeLatex(k, UnitTestLatexConfiguration())
    assert inSelectionMode(k)

def test_can_break_out_of_the_current_Placeholder():
    # Arrange
    k = KeyboardMemory()
    insert(k, DigitNode('2'))
    insertWithEncapsulateCurrent(k, AscendingBranchingNode('', '^{', '}'))
    insert(k, StandardLeafNode('x'))
    assert r'2^{x▦}' == getEditModeLatex(k, UnitTestLatexConfiguration())
    selectLeft(k)
    assert r'2^{\colorbox{blue}{x}}' == getEditModeLatex(k, UnitTestLatexConfiguration())
    # Act
    selectLeft(k)
    # Assert
    assert r'\colorbox{blue}{2^{x}}' == getEditModeLatex(k, UnitTestLatexConfiguration())