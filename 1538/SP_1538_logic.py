# """
# This is the ArrayReader's API interface.
# You should not implement it, or speculate about its implementation
# """
#class ArrayReader(object):
#	 # Compares 4 different elements in the array
#	 # return 4 if the values of the 4 elements are the same (0 or 1).
#	 # return 2 if three elements have a value equal to 0 and one element has value equal to 1 or vice versa.
#	 # return 0 : if two element have a value equal to 0 and two elements have a value equal to 1.
#    def query(self, a: int, b: int, c: int, d: int) -> int:
#
#	 # Returns the length of the array
#    def length(self) -> int:
#

class Solution:
    def guessMajority(self, reader: 'ArrayReader') -> int:
        #query
        #0: 0011
        #2: 0001 / 1110
        #4: 0000 / 1111
        length = reader.length()
        groupA,groupB = 0,0
        groupAIndex = 3
        baseWith3 = reader.query(0,1,2,3)
        groupA += 1
        for i in range(4,length):
            if baseWith3 == reader.query(0,1,2,i):
                groupA += 1
            else:
                groupB += 1
                groupBIndex = i
        baseWithout3 = reader.query(0,1,2,4)
        baseWithoutN = list()
        baseWithoutN.append(reader.query(1,2,3,4))  #0
        baseWithoutN.append(reader.query(0,2,3,4))  #1
        baseWithoutN.append(reader.query(0,1,3,4))  #2
        for i in range(len(baseWithoutN)):
            if baseWithoutN[i] == baseWithout3:
                groupA += 1
            else:
                groupB += 1
                groupBIndex = i

        # print(f"{groupA=}-{groupAIndex=},{groupB=}-{groupBIndex=}")
        if groupA > groupB:
            return groupAIndex
        elif groupA == groupB:
            return -1
        return groupBIndex
