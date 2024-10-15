__all__ = ['my_sum', 'factorial']

from functools import cache
import pytest


def my_sum(iterable):
    tot = 0
    for i in iterable:
        tot += i
    return tot


@cache
def factorial(n):
    return n * factorial(n - 1) if n else 1


@pytest.mark.parametrize('number, expected', [
        (5, 120),
        (3, 6),
        (1, 1)
    ])
def test_factorial(number, expected):
    '''Test our factorial function'''
    answer = factorial(number)
    assert answer == expected
