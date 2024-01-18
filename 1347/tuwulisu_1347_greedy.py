class Solution:
    def minSteps(self, s: str, t: str) -> int:
        dis_s = defaultdict(int)
        dis_t = defaultdict(int)
        for c in s:
            dis_s[c]+=1
        for c in t:
            dis_t[c]+=1
        ans = 0
        for char, count in dis_s.items():
            if dis_t[char] < count:
                ans += count - dis_t[char]
        return ans
