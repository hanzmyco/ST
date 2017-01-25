def longestValidParentheses(s):
    stack = []
    start = 0
    res = 0
    for i in xrange(0, len(s)):
        if s[i] == '(':
            stack.append(i)
        else:
            if len(stack) == 0:
                start = i + 1
            else:
                stack.pop()
                if len(stack) == 0:
                    res = max(res, i - start + 1)
                else:
                    res = max(res, i - stack[len(stack) - 1])
    return res