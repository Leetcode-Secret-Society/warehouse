class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        stack = []
        index_on_popped = 0
        for pushing_element in pushed:
            stack.append(pushing_element)
            while stack and stack[-1]==popped[index_on_popped]:
                index_on_popped+=1
                stack.pop()
        return len(stack)==0
                
