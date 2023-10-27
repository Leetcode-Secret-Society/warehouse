class Solution:
    def removeStars(self, s: str) -> str:
        result = ""
        s_list = list(s)
        star_count = 0
        while len(s_list) > 0:
            popped = s_list.pop()
            if popped == '*':
                star_count += 1
            else: 
                if star_count == 0:
                    result += popped
                star_count = max(star_count - 1, 0)

        # print(result)
        return ''.join(reversed(result))
