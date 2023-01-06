from src import Placeholder, LatexConfiguration, concatLatex

class TreeNode:
  def __init__(self):
    self.parentPlaceholder : Placeholder = None

  def getLatexPart(self, k : 'KeyboardMemory', latexConfiguration : LatexConfiguration) -> str:
    raise Exception('Not implemented: `getLatexPart`.')

  def getLatex(self, k : 'KeyboardMemory', latexConfiguration : LatexConfiguration) -> str:
    latex = self.getLatexPart(k, latexConfiguration)
    if k.selectionDiff is not None and k.selectionDiff != 0:
      if k.inclusiveSelectionLeftBorder == self:
        latex = concatLatex([latexConfiguration.selectionHightlightStart, latex])
      if k.inclusiveSelectionRightBorder == self:
        latex = concatLatex([latex, latexConfiguration.selectionHightlightEnd])
      return latex
    else:
      if k.current == self:
        return concatLatex([latex, latexConfiguration.activePlaceholderLatex()])
      else:
        return latex