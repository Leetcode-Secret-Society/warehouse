class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        smallest = sys.maxsize
        second = sys.maxsize
        for i in range(len(nums)):
            # if smallest > nums[i]:
            if smallest >= nums[i]:
                smallest = nums[i]
            # elif second > nums[i] and nums[i] > smallest:
            elif second >= nums[i]:
                second = nums[i]
            elif nums[i] > second:
                return True
        return False

