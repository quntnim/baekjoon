import sys
input = sys.stdin.readline

class Trie:
    def __init__(self):
        self.root = {}

    def insert(self, s):
        cur_node = self.root
        for c in s:
            if c not in cur_node:
                cur_node[c] = {}
            cur_node = cur_node[c]
        cur_node["*"] = s

    def startsWith(self, s):
        t = self.root
        for c in s:
            if c not in t:
                return False
            t = t[c]
        return True

trie = Trie()
n,m = map(int,input().rstrip().split())
cnt = 0
for i in range(n):
    trie.insert(input().rstrip())

for i in range(m):
    if trie.startsWith(input().rstrip()):cnt+=1

print(cnt)