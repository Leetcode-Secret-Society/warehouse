from typing import List
from collections import deque


class TreeNode():
    def __init__(self, left=None, right=None):
        self.left = left
        self.right = right


class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        root = TreeNode()
        for num in nums:
            cur_node = root
            for d in num:
                if d == '0':
                    if cur_node.left is None:
                        cur_node.left = TreeNode()
                    cur_node = cur_node.left
                else:
                    if cur_node.right is None:
                        cur_node.right = TreeNode()
                    cur_node = cur_node.right

        queue = deque([(root, "")])

        while queue:
            node, cur_string = queue.popleft()
            if not node.left:
                return cur_string + "0" + "0" * (len(nums[0]) - len(cur_string) - 1)
            if not node.right:
                return cur_string + "1" + "0" * (len(nums[0]) - len(cur_string) - 1)
            queue.append((node.left, cur_string + "0"))
            queue.append((node.right, cur_string + "1"))


print(Solution().findDifferentBinaryString(["00", "01"]))
