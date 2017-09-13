class TreeNode(object):

    def __init__(self):
        self.next = [None] * 26
        self.index = -1
        self.list = []

def add_word(root, word, index):
    for i in range(len(word)-1, -1, -1):
        j = ord(word[i]) - ord('a')
        if not root.next[j]:
            root.next[j] = TreeNode()
        if is_palindrome(word, 0, i):
            root.list.append(index)
        root = root.next[j]
    root.list.append(index)
    root.index = index

def is_palindrome(word, i, j):
    while i < j:
        if word[i] != word[j]:
            return False
        i += 1
        j -= 1
    return True


def search(words, i, root, res):
    for j in range(len(words[i])):
        if root.index >= 0 and root.index != i and is_palindrome(words[i], j, len(words[i]) - 1):
            res.append([i, root.index])
        root = root.next[ord(words[i][j]) - ord('a')]
        if not root:
            return 

    for j in root.list:
        if i == k:
            continue
        res.append([i,j])

def padlindromePairs(words):
    res = []
    root = TrieNode()
    for i in range(len(words)):
        add_word(root, words[i], i)
    for i in range(len(words)):
        search(words, i, root, res)
    return res


