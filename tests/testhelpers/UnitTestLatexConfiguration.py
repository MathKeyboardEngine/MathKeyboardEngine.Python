from src import LatexConfiguration

class UnitTestLatexConfiguration(LatexConfiguration):
    def __init__(self) -> None:
        super().__init__()
        self.activePlaceholderShape = '▦'
        self.passivePlaceholderShape = '⬚'
        self.selectionHightlightStart = r'\colorbox{blue}{'
        self.selectionHightlightEnd = '}'