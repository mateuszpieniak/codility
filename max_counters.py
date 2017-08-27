def solution(N, A):
    counters = [0] * N
    max_value = 0
    last_value = 0
    for a in A:
        if a == N + 1:
            last_value = max_value
            continue

        counters[a - 1] = max(counters[a - 1], last_value) + 1
        max_value = max(max_value, counters[a - 1])

    for i in range(N):
        counters[i] = max(counters[i], last_value)
    return counters
