class Solution:
    def largestMerge(self, word1: str, word2: str) -> str:
        def tiebreak(word1, word2):
            if word1 > word2:
                return word1[0], 'i'
            else:
                return word2[0], 'j'
        n1 = len(word1)
        n2 = len(word2)
        i = 0
        j = 0
        ans = []
        while i < n1 or j < n2:
            if j == n2:
                ans.append(word1[i])
                i+=1
            elif i == n1:
                ans.append(word2[j])
                j+=1
            else:
                if word1[i]>word2[j]:
                    ans.append(word1[i])
                    i+=1
                elif word1[i]<word2[j]:
                    ans.append(word2[j])
                    j+=1
                else:
                    s, pick = tiebreak(word1[i:], word2[j:])
                    if pick == 'i':
                        i+=len(s)
                    else:
                        j+=len(s)
                    ans.append(s)
        return "".join(ans)
