class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        def generateNext(p: str):
            j = 0
            next = [0 for _ in range(len(p))]
            for i in range(1,len(p)):
                while j > 0 and p[i] != p[j]:
                    j = next[j - 1]
                if p[i] == p[j]:
                    j += 1
                next[i] = j
            return next

        next = generateNext(s)
        print(next)
        n = len(s)
        print(n)
        print(n % (n - next[n-1]))
        if next[n - 1] != 0 and n % (n-next[n-1]) == 0:
            return True
        else:
            return False


'''
class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        return (s + s).find(s, 1) != len(s)
'''
