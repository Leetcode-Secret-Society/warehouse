class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        if n == 0:
            return True
        prev = 0
        for i in range(len(flowerbed)):
            if prev == 0 and flowerbed[i] == 0:
                next = 0
                try:
                    next = flowerbed[i+1]
                except:
                    pass
                if next == 0:
                    flowerbed[i] = 1
                    n -= 1
            if n == 0:
                return True
            prev = flowerbed[i]
        
        return False
