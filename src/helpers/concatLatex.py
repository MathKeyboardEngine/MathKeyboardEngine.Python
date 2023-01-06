from typing import Iterable

def concatLatex(latexParts: Iterable[str]) -> str:
    s = ""
    for part in latexParts:
        if endsWithLatexCommand(s) and part[0].isalpha():
            s += " "
        s += part
    return s

def endsWithLatexCommand(latex: str) -> bool:
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