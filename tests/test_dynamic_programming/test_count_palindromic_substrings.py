from dynamic_programming.count_palindromic_substrings import count_palindromic_substrings_no_dp


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
