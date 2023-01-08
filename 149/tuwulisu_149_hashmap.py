class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        aspect_points_dict = defaultdict(set)
        max_point = 0
        if len(points)==1:
            return 1
        for i in range(len(points)):
            for j in range(i+1, len(points)):
                y_diff = points[i][0]-points[j][0]
                x_diff = points[i][1]-points[j][1]
                
                if x_diff!=0:
                    aspect = y_diff/x_diff
                    if aspect == 0:
                        x_ref = points[i][0]
                    else:
                        x_ref = points[i][1] - points[i][0]/aspect
                else:
                    aspect = float('inf')
                    x_ref = points[i][1]
                aspect_points_dict[(aspect, x_ref)].add(i)
                aspect_points_dict[(aspect, x_ref)].add(j)
                max_point = max(max_point, len(aspect_points_dict[(aspect, x_ref)]))
        print(aspect_points_dict)
        return max_point
