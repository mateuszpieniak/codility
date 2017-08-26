def solution(A):
    xor_result = 0
    for a in A:
        xor_result ^= a
    return xor_result
