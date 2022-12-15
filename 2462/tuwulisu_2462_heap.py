import heapq
class Solution:
    def totalCost(self, costs: List[int], k: int, candidates: int) -> int:
        front_pointer = candidates
        back_pointer = len(costs) - 1 - candidates
        if back_pointer < front_pointer:
            back_pointer = front_pointer - 1
        front_heap = costs[:front_pointer]
        heapq.heapify(front_heap)
        back_heap = costs[back_pointer+1:]
        heapq.heapify(back_heap)
        total_cost = 0
        #print(front_heap)
        #print(back_heap)
        while k:
            if front_heap and (not back_heap or front_heap[0] <= back_heap[0]):
                target_heap = front_heap
                target_pointer = front_pointer
                side_heap = back_heap
                side_pointer = back_pointer
                direct = 1
            else:
                target_heap = back_heap
                target_pointer = back_pointer
                side_heap = front_heap
                side_pointer = front_pointer
                direct = -1
            hire_cost = heapq.heappop(target_heap)
            #print("pick: ", hire_cost)
            total_cost += hire_cost
            if target_pointer*direct <= side_pointer*direct:
                heapq.heappush(target_heap, costs[target_pointer])
                if direct == 1:
                    front_pointer += direct
                else:
                    back_pointer += direct
            k -= 1
            #print(front_heap)
            #print(back_heap)
        return total_cost
