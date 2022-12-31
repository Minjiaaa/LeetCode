class MyStack:

    def __init__(self):
        self.queue1 = collections.deque()
        self.queue2 = collections.deque()

    def push(self, x: int) -> None:
        self.queue2.append(x) # [3 -> 2 -> 1]
        while self.queue1:
            self.queue2.append(self.queue1.popleft()) #[3, 2, 1]
        self.queue1, self.queue2 = self.queue2, self.queue1
        

    def pop(self) -> int:
        return self.queue1.popleft()
        

    def top(self) -> int:
        return self.queue1[0]
        

    def empty(self) -> bool:
        return not self.queue1


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()