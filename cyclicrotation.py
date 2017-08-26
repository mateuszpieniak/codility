def solution(A, K):
    N = len(A)
    return [A[(i - K) % N] for i in range(len(A))]