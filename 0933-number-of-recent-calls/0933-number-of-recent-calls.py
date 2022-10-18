class RecentCounter:

    def __init__(self):
        self.Q = deque()

    def ping(self, t: int) -> int:
        self.Q.append(t)
        
        while len(self.Q) > 0 and (t - self.Q[0]) > 3000: # Q[0]和即将出栈的元素Q.popleft()
            self.Q.popleft()
        return len(self.Q)
        


# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)