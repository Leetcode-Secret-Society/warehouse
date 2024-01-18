from random import choice


class RandomizedSet:

    def __init__(self):
        self.elements_map = {}
        self.elements = []

    def insert(self, val: int) -> bool:
        if val in self.elements_map:
            return False
        self.elements_map[val] = len(self.elements)
        self.elements.append(val)
        return True

    def remove(self, val: int) -> bool:
        if val not in self.elements_map:
            return False
        last_element = self.elements[-1]
        val_index = self.elements_map[val]
        self.elements[val_index] = last_element
        self.elements_map[last_element] = val_index
        self.elements.pop()
        del self.elements_map[val]
        return True

    def getRandom(self) -> int:
        return choice(self.elements)
