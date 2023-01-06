from src import KeyboardMemory, DigitNode, StandardLeafNode, insert, getEditModeLatex
from tests.testhelpers.UnitTestLatexConfiguration import UnitTestLatexConfiguration

def test_allows_customizing_the_multiplication_operator_sign_even_if_it_is_already_in_the_KeyboardMemory_s_syntax_tree():
    # Arrange
    myMultiplicationSignSetting = r'\times'
    k = KeyboardMemory()
    insert(k, DigitNode('2'))
    insert(k, StandardLeafNode(lambda: myMultiplicationSignSetting))
    insert(k, StandardLeafNode('a'))
    assert r'2\times a▦' == getEditModeLatex(k, UnitTestLatexConfiguration())
    # Act
    myMultiplicationSignSetting = r'\cdot'
    # Assert
    assert r'2\cdot a▦' == getEditModeLatex(k, UnitTestLatexConfiguration())