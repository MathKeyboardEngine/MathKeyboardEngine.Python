from typing import Optional


class LatexConfiguration:
  def __init__(self):
    self.active_placeholder_shape : str = r'\blacksquare'
    self.active_placeholder_color : Optional[str] = None
    self.passive_placeholder_shape : str = r'\square'
    self.passive_placeholder_color : Optional[str] = None
    self.selection_hightlight_start : str = r'\colorbox{#ADD8E6}{\(\displaystyle'
    self.selection_hightlight_end : str = r'\)}'

  def active_placeholder_latex(self) -> str:
    if self.active_placeholder_color is None:
      return self.active_placeholder_shape
    else:
      return r'{\color{' + self.active_placeholder_color + '}' + self.active_placeholder_shape + '}'
  
  def passive_placeholder_latex(self) -> str:
    if self.passive_placeholder_color is None:
      return self.passive_placeholder_shape
    else:
      return r'{\color{' + self.passive_placeholder_color + '}' + self.passive_placeholder_shape + '}'