public class WordDictionary {
    /*
     * @param word: Adds a word into the data structure.
     * @return: nothing
     */
    
    private class TrieNode {
        boolean isLeaf = false;
        TrieNode[] children = new TrieNode[26];
    }
    
    TrieNode root = new TrieNode();
    
    public void addWord(String word) {
        TrieNode cur = root;
        char[] data = word.toLowerCase().toCharArray();
        for (int i = 0; i < data.length; i++) {
            int index = data[i] - 'a';
            if (cur.children[index] == null) {
                cur.children[index] = new TrieNode();
            }
            cur = cur.children[index];
        }
        cur.isLeaf = true;
    }

    /*
     * @param word: A word could contain the dot character '.' to represent any one letter.
     * @return: if the word is in the data structure.
     */
    public boolean search(String word) {
        char[] data = word.toLowerCase().toCharArray();
        return searchHelper(root, data, 0);
    }
    
    private boolean searchHelper(TrieNode cur, char[] data, int index) {
        if (index == data.length) return cur.isLeaf;
        if (data[index] == '.') {
            for (int i = 0; i < 26; i++) {
                if (cur.children[i] != null && searchHelper(cur.children[i], data, index+1)) return true;
            }
            return false;
        } else {
            int pos = data[index] - 'a';
            if (cur.children[pos] == null) return false;
            else return searchHelper(cur.children[pos], data, index+1);
        }
    }
}