from src import StandardBranchingNode

class RoundBracketsNode(StandardBranchingNode):
  def __init__(self, leftBracketLatex: str = r'\left(', rightBracketLatex: str = r'\right)') -> None:
    super().__init__(leftBracketLatex, rightBracketLatex)
