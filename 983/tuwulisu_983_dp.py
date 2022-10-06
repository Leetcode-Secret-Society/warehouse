from typing import List
class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        current_tickets = []
        ticket_durations = [0, 6, 29]
        previous_day = 0
        for day in days:
            day_passed = day - previous_day
            min_local_cost = float('inf')
            new_tickets = []
            for ticket_info in current_tickets:
                ticket_duration, cost = ticket_info[0], ticket_info[1]
                if ticket_duration - day_passed < 0:
                    min_local_cost = min(min_local_cost, cost)
                else:
                    ticket_info[0] = ticket_duration - day_passed
                    new_tickets.append(ticket_info)
            if min_local_cost == float('inf'):
                min_local_cost = 0
            for ticket_duration, cost in zip(ticket_durations, costs):
                new_tickets.append([ticket_duration, cost+min_local_cost])
            current_tickets = new_tickets
            #print(current_tickets)
            previous_day = day
        final_costs = [cost for _, cost in current_tickets]
        return min(final_costs)
