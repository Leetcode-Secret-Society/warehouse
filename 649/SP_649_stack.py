class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        #DRDRR
        #^x
        #dx^xR
        #xxdx^
        #xx^xx
        #xxDxx
        d_stack = deque()
        r_stack = deque()
        for i in range(len(senate)):
            c = senate[i]
            if c == "D":
                d_stack.append(i)
            else:
                r_stack.append(i)
        counter = len(senate) - 1
        while len(d_stack) > 0 and len(r_stack) > 0:
            counter += 1
            if d_stack[0] < r_stack[0]:
                d_stack.append(counter)
            else:
                r_stack.append(counter)
            r_stack.popleft()
            d_stack.popleft()

        return "Dire" if len(d_stack) > 0 else "Radiant"
