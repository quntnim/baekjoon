import sys
input = sys.stdin.readline

class Node:
    def __init__(self):
        self.child = {}
        self.check = False 

class Trie:
    def __init__(self):
        self.root = Node()

    def insert(self, s):
        node = self.root
        for c in s:
            if c not in node.child:
                node.child[c] = Node()
            node = node.child[c]
        node.check = True

    def search(self, s):
        node = self.root
        for c in s:
            if c not in node.child:
                return False
            node = node.child[c]
        return node.check

    def startsWith(self, s):
        node = self.root
        for c in s:
            if node.check:
                return False
            node = node.child[c]
        return True

for _ in range(int(input())):
    trie = Trie()
    n = int(input().rstrip())
    arr = []

    for i in range(n):
        st = list(map(int,input().rstrip()))
        trie.insert(st)
        arr.append(st)

    check = True
    for i in arr:
        check *= trie.startsWith(i)
    
    if check:print('YES')
    else:print('NO')