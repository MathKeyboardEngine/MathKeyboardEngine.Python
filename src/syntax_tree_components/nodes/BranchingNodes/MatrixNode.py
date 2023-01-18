from typing import List, Optional, Tuple

from src import BranchingNode, KeyboardMemory, LatexConfiguration, Placeholder


class MatrixNode(BranchingNode):
    def __init__(self, matrix_type: str, width: int, height: int) -> None:
        grid: List[List[Placeholder]] = []
        left_to_right: List[Placeholder] = []
        for i in range(0, height):
            row: List[Placeholder] = []
            for j in range(0, width):
                placeholder = Placeholder()
                row.append(placeholder)
                left_to_right.append(placeholder)
            grid.append(row)
        super().__init__(left_to_right)
        self.grid = grid
        self.matrix_type = matrix_type
        self.width = width

    def get_latex_part(self, k: KeyboardMemory, latexconfiguration: LatexConfiguration) -> str:
        latex = r'\begin{' + self.matrix_type + '}'
        latex += r' \\ '.join([' & '.join([p.get_latex(k, latexconfiguration) for p in row]) for row in self.grid])
        latex += r'\end{' + self.matrix_type + '}'
        return latex

    def get_move_down_suggestion(self, from_placeholder: Placeholder) -> Optional[Placeholder]:
        (row_index, column_index) = self.get_position_of(from_placeholder)
        if row_index + 1 < len(self.grid):
            return self.grid[row_index + 1][column_index]
        else:
            return None

    def get_move_up_suggestion(self, from_placeholder: Placeholder) -> Optional[Placeholder]:
        (row_index, column_index) = self.get_position_of(from_placeholder)
        if row_index - 1 >= 0:
            return self.grid[row_index - 1][column_index]
        else:
            return None

    def get_position_of(self, placeholder: Placeholder) -> Tuple[int, int]:
        try:
            index = self.placeholders.index(placeholder)
        except:
            raise Exception('The provided Placeholder is not part of this MatrixNode.')
        row_index = int(index / self.width)
        column_index = int(index - row_index * self.width)
        return (row_index, column_index)
