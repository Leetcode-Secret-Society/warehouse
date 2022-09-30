class Solution:
    def killProcess(self, pid: List[int], ppid: List[int], kill: int) -> List[int]:
        stack = [kill]
        ppid_dic = defaultdict(list)
        
        for i in range(len(ppid)):
            ppid_dic[ppid[i]].append(pid[i])
            
        history = set()
        while len(stack) > 0:
            p = stack.pop()
            history.add(p)
            if p in ppid_dic:
                stack += ppid_dic[p]
#         TLE, no hash table
#         for index, value in enumerate(ppid):
#             if value == p:
#                 stack.append(pid[index])
        
        return history
