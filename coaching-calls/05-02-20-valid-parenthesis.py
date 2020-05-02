# Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

'''
#push initial to stack
#pop

# Example 1:
# Input: "()"
# Output: true

# Example 2:
# Input: "()[]{}"
# Output: true

# Example 3:
# Input: "(]"
# Output: false

(

] if item != ")"

if stack empty = return false ?


# Example 4:
# Input: "([)]"
# Output: false

([)]

# Example 5:
# Input: "{[]}"
# Output: true

stack = empty

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
input = "{[]}"
stack = []


for ch in input:
    if ch = "(, [, {"
        stack.append(ch)


    if ch = ")" && stack.peak(-1) == (
        stack.pop

    if ch = "]" && stack.peak(-1) == [
        stack.pop

    if ch = "}" && stack.peak(-1) == {
        stack.pop

if stack.empty:
    return True

return False

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
'''


def validate(s):
    pass


# class Solution {
# public:
#     bool isValid(string s) {
#     }
# };
