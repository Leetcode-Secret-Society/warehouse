class Solution:
    def minimumCosts(self, regular: List[int], express: List[int], expressCost: int) -> List[int]:
        length = len(regular)
        current_cost = 0
        result = []
        dp_r_cost = 0
        dp_e_cost = expressCost
        for i in range(length):
            current_dp_r_cost = min(dp_r_cost, dp_e_cost) + regular[i]
            current_dp_e_cost = min(dp_r_cost + expressCost, dp_e_cost) + express[i]
            dp_r_cost = current_dp_r_cost
            dp_e_cost = current_dp_e_cost
            result.append(min(dp_r_cost, dp_e_cost))
        return result
