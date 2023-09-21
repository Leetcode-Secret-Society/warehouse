from typing import List


class Solution:
    def timeTaken(self, arrival: List[int], state: List[int]) -> List[int]:
        enters = []
        leaves = []

        for i in range(len(arrival)):
            if state[i] == 0:
                enters.append((arrival[i], i))
            else:
                leaves.append((arrival[i], i))

        enter_index = 0
        leave_index = 0
        door_state = 1
        result = [0] * len(arrival)
        t = 0
        while enter_index < len(enters) or leave_index < len(leaves):
            pass_door = True
            if door_state == 0:
                if enter_index < len(enters) and enters[enter_index][0] <= t:
                    result[enters[enter_index][1]] = t
                    enter_index += 1
                    door_state = 0
                elif leave_index < len(leaves) and leaves[leave_index][0] <= t:
                    result[leaves[leave_index][1]] = t
                    leave_index += 1
                    door_state = 1
                else:
                    pass_door = False
            else:
                if leave_index < len(leaves) and leaves[leave_index][0] <= t:
                    result[leaves[leave_index][1]] = t
                    leave_index += 1
                    door_state = 1
                elif enter_index < len(enters) and enters[enter_index][0] <= t:
                    result[enters[enter_index][1]] = t
                    enter_index += 1
                    door_state = 0
                else:
                    pass_door = False
            if not pass_door:
                door_state = 1
            t += 1
        return result
