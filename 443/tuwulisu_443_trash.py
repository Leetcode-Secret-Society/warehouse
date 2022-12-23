class Solution:
    def compress(self, chars: List[str]) -> int:
        previous_char = chars[0]
        count = 1
        index = 0
        for char in chars[1:]:
            if char == previous_char:
                count+=1
            else:
                if count==1:
                    chars[index] = previous_char
                    index+=1
                    count=1
                else:
                    chars[index] = previous_char
                    count2 = count
                    digits = 0
                    while count2:
                        count2=count2//10
                        digits+=1
                    for d in range(digits, 0, -1):
                        chars[index+d] = str(count%10)
                        count=count//10
                    index+=digits+1
                    count=1
                previous_char = char
        if count==1:
            chars[index] = previous_char
            index+=1
            count=1
        else:
            chars[index] = previous_char
            count2 = count
            digits = 0
            while count2:
                count2=count2//10
                digits+=1
            for d in range(digits, 0, -1):
                chars[index+d] = str(count%10)
                count=count//10
            index+=digits+1
            count=1
        return index
