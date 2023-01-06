from src import KeyboardMemory, insert, DigitNode, getEditModeLatex, selectLeft, deleteSelection, moveLeft, selectRight
from tests.testhelpers.UnitTestLatexConfiguration import UnitTestLatexConfiguration

def test_can_delete_a_single_TreeNode_when_the_exclusive_left_border_is_a_TreeNode():
    # Arrange
    k = KeyboardMemory()
    insert(k, DigitNode('1'))
    insert(k, DigitNode('2'))
    assert '12▦' == getEditModeLatex(k, UnitTestLatexConfiguration())
    selectLeft(k)
    assert r'1\colorbox{blue}{2}' == getEditModeLatex(k, UnitTestLatexConfiguration())
    # Act
    deleteSelection(k)
    # Assert
    assert '1▦' == getEditModeLatex(k, UnitTestLatexConfiguration())

def test_can_delete_a_single_TreeNode_when_the_exclusive_left_border_is_a_Placeholder():
    # Arrange
    k = KeyboardMemory()
    insert(k, DigitNode('1'))
    assert '1▦' == getEditModeLatex(k, UnitTestLatexConfiguration())
    selectLeft(k)
    assert r'\colorbox{blue}{1}' == getEditModeLatex(k, UnitTestLatexConfiguration())
    # Act
    deleteSelection(k)
    # Assert
    assert '▦' == getEditModeLatex(k, UnitTestLatexConfiguration())

def test_can_delete_multiple_TreeNodes_when_the_exclusive_left_border_is_a_TreeNode__via_selectLeft():
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
    deleteSelection(k)
    # Assert
    assert '1▦' == getEditModeLatex(k, UnitTestLatexConfiguration())

def test_can_delete_multiple_TreeNodes_when_the_exclusive_left_border_is_a_TreeNode__via_selectRight():
    # Arrange
    k = KeyboardMemory()
    insert(k, DigitNode('1'))
    insert(k, DigitNode('2'))
    insert(k, DigitNode('3'))
    moveLeft(k)
    moveLeft(k)
    assert '1▦23' == getEditModeLatex(k, UnitTestLatexConfiguration())
    selectRight(k)
    selectRight(k)
    assert r'1\colorbox{blue}{23}' == getEditModeLatex(k, UnitTestLatexConfiguration())
    # Act
    deleteSelection(k)
    # Assert
    assert '1▦' == getEditModeLatex(k, UnitTestLatexConfiguration())

def test_can_delete_multiple_TreeNodes_when_the_exclusive_left_border_is_a_Placeholder__via_selectLeft():
    # Arrange
    k = KeyboardMemory()
    insert(k, DigitNode('1'))
    insert(k, DigitNode('2'))
    assert '12▦' == getEditModeLatex(k, UnitTestLatexConfiguration())
    selectLeft(k)
    selectLeft(k)
    assert r'\colorbox{blue}{12}' == getEditModeLatex(k, UnitTestLatexConfiguration())
    # Act
    deleteSelection(k)
    # Assert
    assert '▦' == getEditModeLatex(k, UnitTestLatexConfiguration())

def test_can_delete_multiple_TreeNodes_when_the_exclusive_left_border_is_a_Placeholder__via_selectRight():
    # Arrange
    k = KeyboardMemory()
    insert(k, DigitNode('1'))
    insert(k, DigitNode('2'))
    moveLeft(k)
    moveLeft(k)
    assert '▦12' == getEditModeLatex(k, UnitTestLatexConfiguration())
    selectRight(k)
    selectRight(k)
    assert r'\colorbox{blue}{12}' == getEditModeLatex(k, UnitTestLatexConfiguration())
    # Act
    deleteSelection(k)
    # Assert
    assert '▦' == getEditModeLatex(k, UnitTestLatexConfiguration())