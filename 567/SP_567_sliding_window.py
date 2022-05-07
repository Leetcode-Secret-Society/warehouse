class Solution:
            
    def checkInclusion(self, s1: str, s2: str) -> bool:
        """
        "adc"
        "dcda"
        
        "adc"
        "dcdda"
        """
        # I tried using stack, but i failed...
        if len(s1) > len(s2):
            return False
        def zero() -> int:
            return 0
        s1_dict = {"a":0, "b":0, "c":0, "d":0, "e":0, "f":0, "g":0, "h":0, "i":0, "j":0, "k":0, "l":0, "m":0, "n":0, "o":0, "p":0, "q":0, "r":0, "s":0, "t":0, "u":0, "v":0, "w":0, "x":0, "y":0, "z":0}
        s2_dict = {"a":0, "b":0, "c":0, "d":0, "e":0, "f":0, "g":0, "h":0, "i":0, "j":0, "k":0, "l":0, "m":0, "n":0, "o":0, "p":0, "q":0, "r":0, "s":0, "t":0, "u":0, "v":0, "w":0, "x":0, "y":0, "z":0}
        for i in range(len(s1)):
            s1_dict[s1[i]] += 1
            s2_dict[s2[i]] += 1
        # print(s1_dict)
        # print(s2_dict)
        # print("=======================")
        if s2_dict == s1_dict:
            return True
        for i in range(len(s1), len(s2)):
            # print(s2[i])
            s2_dict[s2[i]] += 1
            # print(s2[i - len(s1)])
            s2_dict[s2[i - len(s1)]] -= 1
            # print(s2_dict)
            if s2_dict == s1_dict:
                return True
        return False
