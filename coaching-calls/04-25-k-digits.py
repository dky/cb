# Edge 1
# s = '11'
# returns 11?
# k = 1

# # Edge 2
# s = '324'
# k = 2
# # returns 0008?

# Edge 2
#s = '100089'
s = '12498'
k = 2
# returns 0008?
# Good way to get rid of leading zeros?

#12498

#498
#124 * Potentially smallest
#249
#298
#198


def rmkd(s, k):
    # print(len(s))
    # if k >= len(s) return "0"
    if k >= len(s):
        return '0'

    # init a stack
    stack = []

    for i in range(len(s)):

        #stack [1]
        #stack [12]
        #is 1 > 2? Nope...

        #Append 2

        #         [1]
        #         [1,2]

        #         [1,2] 2 > 4?
        #         [1,2,4]
        #         #peak = last element added to the stack.
        #         [1,2,4] is 4 > 9
        #         [1,2,4,9]
        #         [1,2,4,9] is 9 > 8? y

        #         [1,2,4]??

        #         [1,2,4,8]

        while k != 0 and stack != [] and stack[-1] > s[i]:
            # print("peek of stack is {}".format(stack[-1]))
            # pop off stack
            print(stack.pop())
            # decrement k
            k -= 1

        #fall through
        stack.append(s[i])

    # return empty string joined to stack.
    print("after loop")
    print(stack)

    ans = str(int(''.join(stack)))  # remove leading 0s
    # k remaining
    if k >= len(ans):
        return '0'

    return ans[:
               -k]  # if k is not 0, remove elements from the end because that is the best we can do


print(rmkd(s, k))
