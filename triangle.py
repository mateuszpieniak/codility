def is_triangular(A, P, Q, R):
    cond1 = A[P] + A[Q] > A[R]
    cond2 = A[Q] + A[R] > A[P]
    cond3 = A[R] + A[P] > A[Q]
    return cond1 and cond2 and cond3


def solution(A):
    A.sort()
    N = len(A)
    for i in range(0, N - 2):
        if is_triangular(A, i, i + 1, i + 2):
            return 1
    return 0
