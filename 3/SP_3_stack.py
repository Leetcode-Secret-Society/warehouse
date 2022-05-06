class Solution:
    def find_element_in_list(element, list_element):
        try:
            index_element = list_element.index(element)
            return index_element
        except ValueError:
            return None
    def lengthOfLongestSubstring(self, s: str) -> int:
        stack = []
        result = 0
        for char in s:
            # print(char)
            index = Solution.find_element_in_list(char, stack)
            if index != None:
                for _ in range(index+1):
                    stack.pop(0)
                
            stack.append(char)
            result = max(result, len(stack))
            
        # print(stack)
        return result
