def solution(A):
    N = len(A)
    sum_all = (N + 1) * (N + 2) // 2
    sum_A = sum(A)
    return sum_all - sum_A
