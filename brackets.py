def solution(S):
    brackets = {
        ']': '[',
        '}': '{',
        ')': '(',
    }

    stack = []
    for s in S:
        if s in brackets.values():
            stack.append(s)
        elif stack and brackets[s] == stack[-1]:
            stack.pop(-1)
        else:
            return 0

    return 0 if stack else 1