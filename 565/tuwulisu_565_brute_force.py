class Solution:
    
    def find_group(self, pool, start, nums):
        current = start
        group = set()
        color=self.latest_color
        while current not in group:
            if current not in self.node_color_map:
                group.add(current)
                current = nums[current]
            else:
                color = self.node_color_map[current]
                break
        for node in group:
            self.node_color_map[node]=color
        if color==self.latest_color:
            self.color_size_map[color]=len(group)
            self.latest_color+=1
        else:
            self.color_size_map[color]+=len(group)
        return group
    def arrayNesting(self, nums: List[int]) -> int:
        self.latest_color = 0
        n = len(nums)
        pool = set([i for i in range(n)])
        groups_size = []
        self.node_color_map = dict()
        self.color_size_map = dict()
        while pool:
            start = pool.pop()
            g = self.find_group(pool, start, nums)
            pool -= g
        groups_size = self.color_size_map.values()
        return max(groups_size)