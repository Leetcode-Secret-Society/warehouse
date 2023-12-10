from typing import List
from collections import defaultdict

class Solution:
    def numberOfGoodPartitions(self, nums: List[int]) -> int:
        num_index_list_mapping = defaultdict(list)
        for i in range(len(nums)):
            num_index_list_mapping[nums[i]].append(i)

        segments = []
        for value in num_index_list_mapping.values():
            segments.append((value[0], value[-1]))

        segments.sort()
        start, end = segments[0]
        segment_count = 0
        for i in range(1, len(segments)):
            cur_start, cur_end = segments[i]
            if end < cur_start:
                segment_count += 1
                start, end = cur_start, cur_end
            else:
                end = max(end, cur_end)

        return 2 ** segment_count % (10 ** 9 + 7)
