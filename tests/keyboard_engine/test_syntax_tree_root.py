from src import KeyboardMemory, Placeholder, get_edit_mode_latex, DescendingBranchingNode, delete_current, insert, move_up, move_down, move_left, move_right, DigitNode
from tests.testhelpers.UnitTestLatexConfiguration import UnitTestLatexConfiguration

def test_is_equal_to_current_on_KeyboardMemory_initialization():
    k = KeyboardMemory()
    assert k.syntax_tree_root is not None
    assert k.syntax_tree_root == k.current

def test_is_a_Placeholder():
    k = KeyboardMemory()
    assert isinstance(k.syntax_tree_root, Placeholder)
    assert '▦' == get_edit_mode_latex(k, UnitTestLatexConfiguration())

def test_cannot_be_deleted():
      k = KeyboardMemory()
      delete_current(k)
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
      calculated_root = k.current.parent_node.parent_placeholder.parent_node.parent_placeholder
      assert calculated_root.parent_node is None
      assert k.syntax_tree_root == calculated_root

def test_impossible_move_requests_in_empty_root_placeholder_do_not_throw():
      k = KeyboardMemory()
      assert '▦' == get_edit_mode_latex(k, UnitTestLatexConfiguration())
      move_left(k)
      assert '▦' == get_edit_mode_latex(k, UnitTestLatexConfiguration())
      move_down(k)
      assert '▦' == get_edit_mode_latex(k, UnitTestLatexConfiguration())
      move_up(k)
      assert '▦' == get_edit_mode_latex(k, UnitTestLatexConfiguration())
      move_right(k)
      assert '▦' == get_edit_mode_latex(k, UnitTestLatexConfiguration())

def test_impossible_move_requests_in_filled_root_placeholder_do_not_throw():
      k = KeyboardMemory()
      insert(k, DigitNode('1'))
      assert '1▦' == get_edit_mode_latex(k, UnitTestLatexConfiguration())
      move_up(k)
      assert '1▦' == get_edit_mode_latex(k, UnitTestLatexConfiguration())
      move_right(k)
      assert '1▦' == get_edit_mode_latex(k, UnitTestLatexConfiguration())
      move_down(k)
      assert '1▦' == get_edit_mode_latex(k, UnitTestLatexConfiguration())
      move_left(k)
      assert '▦1' == get_edit_mode_latex(k, UnitTestLatexConfiguration())
      move_down(k)
      assert '▦1' == get_edit_mode_latex(k, UnitTestLatexConfiguration())
      move_left(k)
      assert '▦1' == get_edit_mode_latex(k, UnitTestLatexConfiguration())
      move_up(k)
      assert '▦1' == get_edit_mode_latex(k, UnitTestLatexConfiguration())