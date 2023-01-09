from typing import List, TypeVar, Union

T = TypeVar('T')

def last_or_none(list : List[T]) -> Union[T, None]:
    return list[-1] if list else None