class Solution:
    def averageWaitingTime(self, customers: List[List[int]]) -> float:
        idle_time = 0
        sum_of_waiting_time = 0
        for arrival, time in customers:
            if arrival>idle_time:
                sum_of_waiting_time += time
                idle_time = arrival+time
            else:
                sum_of_waiting_time += (idle_time - arrival) + time
                idle_time += time
        return sum_of_waiting_time/len(customers)
