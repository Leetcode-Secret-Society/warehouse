from functools import reduce
class Solution:
    def compress(self, chars: List[str]) -> int:
        arr = list()
        current = chars[0]
        count = 0
        for c in chars:
            if current != c:
                arr.append(current)
                arr.append(count)
                current = c
                count = 1
            else:
                count += 1
        arr.append(current)
        arr.append(count)
        
        chars.clear()
        for i in range(len(arr)):
            if arr[i] != 1:
                for content in str(arr[i]):
                    chars.append(content)
        return len(chars)
