from itertools import chain
from typing import List, Union
from src import LatexConfiguration
from src._helpers.concat_latex import concat_latex

class Placeholder:
    def __init__(self):
        self.parent_node : Union['TreeNode', None] = None
        self.nodes : List['TreeNode'] = []

    def get_latex(self, k : 'KeyboardMemory', latexconfiguration : LatexConfiguration) -> str:
        if self == k.inclusive_selection_left_border:
            return concat_latex(chain(
                [latexconfiguration.selection_hightlight_start],
                [x.get_latex(k, latexconfiguration) for x in self.nodes]))
        elif self == k.current:
            if not self.nodes:
                return latexconfiguration.active_placeholder_latex()
            else:
                return concat_latex(chain(
                    [latexconfiguration.active_placeholder_latex()],
                    [x.get_latex(k, latexconfiguration) for x in self.nodes]))
        elif not self.nodes:
            return latexconfiguration.passive_placeholder_latex()
        else:
            return concat_latex([x.get_latex(k, latexconfiguration) for x in self.nodes])
