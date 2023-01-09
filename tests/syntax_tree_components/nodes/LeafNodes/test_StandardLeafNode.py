from src import KeyboardMemory, DigitNode, StandardLeafNode, insert, get_edit_mode_latex
from tests._testhelpers.UnitTestLatexConfiguration import UnitTestLatexConfiguration

def test_allows_customizing_the_multiplication_operator_sign_even_if_it_is_already_in_the_KeyboardMemory_s_syntax_tree():
    # Arrange
    my_multiplication_sign_setting = r'\times'
    k = KeyboardMemory()
    insert(k, DigitNode('2'))
    insert(k, StandardLeafNode(lambda: my_multiplication_sign_setting))
    insert(k, StandardLeafNode('a'))
    assert r'2\times a▦' == get_edit_mode_latex(k, UnitTestLatexConfiguration())
    # Act
    my_multiplication_sign_setting = r'\cdot'
    # Assert
    assert r'2\cdot a▦' == get_edit_mode_latex(k, UnitTestLatexConfiguration())