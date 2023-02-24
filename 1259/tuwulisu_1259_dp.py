class Solution:
    def numberOfWays(self, numPeople: int) -> int:
        w = {0:1, 2:1, 4:2}
        max_known_number = 4
        while max_known_number<numPeople:
            current = max_known_number
            next_possible = 0
            while current >= max_known_number//2:
                oppo = max_known_number - current
                if oppo!=current:
                    next_possible+=w[current]*w[oppo]*2
                else:
                    next_possible+=w[current]*w[oppo]
                current-=2
            max_known_number+=2
            w[max_known_number] = next_possible
        return w[numPeople] % int(10e8+7)

