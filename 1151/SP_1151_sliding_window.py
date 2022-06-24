class Solution:
    def minSwaps(self, data: List[int]) -> int:
        #get 1s
        all_ones = list(filter(lambda ele: ele == 1, data))
        num_all_ones = len(all_ones)
        if num_all_ones == 0:
            return 0
        #sliding window
        ones_count = 0
        max_ones_count = 0
        window = []
        for i in range(num_all_ones):
            window.append(data[i])
            if data[i] == 1:
                ones_count += 1
            # print(ones_count)
        max_ones_count = ones_count
        for i in range(num_all_ones,len(data)):
            #popped = window.pop(0) #no need to pop
            popped = window[i - num_all_ones]
            pushed = data[i]
            window.append(pushed)
            if popped == 1:
                ones_count -= 1
            if pushed == 1:
                ones_count += 1
                max_ones_count = max(max_ones_count, ones_count)
            # print(ones_count)
        return num_all_ones - max_ones_count
