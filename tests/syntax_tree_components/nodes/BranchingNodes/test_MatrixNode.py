import pytest

from src import DigitNode, KeyboardMemory, MatrixNode, Placeholder, delete_left, get_edit_mode_latex, insert, move_down, move_left, move_right, move_up
from tests._testhelpers.UnitTestLatexConfiguration import UnitTestLatexConfiguration


def test_pmatrix_width2_height__1_right_2_down_4_down_6():
    k = KeyboardMemory()
    insert(k, MatrixNode('pmatrix', 2, 3))
    assert r'\begin{pmatrix}▦ & ⬚ \\ ⬚ & ⬚ \\ ⬚ & ⬚\end{pmatrix}' == get_edit_mode_latex(k, UnitTestLatexConfiguration())
    insert(k, DigitNode('1'))
    move_right(k)
    insert(k, DigitNode('2'))
    move_down(k)
    insert(k, DigitNode('4'))
    move_down(k)
    insert(k, DigitNode('6'))
    assert r'\begin{pmatrix}1 & 2 \\ ⬚ & 4 \\ ⬚ & 6▦\end{pmatrix}' == get_edit_mode_latex(k, UnitTestLatexConfiguration())


def test_move_with_left_and_right_through_all_cells_of_the_pmatrix_2by2():
    k = KeyboardMemory()
    insert(k, MatrixNode('pmatrix', 2, 2))
    insert(k, DigitNode('1'))
    move_right(k)
    move_right(k)
    insert(k, DigitNode('3'))
    move_right(k)
    insert(k, DigitNode('4'))
    assert r'\begin{pmatrix}1 & ⬚ \\ 3 & 4▦\end{pmatrix}' == get_edit_mode_latex(k, UnitTestLatexConfiguration())
    move_left(k)
    assert r'\begin{pmatrix}1 & ⬚ \\ 3 & ▦4\end{pmatrix}' == get_edit_mode_latex(k, UnitTestLatexConfiguration())
    move_left(k)
    assert r'\begin{pmatrix}1 & ⬚ \\ 3▦ & 4\end{pmatrix}' == get_edit_mode_latex(k, UnitTestLatexConfiguration())
    move_left(k)
    assert r'\begin{pmatrix}1 & ⬚ \\ ▦3 & 4\end{pmatrix}' == get_edit_mode_latex(k, UnitTestLatexConfiguration())
    move_left(k)
    assert r'\begin{pmatrix}1 & ▦ \\ 3 & 4\end{pmatrix}' == get_edit_mode_latex(k, UnitTestLatexConfiguration())
    move_left(k)
    assert r'\begin{pmatrix}1▦ & ⬚ \\ 3 & 4\end{pmatrix}' == get_edit_mode_latex(k, UnitTestLatexConfiguration())
    move_left(k)
    assert r'\begin{pmatrix}▦1 & ⬚ \\ 3 & 4\end{pmatrix}' == get_edit_mode_latex(k, UnitTestLatexConfiguration())
    move_left(k)
    assert r'▦\begin{pmatrix}1 & ⬚ \\ 3 & 4\end{pmatrix}' == get_edit_mode_latex(k, UnitTestLatexConfiguration())
    move_right(k)
    assert r'\begin{pmatrix}▦1 & ⬚ \\ 3 & 4\end{pmatrix}' == get_edit_mode_latex(k, UnitTestLatexConfiguration())
    move_right(k)
    assert r'\begin{pmatrix}1▦ & ⬚ \\ 3 & 4\end{pmatrix}' == get_edit_mode_latex(k, UnitTestLatexConfiguration())
    move_right(k)
    assert r'\begin{pmatrix}1 & ▦ \\ 3 & 4\end{pmatrix}' == get_edit_mode_latex(k, UnitTestLatexConfiguration())
    move_right(k)
    assert r'\begin{pmatrix}1 & ⬚ \\ ▦3 & 4\end{pmatrix}' == get_edit_mode_latex(k, UnitTestLatexConfiguration())
    move_right(k)
    assert r'\begin{pmatrix}1 & ⬚ \\ 3▦ & 4\end{pmatrix}' == get_edit_mode_latex(k, UnitTestLatexConfiguration())
    move_right(k)
    assert r'\begin{pmatrix}1 & ⬚ \\ 3 & ▦4\end{pmatrix}' == get_edit_mode_latex(k, UnitTestLatexConfiguration())
    move_right(k)
    assert r'\begin{pmatrix}1 & ⬚ \\ 3 & 4▦\end{pmatrix}' == get_edit_mode_latex(k, UnitTestLatexConfiguration())
    move_right(k)
    assert r'\begin{pmatrix}1 & ⬚ \\ 3 & 4\end{pmatrix}▦' == get_edit_mode_latex(k, UnitTestLatexConfiguration())


def test_move_out_of_an_empty_pmatrix_2by2_to_the_previous_node_and_back_in():
    k = KeyboardMemory()
    insert(k, DigitNode('2'))
    insert(k, MatrixNode('pmatrix', 2, 2))
    assert r'2\begin{pmatrix}▦ & ⬚ \\ ⬚ & ⬚\end{pmatrix}' == get_edit_mode_latex(k, UnitTestLatexConfiguration())
    move_left(k)
    assert r'2▦\begin{pmatrix}⬚ & ⬚ \\ ⬚ & ⬚\end{pmatrix}' == get_edit_mode_latex(k, UnitTestLatexConfiguration())
    move_right(k)
    assert r'2\begin{pmatrix}▦ & ⬚ \\ ⬚ & ⬚\end{pmatrix}' == get_edit_mode_latex(k, UnitTestLatexConfiguration())


def test_pmatrix_2by2_delete_content():
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
    delete_left(k)
    assert r'\begin{pmatrix}1 & 2 \\ 3 & ▦\end{pmatrix}' == get_edit_mode_latex(k, UnitTestLatexConfiguration())
    delete_left(k)
    assert r'\begin{pmatrix}1 & 2 \\ ▦ & ⬚\end{pmatrix}' == get_edit_mode_latex(k, UnitTestLatexConfiguration())
    delete_left(k)
    assert r'\begin{pmatrix}1 & ▦ \\ ⬚ & ⬚\end{pmatrix}' == get_edit_mode_latex(k, UnitTestLatexConfiguration())
    delete_left(k)
    assert r'\begin{pmatrix}▦ & ⬚ \\ ⬚ & ⬚\end{pmatrix}' == get_edit_mode_latex(k, UnitTestLatexConfiguration())
    delete_left(k)
    assert '▦' == get_edit_mode_latex(k, UnitTestLatexConfiguration())


def test_pmatrix_2by2_right_down_left_up():
    k = KeyboardMemory()
    insert(k, MatrixNode('pmatrix', 2, 2))
    assert r'\begin{pmatrix}▦ & ⬚ \\ ⬚ & ⬚\end{pmatrix}' == get_edit_mode_latex(k, UnitTestLatexConfiguration())
    move_right(k)
    assert r'\begin{pmatrix}⬚ & ▦ \\ ⬚ & ⬚\end{pmatrix}' == get_edit_mode_latex(k, UnitTestLatexConfiguration())
    move_down(k)
    assert r'\begin{pmatrix}⬚ & ⬚ \\ ⬚ & ▦\end{pmatrix}' == get_edit_mode_latex(k, UnitTestLatexConfiguration())
    move_left(k)
    assert r'\begin{pmatrix}⬚ & ⬚ \\ ▦ & ⬚\end{pmatrix}' == get_edit_mode_latex(k, UnitTestLatexConfiguration())
    move_up(k)
    assert r'\begin{pmatrix}▦ & ⬚ \\ ⬚ & ⬚\end{pmatrix}' == get_edit_mode_latex(k, UnitTestLatexConfiguration())


def test_impossible_updown_requests_in_empty_pmatrix_2by2_should_not_throw():
    # Arrange
    k = KeyboardMemory()
    insert(k, MatrixNode('pmatrix', 2, 2))
    assert r'\begin{pmatrix}▦ & ⬚ \\ ⬚ & ⬚\end{pmatrix}' == get_edit_mode_latex(k, UnitTestLatexConfiguration())
    # Act & Assert
    move_up(k)
    assert r'\begin{pmatrix}▦ & ⬚ \\ ⬚ & ⬚\end{pmatrix}' == get_edit_mode_latex(k, UnitTestLatexConfiguration())
    move_down(k)
    assert r'\begin{pmatrix}⬚ & ⬚ \\ ▦ & ⬚\end{pmatrix}' == get_edit_mode_latex(k, UnitTestLatexConfiguration())
    move_down(k)
    assert r'\begin{pmatrix}⬚ & ⬚ \\ ▦ & ⬚\end{pmatrix}' == get_edit_mode_latex(k, UnitTestLatexConfiguration())
    move_right(k)
    assert r'\begin{pmatrix}⬚ & ⬚ \\ ⬚ & ▦\end{pmatrix}' == get_edit_mode_latex(k, UnitTestLatexConfiguration())
    move_down(k)
    assert r'\begin{pmatrix}⬚ & ⬚ \\ ⬚ & ▦\end{pmatrix}' == get_edit_mode_latex(k, UnitTestLatexConfiguration())
    move_up(k)
    assert r'\begin{pmatrix}⬚ & ▦ \\ ⬚ & ⬚\end{pmatrix}' == get_edit_mode_latex(k, UnitTestLatexConfiguration())
    move_up(k)
    assert r'\begin{pmatrix}⬚ & ▦ \\ ⬚ & ⬚\end{pmatrix}' == get_edit_mode_latex(k, UnitTestLatexConfiguration())


def test_impossible_updown_requests_in_filled_pmatrix_2by2_should_not_throw():
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
    move_down(k)
    assert r'\begin{pmatrix}1 & 2 \\ 3 & 4▦\end{pmatrix}' == get_edit_mode_latex(k, UnitTestLatexConfiguration())
    move_up(k)
    assert r'\begin{pmatrix}1 & 2▦ \\ 3 & 4\end{pmatrix}' == get_edit_mode_latex(k, UnitTestLatexConfiguration())
    move_up(k)
    assert r'\begin{pmatrix}1 & 2▦ \\ 3 & 4\end{pmatrix}' == get_edit_mode_latex(k, UnitTestLatexConfiguration())


def test_impossible_updown_requests_in_filled_pmatrix_2by2_should_not_throw():
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
    move_down(k)
    assert r'\begin{pmatrix}1 & 2 \\ 3 & 4▦\end{pmatrix}' == get_edit_mode_latex(k, UnitTestLatexConfiguration())
    move_up(k)
    assert r'\begin{pmatrix}1 & 2▦ \\ 3 & 4\end{pmatrix}' == get_edit_mode_latex(k, UnitTestLatexConfiguration())
    move_up(k)
    assert r'\begin{pmatrix}1 & 2▦ \\ 3 & 4\end{pmatrix}' == get_edit_mode_latex(k, UnitTestLatexConfiguration())


def test_getMoveDownSuggestion_throws_if_it_is_called_for_a_Placeholder_that_is_not_part_of_the_matrix():
    with pytest.raises(Exception) as ex:
        matrix = MatrixNode('pmatrix', 2, 2)
        placeholder_that_is_not_part_of_the_matrix = Placeholder()
        matrix.get_move_down_suggestion(placeholder_that_is_not_part_of_the_matrix)
    assert 'The provided Placeholder is not part of this MatrixNode.' == str(ex.value)
