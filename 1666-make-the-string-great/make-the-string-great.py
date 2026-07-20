class Solution(object):
    def makeGood(self, s):
        stack = []
        for letter in s:
            if stack and abs(ord(letter) - ord(stack[-1])) == 32:
                stack.pop()
            else:
                stack.append(letter)
        return "".join(stack)