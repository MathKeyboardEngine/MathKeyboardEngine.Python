from typing import Callable, Union
from src import KeyboardMemory, LatexConfiguration, LeafNode

class StandardLeafNode(LeafNode):
  def __init__(self, latex: Union[str, Callable[[], str]]) -> None:
    self.latex : Callable[[], str] = (lambda : latex) if isinstance(latex, str) else latex
  
  def getLatexPart(self, k: KeyboardMemory, latexConfiguration: LatexConfiguration) -> str:
    return self.latex()