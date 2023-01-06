import pytest
from src import KeyboardMemory, insert, DigitNode, getEditModeLatex, selectLeft, insertWithEncapsulateSelectionAndPrevious, AscendingBranchingNode, StandardBranchingNode, StandardLeafNode, enterSelectionMode, DescendingBranchingNode 
from tests.testhelpers.UnitTestLatexConfiguration import UnitTestLatexConfiguration

def test_when_a_single_TreeNode_is_selected_and_the_exclusive_left_border_is_a_TreeNode():
    # Arrange
    k = KeyboardMemory()
    insert(k, DigitNode('2'))
    insert(k, DigitNode('3'))
    assert '23▦' == getEditModeLatex(k, UnitTestLatexConfiguration())
    selectLeft(k)
    assert r'2\colorbox{blue}{3}' == getEditModeLatex(k, UnitTestLatexConfiguration())
    # Act
    insertWithEncapsulateSelectionAndPrevious(k, AscendingBranchingNode('', '^{', '}'))
    # Assert
    assert '2^{3▦}' == getEditModeLatex(k, UnitTestLatexConfiguration())

def test_when_a_single_TreeNode_is_selected_and_the_exclusive_left_border_is_a_Placeholder():
    # Arrange
    k = KeyboardMemory()
    insert(k, DigitNode('2'))
    assert '2▦' == getEditModeLatex(k, UnitTestLatexConfiguration())
    selectLeft(k)
    assert r'\colorbox{blue}{2}' == getEditModeLatex(k, UnitTestLatexConfiguration())
    # Act
    insertWithEncapsulateSelectionAndPrevious(k, AscendingBranchingNode('', '^{', '}'))
    # Assert
    assert '⬚^{2▦}' == getEditModeLatex(k, UnitTestLatexConfiguration())

def test_when_multiple_TreeNodes_are_selected_and_the_exclusive_left_border_is_a_TreeNode():
    # Arrange
    k = KeyboardMemory()
    insert(k, DigitNode('2'))
    insert(k, DigitNode('1'))
    insert(k, DigitNode('0'))
    assert '210▦' == getEditModeLatex(k, UnitTestLatexConfiguration())
    selectLeft(k)
    selectLeft(k)
    assert r'2\colorbox{blue}{10}' == getEditModeLatex(k, UnitTestLatexConfiguration())
    # Act
    insertWithEncapsulateSelectionAndPrevious(k, AscendingBranchingNode('', '^{', '}'))
    # Assert
    assert '2^{10▦}' == getEditModeLatex(k, UnitTestLatexConfiguration())

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
    insertWithEncapsulateSelectionAndPrevious(k, AscendingBranchingNode('', '^{', '}'))
    # Assert
    assert '⬚^{12▦}' == getEditModeLatex(k, UnitTestLatexConfiguration())

def test_invokes_insertWithEncapsulateCurrent_if_inSelectionMode_but_nothing_selected():
    # Arrange
    k = KeyboardMemory()
    insert(k, DigitNode('1'))
    insert(k, StandardLeafNode('+'))
    insert(k, DigitNode('1'))
    insert(k, DigitNode('2'))
    enterSelectionMode(k)
    assert '1+12▦' == getEditModeLatex(k, UnitTestLatexConfiguration())
    # Act
    insertWithEncapsulateSelectionAndPrevious(k, DescendingBranchingNode(r'\frac{', '}{', '}'))
    # Assert
    assert r'1+\frac{12}{▦}' == getEditModeLatex(k, UnitTestLatexConfiguration())

def test_throws_on_inserting_BranchingNode_with_single_Placeholder():
    with pytest.raises(Exception) as ex:
        k = KeyboardMemory()
        insertWithEncapsulateSelectionAndPrevious(k, StandardBranchingNode('[', ']'))
    assert 'Expected 2 placeholders.' == str(ex.value)
