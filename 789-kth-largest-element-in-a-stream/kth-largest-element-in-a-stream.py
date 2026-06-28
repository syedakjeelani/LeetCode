class KthLargest(object):

    def __init__(self, k, nums):
        self.k = k
        self.heap = nums[:k]
        heapq.heapify(self.heap)
        for n in nums[k:]:
            if self.heap[0] < n:
                heapq.heapreplace(self.heap, n)
        
    def add(self, val):
        if len(self.heap) < self.k:
            heapq.heappush(self.heap, val)
        elif val > self.heap[0]:
            heapq.heapreplace(self.heap, val)
        return self.heap[0]
        


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)