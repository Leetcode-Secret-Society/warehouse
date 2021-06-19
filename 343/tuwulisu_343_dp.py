class Solution:
    def __init__(self):
        key_list = [i for i in range(1,11)]
        value_list = [1,2,3,4,6,9,12,18,27,36]
        self.dict_ = dict(zip(key_list, value_list))
    
    def get_ans(self, n: int) -> int:
        if n in self.dict_:
            return self.dict_[n]
        else:
            max_value = 0
            for i in range(2,n//2+1):
                j = n - i
                max_value = max(max_value, self.get_ans(i)*self.get_ans(j))
        self.dict_[n]=max_value
        return max_value
    
    def integerBreak(self, n: int) -> int:
        dict_=dict()
        dict_[2] = 1
        dict_[3] = 2
        dict_[4] = 4
        if n in dict_:
            return dict_[n]
        else:
            return self.get_ans(n)
