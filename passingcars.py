def prefix_sum(A):
    N = len(A)
    P = [0] * (N + 1)
    for i in range(1, N + 1):
        P[i] = P[i - 1] + A[i - 1]
    return P


def count_total(P, x, y):
    return P[y + 1] - P[x]


def solution(A):
    N = len(A)
    P = prefix_sum(A)

    passing_cars = 0
    for i in range(N):
        if passing_cars > 1000000000:
            return -1
        elif A[i] == 0:
            passing_cars += count_total(P, i, N - 1)
    return passing_cars
