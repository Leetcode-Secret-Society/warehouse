class Solution:
    def putMarbles(self, weights: List[int], k: int) -> int:
        if k==1:
            return 0
        split_points = []
        for i in range(1, len(weights)):
            split_points.append(weights[i]+weights[i-1])
        split_points.sort()
        max_score = weights[0] + weights[-1] + sum(split_points[-(k-1):])
        min_score = weights[0] + weights[-1] + sum(split_points[:k-1])
        return max_score - min_score
