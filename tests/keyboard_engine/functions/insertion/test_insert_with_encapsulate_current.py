from src import AscendingBranchingNode, DecimalSeparatorNode, DescendingBranchingNode, DigitNode, KeyboardMemory, MatrixNode, Placeholder, RoundBracketsNode, StandardBranchingNode, StandardLeafNode, get_edit_mode_latex, insert, insert_with_encapsulate_current, move_right
from tests._testhelpers.UnitTestLatexConfiguration import UnitTestLatexConfiguration


def test_does_a_regular_insert_if_current_is_a_Placeholder():
    # Arrange
    k = KeyboardMemory()
    assert isinstance(k.current, Placeholder)
    assert '▦' == get_edit_mode_latex(k, UnitTestLatexConfiguration())
    # Act
    insert_with_encapsulate_current(k, AscendingBranchingNode('', '^{', '}'))
    # Assert
    assert '▦^{⬚}' == get_edit_mode_latex(k, UnitTestLatexConfiguration())


def test_can_encapsulate_complex_stuff_like_matrixes():
    # Arrange
    k = KeyboardMemory()
    insert(k, MatrixNode('pmatrix', 2, 2))
    for i in range(1, 5):
        insert(k, DigitNode(str(i)))
        move_right(k)
    # Act
    insert_with_encapsulate_current(k, DescendingBranchingNode(r'\frac{', '}{', '}'))
    # Assert
    assert r'\frac{\begin{pmatrix}1 & 2 \\ 3 & 4\end{pmatrix}}{▦}' == get_edit_mode_latex(k, UnitTestLatexConfiguration())


def test_can_also_be_used_inside__for_example__a_matrix():
    # Arrange
    k = KeyboardMemory()
    insert(k, MatrixNode('pmatrix', 2, 2))
    insert(k, DigitNode('2'))
    # Act
    insert_with_encapsulate_current(k, AscendingBranchingNode('', '^{', '}'))
    # Assert
    assert r'\begin{pmatrix}2^{▦} & ⬚ \\ ⬚ & ⬚\end{pmatrix}' == get_edit_mode_latex(k, UnitTestLatexConfiguration())


def test_can_encapsulate_multiple_digits():
    # Arrange
    k = KeyboardMemory()
    insert(k, DigitNode('1'))
    insert(k, DigitNode('2'))
    # Act
    insert_with_encapsulate_current(k, DescendingBranchingNode(r'\frac{', '}{', '}'))
    # Assert
    assert r'\frac{12}{▦}' == get_edit_mode_latex(k, UnitTestLatexConfiguration())


def test_can_encapsulate_a_decimal_number():
    # Arrange
    k = KeyboardMemory()
    insert(k, DigitNode('1'))
    insert(k, DigitNode('2'))
    insert(k, DecimalSeparatorNode())
    insert(k, DigitNode('3'))
    # Act
    insert_with_encapsulate_current(k, DescendingBranchingNode(r'\frac{', '}{', '}'))
    # Assert
    assert r'\frac{12.3}{▦}' == get_edit_mode_latex(k, UnitTestLatexConfiguration())


def test_does_not_encapsulate_more_than_it_should():
    # Arrange
    k = KeyboardMemory()
    insert(k, DigitNode('1'))
    insert(k, StandardLeafNode('+'))
    insert(k, DigitNode('2'))
    insert(k, DigitNode('3'))
    # Act
    insert_with_encapsulate_current(k, DescendingBranchingNode(r'\frac{', '}{', '}'))
    # Assert
    assert r'1+\frac{23}{▦}' == get_edit_mode_latex(k, UnitTestLatexConfiguration())


def test_can_encapsulate_round_brackets():
    # Arrange
    k = KeyboardMemory()
    insert(k, DigitNode('1'))
    insert(k, StandardLeafNode('+'))
    insert(k, RoundBracketsNode('(', ')'))
    insert(k, DigitNode('2'))
    insert(k, StandardLeafNode('+'))
    insert(k, DigitNode('3'))
    move_right(k)
    assert r'1+(2+3)▦' == get_edit_mode_latex(k, UnitTestLatexConfiguration())
    power_node = AscendingBranchingNode('', '^{', '}')
    # Act
    insert_with_encapsulate_current(k, power_node)
    # Assert
    assert r'1+(2+3)^{▦}' == get_edit_mode_latex(k, UnitTestLatexConfiguration())
    assert power_node.placeholders[0].get_latex(k, None) == '(2+3)'


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
    move_right(k)
    insert(k, RoundBracketsNode('(', ')'))
    insert(k, StandardLeafNode('x'))
    insert(k, StandardLeafNode('-'))
    insert(k, DigitNode('3'))
    move_right(k)
    move_right(k)
    assert r'1+((x+2)(x-3))▦' == get_edit_mode_latex(k, UnitTestLatexConfiguration())
    # Act
    insert_with_encapsulate_current(k, DescendingBranchingNode(r'\frac{', '}{', '}'), delete_outer_round_brackets_if_any=True)
    # Assert
    assert r'1+\frac{(x+2)(x-3)}{▦}' == get_edit_mode_latex(k, UnitTestLatexConfiguration())


def test_with_deleteOuterRoundBracketsIfAny__does_not_delete_square_brackets_during_encapsulation():
    # Arrange
    k = KeyboardMemory()
    insert(k, DigitNode('1'))
    insert(k, StandardLeafNode('+'))
    insert(k, StandardBranchingNode('|', '|'))
    insert(k, StandardLeafNode('x'))
    insert(k, StandardLeafNode('+'))
    insert(k, DigitNode('3'))
    move_right(k)
    # Act
    fraction = DescendingBranchingNode(r'\frac{', '}{', '}')
    insert_with_encapsulate_current(k, fraction, delete_outer_round_brackets_if_any=True)
    # Assert
    assert r'1+\frac{|x+3|}{▦}' == get_edit_mode_latex(k, UnitTestLatexConfiguration())
    assert fraction.placeholders[0].get_latex(k, None) == '|x+3|'


def test_with_deleteOuterRoundBracketsIfAny__encapsulation_by_single_placeholder_BranchingNode_sets_the_cursor_at_the_right_of__the_new_BranchingNode():
    # Arrange
    k = KeyboardMemory()
    insert(k, RoundBracketsNode('(', ')'))
    insert(k, StandardLeafNode('A'))
    insert(k, StandardLeafNode('B'))
    move_right(k)
    assert '(AB)▦' == get_edit_mode_latex(k, UnitTestLatexConfiguration())
    # Act
    insert_with_encapsulate_current(k, StandardBranchingNode(r'\overrightarrow{', '}'), delete_outer_round_brackets_if_any=True)
    # Assert
    assert r'\overrightarrow{AB}▦' == get_edit_mode_latex(k, UnitTestLatexConfiguration())
