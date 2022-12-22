class Solution:
    def smallestSubsequence(self, s: str, k: int, letter: str, repetition: int) -> str:
        s_length = len(s)
        letter_left = []
        for c in reversed(s):
            previous = letter_left[-1] if letter_left else 0
            letter_left.append(previous+(1 if c==letter else 0))
        letter_left.reverse()
        ans = ""
        monotonic_deque = deque()
        i = 0
        while k:
            if k == repetition:
                for _ in range(k):
                    ans += letter
                break
            while i<s_length and s_length - i >= k and letter_left[i] >= repetition:
                while monotonic_deque and monotonic_deque[-1]>s[i]:
                    monotonic_deque.pop()
                monotonic_deque.append(s[i])
                i += 1
            picked_char = monotonic_deque.popleft()
            if picked_char == letter:
                repetition -= 1
            ans += picked_char
            k -= 1
        return ans
