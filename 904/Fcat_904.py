from typing import List


class StockSpanner:

    def __init__(self):
        self.index = 0
        self.lds_indexes = []
        self.lds_values = []

    def next(self, price: int) -> int:
        while self.lds_indexes:
            if self.lds_values[-1] <= price:
                self.lds_values.pop()
                self.lds_indexes.pop()
            else:
                break
        self.lds_indexes.append(self.index)
        self.lds_values.append(price)
        self.index += 1
        if len(self.lds_indexes) > 1:
            return self.lds_indexes[-1] - self.lds_indexes[-2]
        else:
            return self.lds_indexes[0] + 1

s = StockSpanner()
print(s.next(100))
print(s.next(80))
print(s.next(60))
print(s.next(70))
print(s.next(60))
print(s.next(75))
print(s.next(85))
