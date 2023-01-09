from src import Placeholder, LatexConfiguration
from src._helpers.concat_latex import concat_latex

class TreeNode:
  def __init__(self):
    self.parent_placeholder : Placeholder = None

  def get_latex_part(self, k : 'KeyboardMemory', latexconfiguration : LatexConfiguration) -> str:
    raise Exception('Not implemented: `get_latex_part`.')

  def get_latex(self, k : 'KeyboardMemory', latexconfiguration : LatexConfiguration) -> str:
    latex = self.get_latex_part(k, latexconfiguration)
    if k.selection_diff is not None and k.selection_diff != 0:
      if k.inclusive_selection_left_border == self:
        latex = concat_latex([latexconfiguration.selection_hightlight_start, latex])
      if k.inclusive_selection_right_border == self:
        latex = concat_latex([latex, latexconfiguration.selection_hightlight_end])
      return latex
    else:
      if k.current == self:
        return concat_latex([latex, latexconfiguration.active_placeholder_latex()])
      else:
        return latex