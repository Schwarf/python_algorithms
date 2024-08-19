from dynamic_programming.coin_combinations import coin_combinations_classic, coin_combinations_top_down


def test_coin_combinations_classic1():
    input = [1, 2, 5]
    amount = 5
    expected_result = 4
    assert coin_combinations_classic(input, amount) is expected_result


def test_coin_combinations_classic2():
    input = [5]
    amount = 4
    expected_result = 0
    assert coin_combinations_classic(input, amount) == expected_result


def test_coin_combinations_classic3():
    input = [1]
    amount = 7
    expected_result = 1
    assert coin_combinations_classic(input, amount) == expected_result


def test_coin_combinations_classic4():
    input = [1, 2, 5]
    amount = 500
    expected_result = 12701
    assert coin_combinations_classic(input, amount) == expected_result

###################################################################################
###################################################################################
###################################################################################


def test_coin_combinations_top_down1():
    input = [1, 2, 5]
    amount = 5
    expected_result = 4
    assert coin_combinations_classic(input, amount) is expected_result


def test_coin_combinations_top_down2():
    input = [5]
    amount = 4
    expected_result = 0
    assert coin_combinations_top_down(input, amount) == expected_result


def test_coin_combinations_top_down3():
    input = [1]
    amount = 7
    expected_result = 1
    assert coin_combinations_top_down(input, amount) == expected_result


def test_coin_combinations_top_down4():
    input = [1, 2, 5]
    amount = 500
    expected_result = 12701
    assert coin_combinations_top_down(input, amount) == expected_result

