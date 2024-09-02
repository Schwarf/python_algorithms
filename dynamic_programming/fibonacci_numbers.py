# Compute th nth fibonacci number

def fibonacci_number(n: int) -> int:
    if n == 0:
        return 0
    if n == 1:
        return 1
    second_to_last = 0
    last = 1
    current = 0
    for i in range(2, n+1):
        current = last + second_to_last
        second_to_last = last
        last = current

    return current

