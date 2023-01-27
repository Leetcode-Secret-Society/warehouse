class Node:
    def __init__(self, w, end):
        self.w = w
        self.end = end
        self.next_words = dict()
class Solution:
    def findAllConcatenatedWordsInADict(self, words: List[str]) -> List[str]:
        def dfs(root, word, i, node)->bool:
            if i==len(word):
                return True if node.end else False
            c = word[i]
            if c in node.next_words:
                if dfs(root, word, i+1, node.next_words[c]):
                    return True
            if node.end and c in root.next_words:
                if dfs(root, word, i+1, root.next_words[c]):
                    return True
            return False
        words.sort(key=lambda w: len(w))
        #print(words)
        root = Node('', False)
        ans_list = []
        for word in words:
            if dfs(root, word, 0, root):
                ans_list.append(word)
            parent_node = root
            #print(f"start build: {word}")
            for i, c in enumerate(word):
                is_end = False if i!=len(word)-1 else True
                p = parent_node
                if c not in parent_node.next_words:
                    parent_node.next_words[c]=Node(c, is_end)
                    parent_node=parent_node.next_words[c]
                else:
                    parent_node=parent_node.next_words[c]
                    if not parent_node.end:
                        parent_node.end = is_end
                #print(c, parent_node.w, p.next_words)
            #print('==>', parent_node.w, parent_node.end, id(parent_node))
        """queue = [root]
        while queue:
            n = queue.pop()
            print(n.w, n.end, n.next_words)
            for next_ in n.next_words.values():
                queue.append(next_)"""

        return ans_list
                    
            
            

