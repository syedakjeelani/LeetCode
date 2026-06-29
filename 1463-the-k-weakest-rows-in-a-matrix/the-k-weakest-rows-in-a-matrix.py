class Solution(object):
    def kWeakestRows(self, mat, k):
        heap = []
        for idx, row in enumerate(mat):
            strength = sum(row)
            heapq.heappush(heap, (strength, idx))
        ans = []
        for k in range(k):
            strength, idx = heapq.heappop(heap)
            ans.append(idx)
        return ans