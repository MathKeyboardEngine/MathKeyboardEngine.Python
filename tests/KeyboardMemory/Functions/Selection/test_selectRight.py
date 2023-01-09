from src import KeyboardMemory, inSelectionMode, insert, DigitNode, moveLeft, getEditModeLatex, selectRight, selectLeft, StandardBranchingNode, StandardLeafNode, moveRight
from tests.testhelpers.UnitTestLatexConfiguration import UnitTestLatexConfiguration

def test_can_select_a_single_TreeNode_and_the_selection_is_correctly_displayed__case__the_exclusive_left_border_is_a_TreeNode():
    # Arrange
    k = KeyboardMemory()
    insert(k, DigitNode('1'))
    insert(k, DigitNode('2'))
    moveLeft(k)
    assert '1▦2' == getEditModeLatex(k, UnitTestLatexConfiguration())
    # Act
    selectRight(k)
    # Assert
    assert r'1\colorbox{blue}{2}' == getEditModeLatex(k, UnitTestLatexConfiguration())

def test_can_select_a_single_TreeNode_and_the_selection_is_correctly_displayed__case__the_exclusive_left_border_is_a_Placeholder():
    # Arrange
    k = KeyboardMemory()
    insert(k, DigitNode('1'))
    moveLeft(k)
    assert '▦1' == getEditModeLatex(k, UnitTestLatexConfiguration())
    # Act
    selectRight(k)
    # Assert
    assert r'\colorbox{blue}{1}' == getEditModeLatex(k, UnitTestLatexConfiguration())

def test_can_select_multiple_TreeNodes_and_the_selection_is_correctly_displayed__case__the_exclusive_left_border_is_a_TreeNode():
    # Arrange
    k = KeyboardMemory()
    insert(k, DigitNode('1'))
    insert(k, DigitNode('2'))
    insert(k, DigitNode('3'))
    moveLeft(k)
    moveLeft(k)
    assert '1▦23' == getEditModeLatex(k, UnitTestLatexConfiguration())
    # Act
    selectRight(k)
    selectRight(k)
    # Assert
    assert r'1\colorbox{blue}{23}' == getEditModeLatex(k, UnitTestLatexConfiguration())

def test_can_select_multiple_TreeNodes_and_the_selection_is_correctly_displayed__case__the_exclusive_left_border_is_a_Placeholder():
    # Arrange
    k = KeyboardMemory()
    insert(k, DigitNode('1'))
    insert(k, DigitNode('2'))
    moveLeft(k)
    moveLeft(k)
    assert '▦12' == getEditModeLatex(k, UnitTestLatexConfiguration())
    # Act
    selectRight(k)
    selectRight(k)
    # Assert
    assert r'\colorbox{blue}{12}' == getEditModeLatex(k, UnitTestLatexConfiguration())

def test_stays_in_selection_mode_after_deselecting():
    # Arrange
    k = KeyboardMemory()
    insert(k, DigitNode('1'))
    selectLeft(k)
    assert r'\colorbox{blue}{1}' == getEditModeLatex(k, UnitTestLatexConfiguration())
    # Act
    selectRight(k)
    # Assert
    assert '1▦' == getEditModeLatex(k, UnitTestLatexConfiguration())
    assert inSelectionMode(k)

def test_does_nothing_if_all_on_the_right_available_TreeNodes_are_selected__case__the_exclusive_left_border_is_a_Placeholder_and_the_syntaxTreeRoot():
    # Arrange
    k = KeyboardMemory()
    insert(k, DigitNode('1'))
    moveLeft(k)
    assert '▦1' == getEditModeLatex(k, UnitTestLatexConfiguration())
    selectRight(k)
    assert r'\colorbox{blue}{1}' == getEditModeLatex(k, UnitTestLatexConfiguration())
    # Act
    selectRight(k)
    # Assert
    assert r'\colorbox{blue}{1}' == getEditModeLatex(k, UnitTestLatexConfiguration())

def test_does_nothing_if_all_on_the_right_available_TreeNodes_are_selected_and_the_exclusive_left_border_is_a_TreeNode_and_the_parentPlaceholder_is_the_syntaxTreeRoot():
    # Arrange
    k = KeyboardMemory()
    insert(k, DigitNode('1'))
    insert(k, DigitNode('2'))
    moveLeft(k)
    assert '1▦2' == getEditModeLatex(k, UnitTestLatexConfiguration())
    selectRight(k)
    assert r'1\colorbox{blue}{2}' == getEditModeLatex(k, UnitTestLatexConfiguration())
    # Act
    selectRight(k)
    # Assert
    assert r'1\colorbox{blue}{2}' == getEditModeLatex(k, UnitTestLatexConfiguration())

def test_can_break_out_of_the_current_Placeholder__case__set_a_Placeholder_as_current():
    # Arrange
    k = KeyboardMemory()
    insert(k, StandardBranchingNode(r'\sqrt{', '}'))
    insert(k, DigitNode('2'))
    moveRight(k)
    insert(k, StandardLeafNode('+'))
    insert(k, StandardLeafNode('a'))
    moveLeft(k)
    moveLeft(k)
    moveLeft(k)
    moveLeft(k)
    assert r'\sqrt{▦2}+a' == getEditModeLatex(k, UnitTestLatexConfiguration())
    selectRight(k)
    assert r'\sqrt{\colorbox{blue}{2}}+a' == getEditModeLatex(k, UnitTestLatexConfiguration())
    # Act & Assert
    selectRight(k)
    assert r'\colorbox{blue}{\sqrt{2}}+a' == getEditModeLatex(k, UnitTestLatexConfiguration())
    selectRight(k)
    assert r'\colorbox{blue}{\sqrt{2}+}a' == getEditModeLatex(k, UnitTestLatexConfiguration())
    selectRight(k)
    assert r'\colorbox{blue}{\sqrt{2}+a}' == getEditModeLatex(k, UnitTestLatexConfiguration())

def test_can_break_out_of_the_current_Placeholder__case__set_a_TreeNode_as_current():
    # Arrange
    k = KeyboardMemory()
    insert(k, DigitNode('3'))
    insert(k, StandardBranchingNode(r'\sqrt{', '}'))
    insert(k, DigitNode('2'))
    moveRight(k)
    insert(k, StandardLeafNode('+'))
    insert(k, StandardLeafNode('a'))
    moveLeft(k)
    moveLeft(k)
    moveLeft(k)
    moveLeft(k)
    assert r'3\sqrt{▦2}+a' == getEditModeLatex(k, UnitTestLatexConfiguration())
    selectRight(k)
    assert r'3\sqrt{\colorbox{blue}{2}}+a' == getEditModeLatex(k, UnitTestLatexConfiguration())
    # Act & Assert
    selectRight(k)
    assert r'3\colorbox{blue}{\sqrt{2}}+a' == getEditModeLatex(k, UnitTestLatexConfiguration())
    selectRight(k)
    assert r'3\colorbox{blue}{\sqrt{2}+}a' == getEditModeLatex(k, UnitTestLatexConfiguration())
    selectRight(k)
    assert r'3\colorbox{blue}{\sqrt{2}+a}' == getEditModeLatex(k, UnitTestLatexConfiguration())