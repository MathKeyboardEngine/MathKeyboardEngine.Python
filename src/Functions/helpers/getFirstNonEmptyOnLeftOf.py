from typing import List, Union
from src import Placeholder

def getFirstNonEmptyOnLeftOf(placeholderArray: List[Placeholder], element: Placeholder) -> Union[Placeholder, None]:
  isOnTheLeft = False
  for i in range(len(placeholderArray) - 1, -1, -1):
    placeholder: Placeholder = placeholderArray[i]
    if not isOnTheLeft:
      if placeholder == element:
        isOnTheLeft = True
      continue

    if len(placeholder.nodes) > 0:
      return placeholder
  return None
