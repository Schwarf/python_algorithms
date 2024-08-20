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

