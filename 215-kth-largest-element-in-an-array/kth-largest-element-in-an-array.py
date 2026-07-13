class Solution(object):
    def findKthLargest(self, nums, k):
        heap = nums[:k]
        heapq.heapify(heap)
        for n in nums[k:]:
            if n > heap[0]:
                heapq.heappush(heap,n)
                heapq.heappop(heap)
        return heap[0]
        
        