# Definition for a binary tree node.
from typing import List


class NumArray:

    def __init__(self, nums: List[int]):
        self.tree = [0] * (2 * len(nums))
        self.build_segment_tree(nums)

    def update(self, index: int, val: int) -> None:
        index += len(self.tree) // 2
        self.tree[index] = val
        while index > 0:
            left = index
            right = index
            if index % 2 == 1:
                left = index - 1
            else:
                right = index + 1
            self.tree[index//2] = self.tree[left] + self.tree[right]
            index //= 2

    def sumRange(self, left: int, right: int) -> int:
        n = len(self.tree) // 2
        left += n
        right += n
        total = 0
        while left <= right:
            if (left % 2) == 1:
                total += self.tree[left]
                left += 1

            if (right % 2) == 0:
                total += self.tree[right]
                right -= 1

            left //= 2
            right //= 2

        return total

    def build_segment_tree(self, nums):
        for i in range(len(nums)):
            self.tree[i+len(nums)] = nums[i]
        for i in range(len(nums) - 1, 0, -1):
            self.tree[i] = self.tree[i * 2] + self.tree[i * 2 + 1]
