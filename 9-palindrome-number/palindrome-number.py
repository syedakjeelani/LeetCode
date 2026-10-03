class Solution(object):
    def isPalindrome(self, x):
        if x < 0: return False
        original = x
        reversedNumber = 0
        while x > 0:
            digit = x % 10
            reversedNumber = reversedNumber * 10 + digit
            x //= 10
        return original == reversedNumber
