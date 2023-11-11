class Solution:
    def restoreArray(self, adjacentPairs: List[List[int]]) -> List[int]:
        graph = defaultdict(list)

        for pair in adjacentPairs:
            graph[pair[0]].append(pair[1])
            graph[pair[1]].append(pair[0])

        for key, value in graph.items():
            if len(value) == 1:
                break

        result = [key]
        traversed = {key}

        def dfs(node):
            for next_node in graph[node]:
                if next_node in traversed:
                    continue
                else:
                    traversed.add(next_node)
                    result.append(next_node)
                    dfs(next_node)

        dfs(key)
        return result