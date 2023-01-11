from src import StandardBranchingNode

class RoundBracketsNode(StandardBranchingNode):
  def __init__(self, left_bracket_latex: str = r'\left(', right_bracket_latex: str = r'\right)') -> None:
    super().__init__(left_bracket_latex, right_bracket_latex)
