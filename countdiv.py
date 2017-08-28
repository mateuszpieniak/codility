def solution(A, B, K):
    div_result = B / K - A / K

    if A % K == 0:
        div_result += 1

    return div_result
