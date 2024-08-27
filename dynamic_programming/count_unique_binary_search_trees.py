# Given an integer n, return the number of structurally unique BST's (binary search trees) which has exactly n nodes
# of unique values from 1 to n.
# For n=1,3 the numbers are 1 and 5
# This is principle nothing else but computing the Catalan number C_n.
def count_unique_bst_recursive(n: int):
    if n == 0 or n == 1:
        return 1
    # The key observation is for a binary search: If you pick a number i with 1 <= i <= n as root-value then the
    # left treehas i-1 values (1.. i-1) and the right tree has n-i values (i+1..n). Now since each value between
    # 1..n can be the root value we multiply the number of left-values and right-values for each i and add them up.
    count = 0
    for i in range(1, n + 1):
        count += count_unique_bst_recursive(i - 1) * count_unique_bst_recursive(n - i)
    return count


def count_count_unique_bst_bottom_up(n: int):
    dp = [0] * (n + 1)
    dp[0] = 1
    dp[1] = 1
    # The outer loop computes the ith Catalan number
    # The inner loop implements the formula: C_i = \Sum_{j=1}^i C_{j−1} \times C_{i-j}
    for i in range(2, n + 1):
        for j in range(1, i + 1):
            dp[i] += dp[j - 1] * dp[i - j]
    return dp[n]
