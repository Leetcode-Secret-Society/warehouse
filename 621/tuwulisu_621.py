class Solution:
    def leastInterval(self, tasks, n):
        dict_ = dict()
        set_ = set()
        for task in tasks:
            set_.add(task)
            if task not in dict_:
                dict_[task]=[1,float("-inf")]
            else:
                dict_[task][0]+=1
        time=0
        while len(set_)>0:
            picked_task=None
            for task in iter(set_):
                if dict_[task][1]+n < time:
                    picked_task=task
                    break
            if picked_task:
                dict_[picked_task][0]-=1
                dict_[picked_task][1]=time
                if dict_[picked_task][0] == 0:
                    set_.remove(picked_task)
            time+=1
        return time
s = Solution()
print(s.leastInterval(["A","A","A","B","B","B"],2))