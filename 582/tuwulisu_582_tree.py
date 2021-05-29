class Solution:
    def killProcess(self, pid: List[int], ppid: List[int], kill: int) -> List[int]:
        sub_process_dict = dict()
        for pid_, ppid_ in zip(pid,ppid):
            if ppid_ not in sub_process_dict:
                sub_process_dict[ppid_]=[pid_]
            else:
                sub_process_dict[ppid_].append(pid_)
        queue=[kill]
        result=[]
        while queue:
            new_queue=[]
            for pid in queue:
                if pid in sub_process_dict:
                    new_queue.extend(sub_process_dict[pid])
                result.append(pid)
            queue=new_queue
        return result
