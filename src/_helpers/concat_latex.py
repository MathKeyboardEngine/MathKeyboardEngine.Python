from typing import Iterable

from src._helpers.ends_with_latex_command import ends_with_latex_command


def concat_latex(latex_parts: Iterable[str]) -> str:
    s = ""
    for part in latex_parts:
        if ends_with_latex_command(s) and part[0].isalpha():
            s += " "
        s += part
    return s