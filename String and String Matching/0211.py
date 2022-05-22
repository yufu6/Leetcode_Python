class WordDictionary:

    def __init__(self):
        self.root = {}

    def addWord(self, word: str) -> None:
        cur = self.root
        for w in word:
            if w not in cur:
                cur[w] = {}
            cur = cur[w]
        cur['#'] = True

    def search(self, word: str) -> bool:

        return self.sc(self.root, word, 0)

    def sc(self, nod, word, i):
        if i == len(word):
            return '#' in nod
        if word[i] == '.':
            for child in nod:
                if child != '#' and self.sc(nod[child], word, i + 1):
                    return True
            return False

        if word[i] not in nod:
            return False
        return self.sc(nod[word[i]], word, i + 1)

'''
from collections import defaultdict

class WordDictionary:

    def __init__(self):
        self.dict = defaultdict(set)

    def addWord(self, word: str) -> None:
        self.dict[len(word)].add(word)

    def search(self, word: str) -> bool:
        if '.' not in word:
            return word in self.dict[len(word)]

        for w in self.dict[len(word)]:
            for i in range(len(word)):
                if word[i] != '.' and word[i] != w[i]:
                    break
            else:
                return True

        return False

'''
