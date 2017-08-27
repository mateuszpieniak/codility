def solution(A):
    N = len(A)
    counter = [0] * N

    for a in A:
        if a <= N:
            counter[a - 1] = 1

    for i in range(0, N):
        if counter[i] == 0:
            return 0
    return 1
