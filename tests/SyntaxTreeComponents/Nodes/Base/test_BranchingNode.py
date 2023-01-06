from src import BranchingNode, KeyboardMemory, LatexConfiguration, insert, moveUp, moveDown, getEditModeLatex, Placeholder
from tests.testhelpers.UnitTestLatexConfiguration import UnitTestLatexConfiguration

def test_calling_moveUp_or_moveDown_does_not_throw_even_if_not_implemented():
    k = KeyboardMemory()
    insert(k, DummyBranchingNode())
    assert 'wow >> ▦ << wow' == getEditModeLatex(k, UnitTestLatexConfiguration())
    moveUp(k)
    assert 'wow >> ▦ << wow'== getEditModeLatex(k, UnitTestLatexConfiguration())
    moveDown(k)
    assert 'wow >> ▦ << wow'== getEditModeLatex(k, UnitTestLatexConfiguration())

class DummyBranchingNode(BranchingNode):
  def __init__(self):
    super().__init__([Placeholder()])

  def getLatexPart(self, k: KeyboardMemory, latexConfiguration: LatexConfiguration) -> str:
    return 'wow >> ' + self.placeholders[0].getLatex(k, latexConfiguration) + ' << wow'