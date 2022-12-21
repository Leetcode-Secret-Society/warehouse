import heapq
class MaxStack:
    def __init__(self):
        self.heap = []
        self.count = 0
        self.stack = []
        self.removed_indices = set()

        return 

    def push(self, x: int) -> None:
        heapq.heappush(self.heap, (-x, self.count))
        self.stack.append((x, self.count))
        self.count -= 1
        return 

    def pop(self) -> int:
        while self.stack[-1][1] in self.removed_indices:
            self.stack.pop()
        value, index = self.stack.pop()
        self.removed_indices.add(index)
        return value

    def top(self) -> int:
        while self.stack[-1][1] in self.removed_indices:
            self.stack.pop()
        return self.stack[-1][0]

    def peekMax(self) -> int:
        while self.heap[0][1] in self.removed_indices:
            heapq.heappop(self.heap)
        return -self.heap[0][0]

    def popMax(self) -> int:
        while self.heap[0][1] in self.removed_indices:
            heapq.heappop(self.heap)
        value, index = heapq.heappop(self.heap)
        self.removed_indices.add(index)
        return -value


# Your MaxStack object will be instantiated and called as such:
# obj = MaxStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.peekMax()
# param_5 = obj.popMax()
