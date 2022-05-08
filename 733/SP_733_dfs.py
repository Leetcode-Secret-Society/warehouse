class Solution:
    
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        R, C = len(image), len(image[0])
        init_color = image[sr][sc]
        if init_color == newColor:
            return image
        def dfs(image:List[List[int]], sr:int, sc:int, newColor:int, initColor:int):
            # print(str(sr)+"-"+str(sc))
            if image[sr][sc] == init_color:
                image[sr][sc] = newColor
                if sr-1 >= 0:
                    dfs(image, sr-1 ,sc ,newColor, init_color)
                if sr+1 < R:
                    dfs(image, sr+1 ,sc ,newColor, init_color)
                if sc+1 < C:
                    dfs(image, sr ,sc+1 ,newColor, init_color)
                if sc-1 >= 0:
                    dfs(image, sr ,sc-1 ,newColor, init_color)
        
        dfs(image, sr, sc, newColor, init_color)
        return image
        
