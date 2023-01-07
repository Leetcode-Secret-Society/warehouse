class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        left_cost = 0
        candidate = -1
        remaining_gas = 0
        for i in range(len(gas)):
            remaining_gas += gas[i]-cost[i]
            if remaining_gas>=0:
                if candidate==-1:
                    candidate = i
            else:
                left_cost+=remaining_gas
                remaining_gas = 0
                candidate = -1
        if remaining_gas+left_cost>=0:
            return candidate
        else:
            return -1

