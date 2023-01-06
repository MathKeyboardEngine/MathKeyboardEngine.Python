from typing import Optional

class LatexConfiguration:
  def __init__(self):
    self.activePlaceholderShape : str = r'\blacksquare'
    self.activePlaceholderColor : Optional[str] = None
    self.passivePlaceholderShape : str = r'\square'
    self.passivePlaceholderColor : Optional[str] = None
    self.selectionHightlightStart : str = r'\colorbox{#ADD8E6}{\(\displaystyle'
    self.selectionHightlightEnd : str = r'\)}'

  def activePlaceholderLatex(self) -> str:
    if self.activePlaceholderColor is None:
      return self.activePlaceholderShape
    else:
      return r'{\color{' + self.activePlaceholderColor + '}' + self.activePlaceholderShape + '}'
  
  def passivePlaceholderLatex(self) -> str:
    if self.passivePlaceholderColor is None:
      return self.passivePlaceholderShape
    else:
      return r'{\color{' + self.passivePlaceholderColor + '}' + self.passivePlaceholderShape + '}'