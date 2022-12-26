class Solution:
    def getDistances(self, arr: List[int]) -> List[int]:
        val_index_dict = defaultdict(list)
        for i, n in enumerate(arr):
            val_index_dict[n].append(i)
        ans_list = [0 for _ in arr]
        for list_ in val_index_dict.values():
            length = len(list_)
            prefix_sums = [list_[0]]
            for n in list_[1:]:
                prefix_sums.append(prefix_sums[-1]+n)
            #print(list_, prefix_sums)
            for i, index in enumerate(list_):
                diff_sum = 0
                if i!=length-1:
                    diff_sum += abs( (length-i-1)*index - (prefix_sums[-1]-prefix_sums[i]) )
                if i!=0:
                    diff_sum += abs(i*index - prefix_sums[i-1])
                ans_list[index] += diff_sum
                #print(diff_sum)
            
        return ans_list
