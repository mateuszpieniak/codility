def prefix_sum(S):
    N = len(S)
    P = [[0] * 4] * (N + 1)
    for i in range(1, N + 1):
        P[i] = P[i - 1][:]  # need for copying value
        P[i][S[i - 1]] += 1
    return P


def count_total(P, x, y):
    return [a - b for a, b in zip(P[y + 1], P[x])]


def first_non_zero_idx(A):
    i = 0
    while A[i] == 0:
        i += 1
    return i


def solution(S, P, Q):
    mapping = {
        'A': 0,
        'C': 1,
        'G': 2,
        'T': 3,
    }

    S = map(mapping.get, S)
    sums_per_letter = prefix_sum(S)

    M = len(P)
    result = [0] * M
    for i in range(M):
        slice_diff = count_total(sums_per_letter, P[i], Q[i])
        result[i] = first_non_zero_idx(slice_diff) + 1  # +1 for changing mapping indexing
    return result
