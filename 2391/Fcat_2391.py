from typing import List


class Solution:
    def garbageCollection(self, garbage: List[str], travel: List[int]) -> int:
        p = g = m = p_travel = g_travel = m_travel = 0
        cur_travel = 0
        for i in range(len(garbage)):
            if i != 0:
                cur_travel += travel[i - 1]
            for trash in garbage[i]:
                if trash == "M":
                    m += 1
                    m_travel = cur_travel
                elif trash == "G":
                    g += 1
                    g_travel = cur_travel
                elif trash == "P":
                    p += 1
                    p_travel = cur_travel
        return p + g + m + p_travel + g_travel + m_travel
