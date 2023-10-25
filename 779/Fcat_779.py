class Solution:
    def kthGrammar(self, n: int, k: int) -> int:
        current_node = False
        n -= 1
        last_level_node_count = 2 ** n
        while n > 0:
            n -= 1
            last_level_node_count /= 2
            if k > last_level_node_count:
                current_node = not current_node
                k -= last_level_node_count

        return int(current_node)
