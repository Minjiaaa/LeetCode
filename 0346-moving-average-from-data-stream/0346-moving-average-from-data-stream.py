class MovingAverage:

    def __init__(self, size: int):
        self.size = size
        self.queue = [ ]
        

    def next(self, val: int) -> float:
        size = self.size
        queue = self.queue 
        queue.append(val)
        
        window_sum = sum(queue[-size:])
        
        return window_sum / min(len(queue), size)


# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)