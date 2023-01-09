from typing import List, TypeVar, Union

T = TypeVar('T')

def first_after_or_none(list : List[T], element : T) -> Union[T, None]:
  i = list.index(element)
  if i != -1 and i < len(list) - 1:
    return list[i + 1]
  else:
    return None