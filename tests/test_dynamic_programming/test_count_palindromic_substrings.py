from dynamic_programming.count_palindromic_substrings import count_palindromic_substrings_no_dp, count_palindromic_substrings


def test_count_palindromic_substrings_no_dp():
    string = "abc"
    expected_result = 3
    assert expected_result == count_palindromic_substrings_no_dp(string)


def test_count_palindromic_substrings_no_dp2():
    string = "aaa"
    expected_result = 6
    assert expected_result == count_palindromic_substrings_no_dp(string)


def test_count_palindromic_substrings_no_dp3():
    string = "abba"
    expected_result = 6
    assert expected_result == count_palindromic_substrings_no_dp(string)


def test_count_palindromic_substrings_no_dp4():
    string = "dnncbwoneinoplypwgbwktmvkoimcooyiwirgbxlcttgteqthcvyoueyftiwgwwxvxvg"
    expected_result = 77
    assert expected_result == count_palindromic_substrings_no_dp(string)


def test_count_palindromic_substrings_no_dp5():
    string = "longtimenosee"
    expected_result = 14
    assert expected_result == count_palindromic_substrings_no_dp(string)


def test_count_palindromic_substrings_no_dp6():
    string = "cuuedxumdolqdytmcudgqmxcwelatcphpvmqqgahbgjklekehgsulsyuhdxaggumsqpktltsytkoo"
    expected_result = 84
    assert expected_result == count_palindromic_substrings_no_dp(string)


def test_count_palindromic_substrings_np_dp7():
    string = "ttttttttttttttttttttt"
    expected_result = 231
    assert expected_result == count_palindromic_substrings_no_dp(string)

##################################################################################################################
##################################################################################################################
##################################################################################################################


def test_count_palindromic_substrings():
    string = "abc"
    expected_result = 3
    assert expected_result == count_palindromic_substrings(string)


def test_count_palindromic_substrings2():
    string = "aaa"
    expected_result = 6
    assert expected_result == count_palindromic_substrings(string)


def test_count_palindromic_substrings3():
    string = "abba"
    expected_result = 6
    assert expected_result == count_palindromic_substrings(string)


def test_count_palindromic_substrings4():
    string = "dnncbwoneinoplypwgbwktmvkoimcooyiwirgbxlcttgteqthcvyoueyftiwgwwxvxvg"
    expected_result = 77
    assert expected_result == count_palindromic_substrings(string)


def test_count_palindromic_substrings5():
    string = "longtimenosee"
    expected_result = 14
    assert expected_result == count_palindromic_substrings(string)


def test_count_palindromic_substrings6():
    string = "cuuedxumdolqdytmcudgqmxcwelatcphpvmqqgahbgjklekehgsulsyuhdxaggumsqpktltsytkoo"
    expected_result = 84
    assert expected_result == count_palindromic_substrings(string)


def test_count_palindromic_substrings7():
    string = "ttttttttttttttttttttt"
    expected_result = 231
    assert expected_result == count_palindromic_substrings(string)
