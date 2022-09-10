class Solution:
    def numFactoredBinaryTrees(self, arr: List[int]) -> int:
        MOD = 10 ** 9 + 7
        length = len(arr)
        arr.sort()
        node_dict = {n:1 for n in arr}
        for i in range(length):
            for j in range(0, i+1):
                i_n = arr[i]
                j_n = arr[j]
                if i_n*j_n in node_dict:
                    if i!=j:
                        node_dict[i_n*j_n]+=(node_dict[i_n]*node_dict[j_n]*2) % MOD
                    else:
                        node_dict[i_n*j_n]+=(node_dict[i_n]*node_dict[j_n]) % MOD
        possibility = 0
        for n, p in node_dict.items():
            possibility+=p
        #print(node_dict)
        return possibility % MOD
