from typing import List
from collections import deque, defaultdict
from heapq import heappush, heappop, nsmallest


class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        current_array = deque()
        current_array.append(nums[0])
        num_count = defaultdict(int)
        num_count[nums[0]] += 1
        max_heap_list = []
        min_heap_list = []
        heappush(max_heap_list, nums[0] * -1)
        heappush(min_heap_list, nums[0])
        maximum = nums[0]
        minimum = nums[0]
        maximum_length = 1
        for i in range(1, len(nums)):
            if maximum < nums[i]:
                maximum = nums[i]
                if maximum - minimum > limit:
                    maximum_length = max(maximum_length, len(current_array))
                    new_min = minimum
                    while maximum - new_min > limit:
                        if num_count[new_min] != 0:
                            while current_array[0] != new_min:
                                num_count[current_array.popleft()] -= 1
                            num_count[current_array.popleft()] -= 1
                        else:
                            if not min_heap_list:
                                new_min = nums[i]
                            else:
                                new_min = heappop(min_heap_list)

                    minimum = new_min
            if minimum > nums[i]:
                minimum = nums[i]
                if maximum - minimum > limit:
                    maximum_length = max(maximum_length, len(current_array))
                    new_max = maximum
                    while new_max - minimum > limit:
                        if num_count[new_max] != 0:
                            while current_array[0] != new_max:
                                num_count[current_array.popleft()] -= 1
                            num_count[current_array.popleft()] -= 1
                        else:
                            if not max_heap_list:
                                new_max = nums[i]
                            else:
                                new_max = heappop(max_heap_list)
                                new_max *= -1
                    maximum = new_max
            current_array.append(nums[i])
            heappush(max_heap_list, nums[i] * -1)
            heappush(min_heap_list, nums[i])
            num_count[nums[i]] += 1
        return max(maximum_length, len(current_array))


print(Solution().longestSubarray([1],4))
