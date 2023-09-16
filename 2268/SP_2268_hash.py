class Solution:
    def minimumKeypresses(self, s: str) -> int:
        dic = collections.defaultdict(int)
        result = 0
        for character in s:
            dic[character] += 1
        sorted_dic = sorted(dic.items(), key=lambda x:x[1])
        # print(sorted_dic)
        pad_count = 0
        while sorted_dic:
            pad_count += 1
            popped = sorted_dic.pop()
            result += popped[1] * math.ceil(pad_count / 9)

        return result
