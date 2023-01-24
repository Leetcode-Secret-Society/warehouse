class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        local_max = 0
        global_max = float('-inf')
        last_left_index = 0
        sum_of_nums = 0
        for i, n in enumerate(nums):
            sum_of_nums+=n
            if n > local_max+n:
                last_left_index = i
            local_max = max(n, local_max+n)
            global_max = max(global_max, local_max)
        if global_max<0:
            return global_max
        local_min = 0
        global_min = float('-inf')
        for i, n in enumerate(nums):
            m_n = -n
            local_min = max(m_n, local_min+m_n)
            global_min = max(local_min, global_min)
        global_min = global_min*-1
        #print(global_min)
        if global_min<0:
            sp_sum = sum_of_nums-global_min
            global_max = max(global_max, sp_sum)
        return global_max

