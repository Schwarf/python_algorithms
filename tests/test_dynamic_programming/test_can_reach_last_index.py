from dynamic_programming.can_reach_last_index import can_reach_last_index


def test_can_reach_last_index_true():
    input = [2, 3, 1, 1, 4]
    result = can_reach_last_index(input)
    assert result is True


def test_can_reach_last_index_false():
    input = [3, 2, 1, 0, 4]
    result = can_reach_last_index(input)
    assert result is False


def test_can_reach_last_index_false2():
    input = [0, 3, 1, 1, 4]
    result = can_reach_last_index(input)
    assert result is False

    
def test_can_reach_last_index_true2():
    input = [4, 0, 0, 0, 0]
    result = can_reach_last_index(input)
    assert result is True


def test_can_reach_last_index_true3():
    input = [0]
    result = can_reach_last_index(input)
    assert result is True
