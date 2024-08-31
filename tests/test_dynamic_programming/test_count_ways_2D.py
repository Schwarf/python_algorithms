from dynamic_programming.count_ways_2D import count_ways_in_2d


def test_count_ways_2d_1():
    rows = 3
    columns = 7
    expected_result = 28
    assert expected_result == count_ways_in_2d(rows, columns)


def test_count_ways_2d_2():
    rows = 3
    columns = 2
    expected_result = 3
    assert expected_result == count_ways_in_2d(rows, columns)


def test_count_ways_2d_3():
    rows = 1
    columns = 1
    expected_result = 1
    assert expected_result == count_ways_in_2d(rows, columns)


def test_count_ways_2d_4():
    rows = 15
    columns = 18
    expected_result = 265182525
    assert expected_result == count_ways_in_2d(rows, columns)
