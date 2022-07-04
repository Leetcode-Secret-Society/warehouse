class Solution:
    def maxArea(self, height: List[int]) -> int:
        # O(n)
        result = 0
        i = 0
        j = len(height) - 1
        while i < j:
            dist = j - i
            h = min(height[j], height[i])
            volume = dist * h
            result = max(result, volume)
            #to get larger volume inside, search higher height
            if height[i] < height[j]: 
                i += 1
            else :
                j -= 1
        return result
        # O(n^2), TLE
        # result = 0
        # for i in range(0, len(height)):
        #     for j in range(i+1, len(height)):
        #         dist = j - i
        #         h = min(height[j], height[i])
        #         volume = dist * h
        #         result = max(result, volume)
        # return result
