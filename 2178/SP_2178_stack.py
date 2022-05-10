class Solution:
    def maximumEvenSplit(self, finalSum: int) -> List[int]:
        if finalSum%2 == 1:
            return []
        result = 0
        result_list = []
        for i in range(1,finalSum//2):
            val = i * 2
            result += val
            if result > finalSum:
                result -= result_list.pop(-1)
                result_list.append(val)
            else:
                result_list.append(val)
            # print(val)
            # print(result)
            # print(result_list)
            # print("----")
            if result == finalSum:
                return result_list

        return [finalSum]
