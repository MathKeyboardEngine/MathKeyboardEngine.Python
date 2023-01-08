from src import KeyboardMemory, LatexConfiguration

def getEditModeLatex(k : KeyboardMemory, latexConfiguration : LatexConfiguration) -> str:
  return k.syntaxTreeRoot.getLatex(k, latexConfiguration)