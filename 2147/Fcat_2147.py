from typing import List


class Solution:
    def numberOfWays(self, corridor: str) -> int:
        is_first_s_in_seciton = False
        result = 1
        section_p_count = 0
        MOD = 10 ** 9 + 7
        s_count = 0
        for item in corridor:
            if item == "S":
                if s_count >= 2:
                    if not is_first_s_in_seciton:
                        result *= section_p_count + 1
                        result %= MOD
                    is_first_s_in_seciton = not is_first_s_in_seciton
                    section_p_count = 0
                s_count += 1
            else:
                if s_count >= 2:
                    section_p_count += 1

        if s_count % 2 == 1 or s_count == 0:
            return 0
        else:
            return result
