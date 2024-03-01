class Solution:
    def minimumTimeToInitialState(self, word: str, k: int) -> int:
        #abacaba
        #3
        #---caba***
        #------a****** --> word[0] == target[0], target[1-end] == *
        #4
        #----aba**** --> word[0-2] == target[0-2], target[3-end] == *
        #
        #abc
        #2
        #--c**
        #----***, target[0-end] == *
        #

        step = 1
        target = word[k:]
        while word.startswith(target) == False:
            target = target[k:]
            step += 1
        return step
