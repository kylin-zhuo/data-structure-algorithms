"""
Description:
Implement a function to return product suggestions using products from a product repository after each character is typed by the customer in the search bar.
If there are more than THREE acceptable products, return the product name that is first in the alphabetical order.
Only return product suggestions after the customer has entered two characters.
Product suggestions must start with the characters already typed.
Both the repository and the customer query should be compared in a CASE-INSENSITIVE way.

Input:
The input to the method/function consist of three arguments:

    numProducts, an integer representing the number of various products in Amazon's product repository;
    repository, a list of unique strings representing the various products in Amazon's product repository;
    customerQuery, a string representing the full search query of the customer.

Output:
Return a list of a list of strings, where each list represents the product suggestions made by the system as the customer types each character of the customerQuery. 
Assume the customer types characters in order without deleting/removing any characters.

Example:
Input:
numProducts = 5
repository = ["mobile", "mouse", "moneypot", "monitor", "mousepad"]
customerQuery = "mouse"

Output:
[["mobile", "moneypot", "monitor"],
["mouse", "mousepad"],
["mouse", "mousepad"],
["mouse", "mousepad"]]

"""

# class Product(object):
    
#     self.trie = {}
#     self.count = 0

#     def __init__(self, repository):
#         self.count = len(set(repository))
#         t = self.trie
#         for word in repository:
#             for c in word:
#                 if c not in t:
#                     t[c] = {}
#                 t = t[c]
#             t['#'] = {}
    
#     def stream_query(self, word):
#         res = []
#         node = self.trie

from heapq import heappush, heappop
import unittest

class TrieNode(object):
    
    def __init__(self, val):
        self.children = {}
        self.is_word = False
        self.suggestions = []
        self.val = val

class Trie:

    def __init__(self):
        self.root = TrieNode("")
        self.N = 3
    
    def insert(self, word):
        curr = self.root
        val = ""
        for w in word:
            val += w
            if w not in curr.children:
                curr.children[w] = TrieNode(val)
            curr = curr.children[w]
            heappush(curr.suggestions, word)
            if len(curr.suggestions) > self.N:
                heappop(curr.suggestions)
        curr.is_word = True
    
    def build(self, words):
        for word in words:
            self.insert(word)

    def query(self, keyword):
        res = []
        curr = self.root
        for k in keyword:
            if k not in curr.children:
                res.append([])
                continue
            curr = curr.children[k]
            res.append(curr.suggestions)
        return res
        

class Test(unittest.TestCase):

    def test_trie(self):
        trie = Trie()
        products = ["mobile", "mouse", "moneypot", "monitor", "mousepad"]
        query = "mouse"
        expected = [["mobile", "moneypot", "monitor"], ["mouse", "mousepad"], ["mouse", "mousepad"], ["mouse", "mousepad"]]
        trie.build(products)
        
        self.assertEqual(expected, trie.product_suggestions(products, query), "Should return correct list of matched products")

        # trie = Trie()
        # products = ["ps4", "ps4 slim", "ps4 pro", "xbox", "tissue",
        #             "standing table", "house", "true love", "tracking device"]
        # query = "ps4"
        # expected = [["ps4", "ps4 pro", "ps4 slim"], ["ps4", "ps4 pro", "ps4 slim"]]
        # self.assertEqual(expected, trie.product_suggestions(products, query), "Should return correct list of matched products")
        # query = "tru"
        # expected = [["tracking device", "true love"], ["true love"]]
        # self.assertEqual(expected, trie.product_suggestions(products, query), "Should return correct list of matched products")
        # query = "t"
        # self.assertEqual(None, trie.product_suggestions(products, query),
        #                  "Should return None if query is less than 2 characters")
                         
# unittest.main()

if __name__ == "__main__":

    trie = Trie()
    products = ["mobile", "mouse", "moneypot", "monitor", "mousepad"]
    query = "mouse"
    expected = [["mobile", "moneypot", "monitor"], ["mouse", "mousepad"], ["mouse", "mousepad"], ["mouse", "mousepad"]]
    trie.build(products)
    result = trie.query(query)
    print(result)