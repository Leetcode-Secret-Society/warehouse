class Solution:
    def minMoves2(self, nums: List[int]) -> int:
        length=len(nums)
        nums.sort()
        prefix_sums = [0]
        for n in nums:
            prefix_sums.append(prefix_sums[-1]+n)
        #print(prefix_sums)
        min_move = float('inf')
        for i, n in enumerate(nums):
            move=0
            if i!=length-1:
                #print("post:", prefix_sums[length], prefix_sums[i+1], n*(length-i-1))
                move += prefix_sums[length] - prefix_sums[i+1] - n*(length-i-1)
            if i!=0:
                #print("pre:", n*i, prefix_sums[i])
                move += n*i - prefix_sums[i]
            #print(i, move)
            min_move=min(move, min_move)

        return min_move
