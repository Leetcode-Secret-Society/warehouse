class Solution:
    def simplifyPath(self, path: str) -> str:
        result = ["/"]
        temp = ""
        for i in range(1, len(path)):
            if path[i] == "/":
                if temp == "" or temp == ".":
                    pass
                elif temp == "..":
                    if len(result) != 1:
                        result.pop()
                        result.pop()
                else:
                    result.append(temp)
                    result.append("/")
                temp = ""
            else:
                temp += path[i]
        if temp == "..":
            if len(result) != 1:
                result.pop()
                result.pop()
        elif temp == "." or temp == "":
            pass
        else:
            result.append(temp)
        if len(result) != 1 and result[-1] == "/":
            result.pop()
        return "".join(result)