
# Given a grid with n rows and m columns count the ways from the upper right corner to the lower left corner.
# You can only move down or right.

def count_ways_in_2d(rows: int, columns: int):
    dp = [[0 for x in range(columns)] for y in range(rows)]
    dp[0] = [1]*columns
    for row in dp:
        row[0] = 1
    for row in range(1, rows):
        for col in range(1, columns):
            dp[row][col] = dp[row-1][col] + dp[row][col-1]
    return dp[rows-1][columns-1]



