class Solution(object):
    def topKFrequent(self, nums, k):
        
        #using hashmap and getting the frequency count manually
        freq = {}
        for n in nums:
            if n in freq:
                freq[n] += 1
            else:
                freq[n] = 1
        
        #creating a heap and storing count and the item in the heap
        heap = []
        heapq.heapify(heap)
        for n, count in freq.items():
            heapq.heappush(heap, (-count, n))
        
        #creating a result array to store the result
        result = []
        while k:
            count, n = heapq.heappop(heap)
            result.append(n)
            k -= 1

        #returning the result
        return result
        
        