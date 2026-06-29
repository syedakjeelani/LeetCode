class Solution(object):
    def fillCups(self, amount):
        """
        input is arraz output is integer
        i need to remember the amount of cups left
        in one iteration we read the amount of cups 
        I stop when there are no cups
        yes i can explain t 
        We read the elements from the array 
        Find out the biggest element and the second largest element
        and start subtracing them togeother and do it till we get the second largest number and so on and while doing it for everz iteration increase second count
        example: [1,4,2]
        [1,3,1]
        [0,2,1]
        [0,1,0]
        [0,0,0]
        """
        heap = [-x for x in amount if x > 0]
        heapq.heapify(heap)
        seconds = 0
        while len(heap) > 1:
            first = -heapq.heappop(heap)
            second = -heapq.heappop(heap)
            first -= 1
            second -= 1
            if first > 0:
                heapq.heappush(heap, -first)
            if second > 0:
                heapq.heappush(heap, -second)
            seconds +=1
        return seconds + (-heap[0] if heap else 0)

        