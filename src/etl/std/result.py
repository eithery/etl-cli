#
# (C) Eithery Lab, 2023
# Result[T, E] class
# Represents the result of operation with two possible outcomes
# Result[T, E] = Ok(T) | Err(E)
# It contains either a success result OK(t) where t is a wrapped returned value of type T
# or an error result Err(e) where e is an error of type E explaining what went wrong
#
from __future__ import annotations
from etl.std import T, E, R
from typing import Generic, Optional, Callable
from .error import Error
from .exceptions import InvalidResultException


class Result(Generic[T, E]):
    def __init__(self, value: Optional[T]=None, error: Optional[E]=None):
        self._value = value
        self._error = error
        if isinstance(value, Error):
            self._error = value
            self._value = None


    @property
    def is_ok(self) -> bool:
        return self._error is None


    @property
    def is_error(self) -> bool:
        return not self.is_ok


    def unwrap(self) -> T:
        return self.expect("Cannot unwrap a value for the Error result")


    def expect(self, message: str) -> T:
        if self.is_ok:
            return self._value
        raise InvalidResultException(message)


    def ok(self):
        return self._value if self.is_ok else None


    def err(self):
        return self._error if self.is_error else None


    def match(self, ok: Callable[[T], R], err: Callable[[E], R]) -> R:
        return ok(self._value) if self.is_ok else err(self._error)


    def map(self, func: Callable[[T], R]) -> Result[R, E]:
        return self.match(
            ok = lambda v : Ok(func(v)),
            err = lambda e: Err(e)
        )


    def bind(self, func: Callable[[T], Result[R, E]]) -> Result[R, E]:
        return self.match(
            ok = lambda v : func(v),
            err = lambda e : Err(e)
        )


    def __repr__(self) -> str:
        return self.match(lambda v : f'Ok({v})', lambda e : f'Err({e})')



def Ok(value: Optional[T]=None) -> Result[T, E]:
    return Result(value)


def Err(error: E) -> Result[T, E]:
    return Result(error=error)
