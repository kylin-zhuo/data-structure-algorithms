public class Solution {
    /*
     * @param num: a positive number
     * @return: true if it's a palindrome or false
     */
    public boolean isPalindrome(int num) {
        // write your code here
        String s = "" + num;
        int n = s.length();
        for (int i = 0; ;i++) {
            if (i >= n - i - 1) return true;
            if (s.charAt(i) != s.charAt(n-i-1)) return false;
        }
    }
}