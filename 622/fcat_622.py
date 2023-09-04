class MyCircularQueue:

    def __init__(self, k: int):
        self.queue = [0] * k
        self.capacity = 0
        self.head_index = 0
        self.max_capacity = k

    def enQueue(self, value: int) -> bool:
        if self.isFull():
            return False
        self.capacity += 1
        self.queue[self.rear_index()] = value
        return True

    def deQueue(self) -> bool:
        if self.isEmpty():
            return False
        self.queue[self.head_index] = None
        self.head_index += 1
        self.head_index = self.head_index % self.max_capacity
        self.capacity -= 1
        return True

    def Front(self) -> int:
        if self.isEmpty():
            return -1
        return self.queue[self.head_index]

    def Rear(self) -> int:
        if self.isEmpty():
            return -1
        return self.queue[self.rear_index()]

    def isEmpty(self) -> bool:
        return self.capacity == 0

    def isFull(self) -> bool:
        return self.capacity == self.max_capacity

    def rear_index(self):
        return (self.head_index + self.capacity - 1) % self.max_capacity