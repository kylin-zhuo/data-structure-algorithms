public class Solution {
    /*
     * @param : the array
     * @return: the max xor sum of the subarray in a given array
     */
    
    private class TrieNode {
        int val = 0;
        TrieNode[] children = new TrieNode[2];
    } 
    
    public int maxXorSubarray(int[] nums) {
        // write code here
        TrieNode root = new TrieNode();
        insert(root, 0);
        int res = Integer.MIN_VALUE;
        int prefix = 0;
        for (int i = 0; i < nums.length; i++) {
            prefix = prefix ^ nums[i];
            insert(root, prefix);
            res = Math.max(res, query(root, prefix));
        }
        return res;
    }
    
    void insert(TrieNode root, int prefix) {
        TrieNode cur = root;
        for (int i = 31; i >= 0; i--) 
        {
            int val = ((1 << i) & prefix) >> i;
            if (cur.children[val] == null) 
            {
                cur.children[val] = new TrieNode();
            }
            cur = cur.children[val];
        }
        cur.val = prefix;
    }
    
    int query(TrieNode root, int prefix)
    {
        TrieNode cur = root;
        for (int i = 31; i >= 0; i--) 
        {
            int val = (prefix & (1 << i)) >> i;
            if (cur.children[1 - val] != null) cur = cur.children[1 - val];
            else cur = cur.children[val];
        }
        return prefix ^ (cur.val);
    }
}