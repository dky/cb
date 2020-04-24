# Edge 1
# s = '11'
# returns 11?
# k = 1

# Edge 2
s = '10008'
k = 1
# returns 0008?


def foo(s, k):
    # print(len(s))
    # if k >= len(s) return "0"
    if k >= len(s):
        return '0'

    # init a stack
    stack = []

    for i in range(len(s)):
        # print(i)
        # Ensure k is not 0
        # Ensure the stack is not empty

        # print(s[i])
        # print(stack[-1])
        print(stack)

        while k != 0 and stack != [] and stack[-1] > s[i]:
            # pop off stack
            stack.pop()
            # decrement k
            k -= 1
        stack.append(s[i])
    # return empty string joined to stack.
    return ''.join(stack)


print(foo(s, k))
