class Solution(object):
    def maxProduct(self, nums):
        largest, second = 0, 0 
        for n in nums:
            if n > largest:
                second = largest
                largest = n
            elif n > second:
                second = n
        return (largest - 1) * (second - 1)
        