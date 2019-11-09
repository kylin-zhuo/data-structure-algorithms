
public class Trie {
    
    private class TrieNode {
        boolean isLeaf;
        TrieNode[] children = new TrieNode[26];
        char val;
        
        public TrieNode(char val) {
            this.val = val;
            isLeaf = false;
        }
    }

    
    TrieNode root;
    
    public Trie() {
        // do intialization if necessary
        root = new TrieNode(' ');
    }

    /*
     * @param word: a word
     * @return: nothing
     */
    public void insert(String word) {
        // write your code here
        TrieNode cur = root;
        char[] data = word.toLowerCase().toCharArray();
        for (int i = 0; i < data.length; i++) {
            int index = data[i] - 'a';
            if (cur.children[index] == null) {
                cur.children[index] = new TrieNode(data[i]);
            }
            cur = cur.children[index];
        }
        cur.isLeaf = true;
    }

    /*
     * @param word: A string
     * @return: if the word is in the trie.
     */
    public boolean search(String word) {
        // write your code here
        TrieNode cur = root;
        char[] data = word.toLowerCase().toCharArray();
        for (int i = 0; i < data.length; i++) {
            int index = data[i] - 'a';
            if (cur.children[index] == null) return false;
            cur = cur.children[index];
        }
        return cur.isLeaf;
    }

    /*
     * @param prefix: A string
     * @return: if there is any word in the trie that starts with the given prefix.
     */
    public boolean startsWith(String prefix) {
        // write your code here
        TrieNode cur = root;
        char[] data = prefix.toLowerCase().toCharArray();
        for(int i = 0; i < data.length; i++) {
            int index = data[i] - 'a';
            if (cur.children[index] == null) return false;
            cur = cur.children[index];
        }
        return true;
    }
}