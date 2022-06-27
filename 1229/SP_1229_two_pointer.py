class Solution:
    def minAvailableDuration(self, slots1: List[List[int]], slots2: List[List[int]], duration: int) -> List[int]:
        #O(s1 + s2)
        sorted_slots1 = sorted(slots1, key = lambda slot: slot[0])
        sorted_slots2 = sorted(slots2, key = lambda slot: slot[0])
        slot1 = 0
        slot2 = 0
        while slot1 < len(sorted_slots1) and slot2 < len(sorted_slots2):
            start = max(sorted_slots1[slot1][0],sorted_slots2[slot2][0])
            end = min(sorted_slots1[slot1][1],sorted_slots2[slot2][1])
            if end - start >= duration:
                return [start, start+duration]
            if sorted_slots1[slot1][1] < sorted_slots2[slot2][1]:
                slot1 += 1
            else:
                slot2 += 1
        return []
        #belowing goes TLE O(s1 * s2)
        sorted_slots1 = sorted(slots1, key = lambda slot: slot[0])
        sorted_slots2 = sorted(slots2, key = lambda slot: slot[0])
        for slot2 in sorted_slots2:
            for slot1 in sorted_slots1:
                overlapped_time = min(slot1[1],slot2[1]) - max(slot1[0],slot2[0])
                if overlapped_time >= duration:
                    start = max(slot1[0],slot2[0])
                    return [start, start+duration] 
        return []
        #     s1.0---------s1.1
        #             s2.0------s2.1 
        #   s2.0------s2.1 
        #   s2.0----------------s2.1
        #        s2.0---s2.1
        
