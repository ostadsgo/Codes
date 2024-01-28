from heapq import *


class MedianFinder:
    def __init__(self):
        self.first_half = []
        self.second_half = []

    def addNum(self, num: int) -> None:
        # We must multiply the number by -1 because
        # Python doesn't include built-in max-heap atm.
        heappush(self.first_half, -num)
        popped_element = heappop(self.first_half)
        heappush(self.second_half, -popped_element)

        if len(self.first_half) < len(self.second_half):
            popped_element = heappop(self.second_half)
            heappush(self.first_half, -popped_element)

    def findMedian(self) -> float:
        if len(self.first_half) == len(self.second_half):
            return (-self.first_half[0] + self.second_half[0]) / 2
        return -self.first_half[0]


medianFinder = MedianFinder()
medianFinder.addNum(1)
medianFinder.addNum(2)
medianFinder.findMedian()
medianFinder.addNum(3)
medianFinder.findMedian()
