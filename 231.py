class Solution(object):
    def isPowerOfTwo(self, n):
        return n > 0 and (n & (n - 1)) == 0
    
    def isPowerOf3(self, n):
        return