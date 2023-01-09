from typing import Iterable

def concat_latex(latex_parts: Iterable[str]) -> str:
    s = ""
    for part in latex_parts:
        if ends_with_latex_command(s) and part[0].isalpha():
            s += " "
        s += part
    return s

def ends_with_latex_command(latex: str) -> bool:
    if len(latex) == 0:
        return False
    if latex[-1].isalpha():
        for i in range(len(latex) - 2, -1, -1):
            c = latex[i]
            if c.isalpha():
                continue
            else:
                return c == '\\'
    return False