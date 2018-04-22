public class Solution {
    /*
     * @param n: n pairs
     * @return: All combinations of well-formed parentheses
     */
    public List<String> generateParenthesis(int n) {
        // write your code here
        List<String> result = new ArrayList<String>();
        backtrack("", result, 0, 0, 0, n);
        return result;
    }
    
    private void backtrack(String current, List<String> result, int nleft, int nright, int len, int n) {
        if (nright > nleft || len > 2 * n) return;
        if (len == 2 * n && nleft == nright) {
            result.add(current);
            return;
        }
        backtrack(current + "(", result, nleft+1, nright, len+1, n);
        backtrack(current + ")", result, nleft, nright+1, len+1, n);
    }
}