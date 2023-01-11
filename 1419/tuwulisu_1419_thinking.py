from collections import defaultdict
class Solution:
    def minNumberOfFrogs(self, croakOfFrogs: str) -> int:
        counter = defaultdict(int)
        croak_list = ['c', 'r', 'o', 'a', 'k']
        croak_dict = {c: i for i, c in enumerate(croak_list)}
        current_frog = 0
        max_frog = 0
        for c in croakOfFrogs:
            if c not in croak_list:
                return -1
            if c == 'c':
                current_frog += 1
                counter[c]+=1
            else:
                previous_char = croak_list[croak_dict[c]-1]
                if counter[previous_char] == 0 or counter[c]==counter[previous_char]:
                    print(counter[previous_char], current_frog)
                    return -1
                counter[c]+=1
                if c=='k':
                    for c in croak_list:
                        counter[c]-=1
                    current_frog-=1
            max_frog = max(max_frog, current_frog)
        for c in croak_list:
            if counter[c] != 0:
                return -1
        return max_frog

            
