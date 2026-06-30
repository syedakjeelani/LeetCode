class Solution(object):
    def pickGifts(self, gifts, k):
        heap = [-x for x in gifts if x > 0]
        heapq.heapify(heap)
        while k:
            result = (floor(sqrt(-1*(heap[0]))))

            heapq.heapreplace(heap, -result)
            k -= 1
        return -1 * (int(sum(heap)))   
        