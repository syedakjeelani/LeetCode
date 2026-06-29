class Solution(object):
    def maximumSum(self, nums):
        hashmap = {}
        ans = -1
        for n in nums:
            temp = n
            digitsum = sum(int(d) for d in str(n))
            if digitsum in hashmap:
                ans = max(ans, hashmap[digitsum] + n )
            hashmap[digitsum] = max(hashmap.get(digitsum,0),n)
        return ans