class Solution:
    def longestCommonSubsequence(self, arrays: List[List[int]]) -> List[int]:
        counter = defaultdict(int)
        for array in arrays:
            for n in set(array):
                counter[n]+=1
        ans = []
        for k, v in counter.items():
            if v == len(arrays):
                ans.append(k)
        ans.sort()
        return ans
