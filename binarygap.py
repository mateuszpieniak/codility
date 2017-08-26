def solution(N):
    max_gap = 0
    counter_value = 0
    counter_status = False

    while N > 0:
        remainder = N % 2

        if remainder == 1:
            counter_status = True
            max_gap = max(max_gap, counter_value)
            counter_value = 0

        if counter_status and remainder == 0:
            counter_value += 1

        N /= 2
    return max_gap
