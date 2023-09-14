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

#simplify the code
class Solution:
    def minSwaps(self, data: List[int]) -> int:
        data.append(0)
        one_count = data.count(1)
        current_one_count = data[0:one_count].count(1)
        result = current_one_count
        for i in range(1, len(data) - one_count):
            if data[i - 1] == 1:
                current_one_count -= 1
            if data[i + one_count - 1] == 1:
                current_one_count += 1
                result = max(result, current_one_count)
            
        return one_count - result
