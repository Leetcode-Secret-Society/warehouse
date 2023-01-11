from collections import defaultdict
class Solution:
    def countSubranges(self, nums1: List[int], nums2: List[int]) -> int:
        n = len(nums1)
        meaningful_sum = n/2*100 
        sum_count_dict = defaultdict(int)
        count = 0
        for n1, n2 in zip(nums1, nums2):
            next_sum_count_dict = defaultdict(int)
            for s, c in sum_count_dict.items():
                new_n1 = s+n1
                new_n2 = s-n2
                if new_n1>=-meaningful_sum and new_n1<=meaningful_sum:
                    next_sum_count_dict[new_n1]+=c
                if new_n2>=-meaningful_sum and new_n2<=meaningful_sum:
                    next_sum_count_dict[new_n2]+=c
            next_sum_count_dict[n1]+=1
            next_sum_count_dict[-n2]+=1
            count+=next_sum_count_dict[0]
            #print(next_sum_count_dict)
            sum_count_dict = next_sum_count_dict
        return count % 1000000007
