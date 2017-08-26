from math import fabs


def abs_diff(x, y):
    return fabs(x - y)


def solution(A):
    N = len(A)

    sum_left = A[0]
    sum_right = sum(A[1:])
    min_diff = abs_diff(sum_left, sum_right)

    for P in range(1, N - 1):
        sum_left += A[P]
        sum_right -= A[P]
        min_diff = min(min_diff, abs_diff(sum_left, sum_right))

    return int(min_diff)
