from src import KeyboardMemory, insert, DigitNode, getEditModeLatex, selectLeft, insertWithEncapsulateSelection, DescendingBranchingNode, enterSelectionMode
from tests.testhelpers.UnitTestLatexConfiguration import UnitTestLatexConfiguration

def test_when_a_single_TreeNode_is_selected_and_the_exclusive_left_border_is_a_TreeNode():
    # Arrange
    k = KeyboardMemory()
    insert(k, DigitNode('1'))
    insert(k, DigitNode('2'))
    assert '12▦' == getEditModeLatex(k, UnitTestLatexConfiguration())
    selectLeft(k)
    assert r'1\colorbox{blue}{2}' == getEditModeLatex(k, UnitTestLatexConfiguration())
    # Act
    insertWithEncapsulateSelection(k, DescendingBranchingNode(r'\frac{', '}{', '}'))
    # Assert
    assert r'1\frac{2}{▦}' == getEditModeLatex(k, UnitTestLatexConfiguration())

def test_when_a_single_TreeNode_is_selected_and_the_exclusive_left_border_is_a_Placeholder():
    # Arrange
    k = KeyboardMemory()
    insert(k, DigitNode('1'))
    assert '1▦' == getEditModeLatex(k, UnitTestLatexConfiguration())
    selectLeft(k)
    assert r'\colorbox{blue}{1}' == getEditModeLatex(k, UnitTestLatexConfiguration())
    # Act
    insertWithEncapsulateSelection(k, DescendingBranchingNode(r'\frac{', '}{', '}'))
    # Assert
    assert r'\frac{1}{▦}' == getEditModeLatex(k, UnitTestLatexConfiguration())

def test_when_multiple_TreeNodes_are_selected_and_the_exclusive_left_border_is_a_TreeNode():
    # Arrange
    k = KeyboardMemory()
    insert(k, DigitNode('1'))
    insert(k, DigitNode('2'))
    insert(k, DigitNode('3'))
    assert '123▦' == getEditModeLatex(k, UnitTestLatexConfiguration())
    selectLeft(k)
    selectLeft(k)
    assert r'1\colorbox{blue}{23}' == getEditModeLatex(k, UnitTestLatexConfiguration())
    # Act
    insertWithEncapsulateSelection(k, DescendingBranchingNode(r'\frac{', '}{', '}'))
    # Assert
    assert r'1\frac{23}{▦}' == getEditModeLatex(k, UnitTestLatexConfiguration())

def test_when_multiple_TreeNodes_are_selected_and_the_exclusive_left_border_is_a_Placeholder():
    # Arrange
    k = KeyboardMemory()
    insert(k, DigitNode('1'))
    insert(k, DigitNode('2'))
    assert '12▦' == getEditModeLatex(k, UnitTestLatexConfiguration())
    selectLeft(k)
    selectLeft(k)
    assert r'\colorbox{blue}{12}' == getEditModeLatex(k, UnitTestLatexConfiguration())
    # Act
    insertWithEncapsulateSelection(k, DescendingBranchingNode(r'\frac{', '}{', '}'))
    # Assert
    assert r'\frac{12}{▦}' == getEditModeLatex(k, UnitTestLatexConfiguration())

def test_does_a_regular_insert_when_inSelectionMode_but_nothing_is_selected():
    # Arrange
    k = KeyboardMemory()
    insert(k, DigitNode('1'))
    insert(k, DigitNode('2'))
    enterSelectionMode(k)
    assert '12▦' == getEditModeLatex(k, UnitTestLatexConfiguration())
    # Act
    insertWithEncapsulateSelection(k, DescendingBranchingNode(r'\frac{', '}{', '}'))
    # Assert
    assert r'12\frac{▦}{⬚}' == getEditModeLatex(k, UnitTestLatexConfiguration())