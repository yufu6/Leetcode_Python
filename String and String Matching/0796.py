class Solution:
    def rotateString(self, s: str, goal: str) -> bool:

        for i in range(len(s)):
            s = s[1:] + s [0]
            if s == goal:
                return True
        return False

'''
def rotateString(self, A: str, B: str) -> bool:
        return len(A) == len(B) and B in A + A
'''

'''
KMP:

class Solution:
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

    def rotateString(self, s: str, goal: str) -> bool:
        if not s or not goal or len(s) != len(goal):
            return False
        index = self.kmp(s, goal)
        if index == -1:
            return False
        return True
'''
