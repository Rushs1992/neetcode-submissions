class MedianFinder:

    def __init__(self):
        self.arr = []
        self.res = 0
        

    def addNum(self, num: int) -> None:
        self.arr.append(num)
        self.arr.sort()

    def findMedian(self) -> float:
        n = len(self.arr)
        if n % 2 == 0:
            return (self.arr[n // 2 - 1] + self.arr[n // 2]) / 2.0
        else:
            return float(self.arr[n // 2])