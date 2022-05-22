class Solution:
    def repeatedStringMatch(self, a: str, b: str) -> int:
        m, n = len(a), len(b)
        times = int(n/m + 3)
        for i in range(1, times):
            if b in a*i:
                return i
        return -1

'''
class Solution:
    # KMP 匹配算法，T 为文本串，p 为模式串
    def kmp(self, T: str, p: str) -> int:
        n, m = len(T), len(p)

        next = self.generateNext(p)

        i, j = 0, 0
        while i - j < n:
            while j > 0 and T[i % n] != p[j]:
                j = next[j - 1]
            if T[i % n] == p[j]:
                j += 1
            if j == m:
                return i - m + 1
            i += 1
        return -1

    def generateNext(self, p: str):
        m = len(p)
        next = [0 for _ in range(m)]

        left = 0
        for right in range(1, m):
            while left > 0 and p[left] != p[right]:
                left = next[left - 1]
            if p[left] == p[right]:
                left += 1
            next[right] = left

        return next

    def repeatedStringMatch(self, a: str, b: str) -> int:
        len_a = len(a)
        len_b = len(b)
        index = self.kmp(a, b)
        if index == -1:
            return -1
        if len_a - index >= len_b:
            return 1
        return (index + len(b) - 1) // len(a) + 1
'''
