class Solution(object):
    def topKFrequent(self, nums, k):
        freq = {}
        for n in nums:
            freq[n] = freq.get(n, 0) + 1
        heap = [(-count, n) for n, count in freq.items()]
        heapq.heapify(heap)
        return[heapq.heappop(heap)[1] for _ in range(k)]
        