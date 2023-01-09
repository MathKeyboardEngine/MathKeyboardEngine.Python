from src import KeyboardMemory, Placeholder, getEditModeLatex, DescendingBranchingNode, deleteCurrent, insert, moveUp, moveDown, moveLeft, moveRight, DigitNode
from tests.testhelpers.UnitTestLatexConfiguration import UnitTestLatexConfiguration

def test_is_equal_to_current_on_KeyboardMemory_initialization():
    k = KeyboardMemory()
    assert k.syntaxTreeRoot is not None
    assert k.syntaxTreeRoot == k.current

def test_is_a_Placeholder():
    k = KeyboardMemory()
    assert isinstance(k.syntaxTreeRoot, Placeholder)
    assert '▦' == getEditModeLatex(k, UnitTestLatexConfiguration())

def test_cannot_be_deleted():
      k = KeyboardMemory()
      deleteCurrent(k)
      assert k.current is not None
      assert isinstance(k.current, Placeholder)

def test_is_reachable_via_the_chain_of_parents():
      k = KeyboardMemory()

      fraction1 = DescendingBranchingNode(r'\frac{', '}{', '}')
      insert(k, fraction1)
      assert k.current == fraction1.placeholders[0]

      fraction2 = DescendingBranchingNode(r'\frac{', '}{', '}')
      insert(k, fraction2)
      assert k.current == fraction2.placeholders[0]

      assert isinstance(k.current, Placeholder)
      calculatedRoot = k.current.parentNode.parentPlaceholder.parentNode.parentPlaceholder
      assert calculatedRoot.parentNode is None
      assert k.syntaxTreeRoot == calculatedRoot

def test_impossible_move_requests_in_empty_root_placeholder_do_not_throw():
      k = KeyboardMemory()
      assert '▦' == getEditModeLatex(k, UnitTestLatexConfiguration())
      moveLeft(k)
      assert '▦' == getEditModeLatex(k, UnitTestLatexConfiguration())
      moveDown(k)
      assert '▦' == getEditModeLatex(k, UnitTestLatexConfiguration())
      moveUp(k)
      assert '▦' == getEditModeLatex(k, UnitTestLatexConfiguration())
      moveRight(k)
      assert '▦' == getEditModeLatex(k, UnitTestLatexConfiguration())

def test_impossible_move_requests_in_filled_root_placeholder_do_not_throw():
      k = KeyboardMemory()
      insert(k, DigitNode('1'))
      assert '1▦' == getEditModeLatex(k, UnitTestLatexConfiguration())
      moveUp(k)
      assert '1▦' == getEditModeLatex(k, UnitTestLatexConfiguration())
      moveRight(k)
      assert '1▦' == getEditModeLatex(k, UnitTestLatexConfiguration())
      moveDown(k)
      assert '1▦' == getEditModeLatex(k, UnitTestLatexConfiguration())
      moveLeft(k)
      assert '▦1' == getEditModeLatex(k, UnitTestLatexConfiguration())
      moveDown(k)
      assert '▦1' == getEditModeLatex(k, UnitTestLatexConfiguration())
      moveLeft(k)
      assert '▦1' == getEditModeLatex(k, UnitTestLatexConfiguration())
      moveUp(k)
      assert '▦1' == getEditModeLatex(k, UnitTestLatexConfiguration())