class Solution:
    def pick_char(self, char_list, prev):
        picked_char = None
        for i, char_count in enumerate(char_list):
            char, count = char_count[0], char_count[1]
            if char != prev:
                picked_char = char
                char_count[1] = count -1
                picked_index = i
                break
        else:
            return picked_char
        if char_list[picked_index][1] == 0:
            char_list.remove(char_list[picked_index])
        else:
            while picked_index<len(char_list)-1:
                if char_list[picked_index][1]<char_list[picked_index+1][1]:
                    char_list[picked_index], char_list[picked_index+1] = char_list[picked_index+1], char_list[picked_index]
                picked_index+=1
        return picked_char
        
        
    def reorganizeString(self, s: str) -> str:
        dict_ = dict()
        for c in s:
            if c not in dict_:
                dict_[c]=1
            else:
                dict_[c]+=1
        char_list = []
        for key, value in dict_.items():
            char_list.append([key,value])
        char_list.sort(reverse=True, key=lambda x: x[1])
        print(char_list)
        ans_list = []
        prev = None
        for i in range(len(s)):
            picked_char = self.pick_char(char_list, prev)
            prev = picked_char
            if picked_char:
                ans_list.append(picked_char)
            else:
                return ""
        return "".join(ans_list)
