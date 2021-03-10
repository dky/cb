'''
x = "1234565432123456543456565656565" -> k = 5

219 -> 21, 19
0800

     /
    /  \
   /    \
  /      \
 /
/


s = 811119 
k = 8

// If k was > than s 
// Invalid index

// Not just removing the largest number... Is it?
81111
11119
// Sorting screws up order 
// discard things originally
// generic case?
// really large k
'''


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


# edge cases
# returns 11
s = '11'
k = 1

# second edge
# 0008? why?
s = '10008'  # coach you are breaking out
k = 1

print(foo(s, k))

# y = "87654321" ->
# k = 2
# nums = "122149"
# k = 1
# #O(n)
# current = 1
# 12321 = k
