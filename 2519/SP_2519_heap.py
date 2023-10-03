import heapq

class Solution:
    def kBigIndices(self, nums: List[int], k: int) -> int:
        left_passed = [False] * len(nums)
        left_heap = []
        for i in range(len(nums)):
            if len(left_heap) == k and -left_heap[0] < nums[i]:
                left_passed[i] = True
            heapq.heappush(left_heap, -nums[i])
            if len(left_heap) > k:
                heapq.heappop(left_heap)
        # print(f"{left_passed=}")
    
        right_heap = []
        result = 0
        for i in range(len(nums)-1,0,-1):
            if len(right_heap) == k and -right_heap[0] < nums[i] and left_passed[i]:
                result += 1
            heapq.heappush(right_heap, -nums[i])
            if len(right_heap) > k:
                heapq.heappop(right_heap)
        # print(f"{right_passed=}")
        
            
        return result
