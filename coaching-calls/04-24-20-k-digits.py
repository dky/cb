def foo(s, k):
    if k >= len(s):
        return '0'
    # use a stack
    # while we have k left,
    # and the previously seen element is larger than our currrent element,
    # we should be popping
    stack = []
    # //[2, 6, 5]
    # //5?
    # 8 1
    for i in range(len(s)):
        while k != 0 and stack != [] and stack[-1] > s[i]:
            stack.pop()
            k -= 1
        stack.append(s[i])
    return ''.join(stack)


# edge case 1
# returns 11
# s = '11'
# k = 1

# edge case 2
# 0008? why?
s = '10008'
k = 1

print(foo(s, k))
