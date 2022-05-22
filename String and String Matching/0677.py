
class MapSum:

    def __init__(self):
        self._dict = dict()

    def insert(self, key: str, val: int) -> None:
        self._dict[key] = val

    def sum(self, prefix: str) -> int:
        result = 0
        for key in self._dict.keys():
            #print(key)
            if key.find(prefix) == 0:
                result = result + self._dict[key]
        return result

# Your MapSum object will be instantiated and called as such:
# obj = MapSum()
# obj.insert(key,val)
# param_2 = obj.sum(prefix)
'''
Use prefix tree with Node class
class TrieNode:
    def __init__(self):
        self.children = {}
        self.score = 0

class MapSum:

    def __init__(self):
        self.map = {}
        self.root = TrieNode()

    def insert(self, key: str, val: int) -> None:
        delta = val - self.map.get(key, 0)
        self.map[key] = val
        cur = self.root
        cur.score += delta
        for char in key:
            cur = cur.children.setdefault(char, TrieNode())
            cur.score += delta

        19-21 equal to:
        for c in key:
            if c not in curr.children:
                curr.children[c] = TrieNode()
            curr = curr.children[c]
            curr.score += delta

    def sum(self, prefix: str) -> int:
        cur = self.root
        for char in prefix:
            if char not in cur.children:
                return 0
            cur = cur.children[char]
        return cur.score
'''
'''
with defaultdict

from collections import defaultdict
class TrieNode(object):
    def __init__(self):
        self.children=defaultdict(TrieNode)
        self.isWord=False
        self.freq=0

class MapSum(object):

    def __init__(self):
        self.root=TrieNode()
        self._dict={}

    def insert(self, key, val):
        current=self.root
        for letter in key:
            current=current.children[letter]
            current.freq+=val-self._dict.get(key,0)
        current.isWord=True
        self._dict[key]=val

    def sum(self, prefix):
        current =self.root
        for letter in prefix:
            current=current.children.get(letter)
            if current==None:
                return 0
        return current.freq

# Your MapSum object will be instantiated and called as such:
# obj = MapSum()
# obj.insert(key,val)
# param_2 = obj.sum(prefix)


'''
# Your MapSum object will be instantiated and called as such:
# obj = MapSum()
# obj.insert(key,val)
# param_2 = obj.sum(prefix)
