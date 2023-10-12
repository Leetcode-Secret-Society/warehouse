class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        letter_list = list()
        digit_list = list()
        for log in logs:
            elements = log.split(" ")
            key = elements[0]
            if elements[1].isdigit():
                digit_list.append(log)
            else:
                letter_list.append(log)
        result = list()
        def get_letter_key(log):
            elements = log.split(" ", maxsplit=1)
            return (elements[1], elements[0])
        result += sorted(letter_list, key=get_letter_key)
        result += digit_list

        return result

