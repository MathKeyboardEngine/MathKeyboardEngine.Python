from typing import List
from src import BranchingNode, KeyboardMemory, LatexConfiguration, Placeholder

class StandardBranchingNode(BranchingNode):
  def __init__(self, before: str, then: str, *rest: str) -> None:
    placeholder_count = len(rest) + 1
    placeholders : List[Placeholder] = [Placeholder() for i in range(0, placeholder_count)]
    super().__init__(placeholders)
    self.before = before
    self.then = then
    self.rest = rest

  def get_latex_part(self, k: KeyboardMemory, latexconfiguration: LatexConfiguration) -> str:
    latex = self.before + self.placeholders[0].get_latex(k, latexconfiguration) + self.then
    for i in range(0, len(self.rest)):
      latex += self.placeholders[i + 1].get_latex(k, latexconfiguration) + self.rest[i]
    return latex
