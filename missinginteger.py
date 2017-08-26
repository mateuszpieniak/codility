def solution(A):
    N = len(A)
    counter = [0] * (N + 1)

    for a in A:
        if 1 <= a <= N + 1:
            counter[a - 1] = 1

    for i in range(0, N + 1):
        if counter[i] == 0:
            return i + 1
    return 1
