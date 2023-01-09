from typing import List, Optional, Tuple
from src import BranchingNode, KeyboardMemory, Placeholder, LatexConfiguration

class MatrixNode(BranchingNode):
  def __init__(self, matrixType: str, width: int, height: int) -> None:
    grid: List[List[Placeholder]] = []
    leftToRight: List[Placeholder] = []
    for i in range(0, height):
      row: List[Placeholder] = []
      for j  in range(0, width):
        placeholder = Placeholder()
        row.append(placeholder)
        leftToRight.append(placeholder)
      grid.append(row)
    super().__init__(leftToRight)
    self.grid = grid
    self.matrixType = matrixType
    self.width = width

  def get_latex_part(self, k: KeyboardMemory, latexconfiguration: LatexConfiguration) -> str:
    latex = r'\begin{' + self.matrixType+ '}'
    latex += r' \\ '.join([' & '.join([p.get_latex(k, latexconfiguration) for p in row]) for row in self.grid])
    latex += r'\end{' + self.matrixType + '}'
    return latex

  def get_move_down_suggestion(self, fromPlaceholder: Placeholder) -> Optional[Placeholder]:
    (rowIndex, columnIndex) = self.getPositionOf(fromPlaceholder)
    if rowIndex + 1 < len(self.grid):
      return self.grid[rowIndex + 1][columnIndex]
    else:
      return None

  def get_move_up_suggestion(self, fromPlaceholder: Placeholder) -> Optional[Placeholder]:
    (rowIndex, columnIndex) = self.getPositionOf(fromPlaceholder)
    if rowIndex - 1 >= 0:
      return self.grid[rowIndex - 1][columnIndex]
    else:
      return None

  def getPositionOf(self, placeholder: Placeholder) -> Tuple[int, int]:
    try:
      index = self.placeholders.index(placeholder)
    except:
      raise Exception('The provided Placeholder is not part of this MatrixNode.')
    rowIndex = int(index / self.width)
    columnIndex  = int(index - rowIndex * self.width)
    return (rowIndex, columnIndex)
