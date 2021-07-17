class Solution(object):
    def checkSubarraySum(self, nums, k):
        if k == 0:
            return any(nums[i] == 0 and nums[i + 1] == 0 for i in xrange(len(nums) - 1))
        mods, cum_sum_mod_k = {0: -1}, 0
        for i, n in enumerate(nums):
            cum_sum_mod_k = (cum_sum_mod_k + n) % k
            if cum_sum_mod_k in mods and i - mods[cum_sum_mod_k] > 1:
                return True
            if cum_sum_mod_k not in mods:
                mods[cum_sum_mod_k] = i
        return False
