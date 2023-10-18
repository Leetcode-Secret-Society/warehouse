class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        result = ""
        gcd = math.gcd(len(str1),len(str2))
        for i in range(gcd):
            if str1[i] == str2[i]:
                result += str1[i]
        full_result = result * (max(len(str1),len(str2)) // gcd)
        
        for i in range(max(len(str1),len(str2))):
            try :
                if str1[i] != full_result[i]:
                    return ""
            except :
                pass
            try :
                if str2[i] != full_result[i]:
                    return ""
            except :
                pass
        
        
        return result
