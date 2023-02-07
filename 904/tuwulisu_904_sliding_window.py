class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        counter = defaultdict(int)
        highest_ans = 0
        i = len(fruits) - 1
        j = len(fruits) - 1
        while i>=0:
            counter[fruits[i]]+=1
            while len(counter)>2:
                counter[fruits[j]]-=1
                if counter[fruits[j]]==0:
                    del counter[fruits[j]]
                j-=1
            highest_ans = max(highest_ans, sum(counter.values()))
            i-=1
        return highest_ans
            
