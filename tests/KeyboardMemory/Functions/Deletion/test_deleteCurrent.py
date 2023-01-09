from src import AscendingBranchingNode, DecimalSeparatorNode, deleteCurrent, DescendingBranchingNode, DigitNode, KeyboardMemory, getEditModeLatex, insert, insertWithEncapsulateCurrent, insertWithEncapsulateSelectionAndPrevious, MatrixNode, moveDown, moveLeft, moveRight, moveUp, RoundBracketsNode, selectLeft, StandardBranchingNode, StandardLeafNode
from tests.testhelpers.UnitTestLatexConfiguration import UnitTestLatexConfiguration

def test_can_also_be_used_to_delete_empty_Placeholders_in_some_cases__in_the_experience_of_the_user__x():
    # Arrange
    k = KeyboardMemory()
    insert(k, DigitNode('2'))
    insert(k, StandardLeafNode('x'))
    insert(k, StandardLeafNode('+')) # oops, typo!
    insertWithEncapsulateCurrent(k, AscendingBranchingNode('', '^{', '}'))
    insert(k, DigitNode('3'))
    moveDown(k)
    deleteCurrent(k); # trying to fix typo
    assert '2x▦^{3}' == getEditModeLatex(k, UnitTestLatexConfiguration())
    moveUp(k)
    assert '2x⬚^{3▦}' == getEditModeLatex(k, UnitTestLatexConfiguration()) # Huh? Let's delete that empty placeholder!
    moveDown(k)
    assert '2x▦^{3}' == getEditModeLatex(k, UnitTestLatexConfiguration())
    # Act
    deleteCurrent(k)
    moveUp(k)
    # Assert
    assert '2x^{3▦}' == getEditModeLatex(k, UnitTestLatexConfiguration())

def test_can_also_be_used_to_delete_empty_Placeholders_in_some_cases__in_the_experience_of_the_user__1plus2point5():
    # Arrange
    k = KeyboardMemory()
    insert(k, DigitNode('1'))
    insert(k, StandardLeafNode('+'))
    insert(k, DigitNode('2'))
    insert(k, DecimalSeparatorNode())
    insert(k, DigitNode('5'))
    insert(k, StandardLeafNode('+')) # oops, typo!
    insertWithEncapsulateCurrent(k, AscendingBranchingNode('', '^{', '}'))
    insert(k, DigitNode('3'))
    moveDown(k)
    deleteCurrent(k) # trying to fix typo
    assert '1+2.5▦^{3}' == getEditModeLatex(k, UnitTestLatexConfiguration())
    moveUp(k)
    assert '1+2.5⬚^{3▦}' == getEditModeLatex(k, UnitTestLatexConfiguration()) # Huh? Let's delete that empty placeholder!
    moveDown(k)
    assert '1+2.5▦^{3}' == getEditModeLatex(k, UnitTestLatexConfiguration())
    # Act
    deleteCurrent(k)
    moveUp(k)
    # Assert
    assert '1+2.5^{3▦}' == getEditModeLatex(k, UnitTestLatexConfiguration())

def test_can_also_be_used_to_delete_empty_Placeholders_in_some_cases__in_the_experience_of_the_user__2point5():
    # Arrange
    k = KeyboardMemory()
    insert(k, DigitNode('2'))
    insert(k, DecimalSeparatorNode())
    insert(k, DigitNode('5'))
    insert(k, StandardLeafNode('+')) # oops, typo!
    insertWithEncapsulateCurrent(k, AscendingBranchingNode('', '^{', '}'))
    insert(k, DigitNode('3'))
    moveDown(k)
    deleteCurrent(k) # trying to fix typo
    assert '2.5▦^{3}' == getEditModeLatex(k, UnitTestLatexConfiguration())
    moveUp(k)
    assert '2.5⬚^{3▦}' == getEditModeLatex(k, UnitTestLatexConfiguration()) # Huh? Let's delete that empty placeholder!
    moveDown(k)
    assert '2.5▦^{3}' == getEditModeLatex(k, UnitTestLatexConfiguration())
    # Act
    deleteCurrent(k)
    moveUp(k)
    # Assert
    assert '2.5^{3▦}' == getEditModeLatex(k, UnitTestLatexConfiguration())

def test_does_nothing_sometimes():
    # Arrange
    k = KeyboardMemory()
    insert(k, MatrixNode('pmatrix', 2, 2))
    moveDown(k)
    insert(k, DigitNode('3'))
    moveUp(k)
    moveRight(k)
    assert r'\begin{pmatrix}⬚ & ▦ \\ 3 & ⬚\end{pmatrix}' == getEditModeLatex(k, UnitTestLatexConfiguration())
    # Act
    deleteCurrent(k)
    # Assert
    assert r'\begin{pmatrix}⬚ & ▦ \\ 3 & ⬚\end{pmatrix}' == getEditModeLatex(k, UnitTestLatexConfiguration())

def test_deletes_the_last_TreeNodes_from_the_previous_Placeholders():
    # Arrange
    k = KeyboardMemory()
    insert(k, MatrixNode('pmatrix', 2, 2))
    insert(k, DigitNode('1'))
    insert(k, DigitNode('2'))
    moveRight(k)
    assert r'\begin{pmatrix}12 & ▦ \\ ⬚ & ⬚\end{pmatrix}' == getEditModeLatex(k, UnitTestLatexConfiguration())
    # Act
    deleteCurrent(k)
    # Assert
    assert r'\begin{pmatrix}1▦ & ⬚ \\ ⬚ & ⬚\end{pmatrix}' == getEditModeLatex(k, UnitTestLatexConfiguration())

def test_can_revert_insertWithEncapsulateCurrent_sometimes__execution_path_with_multiple_digits_treated_as_a_single_thing():
    # Arrange
    k = KeyboardMemory()
    insert(k, DigitNode('2'))
    powerNode = AscendingBranchingNode('', '^{', '}')
    insertWithEncapsulateCurrent(k, powerNode)
    d3 = DigitNode('3')
    insert(k, d3)
    insertWithEncapsulateCurrent(k, AscendingBranchingNode('', '^{', '}'))
    assert '2^{3^{▦}}' == getEditModeLatex(k, UnitTestLatexConfiguration())
    # Act & assert
    deleteCurrent(k)
    assert '2^{3▦}' == getEditModeLatex(k, UnitTestLatexConfiguration())
    assert d3.parentPlaceholder == powerNode.placeholders[1]
    deleteCurrent(k)
    assert '2^{▦}' == getEditModeLatex(k, UnitTestLatexConfiguration())

def test_can_delete_from_the_first_placeholder_of_a_BranchingNode():
    # Arrange
    k = KeyboardMemory()
    insert(k, DescendingBranchingNode(r'\frac{', '}{', '}'))
    insert(k, DigitNode('1'))
    insert(k, DigitNode('2'))
    assert r'\frac{12▦}{⬚}' == getEditModeLatex(k, UnitTestLatexConfiguration())
    # Act
    deleteCurrent(k)
    # Assert
    assert r'\frac{1▦}{⬚}' == getEditModeLatex(k, UnitTestLatexConfiguration())

def test_can_revert_raising_selection_to_the_power_of_an_empty_Placeholder():
    # Arrange
    k = KeyboardMemory()
    insert(k, DigitNode('1'))
    insert(k, DigitNode('2'))
    assert '12▦' == getEditModeLatex(k, UnitTestLatexConfiguration())
    selectLeft(k)
    selectLeft(k)
    assert r'\colorbox{blue}{12}' == getEditModeLatex(k, UnitTestLatexConfiguration())
    insertWithEncapsulateSelectionAndPrevious(k, AscendingBranchingNode('', '^{', '}'))
    assert '⬚^{12▦}' == getEditModeLatex(k, UnitTestLatexConfiguration())
    moveDown(k)
    assert '▦^{12}' == getEditModeLatex(k, UnitTestLatexConfiguration())
    # Act
    deleteCurrent(k)
    # Assert
    assert '12▦' == getEditModeLatex(k, UnitTestLatexConfiguration())

def test_from_the_right_of_a_single_Placeholder_BranchingNode__Placeholder_contains_TreeNodes():
    # Arrange
    k = KeyboardMemory()
    insert(k, RoundBracketsNode('(', ')'))
    insert(k, DigitNode('1'))
    insert(k, StandardLeafNode('+'))
    insert(k, StandardLeafNode('x'))
    moveRight(k)
    assert '(1+x)▦' == getEditModeLatex(k, UnitTestLatexConfiguration())
    # Act
    deleteCurrent(k)
    # Assert
    assert '1+x▦' == getEditModeLatex(k, UnitTestLatexConfiguration())

def test_from_the_right_of_a_BranchingNode__last_Placeholder_contains_a_LeafNode():
    # Arrange
    k = KeyboardMemory()
    insert(k, DigitNode('1'))
    insertWithEncapsulateCurrent(k, DescendingBranchingNode(r'\frac{', '}{', '}'))
    insert(k, StandardLeafNode('x'))
    moveRight(k)
    assert r'\frac{1}{x}▦' == getEditModeLatex(k, UnitTestLatexConfiguration())
    # Act
    deleteCurrent(k)
    # Assert
    assert r'\frac{1}{▦}' == getEditModeLatex(k, UnitTestLatexConfiguration())

def test_from_the_right_of_a_BranchingNode__last_Placeholder_contains_nested_BranchingNodes():
    # Arrange
    k = KeyboardMemory()
    insert(k, DigitNode('1'))
    insertWithEncapsulateCurrent(k, DescendingBranchingNode(r'\frac{', '}{', '}'))
    insert(k, DigitNode('1'))
    insertWithEncapsulateCurrent(k, DescendingBranchingNode(r'\frac{', '}{', '}'))
    insert(k, DigitNode('1'))
    insertWithEncapsulateCurrent(k, DescendingBranchingNode(r'\frac{', '}{', '}'))
    insert(k, StandardLeafNode('x'))
    moveRight(k)
    moveRight(k)
    moveRight(k)
    assert r'\frac{1}{\frac{1}{\frac{1}{x}}}▦' == getEditModeLatex(k, UnitTestLatexConfiguration())
    # Act
    deleteCurrent(k)
    # Assert
    assert r'\frac{1}{\frac{1}{\frac{1}{▦}}}' == getEditModeLatex(k, UnitTestLatexConfiguration())

def test_from_the_right_of_a_BranchingNode__last_Placeholder_is_empty_and_first_Placeholder_contains_1_LeafNode():
    # Arrange
    k = KeyboardMemory()
    insert(k, DigitNode('1'))
    insertWithEncapsulateCurrent(k, DescendingBranchingNode(r'\frac{', '}{', '}'))
    moveRight(k)
    moveRight(k)
    assert r'\frac{1}{⬚}▦' == getEditModeLatex(k, UnitTestLatexConfiguration())
    # Act
    deleteCurrent(k)
    # Assert
    assert '1▦' == getEditModeLatex(k, UnitTestLatexConfiguration())

def test_deletes_a_subscript__a_BranchingNode__with_two_Placeholders__from_its_empty_Placeholder():
    # Arrange
    k = KeyboardMemory()
    insert(k, DigitNode('1'))
    insert(k, DigitNode('2'))
    insertWithEncapsulateCurrent(k, DescendingBranchingNode('', '_{', '}'))
    assert '12_{▦}' == getEditModeLatex(k, UnitTestLatexConfiguration())
    # Act
    deleteCurrent(k)
    # Assert
    assert '12▦' == getEditModeLatex(k, UnitTestLatexConfiguration())

def test_deletes_a_subscript__a_BranchingNode__with_two_Placeholders__from_the_right():
    # Arrange
    k = KeyboardMemory()
    insert(k, DigitNode('1'))
    insert(k, DigitNode('2'))
    insertWithEncapsulateCurrent(k, DescendingBranchingNode('', '_{', '}'))
    moveRight(k)
    assert '12_{⬚}▦' == getEditModeLatex(k, UnitTestLatexConfiguration())
    # Act
    deleteCurrent(k)
    # Assert
    assert '12▦' == getEditModeLatex(k, UnitTestLatexConfiguration())

def test_deletes_a_subscript__a_BranchingNode__with_two_Placeholders__from_the_right__case_with_a_BranchingNode_on_the_right():
    # Arrange
    k = KeyboardMemory()
    insert(k, DigitNode('1'))
    insert(k, DigitNode('2'))
    insertWithEncapsulateCurrent(k, DescendingBranchingNode('', '_{', '}'))
    moveRight(k)
    insert(k, StandardBranchingNode(r'\sqrt{', '}'))
    moveLeft(k)
    assert r'12_{⬚}▦\sqrt{⬚}' == getEditModeLatex(k, UnitTestLatexConfiguration())
    # Act
    deleteCurrent(k)
    # Assert
    assert r'12▦\sqrt{⬚}' == getEditModeLatex(k, UnitTestLatexConfiguration())

def test_deletes_a_single_column_matrix__or_any_BranchingNode__from_the_right_if_the_only_non_empty_Placeholder_is_at_index_0():
    # Arrange
    k = KeyboardMemory()
    insert(k, MatrixNode('pmatrix', 1, 3))
    insert(k, DigitNode('1'))
    insert(k, DigitNode('2'))
    moveDown(k)
    moveRight(k)
    moveRight(k)
    assert r'\begin{pmatrix}12 \\ ⬚ \\ ⬚\end{pmatrix}▦' == getEditModeLatex(k, UnitTestLatexConfiguration())
    # Act
    deleteCurrent(k)
    # Assert
    assert '12▦' == getEditModeLatex(k, UnitTestLatexConfiguration())

def test_deletes_a_fraction__a_BranchingNode_with_two_Placeholders__from_its_second_Placeholder__case_with_a_BranchingNode_on_the_right():
    # Arrange
    k = KeyboardMemory()
    insert(k, DescendingBranchingNode(r'\frac{', '}{', '}'))
    insert(k, StandardLeafNode('a'))
    insert(k, StandardLeafNode('b'))
    moveDown(k)
    moveRight(k)
    insert(k, StandardBranchingNode(r'\sqrt{', '}'))
    moveLeft(k)
    moveLeft(k)
    assert r'\frac{ab}{▦}\sqrt{⬚}' == getEditModeLatex(k, UnitTestLatexConfiguration())
    # Act
    deleteCurrent(k)
    # Assert
    assert r'ab▦\sqrt{⬚}' == getEditModeLatex(k, UnitTestLatexConfiguration())

def test_deletes_the_last_TreeNode_of_the_last_Placeholder_with_content():
    # Arrange
    k = KeyboardMemory()
    insert(k, MatrixNode('pmatrix', 2, 2))
    insert(k, DigitNode('1'))
    insert(k, DigitNode('2'))
    moveDown(k)
    insert(k, DigitNode('3'))
    insert(k, DigitNode('4'))
    moveRight(k)
    moveRight(k)
    assert r'\begin{pmatrix}12 & ⬚ \\ 34 & ⬚\end{pmatrix}▦' == getEditModeLatex(k, UnitTestLatexConfiguration())
    # Act & Assert
    deleteCurrent(k)
    assert r'\begin{pmatrix}12 & ⬚ \\ 3▦ & ⬚\end{pmatrix}' == getEditModeLatex(k, UnitTestLatexConfiguration())
    deleteCurrent(k)
    assert r'\begin{pmatrix}12 & ⬚ \\ ▦ & ⬚\end{pmatrix}' == getEditModeLatex(k, UnitTestLatexConfiguration())
    deleteCurrent(k)
    assert r'\begin{pmatrix}1▦ & ⬚ \\ ⬚ & ⬚\end{pmatrix}' == getEditModeLatex(k, UnitTestLatexConfiguration())

def test_does_nothing_from_the_first_Placeholder_if_multiple_sibling_Placeholders_are_filled():
    # Arrange
    k = KeyboardMemory()
    insert(k, MatrixNode('pmatrix', 2, 2))
    moveRight(k)
    insert(k, DigitNode('2'))
    moveDown(k)
    assert r'\begin{pmatrix}⬚ & 2 \\ ⬚ & ▦\end{pmatrix}' == getEditModeLatex(k, UnitTestLatexConfiguration())
    insert(k, DigitNode('4'))
    moveLeft(k)
    moveLeft(k)
    moveUp(k)
    assert r'\begin{pmatrix}▦ & 2 \\ ⬚ & 4\end{pmatrix}' == getEditModeLatex(k, UnitTestLatexConfiguration())
    # Act
    deleteCurrent(k)
    # Assert
    assert r'\begin{pmatrix}▦ & 2 \\ ⬚ & 4\end{pmatrix}' == getEditModeLatex(k, UnitTestLatexConfiguration())

#  it(`deletes a ${BranchingNode.name} from one of its ${Placeholder.name}s: sets ${nameof<KeyboardMemory>('current')} at (the right of) the previous ${TreeNode.name}`, () => {
def test_deletes_a_BranchingNode_from_one_of_its_Placeholders__sets_current_at_the_previous_TreeNode():
    # Arrange
    k = KeyboardMemory()
    insert(k, DigitNode('2'))
    insert(k, StandardLeafNode(r'\times'))
    insert(k, MatrixNode('pmatrix', 2, 2))
    assert r'2\times\begin{pmatrix}▦ & ⬚ \\ ⬚ & ⬚\end{pmatrix}' == getEditModeLatex(k, UnitTestLatexConfiguration())
    # Act
    deleteCurrent(k)
    # Assert
    assert r'2\times▦' == getEditModeLatex(k, UnitTestLatexConfiguration())