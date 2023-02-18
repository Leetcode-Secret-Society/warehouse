class Solution:
    def maxArea(self, h: int, w: int, horizontalCuts: List[int], verticalCuts: List[int]) -> int:
        horizontalCuts.sort()
        verticalCuts.sort()
        horizontalCuts.append(h)
        verticalCuts.append(w)
        previous_hc = 0
        max_width = 0
        for hc in horizontalCuts:
            max_width = max(max_width, hc-previous_hc)
            previous_hc = hc
        max_height = 0
        previous_vc = 0
        for vc in verticalCuts:
            max_height = max(max_height, vc - previous_vc)
            previous_vc = vc
        return (max_width * max_height) % 1000000007
