class Task:
    def __init__(self, enqueue, length, index):
        self.enqueue = enqueue
        self.length = length
        self.index = index

    def __gt__(self, other):
        if self.length == other.length:
            return self.index > other.index
        else:
            return self.length > other.length

    def __repr__(self):
        return str(self.index)
class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        task_list = [Task(task[0], task[1], i) for i, task in enumerate(tasks)]
        task_list.sort(key=lambda t: t.enqueue, reverse=True)
        heap = []
        previous_enqueue = task_list[-1].enqueue
        for task in task_list[::-1]:
            if previous_enqueue == task.enqueue:
                heap.append(task)
                task_list.pop()
            else:
                break
        heapq.heapify(heap)
        current_timestamp = previous_enqueue
        ans_list = []
        while heap:
            #print(heap)
            task = heapq.heappop(heap)
            ans_list.append(task.index)
            current_timestamp += task.length
            while task_list and task_list[-1].enqueue <= current_timestamp:
                heapq.heappush(heap, task_list.pop())
            if not heap and task_list:
                previous_enqueue = task_list[-1].enqueue
                for task in task_list[::-1]:
                    if previous_enqueue == task.enqueue:
                        heap.append(task)
                        task_list.pop()
                    else:
                        break
                heapq.heapify(heap)
                current_timestamp = previous_enqueue
            #print(current_timestamp)
        return ans_list
