from src import AscendingBranchingNode, DecimalSeparatorNode, DescendingBranchingNode, DigitNode, KeyboardMemory, MatrixNode, RoundBracketsNode, StandardBranchingNode, StandardLeafNode, delete_left, get_edit_mode_latex, insert, insert_with_encapsulate_current, insert_with_encapsulate_selection_and_previous, move_down, move_left, move_right, move_up, select_left
from tests._testhelpers.UnitTestLatexConfiguration import UnitTestLatexConfiguration


def test_can_also_be_used_to_delete_empty_Placeholders_in_some_cases__in_the_experience_of_the_user__x():
    # Arrange
    k = KeyboardMemory()
    insert(k, DigitNode('2'))
    insert(k, StandardLeafNode('x'))
    insert(k, StandardLeafNode('+'))   # oops, typo!
    insert_with_encapsulate_current(k, AscendingBranchingNode('', '^{', '}'))
    insert(k, DigitNode('3'))
    move_down(k)
    delete_left(k)
    # trying to fix typo
    assert '2x▦^{3}' == get_edit_mode_latex(k, UnitTestLatexConfiguration())
    move_up(k)
    assert '2x⬚^{3▦}' == get_edit_mode_latex(k, UnitTestLatexConfiguration())   # Huh? Let's delete that empty placeholder!
    move_down(k)
    assert '2x▦^{3}' == get_edit_mode_latex(k, UnitTestLatexConfiguration())
    # Act
    delete_left(k)
    move_up(k)
    # Assert
    assert '2x^{3▦}' == get_edit_mode_latex(k, UnitTestLatexConfiguration())


def test_can_also_be_used_to_delete_empty_Placeholders_in_some_cases__in_the_experience_of_the_user__1plus2point5():
    # Arrange
    k = KeyboardMemory()
    insert(k, DigitNode('1'))
    insert(k, StandardLeafNode('+'))
    insert(k, DigitNode('2'))
    insert(k, DecimalSeparatorNode())
    insert(k, DigitNode('5'))
    insert(k, StandardLeafNode('+'))   # oops, typo!
    insert_with_encapsulate_current(k, AscendingBranchingNode('', '^{', '}'))
    insert(k, DigitNode('3'))
    move_down(k)
    delete_left(k)   # trying to fix typo
    assert '1+2.5▦^{3}' == get_edit_mode_latex(k, UnitTestLatexConfiguration())
    move_up(k)
    assert '1+2.5⬚^{3▦}' == get_edit_mode_latex(k, UnitTestLatexConfiguration())   # Huh? Let's delete that empty placeholder!
    move_down(k)
    assert '1+2.5▦^{3}' == get_edit_mode_latex(k, UnitTestLatexConfiguration())
    # Act
    delete_left(k)
    move_up(k)
    # Assert
    assert '1+2.5^{3▦}' == get_edit_mode_latex(k, UnitTestLatexConfiguration())


def test_can_also_be_used_to_delete_empty_Placeholders_in_some_cases__in_the_experience_of_the_user__2point5():
    # Arrange
    k = KeyboardMemory()
    insert(k, DigitNode('2'))
    insert(k, DecimalSeparatorNode())
    insert(k, DigitNode('5'))
    insert(k, StandardLeafNode('+'))   # oops, typo!
    insert_with_encapsulate_current(k, AscendingBranchingNode('', '^{', '}'))
    insert(k, DigitNode('3'))
    move_down(k)
    delete_left(k)   # trying to fix typo
    assert '2.5▦^{3}' == get_edit_mode_latex(k, UnitTestLatexConfiguration())
    move_up(k)
    assert '2.5⬚^{3▦}' == get_edit_mode_latex(k, UnitTestLatexConfiguration())   # Huh? Let's delete that empty placeholder!
    move_down(k)
    assert '2.5▦^{3}' == get_edit_mode_latex(k, UnitTestLatexConfiguration())
    # Act
    delete_left(k)
    move_up(k)
    # Assert
    assert '2.5^{3▦}' == get_edit_mode_latex(k, UnitTestLatexConfiguration())


def test_does_nothing_sometimes():
    # Arrange
    k = KeyboardMemory()
    insert(k, MatrixNode('pmatrix', 2, 2))
    move_down(k)
    insert(k, DigitNode('3'))
    move_up(k)
    move_right(k)
    assert r'\begin{pmatrix}⬚ & ▦ \\ 3 & ⬚\end{pmatrix}' == get_edit_mode_latex(k, UnitTestLatexConfiguration())
    # Act
    delete_left(k)
    # Assert
    assert r'\begin{pmatrix}⬚ & ▦ \\ 3 & ⬚\end{pmatrix}' == get_edit_mode_latex(k, UnitTestLatexConfiguration())


def test_deletes_the_last_TreeNodes_from_the_previous_Placeholders():
    # Arrange
    k = KeyboardMemory()
    insert(k, MatrixNode('pmatrix', 2, 2))
    insert(k, DigitNode('1'))
    insert(k, DigitNode('2'))
    move_right(k)
    assert r'\begin{pmatrix}12 & ▦ \\ ⬚ & ⬚\end{pmatrix}' == get_edit_mode_latex(k, UnitTestLatexConfiguration())
    # Act
    delete_left(k)
    # Assert
    assert r'\begin{pmatrix}1▦ & ⬚ \\ ⬚ & ⬚\end{pmatrix}' == get_edit_mode_latex(k, UnitTestLatexConfiguration())


def test_can_revert_insertWithEncapsulateCurrent_sometimes__execution_path_with_multiple_digits_treated_as_a_single_thing():
    # Arrange
    k = KeyboardMemory()
    insert(k, DigitNode('2'))
    power_node = AscendingBranchingNode('', '^{', '}')
    insert_with_encapsulate_current(k, power_node)
    d3 = DigitNode('3')
    insert(k, d3)
    insert_with_encapsulate_current(k, AscendingBranchingNode('', '^{', '}'))
    assert '2^{3^{▦}}' == get_edit_mode_latex(k, UnitTestLatexConfiguration())
    # Act & assert
    delete_left(k)
    assert '2^{3▦}' == get_edit_mode_latex(k, UnitTestLatexConfiguration())
    assert d3.parent_placeholder == power_node.placeholders[1]
    delete_left(k)
    assert '2^{▦}' == get_edit_mode_latex(k, UnitTestLatexConfiguration())


def test_can_delete_from_the_first_placeholder_of_a_BranchingNode():
    # Arrange
    k = KeyboardMemory()
    insert(k, DescendingBranchingNode(r'\frac{', '}{', '}'))
    insert(k, DigitNode('1'))
    insert(k, DigitNode('2'))
    assert r'\frac{12▦}{⬚}' == get_edit_mode_latex(k, UnitTestLatexConfiguration())
    # Act
    delete_left(k)
    # Assert
    assert r'\frac{1▦}{⬚}' == get_edit_mode_latex(k, UnitTestLatexConfiguration())


def test_can_revert_raising_selection_to_the_power_of_an_empty_Placeholder():
    # Arrange
    k = KeyboardMemory()
    insert(k, DigitNode('1'))
    insert(k, DigitNode('2'))
    assert '12▦' == get_edit_mode_latex(k, UnitTestLatexConfiguration())
    select_left(k)
    select_left(k)
    assert r'\colorbox{blue}{12}' == get_edit_mode_latex(k, UnitTestLatexConfiguration())
    insert_with_encapsulate_selection_and_previous(k, AscendingBranchingNode('', '^{', '}'))
    assert '⬚^{12▦}' == get_edit_mode_latex(k, UnitTestLatexConfiguration())
    move_down(k)
    assert '▦^{12}' == get_edit_mode_latex(k, UnitTestLatexConfiguration())
    # Act
    delete_left(k)
    # Assert
    assert '12▦' == get_edit_mode_latex(k, UnitTestLatexConfiguration())


def test_from_the_right_of_a_single_Placeholder_BranchingNode__Placeholder_contains_TreeNodes():
    # Arrange
    k = KeyboardMemory()
    insert(k, RoundBracketsNode('(', ')'))
    insert(k, DigitNode('1'))
    insert(k, StandardLeafNode('+'))
    insert(k, StandardLeafNode('x'))
    move_right(k)
    assert '(1+x)▦' == get_edit_mode_latex(k, UnitTestLatexConfiguration())
    # Act
    delete_left(k)
    # Assert
    assert '1+x▦' == get_edit_mode_latex(k, UnitTestLatexConfiguration())


def test_from_the_right_of_a_BranchingNode__last_Placeholder_contains_a_LeafNode():
    # Arrange
    k = KeyboardMemory()
    insert(k, DigitNode('1'))
    insert_with_encapsulate_current(k, DescendingBranchingNode(r'\frac{', '}{', '}'))
    insert(k, StandardLeafNode('x'))
    move_right(k)
    assert r'\frac{1}{x}▦' == get_edit_mode_latex(k, UnitTestLatexConfiguration())
    # Act
    delete_left(k)
    # Assert
    assert r'\frac{1}{▦}' == get_edit_mode_latex(k, UnitTestLatexConfiguration())


def test_from_the_right_of_a_BranchingNode__last_Placeholder_contains_nested_BranchingNodes():
    # Arrange
    k = KeyboardMemory()
    insert(k, DigitNode('1'))
    insert_with_encapsulate_current(k, DescendingBranchingNode(r'\frac{', '}{', '}'))
    insert(k, DigitNode('1'))
    insert_with_encapsulate_current(k, DescendingBranchingNode(r'\frac{', '}{', '}'))
    insert(k, DigitNode('1'))
    insert_with_encapsulate_current(k, DescendingBranchingNode(r'\frac{', '}{', '}'))
    insert(k, StandardLeafNode('x'))
    move_right(k)
    move_right(k)
    move_right(k)
    assert r'\frac{1}{\frac{1}{\frac{1}{x}}}▦' == get_edit_mode_latex(k, UnitTestLatexConfiguration())
    # Act
    delete_left(k)
    # Assert
    assert r'\frac{1}{\frac{1}{\frac{1}{▦}}}' == get_edit_mode_latex(k, UnitTestLatexConfiguration())


def test_from_the_right_of_a_BranchingNode__last_Placeholder_is_empty_and_first_Placeholder_contains_1_LeafNode():
    # Arrange
    k = KeyboardMemory()
    insert(k, DigitNode('1'))
    insert_with_encapsulate_current(k, DescendingBranchingNode(r'\frac{', '}{', '}'))
    move_right(k)
    move_right(k)
    assert r'\frac{1}{⬚}▦' == get_edit_mode_latex(k, UnitTestLatexConfiguration())
    # Act
    delete_left(k)
    # Assert
    assert '1▦' == get_edit_mode_latex(k, UnitTestLatexConfiguration())


def test_deletes_a_subscript__a_BranchingNode__with_two_Placeholders__from_its_empty_Placeholder():
    # Arrange
    k = KeyboardMemory()
    insert(k, DigitNode('1'))
    insert(k, DigitNode('2'))
    insert_with_encapsulate_current(k, DescendingBranchingNode('', '_{', '}'))
    assert '12_{▦}' == get_edit_mode_latex(k, UnitTestLatexConfiguration())
    # Act
    delete_left(k)
    # Assert
    assert '12▦' == get_edit_mode_latex(k, UnitTestLatexConfiguration())


def test_deletes_a_subscript__a_BranchingNode__with_two_Placeholders__from_the_right():
    # Arrange
    k = KeyboardMemory()
    insert(k, DigitNode('1'))
    insert(k, DigitNode('2'))
    insert_with_encapsulate_current(k, DescendingBranchingNode('', '_{', '}'))
    move_right(k)
    assert '12_{⬚}▦' == get_edit_mode_latex(k, UnitTestLatexConfiguration())
    # Act
    delete_left(k)
    # Assert
    assert '12▦' == get_edit_mode_latex(k, UnitTestLatexConfiguration())


def test_deletes_a_subscript__a_BranchingNode__with_two_Placeholders__from_the_right__case_with_a_BranchingNode_on_the_right():
    # Arrange
    k = KeyboardMemory()
    insert(k, DigitNode('1'))
    insert(k, DigitNode('2'))
    insert_with_encapsulate_current(k, DescendingBranchingNode('', '_{', '}'))
    move_right(k)
    insert(k, StandardBranchingNode(r'\sqrt{', '}'))
    move_left(k)
    assert r'12_{⬚}▦\sqrt{⬚}' == get_edit_mode_latex(k, UnitTestLatexConfiguration())
    # Act
    delete_left(k)
    # Assert
    assert r'12▦\sqrt{⬚}' == get_edit_mode_latex(k, UnitTestLatexConfiguration())


def test_deletes_a_single_column_matrix__or_any_BranchingNode__from_the_right_if_the_only_non_empty_Placeholder_is_at_index_0():
    # Arrange
    k = KeyboardMemory()
    insert(k, MatrixNode('pmatrix', 1, 3))
    insert(k, DigitNode('1'))
    insert(k, DigitNode('2'))
    move_down(k)
    move_right(k)
    move_right(k)
    assert r'\begin{pmatrix}12 \\ ⬚ \\ ⬚\end{pmatrix}▦' == get_edit_mode_latex(k, UnitTestLatexConfiguration())
    # Act
    delete_left(k)
    # Assert
    assert '12▦' == get_edit_mode_latex(k, UnitTestLatexConfiguration())


def test_deletes_a_fraction__a_BranchingNode_with_two_Placeholders__from_its_second_Placeholder__case_with_a_BranchingNode_on_the_right():
    # Arrange
    k = KeyboardMemory()
    insert(k, DescendingBranchingNode(r'\frac{', '}{', '}'))
    insert(k, StandardLeafNode('a'))
    insert(k, StandardLeafNode('b'))
    move_down(k)
    move_right(k)
    insert(k, StandardBranchingNode(r'\sqrt{', '}'))
    move_left(k)
    move_left(k)
    assert r'\frac{ab}{▦}\sqrt{⬚}' == get_edit_mode_latex(k, UnitTestLatexConfiguration())
    # Act
    delete_left(k)
    # Assert
    assert r'ab▦\sqrt{⬚}' == get_edit_mode_latex(k, UnitTestLatexConfiguration())


def test_deletes_the_last_TreeNode_of_the_last_Placeholder_with_content():
    # Arrange
    k = KeyboardMemory()
    insert(k, MatrixNode('pmatrix', 2, 2))
    insert(k, DigitNode('1'))
    insert(k, DigitNode('2'))
    move_down(k)
    insert(k, DigitNode('3'))
    insert(k, DigitNode('4'))
    move_right(k)
    move_right(k)
    assert r'\begin{pmatrix}12 & ⬚ \\ 34 & ⬚\end{pmatrix}▦' == get_edit_mode_latex(k, UnitTestLatexConfiguration())
    # Act & Assert
    delete_left(k)
    assert r'\begin{pmatrix}12 & ⬚ \\ 3▦ & ⬚\end{pmatrix}' == get_edit_mode_latex(k, UnitTestLatexConfiguration())
    delete_left(k)
    assert r'\begin{pmatrix}12 & ⬚ \\ ▦ & ⬚\end{pmatrix}' == get_edit_mode_latex(k, UnitTestLatexConfiguration())
    delete_left(k)
    assert r'\begin{pmatrix}1▦ & ⬚ \\ ⬚ & ⬚\end{pmatrix}' == get_edit_mode_latex(k, UnitTestLatexConfiguration())


def test_does_nothing_from_the_first_Placeholder_if_multiple_sibling_Placeholders_are_filled():
    # Arrange
    k = KeyboardMemory()
    insert(k, MatrixNode('pmatrix', 2, 2))
    move_right(k)
    insert(k, DigitNode('2'))
    move_down(k)
    assert r'\begin{pmatrix}⬚ & 2 \\ ⬚ & ▦\end{pmatrix}' == get_edit_mode_latex(k, UnitTestLatexConfiguration())
    insert(k, DigitNode('4'))
    move_left(k)
    move_left(k)
    move_up(k)
    assert r'\begin{pmatrix}▦ & 2 \\ ⬚ & 4\end{pmatrix}' == get_edit_mode_latex(k, UnitTestLatexConfiguration())
    # Act
    delete_left(k)
    # Assert
    assert r'\begin{pmatrix}▦ & 2 \\ ⬚ & 4\end{pmatrix}' == get_edit_mode_latex(k, UnitTestLatexConfiguration())


def test_deletes_a_BranchingNode_from_one_of_its_Placeholders__sets_current_at_the_previous_TreeNode():
    # Arrange
    k = KeyboardMemory()
    insert(k, DigitNode('2'))
    insert(k, StandardLeafNode(r'\times'))
    insert(k, MatrixNode('pmatrix', 2, 2))
    assert r'2\times\begin{pmatrix}▦ & ⬚ \\ ⬚ & ⬚\end{pmatrix}' == get_edit_mode_latex(k, UnitTestLatexConfiguration())
    # Act
    delete_left(k)
    # Assert
    assert r'2\times▦' == get_edit_mode_latex(k, UnitTestLatexConfiguration())
