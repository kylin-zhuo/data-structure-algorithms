public class Solution {
    /*
     * @param s: the string that represents a number
     * @return: whether the string is a valid number
     */
    public boolean isNumber(String s) {
        // write your code here
        if (s == null) return false;
        String ss = s.trim();
        if (ss.length() == 0) return false;
        if (ss.split(" ").length > 1) return false;
        if (ss.equals(".") || ss.equals(".")) return false;
        if (ss.charAt(0) == '+' || ss.charAt(0) == '-') {
            ss = ss.substring(1);
        }
        int countE = 0;
        int countD = 0;
        for (int i = 0; i < ss.length(); i++) {
            char c = ss.charAt(i);
            if (c != 'e' && c != '.' && (c < '0' || c > '9')) return false;
            if (c == 'e') countE += 1;
            if (c == '.') countD += 1;
            if (countE > 1 || countD > 1) return false;
        }
        if (ss.charAt(ss.length()-1) == 'e' || ss.charAt(0) == 'e') return false;
        if (countE < 1 || countD < 1) return true;
        return ss.indexOf('.') < ss.indexOf('e');
        
    }
}