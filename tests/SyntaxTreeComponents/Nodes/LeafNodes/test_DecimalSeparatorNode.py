from src import insert, DecimalSeparatorNode, DigitNode, KeyboardMemory, getEditModeLatex
from tests.testhelpers.UnitTestLatexConfiguration import UnitTestLatexConfiguration

def test_allows_customizing_the_decimal_separator_even_if_it_is_already_in_the_KeyboardMemory_s_syntaxt_tree():
    # Arrange
    myDecimalSeparatorSetting = '{,}'
    k = KeyboardMemory()
    insert(k, DigitNode('1'))
    insert(k, DecimalSeparatorNode(lambda: myDecimalSeparatorSetting))
    insert(k, DigitNode('2'))
    assert '1{,}2▦' == getEditModeLatex(k, UnitTestLatexConfiguration())
    # Act
    myDecimalSeparatorSetting = '.'
    # Assert
    assert '1.2▦' == getEditModeLatex(k, UnitTestLatexConfiguration())
