class Solution(object):
    def minStoneSum(self, piles, k):
        heap = [-x for x in piles if x > 0]
        heapq.heapify(heap)
        while k:    
            remains = (heap[0] + (floor( -1 * (heap[0]) / 2)))
            heapq.heapreplace(heap, remains)
            k -= 1
        return int(-1 * sum(heap))