class Solution:
    def divideArray(self, nums: List[int], k: int) -> List[List[int]]:
        nums.sort()
        win = []
        ans = []
        for n in nums:
            if not win or n-win[0]<=k:
                win.append(n)
            else:
                return []
            if len(win)==3:
                ans.append(win)
                win = []
        return ans
