from src import KeyboardMemory, LatexConfiguration, PartOfNumberWithDigits


class DigitNode(PartOfNumberWithDigits):
    def __init__(self, digit: str) -> None:
        super().__init__()
        self.latex = digit

    def get_latex_part(self, k: KeyboardMemory, latexconfiguration: LatexConfiguration) -> str:
        return self.latex
