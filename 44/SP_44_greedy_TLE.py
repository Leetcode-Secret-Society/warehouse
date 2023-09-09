class Solution:
    def get_char_at_index(self, input_string, index):
        try:
            char = input_string[index]
            return char
        except IndexError:
            return None

    def isMatch(self, s: str, p: str) -> bool:
        if s == p:
            return True
        if p == '*':
            return True
        if self.get_char_at_index(p,0) == '*' and self.get_char_at_index(p,1) == "*":
            return self.isMatch(s,p[1:])
        if not s and p[0] == '*':
            return self.isMatch(s,p[1:])
        if not s or not p:
            return False
        if s[0] == p[0]:
            #return True
            return self.isMatch(s[1:],p[1:])
        if p[0] == '?':
            #return True
            return self.isMatch(s[1:],p[1:])
        if p[0] == '*': #there are still some chars after start
            return self.isMatch(s,p[1:]) or self.isMatch(s[1:],p)


        return False
