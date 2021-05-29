class Solution:
    def __init__(self):
        self.dp_dict=dict()
        self.dp_dict[0]=1
        self.dp_dict[1]=1
        self.dp_dict[2]=2
        self.dp_dict[3]=5
    def numTrees(self, n: int) -> int:
        if n in self.dp_dict:
            return self.dp_dict[n]
        else:
            variation=0
            for i in range(n):
                left_node = i
                right_node = n-i-1
                left_variation = self.numTrees(left_node)
                right_variation = self.numTrees(right_node)
                variation+=left_variation*right_variation
            self.dp_dict[n]=variation
            return variation
