from typing import List, TypeVar, Union, Callable

T = TypeVar('T')


def first_or_none(lambda_expression: Callable[[], T], list: List[T]) -> Union[T, None]:
    return next(iter(filter(lambda_expression, list)), None)