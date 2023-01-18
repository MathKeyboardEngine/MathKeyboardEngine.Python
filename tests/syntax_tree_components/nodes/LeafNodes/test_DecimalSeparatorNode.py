from src import DecimalSeparatorNode, DigitNode, KeyboardMemory, get_edit_mode_latex, insert
from tests._testhelpers.UnitTestLatexConfiguration import UnitTestLatexConfiguration


def test_allows_customizing_the_decimal_separator_even_if_it_is_already_in_the_KeyboardMemory_s_syntaxt_tree():
    # Arrange
    my_decimal_separator_setting = '{,}'
    k = KeyboardMemory()
    insert(k, DigitNode('1'))
    insert(k, DecimalSeparatorNode(lambda: my_decimal_separator_setting))
    insert(k, DigitNode('2'))
    assert '1{,}2▦' == get_edit_mode_latex(k, UnitTestLatexConfiguration())
    # Act
    my_decimal_separator_setting = '.'
    # Assert
    assert '1.2▦' == get_edit_mode_latex(k, UnitTestLatexConfiguration())
