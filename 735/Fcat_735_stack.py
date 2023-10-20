from typing import List


class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        for asteroid in asteroids:
            if asteroid < 0:
                while stack and 0 < stack[-1] < asteroid * -1:
                    stack.pop()
                if not stack or stack[-1] < 0:
                    stack.append(asteroid)
                elif stack[-1] == asteroid * -1:
                    stack.pop()
            else:
                stack.append(asteroid)
        return stack
