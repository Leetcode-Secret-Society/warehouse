from typing import List

class Solution:
    def trap(self, height: List[int]) -> int:
        water = 0
        highest = height[0]
        peak = [highest]

        for i in range(1, len(height)):

            while len(peak) > 1 and height[i] > peak[-1]:
                if highest == peak[-1]:
                    break
                peak.pop()
            highest = max(highest, height[i])
            peak.append(height[i])

        peak_index = 0
        over_highest = False
        for h in height:
            if h == peak[peak_index]:
                peak_index += 1
                if peak_index > len(peak):
                    break
                if peak[peak_index-1] == highest:
                    over_highest = True
            else:
                if over_highest:
                    water += (peak[peak_index] - h)
                else:
                    water += (peak[peak_index-1] - h)

        return water
print(Solution().trap([4]))