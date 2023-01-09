from src import getEditModeLatex, getViewModeLatex, KeyboardMemory, insert, DigitNode, moveDown, DescendingBranchingNode
from tests.testhelpers.UnitTestLatexConfiguration import UnitTestLatexConfiguration

def test_can_get_the_LaTeX_for_a_BranchingNode():
  # Arrange
  k = KeyboardMemory()
  insert(k, DescendingBranchingNode(r'\frac{', '}{', '}'))
  # Act & Assert
  assert r'\frac{▦}{⬚}' == getEditModeLatex(k, UnitTestLatexConfiguration())
  assert r'\frac{⬚}{⬚}' == getViewModeLatex(k, UnitTestLatexConfiguration())
  assert r'\frac{⬚}{⬚}' == getViewModeLatex(DescendingBranchingNode(r'\frac{', '}{', '}'), UnitTestLatexConfiguration())

def test_can_get_the_LaTeX_for_a_LeafNode():
  # Arrange
  k = KeyboardMemory()
  insert(k, DigitNode('3'))
  # Act & Assert
  assert '3▦' == getEditModeLatex(k, UnitTestLatexConfiguration())
  assert '3' == getViewModeLatex(k, UnitTestLatexConfiguration())
  assert '3' == getViewModeLatex(DigitNode('3'), UnitTestLatexConfiguration())

def test_can_get_the_LaTeX_for_a_Placeholder():
  # Arrange
  k = KeyboardMemory()
  fraction = DescendingBranchingNode(r'\frac{', '}{', '}')
  insert(k, fraction)
  insert(k, DigitNode('3'))
  moveDown(k)
  # Act & Assert
  assert r'\frac{3}{▦}' == getEditModeLatex(k, UnitTestLatexConfiguration())
  assert '3' == getViewModeLatex(fraction.placeholders[0], UnitTestLatexConfiguration())
