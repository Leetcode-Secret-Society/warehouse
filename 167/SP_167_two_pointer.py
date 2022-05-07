class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        """"""
        [2,5,7,11,15]
        12
        """"""
        left = 0
        right = len(numbers) - 1
        while left < right:
            # print(str(left)+"-"+str(right))
            sum = numbers[left] + numbers[right]
            if sum < target:
                left += 1
            elif sum > target:
                right -= 1
            else:
                return [left+1, right+1]
        return []
