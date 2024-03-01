class Solution:
    def _calculate_sum_of_peaks(self, maxHeights):
        sum_of_peaks = []
        monotonic_stack = []
        curr_sum = 0
        for i, h in enumerate(maxHeights):
            while monotonic_stack and monotonic_stack[-1][1] > h:
                prev_i, prev_h = monotonic_stack.pop()
                if monotonic_stack:
                    count = prev_i - monotonic_stack[-1][0]
                else:
                    count = prev_i + 1
                curr_sum -= (prev_h - h) * count
            sum_of_peaks.append(curr_sum)
            if not monotonic_stack or monotonic_stack[-1][1] <= h:
                curr_sum += h
                monotonic_stack.append((i, h))
        return sum_of_peaks

    def maximumSumOfHeights(self, maxHeights: List[int]) -> int:
        left_sum_of_peaks = self._calculate_sum_of_peaks(maxHeights)
        right_sum_of_peaks = list(reversed(self._calculate_sum_of_peaks(reversed(maxHeights))))
        #print(left_sum_of_peaks, right_sum_of_peaks)
        return max([left_sum+right_sum+peak_h for left_sum, right_sum, peak_h in zip(left_sum_of_peaks, right_sum_of_peaks, maxHeights)])
