from typing import List


class Solution:
    def movesToMakeZigzag(self, nums: List[int]) -> int:
        def checkMoves(bigger, inputs):
            moves = 0
            for i in range(len(inputs)-1):
                if bigger:
                    if inputs[i+1] <= inputs[i]:
                        moves += (inputs[i] - inputs[i+1]) + 1
                        inputs[i] -= (inputs[i] - inputs[i+1]) + 1
                else:
                    if inputs[i] <= inputs[i+1]:
                        moves += (inputs[i+1] - inputs[i]) + 1
                        inputs[i+1] -= (inputs[i+1] - inputs[i]) + 1
                bigger = not bigger
            return moves

        return min(checkMoves(True, list(nums)), checkMoves(False, nums))


print(Solution().movesToMakeZigzag([10,4,4,10,10,6,2,3]))