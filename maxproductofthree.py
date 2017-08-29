from operator import mul


def solution(A):
    A.sort()
    N = len(A)

    some_prod = 1
    max_prod = reduce(mul, A[N - 3:], 1)
    if A[0] < 0 and A[1] < 0:
        some_prod = A[0] * A[1] * A[N - 1]
    return max(max_prod, some_prod)
