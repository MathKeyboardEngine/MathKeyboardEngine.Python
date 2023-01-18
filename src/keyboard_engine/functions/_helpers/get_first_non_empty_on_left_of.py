from typing import List, Union

from src import Placeholder


def get_first_non_empty_on_left_of(list: List[Placeholder], element: Placeholder) -> Union[Placeholder, None]:
    is_on_the_left = False
    for i in range(len(list) - 1, -1, -1):
        placeholder: Placeholder = list[i]
        if not is_on_the_left:
            if placeholder == element:
                is_on_the_left = True
            continue

        if len(placeholder.nodes) > 0:
            return placeholder
    return None
