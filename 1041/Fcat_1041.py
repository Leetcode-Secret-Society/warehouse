class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        states_direction = [(1,0), (0,-1), (-1,0), (0,1)]

        state = 3
        pos = [0,0]
        instructions *= 4

        for instruction in instructions:
            if instruction == 'G':
                x, y = states_direction[state]
                pos[0] += x
                pos[1] += y
                continue
            elif instruction == 'L':
                state -= 1
            elif instruction == 'R':
                state += 1
            state %= 4
        return pos[0] == 0 and pos[1] == 0
