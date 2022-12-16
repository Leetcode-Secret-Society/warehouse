class Solution:
    def binary_search(self, arr, target):
        lower_bound = 0
        upper_bound = len(arr) - 1
        while lower_bound <= upper_bound:
            mid = (lower_bound+upper_bound)//2
            candidate = arr[mid]
            if target < candidate:
                upper_bound = mid -1
            elif target > candidate:
                lower_bound = mid + 1
            else:
                return mid, mid
        return upper_bound, lower_bound

    def fullBloomFlowers(self, flowers: List[List[int]], persons: List[int]) -> List[int]:
        bloom_dict = defaultdict(int)
        bloom_points = []
        flower_counts = []
        for flower in flowers:
            beg = flower[0]
            end = flower[1]+1
            bloom_dict[beg]+=1
            bloom_dict[end]-=1
        bloom_points = [(k,v) for k, v in bloom_dict.items()]
        bloom_points.sort(key=lambda x: x[0])
        flower_counts.append(bloom_points[0][1]) # this should always be 1
        for bloom_point in bloom_points[1:]:
            flower_counts.append(flower_counts[-1]+bloom_point[1])
        ans = []
        #for b in zip(bloom_points, flower_counts):
        #    print(b)
        bloom_timestamps = [b[0] for b in bloom_points]
        for person in persons:
            beg, _ = self.binary_search(bloom_timestamps, person)
            ans.append(flower_counts[beg])
        return ans

