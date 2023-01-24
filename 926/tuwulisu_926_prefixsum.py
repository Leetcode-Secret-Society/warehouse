class Solution:
    def minFlipsMonoIncr(self, s: str) -> int:
        zeros = [0]
        ones = [0]
        for c in s:
            if c == '0':
                zeros.append(zeros[-1]+1)
                ones.append(ones[-1])
            else:
                zeros.append(zeros[-1])
                ones.append(ones[-1]+1)
        min_flips = float('inf')
        for i in range(len(s)):
            all_one_from_i = zeros[-1] - zeros[i] + ones[i]
            min_flips = min(min_flips, all_one_from_i)
        min_flips = min(min_flips, ones[-1])
        return min_flips


        
