class Solution:
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
        if k==0:
            return 0
        left = 0
        right = 0
        distinct_char_count = 0
        char_counter = defaultdict(int)
        max_length = 0
        while right < len(s):
            if distinct_char_count <= k:
                if s[right] not in char_counter:
                    distinct_char_count+=1
                char_counter[s[right]]+=1
                right += 1
            else:
                max_length = max(max_length, right-left-1)
                char_counter[s[left]]-=1
                if char_counter[s[left]]==0:
                    del char_counter[s[left]]
                    distinct_char_count -= 1
                left += 1
        if distinct_char_count <= k:
            max_length = max(max_length, right-left)
        else:
            max_length = max(max_length, right-left-1)
        return max_length

