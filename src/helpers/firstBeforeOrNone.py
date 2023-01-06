from typing import List, TypeVar, Union

T = TypeVar('T')

def firstBeforeOrNone(array: List[T], element: T) -> Union[T, None]:
  i = array.index(element)
  if i > 0:
    return array[i - 1]
  else:
    return None