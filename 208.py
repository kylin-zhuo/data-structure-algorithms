"""
208. Implement Trie (Prefix Tree)

Implement a trie with insert, search, and startsWith methods.

Note:
You may assume that all inputs are consist of lowercase letters a-z.
"""

class TrieNode(object):
    def __init__(self):
        self.children = [None] * 26
        self.isLeaf = False

class Trie(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = TrieNode()

    def charToIndex(self, ch):
        return ord(ch) - ord('a')
        
    def insert(self, word):
        """
        Inserts a word into the trie.
        :type word: str
        :rtype: void
        """
        # if not present, insert the key into this trie
        pCrawl = self.root
        length = len(word)
        for level in range(length):
            index = self.charToIndex(word[level])
            if not pCrawl.children[index]:
                pCrawl.children[index] = TrieNode()
            pCrawl = pCrawl.children[index]
            
            # mark the last node as leaf
        pCrawl.isLeaf = True

    def search(self, word):
        """
        Returns if the word is in the trie.
        :type word: str
        :rtype: bool
        """
        pCrawl = self.root
        length = len(word)
        for level in range(length):
            index = self.charToIndex(word[level])
            if not pCrawl.children[index]:
                return False
            pCrawl = pCrawl.children[index]
        
        return pCrawl != None and pCrawl.isLeaf

    def startsWith(self, prefix):
        """
        Returns if there is any word in the trie that starts with the given prefix.
        :type prefix: str
        :rtype: bool
        """
        pCrawl = self.root
        length = len(prefix)
        for level in range(length):
            index = self.charToIndex(prefix[level])
            if not pCrawl.children[index]:
                return False
            pCrawl = pCrawl.children[index]
        return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)