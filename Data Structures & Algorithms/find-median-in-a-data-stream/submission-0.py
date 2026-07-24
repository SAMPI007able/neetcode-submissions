class MedianFinder:

    def __init__(self):
        self.left_heap = []
        self.right_heap = []

    def addNum(self, num: int) -> None:
        if not self.left_heap or num < -self.left_heap[0]:
            heapq.heappush(self.left_heap, -num)
            if len(self.left_heap) > 1 + len(self.right_heap):
                heapq.heappush(self.right_heap, -heapq.heappop(self.left_heap))
        else:
            heapq.heappush(self.right_heap, num)
            if len(self.right_heap) > len(self.left_heap):
                heapq.heappush(self.left_heap, -heapq.heappop(self.right_heap))

    def findMedian(self) -> float:
        if len(self.right_heap) == len(self.left_heap):
            return (self.right_heap[0] + (-self.left_heap[0])) / 2
        return -self.left_heap[0]
        
        