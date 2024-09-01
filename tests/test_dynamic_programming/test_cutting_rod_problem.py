from dynamic_programming.cutting_rod_problem import cut_rod_recursive, cut_rod_top_down


def test_cut_rod_recursive1():
    prices = [0, 1, 5, 8, 9, 10, 17, 17, 20, 24, 30]
    length = 8
    expected_result = 22
    assert expected_result == cut_rod_recursive(length, prices)


def test_cut_rod_recursive2():
    prices = [0, 1, 5, 8, 9, 10, 17, 17, 20, 24, 30]
    length = 9
    expected_result = 25
    assert expected_result == cut_rod_recursive(length, prices)


def test_cut_rod_recursive3():
    prices = [0, 1, 5, 8, 9, 10, 17, 17, 20, 24, 30]
    length = 15
    expected_result = 43
    assert expected_result == cut_rod_recursive(length, prices)

#############################################################################################################
#############################################################################################################
#############################################################################################################