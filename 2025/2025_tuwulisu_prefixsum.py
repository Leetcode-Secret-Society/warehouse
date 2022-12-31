class Solution:
    def waysToPartition(self, nums: List[int], k: int) -> int:
        prefix_sums = [nums[0]]
        for i, n in enumerate(nums[1:]):
            prefix_sums.append(prefix_sums[-1]+n)
        
        swap_k_possibilities = []
        unchanged_ans = 0
        right_diff_counts = defaultdict(int)
        left_diff_counts = defaultdict(int)
        for i, n in enumerate(nums[:-1]):
            left_sum = prefix_sums[i]
            right_sum = prefix_sums[-1]-prefix_sums[i]
            if left_sum == right_sum:
                unchanged_ans+=1
            right_left_diff = right_sum - left_sum
            left_right_diff = left_sum - right_sum
            right_diff_counts[right_left_diff]+=1

        for i, n in enumerate(nums):
            swap_k_diff = k - n
            swap_k_possibility = left_diff_counts[swap_k_diff] + right_diff_counts[swap_k_diff]
            swap_k_possibilities.append(swap_k_possibility)

            left_sum = prefix_sums[i]
            right_sum = prefix_sums[-1]-prefix_sums[i]
            right_left_diff = right_sum - left_sum
            left_right_diff = left_sum - right_sum
            left_diff_counts[left_right_diff]+=1
            right_diff_counts[right_left_diff]-=1
            #print(f"{i}: {swap_k_diff} {left_right_diff} {right_left_diff}")
            #print(left_diff_counts)
            #print(right_diff_counts)
            
        #print(swap_k_possibilities)    

        return max(unchanged_ans, max(swap_k_possibilities))
