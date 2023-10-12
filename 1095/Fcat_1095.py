class Solution:
    def findInMountainArray(self, target: int, mountain_arr: 'MountainArray') -> int:
        l = 0
        r = mountain_arr.length() - 1
        top = 0
        while l <= r:
            m = (l+r) // 2
            m_v = mountain_arr.get(m)
            if m_v > mountain_arr.get(m+1):
                if m_v > mountain_arr.get(m-1):
                    top = m
                    break
                else:
                    r = m
            else:
                l = m + 1

        l = 0
        r = top
        while l <= r:
            m = (l+r) // 2
            cur_v = mountain_arr.get(m)
            if cur_v == target:
                return m
            elif l == r:
                break
            elif cur_v > target:
                r = m
            else:
                l = m + 1

        l = top + 1
        r = mountain_arr.length() - 1
        while l <= r:
            m = (l + r) // 2
            cur_v = mountain_arr.get(m)
            if cur_v == target:
                return m
            elif l == r:
                break
            elif cur_v > target:
                l = m + 1
            else:
                r = m

        return -1