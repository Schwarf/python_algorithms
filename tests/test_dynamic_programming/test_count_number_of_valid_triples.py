from dynamic_programming.count_number_of_valid_triples import valid_triples


def test_valid_triples():
    input = [2, 5, 3, 4, 1]
    expected_result = 3
    assert expected_result == valid_triples(input)


def test_valid_triples2():
    input = [2, 1, 3]
    expected_result = 0
    assert expected_result == valid_triples(input)


def test_valid_triples3():
    input = [1, 2, 3, 4]
    expected_result = 4
    assert expected_result == valid_triples(input)


def test_valid_triples4():
    input = [89, 61, 13, 36, 37, 39, 97, 76, 84, 18, 12, 24, 71, 33, 44, 85, 70, 82, 15, 74, 35, 66, 59,
                           8, 3, 96, 30, 16, 41, 7, 10, 68, 92, 83, 95, 77, 9, 14, 81, 88, 38]
    expected_result = 3514
    assert expected_result == valid_triples(input)
