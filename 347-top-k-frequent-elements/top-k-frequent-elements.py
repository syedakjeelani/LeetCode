class Solution(object):
    def topKFrequent(self, nums, k):
        freq = {}
        for n in nums:
            if n in freq:
                freq[n] += 1
            else:
                freq[n] = 1
        heap = []
        heapq.heapify(heap)
        for n, count in freq.items():
            heapq.heappush(heap, (-count, n))
        result = []
        while k:
            count, n = heapq.heappop(heap)
            result.append(n)
            k -= 1
        return result
        
        