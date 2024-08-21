# Given a string s, return the number of palindromic substrings in it.
# A string is a palindrome when it reads the same backward as forward.
# A substring is a contiguous sequence of characters within the string.


def count_palindromic_substrings_no_dp(string: str):
    n = len(string)
    count = 0
    for i in range(0, n):
        for j in range(i+1, n+1):
            if string[i:j] == string[i:j][::-1]:
                count += 1
    return count
