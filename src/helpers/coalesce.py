from typing import TypeVar, Union

T = TypeVar('T')

def coalesce(x : Union[T, None], default : T) -> T:
    if x is None:
        return default
    else:
        return x