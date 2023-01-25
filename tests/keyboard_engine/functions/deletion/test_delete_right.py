from src import AscendingBranchingNode, DescendingBranchingNode, DigitNode, KeyboardMemory, MatrixNode, RoundBracketsNode, StandardBranchingNode, StandardLeafNode, delete_right, get_edit_mode_latex, insert, insert_with_encapsulate_current, move_down, move_left, move_right, move_up
from tests._testhelpers.UnitTestLatexConfiguration import UnitTestLatexConfiguration


def test_can_delete_an_empty_single_placeholder_branchingnode_from_its_placeholder():
    # Arrange
    k = KeyboardMemory()
    insert(k, StandardBranchingNode(r'\sqrt{', '}'))
    assert r'\sqrt{▦}' == get_edit_mode_latex(k, UnitTestLatexConfiguration())
    move_right(k)
    insert(k, DigitNode('1'))
    move_left(k)
    move_left(k)
    assert r'\sqrt{▦}1' == get_edit_mode_latex(k, UnitTestLatexConfiguration())
    # Act & assert
    delete_right(k)
    assert '▦1' == get_edit_mode_latex(k, UnitTestLatexConfiguration())
    delete_right(k)
    assert '▦' == get_edit_mode_latex(k, UnitTestLatexConfiguration())


def test_can_delete_an_empty_multi_placeholder_branchingnode_from_any_placeholder__case__first():
    # Arrange
    k = KeyboardMemory()
    insert(k, DescendingBranchingNode(r'\frac{', '}{', '}'))
    assert r'\frac{▦}{⬚}' == get_edit_mode_latex(k, UnitTestLatexConfiguration())
    move_right(k)
    move_right(k)
    insert(k, DigitNode('1'))
    move_left(k)
    move_left(k)
    move_left(k)
    assert r'\frac{▦}{⬚}1' == get_edit_mode_latex(k, UnitTestLatexConfiguration())
    # Act & assert
    delete_right(k)
    assert '▦1' == get_edit_mode_latex(k, UnitTestLatexConfiguration())
    delete_right(k)
    assert '▦' == get_edit_mode_latex(k, UnitTestLatexConfiguration())


def test_can_delete_an_empty_multi_placeholder_branchingnode_from_any_placeholder__case__last():
    # Arrange
    k = KeyboardMemory()
    insert(k, DescendingBranchingNode(r'\frac{', '}{', '}'))
    assert r'\frac{▦}{⬚}' == get_edit_mode_latex(k, UnitTestLatexConfiguration())
    move_right(k)
    move_right(k)
    insert(k, DigitNode('1'))
    move_left(k)
    move_left(k)
    assert r'\frac{⬚}{▦}1' == get_edit_mode_latex(k, UnitTestLatexConfiguration())
    # Act & assert
    delete_right(k)
    assert '▦1' == get_edit_mode_latex(k, UnitTestLatexConfiguration())
    delete_right(k)
    assert '▦' == get_edit_mode_latex(k, UnitTestLatexConfiguration())


def test_does_nothing_if_an_empty_syntaxTreeRoot_is_keyboardmemory_s_current():
    # Arrange
    k = KeyboardMemory()
    # Act
    delete_right(k)
    # Assert
    assert '▦' == get_edit_mode_latex(k, UnitTestLatexConfiguration())


def test_does_nothing_if_there_are_only_TreeNodes_on_the_left_instead_of_the_right():
    # Arrange
    k = KeyboardMemory()
    insert(k, DigitNode('1'))
    assert '1▦' == get_edit_mode_latex(k, UnitTestLatexConfiguration())
    # Act
    delete_right(k)
    # Assert
    assert '1▦' == get_edit_mode_latex(k, UnitTestLatexConfiguration())


def test_deletes_leafnodes_and_empty_branchingnodes_that_are_on_the_right_of_the_cursor__current_is_placeholder():
    # Arrange
    k = KeyboardMemory()
    insert(k, DigitNode('1'))
    insert(k, DigitNode('2'))
    insert(k, StandardBranchingNode(r'\sqrt{', '}'))
    move_right(k)
    insert(k, DescendingBranchingNode(r'\frac{', '}{', '}'))
    assert r'12\sqrt{⬚}\frac{▦}{⬚}' == get_edit_mode_latex(k, UnitTestLatexConfiguration())
    move_left(k)
    move_left(k)
    move_left(k)
    move_left(k)
    move_left(k)
    assert r'▦12\sqrt{⬚}\frac{⬚}{⬚}' == get_edit_mode_latex(k, UnitTestLatexConfiguration())
    # Act & assert
    delete_right(k)
    assert r'▦2\sqrt{⬚}\frac{⬚}{⬚}' == get_edit_mode_latex(k, UnitTestLatexConfiguration())
    delete_right(k)
    assert r'▦\sqrt{⬚}\frac{⬚}{⬚}' == get_edit_mode_latex(k, UnitTestLatexConfiguration())
    delete_right(k)
    assert r'▦\frac{⬚}{⬚}' == get_edit_mode_latex(k, UnitTestLatexConfiguration())
    delete_right(k)
    assert r'▦' == get_edit_mode_latex(k, UnitTestLatexConfiguration())


def test_deletes_leafnodes_and_empty_branchingnodes_that_are_on_the_right_of_the_cursor__current_is_treenode():
    # Arrange
    k = KeyboardMemory()
    insert(k, DigitNode('1'))
    insert(k, DigitNode('2'))
    insert(k, StandardBranchingNode(r'\sqrt{', '}'))
    move_right(k)
    insert(k, DescendingBranchingNode(r'\frac{', '}{', '}'))
    assert r'12\sqrt{⬚}\frac{▦}{⬚}' == get_edit_mode_latex(k, UnitTestLatexConfiguration())
    move_left(k)
    move_left(k)
    move_left(k)
    move_left(k)
    assert r'1▦2\sqrt{⬚}\frac{⬚}{⬚}' == get_edit_mode_latex(k, UnitTestLatexConfiguration())
    # Act & assert
    delete_right(k)
    assert r'1▦\sqrt{⬚}\frac{⬚}{⬚}' == get_edit_mode_latex(k, UnitTestLatexConfiguration())
    delete_right(k)
    assert r'1▦\frac{⬚}{⬚}' == get_edit_mode_latex(k, UnitTestLatexConfiguration())
    delete_right(k)
    assert r'1▦' == get_edit_mode_latex(k, UnitTestLatexConfiguration())


def test_deletes_non_empty_single_placeholder_branchingnodes_in_parts__current_is_placeholder():
    # Arrange
    k = KeyboardMemory()
    insert(k, StandardBranchingNode(r'\sqrt{', '}'))
    insert(k, DigitNode('1'))
    insert(k, StandardLeafNode('-'))
    insert(k, StandardLeafNode('x'))
    move_left(k)
    move_left(k)
    move_left(k)
    move_left(k)
    assert r'▦\sqrt{1-x}' == get_edit_mode_latex(k, UnitTestLatexConfiguration())
    # Act & assert
    delete_right(k)
    assert r'▦1-x' == get_edit_mode_latex(k, UnitTestLatexConfiguration())
    delete_right(k)
    assert r'▦-x' == get_edit_mode_latex(k, UnitTestLatexConfiguration())
    delete_right(k)
    assert r'▦x' == get_edit_mode_latex(k, UnitTestLatexConfiguration())
    delete_right(k)
    assert '▦' == get_edit_mode_latex(k, UnitTestLatexConfiguration())


def test_deletes_non_empty_single_placeholder_branchingnodes_in_parts__current_is_treenode():
    # Arrange
    k = KeyboardMemory()
    insert(k, DigitNode('7'))
    insert(k, StandardBranchingNode(r'\sqrt{', '}'))
    insert(k, DigitNode('1'))
    insert(k, StandardLeafNode('-'))
    insert(k, StandardLeafNode('x'))
    move_left(k)
    move_left(k)
    move_left(k)
    move_left(k)
    assert r'7▦\sqrt{1-x}' == get_edit_mode_latex(k, UnitTestLatexConfiguration())
    # Act & assert
    delete_right(k)
    assert r'7▦1-x' == get_edit_mode_latex(k, UnitTestLatexConfiguration())
    delete_right(k)
    assert r'7▦-x' == get_edit_mode_latex(k, UnitTestLatexConfiguration())
    delete_right(k)
    assert r'7▦x' == get_edit_mode_latex(k, UnitTestLatexConfiguration())
    delete_right(k)
    assert '7▦' == get_edit_mode_latex(k, UnitTestLatexConfiguration())


def test_steps_into_complex_branchingnodes__current_is_treenode():
    # Arrange
    k = KeyboardMemory()
    insert(k, DigitNode('7'))
    insert(k, RoundBracketsNode('(', ')'))
    insert(k, DigitNode('1'))
    insert(k, StandardLeafNode('-'))
    insert(k, StandardLeafNode('x'))
    move_right(k)
    insert_with_encapsulate_current(k, AscendingBranchingNode('', '^{', '}'))
    insert(k, DigitNode('2'))
    move_left(k)
    move_left(k)
    move_left(k)
    move_left(k)
    move_left(k)
    move_left(k)
    move_left(k)
    assert r'7▦(1-x)^{2}' == get_edit_mode_latex(k, UnitTestLatexConfiguration())
    # Act & assert
    delete_right(k)
    assert '7▦1-x^{2}' == get_edit_mode_latex(k, UnitTestLatexConfiguration())
    delete_right(k)
    assert '7▦-x^{2}' == get_edit_mode_latex(k, UnitTestLatexConfiguration())
    delete_right(k)
    assert '7▦x^{2}' == get_edit_mode_latex(k, UnitTestLatexConfiguration())
    delete_right(k)
    assert '7▦^{2}' == get_edit_mode_latex(k, UnitTestLatexConfiguration())
    delete_right(k)
    assert '7▦2' == get_edit_mode_latex(k, UnitTestLatexConfiguration())
    delete_right(k)
    assert '7▦' == get_edit_mode_latex(k, UnitTestLatexConfiguration())


def test_steps_into_complex_branchingnodes__current_is_placeholder():
    # Arrange
    k = KeyboardMemory()
    insert(k, RoundBracketsNode('(', ')'))
    insert(k, DigitNode('1'))
    insert(k, StandardLeafNode('-'))
    insert(k, StandardLeafNode('x'))
    move_right(k)
    insert_with_encapsulate_current(k, AscendingBranchingNode('', '^{', '}'))
    insert(k, DigitNode('2'))
    move_left(k)
    move_left(k)
    move_left(k)
    move_left(k)
    move_left(k)
    move_left(k)
    move_left(k)
    assert r'▦(1-x)^{2}' == get_edit_mode_latex(k, UnitTestLatexConfiguration())
    # Act & assert
    delete_right(k)
    assert '▦1-x^{2}' == get_edit_mode_latex(k, UnitTestLatexConfiguration())
    delete_right(k)
    assert '▦-x^{2}' == get_edit_mode_latex(k, UnitTestLatexConfiguration())
    delete_right(k)
    assert '▦x^{2}' == get_edit_mode_latex(k, UnitTestLatexConfiguration())
    delete_right(k)
    assert '▦^{2}' == get_edit_mode_latex(k, UnitTestLatexConfiguration())
    delete_right(k)
    assert '▦2' == get_edit_mode_latex(k, UnitTestLatexConfiguration())
    delete_right(k)
    assert '▦' == get_edit_mode_latex(k, UnitTestLatexConfiguration())


def test_can_delete_a_matrixnode_with_content_gaps():
    # Arrange
    k = KeyboardMemory()
    insert(k, MatrixNode('pmatrix', 2, 2))
    move_right(k)
    insert(k, DigitNode('1'))
    move_down(k)
    insert(k, StandardBranchingNode(r'\sqrt{', '}'))
    assert r'\begin{pmatrix}⬚ & 1 \\ ⬚ & \sqrt{▦}\end{pmatrix}' == get_edit_mode_latex(k, UnitTestLatexConfiguration())
    move_up(k)
    move_left(k)
    move_left(k)
    move_left(k)
    assert r'▦\begin{pmatrix}⬚ & 1 \\ ⬚ & \sqrt{⬚}\end{pmatrix}' == get_edit_mode_latex(k, UnitTestLatexConfiguration())
    # Act & assert
    delete_right(k)
    assert r'\begin{pmatrix}⬚ & ▦ \\ ⬚ & \sqrt{⬚}\end{pmatrix}' == get_edit_mode_latex(k, UnitTestLatexConfiguration())
    delete_right(k)
    assert r'\begin{pmatrix}⬚ & ⬚ \\ ⬚ & ▦\end{pmatrix}' == get_edit_mode_latex(k, UnitTestLatexConfiguration())
    delete_right(k)
    assert '▦' == get_edit_mode_latex(k, UnitTestLatexConfiguration())


def test_can_delete_a_matrixnode_with_full_content():
    # Arrange
    k = KeyboardMemory()
    insert(k, MatrixNode('pmatrix', 2, 2))
    insert(k, DigitNode('1'))
    move_right(k)
    insert(k, DigitNode('2'))
    move_right(k)
    insert(k, DigitNode('3'))
    move_right(k)
    insert(k, DigitNode('4'))
    assert r'\begin{pmatrix}1 & 2 \\ 3 & 4▦\end{pmatrix}' == get_edit_mode_latex(k, UnitTestLatexConfiguration())
    move_up(k)
    move_left(k)
    move_left(k)
    move_left(k)
    move_left(k)
    assert r'▦\begin{pmatrix}1 & 2 \\ 3 & 4\end{pmatrix}' == get_edit_mode_latex(k, UnitTestLatexConfiguration())
    # Act & assert
    delete_right(k)
    assert r'\begin{pmatrix}▦ & 2 \\ 3 & 4\end{pmatrix}' == get_edit_mode_latex(k, UnitTestLatexConfiguration())
    delete_right(k)
    assert r'\begin{pmatrix}⬚ & ▦ \\ 3 & 4\end{pmatrix}' == get_edit_mode_latex(k, UnitTestLatexConfiguration())
    delete_right(k)
    assert r'\begin{pmatrix}⬚ & ⬚ \\ ▦ & 4\end{pmatrix}' == get_edit_mode_latex(k, UnitTestLatexConfiguration())
    delete_right(k)
    assert r'\begin{pmatrix}⬚ & ⬚ \\ ⬚ & ▦\end{pmatrix}' == get_edit_mode_latex(k, UnitTestLatexConfiguration())
    delete_right(k)
    assert '▦' == get_edit_mode_latex(k, UnitTestLatexConfiguration())


def test_lets_the_cursor_pull_exponents_and_subscripts_towards_itself():
    # Arrange
    k = KeyboardMemory()
    insert(k, AscendingBranchingNode('', '^{', '}'))
    move_right(k)
    insert(k, DigitNode('2'))
    move_left(k)
    move_left(k)
    move_left(k)
    assert r'▦⬚^{2}' == get_edit_mode_latex(k, UnitTestLatexConfiguration())
    # Act & assert
    delete_right(k)
    assert r'▦2' == get_edit_mode_latex(k, UnitTestLatexConfiguration())
    delete_right(k)
    assert r'▦' == get_edit_mode_latex(k, UnitTestLatexConfiguration())
