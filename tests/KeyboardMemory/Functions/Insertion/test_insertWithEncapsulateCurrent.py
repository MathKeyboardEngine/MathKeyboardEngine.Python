from src import AscendingBranchingNode, DecimalSeparatorNode, DescendingBranchingNode, RoundBracketsNode, DigitNode, MatrixNode, Placeholder, KeyboardMemory, StandardLeafNode, StandardBranchingNode, getEditModeLatex, insertWithEncapsulateCurrent, insert, moveRight
from tests.testhelpers.UnitTestLatexConfiguration import UnitTestLatexConfiguration

def test_does_a_regular_insert_if_current_is_a_Placeholder():
    # Arrange
    k = KeyboardMemory()
    assert isinstance(k.current, Placeholder)
    assert '▦' == getEditModeLatex(k, UnitTestLatexConfiguration())
    # Act
    insertWithEncapsulateCurrent(k, AscendingBranchingNode('', '^{', '}'))
    # Assert
    assert '▦^{⬚}' == getEditModeLatex(k, UnitTestLatexConfiguration())

def test_can_encapsulate_complex_stuff_like_matrixes():
    # Arrange
    k = KeyboardMemory()
    insert(k, MatrixNode('pmatrix', 2, 2))
    for i in range(1, 5):
      insert(k, DigitNode(str(i)))
      moveRight(k)
    # Act
    insertWithEncapsulateCurrent(k, DescendingBranchingNode(r'\frac{', '}{', '}'))
    # Assert
    assert r'\frac{\begin{pmatrix}1 & 2 \\ 3 & 4\end{pmatrix}}{▦}' == getEditModeLatex(k, UnitTestLatexConfiguration())

def test_can_also_be_used_inside__for_example__a_matrix():
    # Arrange
    k = KeyboardMemory()
    insert(k, MatrixNode('pmatrix', 2, 2))
    insert(k, DigitNode('2'))
    # Act
    insertWithEncapsulateCurrent(k, AscendingBranchingNode('', '^{', '}'))
    # Assert
    assert r'\begin{pmatrix}2^{▦} & ⬚ \\ ⬚ & ⬚\end{pmatrix}' == getEditModeLatex(k, UnitTestLatexConfiguration())


def test_can_encapsulate_multiple_digits():
    # Arrange
    k = KeyboardMemory()
    insert(k, DigitNode('1'))
    insert(k, DigitNode('2'))
    # Act
    insertWithEncapsulateCurrent(k, DescendingBranchingNode(r'\frac{', '}{', '}'))
    # Assert
    assert r'\frac{12}{▦}' == getEditModeLatex(k, UnitTestLatexConfiguration())

def test_can_encapsulate_a_decimal_number():
    # Arrange
    k = KeyboardMemory()
    insert(k, DigitNode('1'))
    insert(k, DigitNode('2'))
    insert(k, DecimalSeparatorNode())
    insert(k, DigitNode('3'))
    # Act
    insertWithEncapsulateCurrent(k, DescendingBranchingNode(r'\frac{', '}{', '}'))
    # Assert
    assert r'\frac{12.3}{▦}' == getEditModeLatex(k, UnitTestLatexConfiguration())

def test_does_not_encapsulate_more_than_it_should():
    # Arrange
    k = KeyboardMemory()
    insert(k, DigitNode('1'))
    insert(k, StandardLeafNode('+'))
    insert(k, DigitNode('2'))
    insert(k, DigitNode('3'))
    # Act
    insertWithEncapsulateCurrent(k, DescendingBranchingNode(r'\frac{', '}{', '}'))
    # Assert
    assert r'1+\frac{23}{▦}'== getEditModeLatex(k, UnitTestLatexConfiguration())

def test_can_encapsulate_round_brackets():
    # Arrange
    k = KeyboardMemory()
    insert(k, DigitNode('1'))
    insert(k, StandardLeafNode('+'))
    insert(k, RoundBracketsNode('(', ')'))
    insert(k, DigitNode('2'))
    insert(k, StandardLeafNode('+'))
    insert(k, DigitNode('3'))
    moveRight(k)
    assert r'1+(2+3)▦' == getEditModeLatex(k, UnitTestLatexConfiguration())
    powerNode = AscendingBranchingNode('', '^{', '}')
    # Act
    insertWithEncapsulateCurrent(k, powerNode)
    # Assert
    assert r'1+(2+3)^{▦}' == getEditModeLatex(k, UnitTestLatexConfiguration())
    assert powerNode.placeholders[0].getLatex(k, None) == '(2+3)'

def test_with_deleteOuterRoundBracketsIfAny__deletes_outer_round_brackets_during_encapsulation():
    # Arrange
    k = KeyboardMemory()
    insert(k, DigitNode('1'))
    insert(k, StandardLeafNode('+'))
    insert(k, RoundBracketsNode('(', ')'))
    insert(k, RoundBracketsNode('(', ')'))
    insert(k, StandardLeafNode('x'))
    insert(k, StandardLeafNode('+'))
    insert(k, DigitNode('2'))
    moveRight(k)
    insert(k, RoundBracketsNode('(', ')'))
    insert(k, StandardLeafNode('x'))
    insert(k, StandardLeafNode('-'))
    insert(k, DigitNode('3'))
    moveRight(k)
    moveRight(k)
    assert r'1+((x+2)(x-3))▦' == getEditModeLatex(k, UnitTestLatexConfiguration())
    # Act
    insertWithEncapsulateCurrent(k, DescendingBranchingNode(r'\frac{', '}{', '}'), True)
    # Assert
    assert r'1+\frac{(x+2)(x-3)}{▦}' == getEditModeLatex(k, UnitTestLatexConfiguration())

def test_with_deleteOuterRoundBracketsIfAny__does_not_delete_square_brackets_during_encapsulation():
    # Arrange
    k = KeyboardMemory()
    insert(k, DigitNode('1'))
    insert(k, StandardLeafNode('+'))
    insert(k, StandardBranchingNode('|', '|'))
    insert(k, StandardLeafNode('x'))
    insert(k, StandardLeafNode('+'))
    insert(k, DigitNode('3'))
    moveRight(k)
    # Act
    fraction = DescendingBranchingNode(r'\frac{', '}{', '}')
    insertWithEncapsulateCurrent(k, fraction, True)
    # Assert
    assert r'1+\frac{|x+3|}{▦}' == getEditModeLatex(k, UnitTestLatexConfiguration())
    assert fraction.placeholders[0].getLatex(k, None) == '|x+3|'

def test_with_deleteOuterRoundBracketsIfAny__encapsulation_by_single_placeholder_BranchingNode_sets_the_cursor_at_the_right_of__the_new_BranchingNode():
    # Arrange
    k = KeyboardMemory()
    insert(k, RoundBracketsNode('(', ')'))
    insert(k, StandardLeafNode('A'))
    insert(k, StandardLeafNode('B'))
    moveRight(k)
    assert '(AB)▦' == getEditModeLatex(k, UnitTestLatexConfiguration())
    # Act
    insertWithEncapsulateCurrent(k, StandardBranchingNode(r'\overrightarrow{', '}'), True)
    # Assert
    assert r'\overrightarrow{AB}▦' == getEditModeLatex(k, UnitTestLatexConfiguration())