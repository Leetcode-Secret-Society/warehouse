class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:

        """
        3,1,6,5,4

        3           [3]         a[0] { dp[0] = a[0] }
        3,1         [1,1]       a[0] > a[1] { dp[1] = a[1] * len(0..1) }
        3,1,6       [1,1,6]     a[1] < a[2] { dp[2] = a[2] * len(2..2) + dp[1] }
        3,1,6,5     [1,1,5,5]   a[2] > a[3] { dp[3] = a[3] * len(2..3) + dp[1] }
        3,1,6,5,4   [1,1,4,4,4] a[3] > a[4] { dp[4] = a[4] * len(2..4) + dp[1] }
        """
        dp = [0] * len(arr)
        index_stack = []
        for i in range(len(arr)):
            if i == 0:
                dp[i] = arr[i]    
            else :
                while len(index_stack) > 0 and arr[index_stack[-1]] > arr[i]:
                    index_stack.pop()

                if len(index_stack) > 0:
                    j = index_stack[-1]
                    dp[i] = arr[i]*(i-j) + dp[j]
                else:
                    dp[i] = arr[i]*(i+1) 

            index_stack.append(i)

            
        return sum(dp) % (10**9+7)
        """
        TLE
        3,1,2,4
    [3]
        3           3
        3,1         1
        3,1,2       1
        3,1,2,4     1
    [1]
          1         1
          1,2       1
          1,2,4     1
    [2]
            2       2
            2,4     2
    [4]
              4     4
        """
        result = 0
        for i in range(len(arr)):
            current_min = arr[i]
            for j in range(i, len(arr)):
                # print((i,j))
                current_min = min(arr[j], current_min)
                # print("add:"+str(current_min))
                result += current_min

        
        return result % (10**9 + 7)
