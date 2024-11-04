from typing import Callable, List, Union


class LatexParserConfiguration:
    def __init__(self) -> None:
        self.additional_digits: Union[List[str], None] = None
        self.decimal_separator_matchers: List[str] = ['.', '{,}']
        self.preferred_decimal_separator: Union[Callable[[], str], None] = None
        self.prefer_roundbracketsnode: bool = True
