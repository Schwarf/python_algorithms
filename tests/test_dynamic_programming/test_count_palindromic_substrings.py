from dynamic_programming.count_palindromic_substrings import count_palindromic_substrings_no_dp, count_palindromic_substrings
import pytest

test_cases = [
    ("abc", 3),
    ("aaa", 6),
    ("abba", 6),
    ("dnncbwoneinoplypwgbwktmvkoimcooyiwirgbxlcttgteqthcvyoueyftiwgwwxvxvg", 77),
    ("longtimenosee", 14),
    ("cuuedxumdolqdytmcudgqmxcwelatcphpvmqqgahbgjklekehgsulsyuhdxaggumsqpktltsytkoo", 84),
    ("ttttttttttttttttttttt", 231)
]


@pytest.mark.parametrize("string, expected_result", test_cases)
def test_count_palindromic_substrings_no_dp(string: str, expected_result: int):
    assert expected_result == count_palindromic_substrings_no_dp(string)

##################################################################################################################
##################################################################################################################
##################################################################################################################


@pytest.mark.parametrize("string, expected_result", test_cases)
def test_count_palindromic_substrings(string: str, expected_result: int):
    assert expected_result == count_palindromic_substrings(string)

