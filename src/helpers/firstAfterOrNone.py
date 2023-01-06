from typing import List, TypeVar, Union

T = TypeVar('T')

def firstAfterOrNone(array : List[T], element : T) -> Union[T, None]:
  i = array.index(element)
  if i != -1 and i < len(array) - 1:
    return array[i + 1]
  else:
    return None