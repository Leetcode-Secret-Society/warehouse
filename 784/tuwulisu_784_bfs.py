class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        queue = [s]
        ans_set = set([s])
        while queue:
            next_queue = []
            for s in queue:
                for i, c in enumerate(s):
                    if c.isalpha():
                        if c.islower():
                            new_s = s[:i] + c.upper() + s[i+1:]
                        else:
                            new_s = s[:i] + c.lower() + s[i+1:]
                        if new_s not in ans_set:
                            ans_set.add(new_s)
                            next_queue.append(new_s)
            queue = next_queue
        return list(ans_set)
