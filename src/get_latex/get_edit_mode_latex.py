from src import KeyboardMemory, LatexConfiguration

def get_edit_mode_latex(k : KeyboardMemory, latexconfiguration : LatexConfiguration) -> str:
  return k.syntax_tree_root.get_latex(k, latexconfiguration)