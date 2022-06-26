class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        k-=1
        s4 = "0111001101100011"
        s_lens = [1]
        for _ in range(19):
            next_len = s_lens[-1]*2+1
            s_lens.append(next_len)
            if next_len>k:
                break
        #print(s_lens)
        invert_count = 0
        #print(k)
        while k>=len(s4):
            half_point = s_lens.pop()//2
            if k >= half_point:
                invert_count += 1
                k = half_point - (k-half_point)
            #print(k)
        #print(invert_count)
        if invert_count%2==0:
            return s4[k]
        else:
            return '1' if s4[k]=='0' else '0'
            
            
