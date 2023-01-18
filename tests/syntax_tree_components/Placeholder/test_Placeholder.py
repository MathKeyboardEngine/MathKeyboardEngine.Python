from src import KeyboardMemory, StandardLeafNode, get_view_mode_latex, insert
from tests._testhelpers.UnitTestLatexConfiguration import UnitTestLatexConfiguration


def test_The_minimum_amount_of_required_space_is_added_by_Placeholder_get_latex():
    for data in [
      [r'\sin', r'a', r'\sin a'],
      [r'\sin', r'2', r'\sin2'],
      [r'2', r'\pi', r'2\pi'],
      [r'a', r'\pi', r'a\pi'],
      [r'\alpha', r'\pi', r'\alpha\pi'],
      [r'\pi', r'\pi'],
    ]:
        k = KeyboardMemory()
        for i in range(0, len(data) - 1):
          insert(k, StandardLeafNode(data[i]))
        assert data[-1] == get_view_mode_latex(k, UnitTestLatexConfiguration())