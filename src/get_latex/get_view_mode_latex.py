from typing import Union

from src import KeyboardMemory, LatexConfiguration, Placeholder, TreeNode

empty_keyboardmemory = KeyboardMemory()

def get_view_mode_latex(x : Union[KeyboardMemory, Placeholder, TreeNode], latexconfiguration : LatexConfiguration) -> str:
  syntax_tree_component = x.syntax_tree_root if isinstance(x, KeyboardMemory) else x
  return syntax_tree_component.get_latex(empty_keyboardmemory, latexconfiguration)
