from math import ceil


def solution(X, Y, D):
    return int(ceil(1.0 * (Y - X) / D))
