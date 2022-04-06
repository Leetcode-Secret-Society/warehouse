from collections import defaultdict
from typing import List


class FirstUnique:

    def __init__(self, nums: List[int]):
        self.counter = defaultdict(int)
        self.nums = nums
        for num in nums:
            self.counter[num] += 1
        self.index = 0

        for index in range(len(nums)):
            if self.counter[nums[index]] == 1:
                self.index = index
                break
        else:
            self.index = -1


    def showFirstUnique(self) -> int:
        if self.index == -1:
            return -1
        return self.nums[self.index]

    def add(self, value: int) -> None:
        self.counter[value] += 1
        self.nums.append(value)
        if self.index == -1:
            if self.counter[value] == 1:
                self.index = len(self.nums) - 1
        elif value == self.nums[self.index]:
            for index in range(self.index, len(self.nums)):
                if self.counter[self.nums[index]] == 1:
                    self.index = index
                    break
            else:
                self.index = -1
