def solution(X, A):
    N = len(A)
    counter = [0] * X
    n_leaves = 0
    for i in range(N):
        if counter[A[i] - 1] == 0:
            counter[A[i] - 1] = 1
            n_leaves += 1
        if n_leaves == X:
            return i
    return -1
