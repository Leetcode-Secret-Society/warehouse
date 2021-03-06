from typing import List


class Solution:
    def shortestDistanceColor(self, colors: List[int], queries: List[List[int]]) -> List[int]:
        one_indexes = []
        two_indexes = []
        three_indexes = []
        dp = [[-1,-1,-1] for i in range(len(colors))]
        for i, color in enumerate(colors):
            if color == 1:
                one_indexes.append(i)
            elif color == 2:
                two_indexes.append(i)
            elif color == 3:
                three_indexes.append(i)

        def build_color_dp(color, indexes):
            if not indexes:
                return
            for i in range(indexes[0]):
                dp[i][color-1] = indexes[0] - i

            for i in range(len(indexes)-1):
                middle = (indexes[i]+indexes[i+1]) // 2
                for j in range(indexes[i], indexes[i+1]):
                    if j <= middle:
                        dp[j][color - 1] = j - indexes[i]
                    else:
                        dp[j][color - 1] = indexes[i+1] - j
            distance = 0
            for i in range(indexes[-1], len(colors)):
                dp[i][color-1] = distance
                distance += 1

        build_color_dp(1, one_indexes)
        build_color_dp(2, two_indexes)
        build_color_dp(3, three_indexes)
        result = []

        for i, target in queries:
            result.append(dp[i][target-1])
        return result

print(Solution().shortestDistanceColor(colors = [3,2,2,1,3,2,3,3,2,2,2,3,2,2,2,2,1,2,3,2,3,3,1,1,1,3,2,3,2,1,3,1,1,3,2,1,1,2,2,3,2,1,1,2,2,2,3,2,2,1,3,2,2,1,2,3,1,2,1,3,1,3,2,1,2,3,2,3,3,2,3,3,1,3,2,2,2,3,1,3,3,1,1,3,1,3,3,2,3,1,3,1,2,3,3,2,1,3,2,1,1,1,1,3,1,1,2,2,2,3,3,1,2,2,1,1,2,3,3,1,3,1,2,1,3,3,1,2,2,1,1,2,2,2,3,1,2,2,1,2,2,3,3,2,3,3,1,2,1,2,1,1,3,3,3,2,2,2,1,3,3,2,3,1,1,3,3,3,3,3,2,3,1,1,1,1,1,1,1,1,1,2,3,1,3,3,3,2,2,2,2,2,2,1,3,3,2,1,2,1,3,3,1,2,3,1,2,1,3,1,1,1,3,1,2,3,3,1,3,2,2,3,1,3,2,2,1,1,1,2,1,3,3,2,2,1,2,3,3,3,3,1,1,2,3,2,3,3,3,2,2,2,3,1,1,1,3,3,2,1,1,2,1,1,3,2,1,1,1,2,1,2,1,3,3,3,1,3,1,2,2,1,3,3,3,2,1,2,2,1,1,3,2,1,3,2,2,1,1,3,2,2,3,1,2,1,2,3,2,3,2,2,2,1,2,1,1,3,3,3,3,2,3,1,3,3,1,1,1,3,2,1,3,3,2,2,2,1,3,2,3,1,1,1,2,2,3,1,2,1,2,1,1,1,3,1,2,1,3,1,2,2,2,2,2,2,1,2,3,1,1,1,3,3,1,1,2,3,3,3,3,1,3,1,3,3,3,3,3,3,3,3,2,3,1,2,3,1,3,2,2,1,3,3,3,2,1,2,3,1,1,3,2,3,2,3,2,2,1,3,1,3,3,1,2,2,1,3,2,2,1,1,3,2,3,2,2,3,3,2,1,3,1,1,2,1,2,2,2,3,1,1,3,1,3,1,1,2,3,3,3,1,1,3,2,3,3,2,3,3,3,1,2,2,1,2,2,2,1,1,1,1,3,2,3,2,1,1,1,3,3,1,2,3,3,2,2,3,3,3],
                                       queries = [[368,1],[394,3],[483,1],[7,1],[240,2],[437,1],[316,2],[68,1],[126,2],[129,3],[474,3],[201,3],[226,3],[486,1],[127,1],[273,1],[150,1],[72,1],[36,3],[211,1],[461,2],[57,2],[393,3],[34,2],[89,3],[173,1],[265,3],[219,1],[65,1],[194,2],[449,1],[354,2],[467,1],[157,2],[133,3],[87,3],[307,2],[167,1],[281,1],[85,2],[77,1],[64,2],[139,3],[452,1],[231,2],[383,2],[103,1],[362,2],[232,2],[143,2],[345,2],[239,1],[341,2],[455,2],[15,3],[25,1],[1,2],[370,1],[429,3],[93,3],[308,1],[393,1],[53,3],[365,1],[290,2],[333,3],[426,2],[245,2],[260,2],[21,3],[269,1],[264,2],[68,2],[119,1],[170,3],[321,1],[431,2],[464,3],[472,1],[497,2],[496,2],[447,2],[22,3],[42,3],[309,3],[107,2],[363,2],[66,3],[296,3],[63,3],[465,2],[289,3],[64,1],[450,2],[241,1],[270,1],[423,3],[98,1],[234,1],[207,1],[63,1],[462,1],[112,1],[41,3],[405,1],[124,2],[27,3],[331,3],[266,3],[376,1],[436,3],[16,1],[211,2],[65,2],[364,3],[387,3],[420,2],[344,2],[182,3],[409,2],[93,1],[309,2],[78,3],[118,3],[86,1],[1,2],[21,3],[387,2],[265,2],[208,3],[78,3],[472,2],[330,1],[112,1],[214,2],[75,3],[117,2],[139,1],[59,1],[320,1],[30,1],[165,1],[158,2],[85,2],[445,1],[130,1],[317,1],[177,1],[175,1],[108,1],[6,3],[464,1],[435,3],[287,2],[476,2],[146,3],[411,3],[344,3],[246,3],[480,1],[220,1],[367,1],[347,1],[93,3],[126,3],[9,3],[236,2],[11,2],[252,3],[419,1],[196,1],[487,2],[123,3],[450,2],[14,2],[412,2],[180,1],[243,3],[198,1],[377,1],[195,3],[220,2],[231,2],[171,2],[138,3],[340,3],[491,2],[239,1],[338,3],[73,2],[166,1],[95,1],[405,1],[319,3],[11,1],[395,1],[394,1],[46,3],[439,2],[377,3],[77,3],[231,1],[13,3],[288,2],[485,2],[457,1],[247,3],[347,1],[140,3],[482,2],[191,2],[219,1],[470,1],[350,2],[273,2],[122,3],[379,1],[102,3],[10,3],[76,3],[174,3],[376,1],[439,2],[198,1],[161,2],[415,3],[63,2],[178,3],[35,2],[221,2],[105,2],[65,3],[39,3],[115,2],[271,3],[333,3],[360,1],[342,1],[44,3],[42,1],[80,1],[417,1],[486,1],[228,1],[301,2],[235,3],[167,2],[296,2],[495,2],[305,2],[295,3],[394,3],[223,3],[402,1],[74,2],[265,1],[326,2],[20,1],[238,1],[366,2],[43,1],[144,2],[195,2],[319,2],[249,2],[451,1],[38,1],[392,2],[43,3],[102,3],[153,2],[6,2],[429,3],[289,2],[463,2],[57,3],[14,2],[470,2],[270,1],[317,1],[126,3],[133,2],[223,1],[439,3],[172,1],[411,1],[477,3],[243,1],[213,1],[129,2],[362,3],[321,1],[384,1],[427,2],[244,2],[361,1],[74,2],[122,3],[466,1],[257,3],[360,2],[95,1],[93,2],[411,1],[388,3],[461,1],[248,3],[88,2],[372,2],[66,3],[152,2],[419,1],[116,3],[253,3],[419,2],[88,3],[364,3],[179,3],[333,3],[46,2],[2,2],[392,2],[449,3],[386,1],[449,3],[415,3],[110,3],[78,2],[361,3],[330,1],[324,2],[46,2],[471,3],[412,1],[46,1],[61,3],[352,3],[468,1],[32,1],[175,3],[403,1],[134,3],[256,2],[496,1],[181,1],[22,2],[36,3],[115,3],[229,3],[113,3],[414,3],[277,2],[5,3],[273,3],[52,2],[427,1],[158,3],[322,3],[134,1],[428,2],[378,2],[49,3],[228,1],[275,1],[41,3],[264,1],[440,2],[365,1],[207,2],[107,1],[399,2],[170,1],[395,2],[412,1],[468,3],[55,3],[481,1],[23,3],[487,2],[164,3],[454,2],[139,2],[395,2],[346,2],[469,1],[273,3],[136,2],[102,1],[130,2],[46,3],[182,1],[52,1],[50,2],[202,1],[491,1],[476,3],[328,3],[304,2],[246,1],[328,3],[197,1],[59,2],[127,2],[226,2],[147,3],[305,3],[75,3],[332,1],[317,1],[445,3],[450,3],[198,3],[131,3],[260,2],[337,2],[429,3],[112,3],[13,1],[155,3],[360,3],[108,1],[360,3],[139,1],[472,3],[437,2],[307,1],[201,1],[448,3],[308,3],[220,2],[78,1],[161,1],[189,3],[120,2],[217,1],[34,2],[419,1],[338,3],[57,1],[430,3],[308,2],[94,2],[185,3],[293,1],[429,3],[28,1],[498,1],[131,3],[11,3],[53,3],[106,2],[57,2],[8,2],[8,2],[116,1],[436,1],[70,2],[142,3],[44,2],[157,1],[248,1],[255,1],[297,2],[9,3],[311,1],[268,1],[71,2],[43,3],[125,3],[188,3],[104,1],[461,3],[340,2],[212,2],[384,1],[47,2],[128,2],[59,3],[349,2],[266,1],[246,2],[19,1],[171,2],[391,1],[269,1],[304,2],[332,1],[91,1],[399,1],[434,3],[430,1],[243,1],[171,3],[32,1],[437,3],[125,3],[383,2],[8,3],[275,1],[445,2]]))