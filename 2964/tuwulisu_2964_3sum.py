class Solution:
    def divisibleTripletCount(self, nums: List[int], d: int) -> int:
        last_r_index = defaultdict(set)
        for i, n in enumerate(nums):
            if n%d == 0:
                last_r_index[0].add(i)
            else:
                last_r_index[d-n%d].add(i)
        ans = 0
        for i, n1 in enumerate(nums[:-1]):
            for j in range(i+1, len(nums)):
                n2 = nums[j]
                fit_set = last_r_index[(n1+n2)%d]
                fit_triplet_count = len(fit_set)
                if i in fit_set:
                    fit_triplet_count -= 1
                if j in fit_set:
                    fit_triplet_count -= 1
                ans += fit_triplet_count
        return ans//3
