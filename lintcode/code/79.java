public class Solution {
    /*
     * @param strs: A list of strings
     * @return: The longest common prefix
     */
    public String longestCommonPrefix(String[] strs) {
        // write your code here
        if (strs == null || strs.length == 0) return "";
        if (strs.length == 1) return strs[0];

        int n = strs.length;
        boolean flag = true;
        boolean completed = true;
        int i;
        for (i = 0; i < strs[0].length() && flag; i ++) {
            char c = strs[0].charAt(i);
            for (int j = 1; j < n; j ++) {
                if (i > strs[j].length() - 1 || strs[j].charAt(i) != c) {
                    flag = false;
                    completed = false;
                    break;
                }
            }
        }
        return completed ? strs[0].substring(0, i):strs[0].substring(0, i-1);
    }
}