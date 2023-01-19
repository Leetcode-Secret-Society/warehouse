class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        n = len(nums[0])
        #counter = [[0, 0] for _ in range(n)]
        nums_set = set(nums)
        """for s in nums:
            for i, c in enumerate(s):
                if c == '0':
                    counter[i][0]+=1
                else:
                    counter[i][1]+=1"""
        ans = []
        complete_n = math.pow(2, n-1)
        final_ans = ""
        def find_num(i):
            if i==n:
                if "".join(ans) not in nums_set:
                    return True
                else:
                    return False
            ans.append('0')
            if True:# counter[i][0]<complete_n:
                pick_0 = find_num(i+1)
                if pick_0:
                    return pick_0
            ans[-1]='1'
            if True:#counter[i][1]<complete_n:
                pick_1 = find_num(i+1)
                if pick_1:
                    return pick_1
            ans.pop()
            return False
        find_num(0)

        return "".join(ans)
