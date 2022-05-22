class Solution:
    def strStr(self, haystack: str, needle: str) -> int:

        def nextLst(p: str):
            plen = len(p)
            next = [0 for _ in range(plen)]
            j = 0

            for i in range(1, plen):
                while j > 0 and p[i] != p[j]:
                    j = next[j-1]
                if p[i] == p[j]:
                    j += 1
                next[i] = j

            return next

        nextl = nextLst(needle)
        j= 0

        if len(needle) == 0:
            return 0

        for i in range(len(haystack)):
            while j > 0 and haystack[i] != needle[j]:
                j = nextl[j - 1]
            if haystack[i] == needle[j]:
                j += 1
            if j == len(needle):
                print(i, j)
                return (i-j + 1)
        return -1
