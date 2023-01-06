from typing import Union
from src import KeyboardMemory, LatexConfiguration, Placeholder, TreeNode

emptyKeyboardMemory = KeyboardMemory()

def getViewModeLatex(x : Union[KeyboardMemory, Placeholder, TreeNode], latexConfiguration : LatexConfiguration) -> str:
  syntaxTreeComponent = x.syntaxTreeRoot if isinstance(x, KeyboardMemory) else x
  return syntaxTreeComponent.getLatex(emptyKeyboardMemory, latexConfiguration)

def getEditModeLatex(k : KeyboardMemory, latexConfiguration : LatexConfiguration) -> str:
  return k.syntaxTreeRoot.getLatex(k, latexConfiguration)
