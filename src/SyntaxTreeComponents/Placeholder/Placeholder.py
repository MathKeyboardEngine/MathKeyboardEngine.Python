from itertools import chain
from typing import List, Union
from src import concatLatex, LatexConfiguration

class Placeholder:
    def __init__(self):
        self.parentNode : Union['TreeNode', None] = None
        self.nodes : List['TreeNode'] = []

    def getLatex(self, k : 'KeyboardMemory', latexConfiguration : LatexConfiguration) -> str:
        if self == k.inclusiveSelectionLeftBorder:
            return concatLatex(chain(
                [latexConfiguration.selectionHightlightStart],
                [x.getLatex(k, latexConfiguration) for x in self.nodes]))
        elif self == k.current:
            if not self.nodes:
                return latexConfiguration.activePlaceholderLatex()
            else:
                return concatLatex(chain(
                    [latexConfiguration.activePlaceholderLatex()],
                    [x.getLatex(k, latexConfiguration) for x in self.nodes]))
        elif not self.nodes:
            return latexConfiguration.passivePlaceholderLatex()
        else:
            return concatLatex([x.getLatex(k, latexConfiguration) for x in self.nodes])
