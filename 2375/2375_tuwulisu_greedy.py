class Solution:
    def smallestNumber(self, pattern: str) -> str:
        d_counts = []
        curr_d_count = 0
        for direction in reversed(pattern):
            if direction=='D':
                curr_d_count+=1
            else:
                curr_d_count=0
            d_counts.append(curr_d_count)
        d_counts.reverse()
        start = d_counts[0]+1
        nums = [chr(start+48)]
        current_max = start
        for i, direction in enumerate(pattern):
            if direction == 'I':
                if i+1<len(d_counts) and d_counts[i+1]!=0:
                    start=current_max+d_counts[i+1]+1
                else:
                    start=current_max+1
                nums.append(chr(start+48))
            else:
                start-=1
                nums.append(chr(start+48))
            current_max = max(start, current_max)
        return "".join(nums)
        
            
        
