class TrieNode:
    def __init__(self):
        self.children = {}
        self.endOfTheWord = False
class Trie:
    def __init__(self):
        self.root = TrieNode()
    def insertNode(self,word):
        current = self.root
        for char in word:
            if char not in current.children:
                current.children[char] = TrieNode()
            current = current.children[char]
        current.endOfTheWord = True
    def search(self,prefix):
        current = self.root
        for char in prefix:
            if char not in current.children:
                return []
            current = current.children[char]

        result = []
        self._dfs(current,prefix,result)
        print(result)
    def _dfs(self,node,prefix,result):
        if node.endOfTheWord:
            result.append(prefix)
        for char, nextNode in node.children.items():
            self._dfs(nextNode,prefix + char,result)

trie = Trie()
trie.insertNode("cart")
trie.insertNode("art")
trie.insertNode("car")
trie.insertNode("carpenter")
trie.insertNode("carpet")
trie.search("carp")