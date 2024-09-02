import pytest

from dynamic_programming.fibonacci_numbers import fibonacci_number

test_cases = [
    (0, 0),
    (1, 1),
    (2, 1),
    (3, 2),
    (4, 3),
    (5, 5),
    (6, 8),
    (7, 13),
    (8, 21),
    (9, 34),
    (10, 55),
    (11, 89),
    (12, 144),
    (13, 233),
    (14, 377)
]


@pytest.mark.parametrize("n, expected_result", test_cases)
def test_fibonacci_number(n: int, expected_result: int) -> None:
    assert fibonacci_number(n) == expected_result
