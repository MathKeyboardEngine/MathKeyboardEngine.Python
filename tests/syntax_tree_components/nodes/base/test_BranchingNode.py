from src import BranchingNode, KeyboardMemory, LatexConfiguration, Placeholder, get_edit_mode_latex, insert, move_down, move_up
from tests._testhelpers.UnitTestLatexConfiguration import UnitTestLatexConfiguration


def test_calling_moveUp_or_moveDown_does_not_throw_even_if_not_implemented():
    k = KeyboardMemory()
    insert(k, DummyBranchingNode())
    assert 'wow >> ▦ << wow' == get_edit_mode_latex(k, UnitTestLatexConfiguration())
    move_up(k)
    assert 'wow >> ▦ << wow' == get_edit_mode_latex(k, UnitTestLatexConfiguration())
    move_down(k)
    assert 'wow >> ▦ << wow' == get_edit_mode_latex(k, UnitTestLatexConfiguration())


class DummyBranchingNode(BranchingNode):
    def __init__(self):
        super().__init__([Placeholder()])

    def get_latex_part(self, k: KeyboardMemory, latexconfiguration: LatexConfiguration) -> str:
        return 'wow >> ' + self.placeholders[0].get_latex(k, latexconfiguration) + ' << wow'
