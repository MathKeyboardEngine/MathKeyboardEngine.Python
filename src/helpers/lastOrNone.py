from typing import List, TypeVar, Union

T = TypeVar('T')

def lastOrNone(list : List[T]) -> Union[T, None]:
    return list[-1] if list else None