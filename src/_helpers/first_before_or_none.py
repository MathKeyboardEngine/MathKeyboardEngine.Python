from typing import List, TypeVar, Union

T = TypeVar('T')


def first_before_or_none(list: List[T], element: T) -> Union[T, None]:
    i = list.index(element)
    if i > 0:
        return list[i - 1]
    else:
        return None
