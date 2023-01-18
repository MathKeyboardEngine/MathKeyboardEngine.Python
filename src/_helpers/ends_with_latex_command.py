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
