# """
# This is ArrayReader's API interface.
# You should not implement it, or speculate about its implementation
# """
#class ArrayReader(object):
#	 # Compares the sum of arr[l..r] with the sum of arr[x..y]
#	 # return 1 if sum(arr[l..r]) > sum(arr[x..y])
#	 # return 0 if sum(arr[l..r]) == sum(arr[x..y])
#	 # return -1 if sum(arr[l..r]) < sum(arr[x..y])
#    def compareSub(self, l: int, r: int, x: int, y: int) -> int:
#
#	 # Returns the length of the array
#    def length(self) -> int:
#


class Solution:
    def getIndex(self, reader: 'ArrayReader') -> int:
        l = 0
        leng = reader.length()
        while leng > 1:
            leng //= 2
            r = l + leng - 1        #l + leng - 1
            x = l + leng            #r + 1
            y = l + leng + leng - 1 #r + leng
            result = reader.compareSub(l,r,x,y)
            if result == 0:
                return y + 1        #must be right most one
            elif result == -1:
                l += leng           #shift left
            else:
                pass          #shift right, default
        return l
