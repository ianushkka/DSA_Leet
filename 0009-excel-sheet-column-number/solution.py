import string

class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        s = string.ascii_uppercase

        d = {val: key for key, val in enumerate(s, start=1)}

        c = columnTitle[::-1]
        res = 0
        for i in range(len(c)):
            res += (26**i) * (d[c[i]])

        return res
