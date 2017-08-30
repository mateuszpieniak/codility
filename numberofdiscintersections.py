def solution(A):
    N = len(A)

    if N == 0 or N == 1:
        return 0

    bounds_left = [(i - a, 1) for i, a in enumerate(A)]
    bounds_right = [(i + a, -1) for i, a in enumerate(A)]
    bounds = bounds_left + bounds_right
    bounds.sort(key=lambda x: x[0])
    disc_status = list(zip(*bounds)[1])

    curr_intersections = 0
    intersections = 0
    M = len(disc_status)
    for i in range(1, M):
        curr_intersections += disc_status[i]

        if disc_status[i] == 1:
            intersections += curr_intersections

        if intersections > 10000000:
            return -1

    return intersections

