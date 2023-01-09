from src import LatexConfiguration

class UnitTestLatexConfiguration(LatexConfiguration):
    def __init__(self) -> None:
        super().__init__()
        self.active_placeholder_shape = '▦'
        self.passive_placeholder_shape = '⬚'
        self.selection_hightlight_start = r'\colorbox{blue}{'
        self.selection_hightlight_end = '}'