class Solution:
    def reverseDegree(self, s: str) -> int:
        rev_degree = 0
        for i , c in enumerate(s):
            rev_val = 26 - (ord(c) - ord('a'))
            position = i+1

            rev_degree += rev_val * position
        return rev_degree
        


        