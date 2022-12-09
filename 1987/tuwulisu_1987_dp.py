class Solution:
    def numberOfUniqueGoodSubsequences(self, binary: str) -> int:
        two_count = 1
        one_count = 0
        zero_count = 0
        end_count = 0
        found_first_one = False
        for c in binary:
            if not found_first_one:
                if c == '1':
                    found_first_one = True
                continue
            else:
                if c == '1':
                    zero_count += two_count
                    end_count += one_count
                    two_count = two_count + one_count
                    one_count = 0
                elif c == '0':
                    one_count += two_count
                    end_count += zero_count
                    two_count = two_count + zero_count
                    zero_count = 0
        if found_first_one==False:
            return 1
        ans = two_count + one_count + zero_count + end_count + (1 if '0' in binary else 0)
        return ans % 1000000007
                
