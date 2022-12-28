class Solution:
    def minStoneSum(self, piles: List[int], k: int) -> int:
        s = sum(piles)
        ne_piles = [-1*p for p in piles]
        heapq.heapify(ne_piles)
        while k:
            n = heapq.heappop(ne_piles)
            s+=n-(n//2)
            heapq.heappush(ne_piles, n//2)
            k-=1
        return s
