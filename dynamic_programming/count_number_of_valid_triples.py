from typing import List


# There are n number in an array. Each number has a unique value.
# You have to form valid triple:
# A valid triple with indices (i, j, k) is valid (array[i], array[j], array[k]).
# if: (array[i] < array[j] < array[k]) or (array[i] > array[j] > array[k]) where (0 <= i < j < k < n).
# Return the number of valid triples you can form given the conditions.
# LC-1395
def valid_triples(input_array: List[int]) -> int:
    count = 0
    for i in range(0, len(input_array) - 2):
        for j in range(i + 1, len(input_array) - 1):
            for k in range(j + 1, len(input_array)):
                if input_array[k] > input_array[j] > input_array[i]:
                    count += 1
                elif input_array[i] > input_array[j] > input_array[k]:
                    count += 1
    return count


def valid_triples_dp(input_array: List[int]) -> int:
    n = len(input_array)
    count_smaller_left = [0] * n
    count_greater_left = [0] * n
    count_greater_right = [0] * n
    count_smaller_right = [0] * n
    for i in range(1, n):
        for j in range(0, i):
            if input_array[j] < input_array[i]:
                count_smaller_left[i] += 1
            if input_array[j] > input_array[i]:
                count_greater_left[i] += 1

    for i in range(n - 2, -1, -1):
        for j in range(i + 1, n):
            if input_array[j] > input_array[i]:
                count_greater_right[i] += 1
            if input_array[j] < input_array[i]:
                count_smaller_right[i] += 1
    count = 0
    for i in range(1, n - 1):
        count += count_smaller_left[i] * count_greater_right[i]
        count += count_greater_left[i] * count_smaller_right[i]

    return count
