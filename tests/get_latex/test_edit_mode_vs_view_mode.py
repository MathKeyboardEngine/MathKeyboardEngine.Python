from src import get_edit_mode_latex, get_view_mode_latex, KeyboardMemory, insert, DigitNode, move_down, DescendingBranchingNode
from tests.testhelpers.UnitTestLatexConfiguration import UnitTestLatexConfiguration

def test_can_get_the_LaTeX_for_a_BranchingNode():
  # Arrange
  k = KeyboardMemory()
  insert(k, DescendingBranchingNode(r'\frac{', '}{', '}'))
  # Act & Assert
  assert r'\frac{▦}{⬚}' == get_edit_mode_latex(k, UnitTestLatexConfiguration())
  assert r'\frac{⬚}{⬚}' == get_view_mode_latex(k, UnitTestLatexConfiguration())
  assert r'\frac{⬚}{⬚}' == get_view_mode_latex(DescendingBranchingNode(r'\frac{', '}{', '}'), UnitTestLatexConfiguration())

def test_can_get_the_LaTeX_for_a_LeafNode():
  # Arrange
  k = KeyboardMemory()
  insert(k, DigitNode('3'))
  # Act & Assert
  assert '3▦' == get_edit_mode_latex(k, UnitTestLatexConfiguration())
  assert '3' == get_view_mode_latex(k, UnitTestLatexConfiguration())
  assert '3' == get_view_mode_latex(DigitNode('3'), UnitTestLatexConfiguration())

def test_can_get_the_LaTeX_for_a_Placeholder():
  # Arrange
  k = KeyboardMemory()
  fraction = DescendingBranchingNode(r'\frac{', '}{', '}')
  insert(k, fraction)
  insert(k, DigitNode('3'))
  move_down(k)
  # Act & Assert
  assert r'\frac{3}{▦}' == get_edit_mode_latex(k, UnitTestLatexConfiguration())
  assert '3' == get_view_mode_latex(fraction.placeholders[0], UnitTestLatexConfiguration())
