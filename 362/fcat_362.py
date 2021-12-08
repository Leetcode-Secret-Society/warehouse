from collections import deque

class HitCounter:

    def __init__(self):
        self.hit_count_in_5m = 0
        self.hit_history = deque()

    def hit(self, timestamp: int) -> None:
        self.hit_history.append(timestamp)
        self.hit_count_in_5m += 1

    def getHits(self, timestamp: int) -> int:
        while self.hit_history:
            if self.hit_history[0] + 300 <= timestamp:
                self.hit_history.popleft()
                self.hit_count_in_5m -= 1
            else:
                break
        return self.hit_count_in_5m

