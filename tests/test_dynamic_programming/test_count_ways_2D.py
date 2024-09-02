from dynamic_programming.count_ways_2D import count_ways_in_2d
import pytest

test_cases = [(3, 7, 28),
              (3, 2, 3),
              (1, 1, 1),
              (15, 18, 265182525)]


@pytest.mark.parametrize("rows, columns, expected_result", test_cases)
def test_count_ways_2d(rows: int, columns: int, expected_result: int):
    assert expected_result == count_ways_in_2d(rows, columns)
