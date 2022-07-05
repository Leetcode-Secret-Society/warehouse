class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        result = []
        if len(p) > len(s):
            return result
        p_dic = {"a":0,"b":0,"c":0,"d":0,"e":0,"f":0,"g":0,"h":0,"i":0,"j":0,"k":0,"l":0,"m":0,"n":0,"o":0,"p":0,"q":0,"r":0,"s":0,"t":0,"u":0,"v":0,"w":0,"x":0,"y":0,"z":0}
        for p_char in p:
            p_dic[p_char] = p_dic.get(p_char, 0) + 1
        # print(p_dic)
        s_dic = {"a":0,"b":0,"c":0,"d":0,"e":0,"f":0,"g":0,"h":0,"i":0,"j":0,"k":0,"l":0,"m":0,"n":0,"o":0,"p":0,"q":0,"r":0,"s":0,"t":0,"u":0,"v":0,"w":0,"x":0,"y":0,"z":0}
        for s_char_index in range(0,len(p)):
            s_char = s[s_char_index]
            s_dic[s_char] = s_dic.get(s_char, 0) + 1
        # print(s_dic)
        if s_dic == p_dic:
            result.append(0)
        for s_char_index in range(len(p), len(s)):
            s_char = s[s_char_index]
            to_pop_char = s[s_char_index - len(p)]
            s_dic[to_pop_char] -= 1
            s_dic[s_char] = s_dic.get(s_char, 0) + 1
            # print(f"{s_char=} {to_pop_char=} {s_dic}")
            if s_dic == p_dic:
                result.append(s_char_index - len(p) + 1)
        return result
            
