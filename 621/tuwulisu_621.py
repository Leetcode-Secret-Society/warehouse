class Solution:
    def leastInterval(self, tasks, n):
        def maintain_priority(list_: list,index: int)->None:
            while index != len(list_)-1 and list_[index]<list_[index+1]:
                list_[index], list_[index+1] = list_[index+1], list_[index]
                index += 1
        dict_ = dict()
        for task in tasks:
            if task not in dict_:
                dict_[task]=[1,float("-inf")]
            else:
                dict_[task][0]+=1
        priority_list=[]
        for key,val in dict_.items():
            priority_list.append([val[0],key])
        priority_list.sort(key=lambda e:e[0],reverse=True)
        time=0
        while len(priority_list)>0:
            picked_task=None
            for index,ele in enumerate(priority_list):
                task=ele[1]
                if task in dict_ and dict_[task][1]+n < time:
                    picked_task=task
                    priority_list[index][0]-=1
                    maintain_priority(priority_list,index)
                    if priority_list[-1][0]==0:
                        priority_list.pop()
                    break
            if picked_task:
                dict_[picked_task][0]-=1
                dict_[picked_task][1]=time
                if dict_[picked_task][0] == 0:
                    dict_.pop(picked_task)
            #print(picked_task)
            time+=1
        return time
