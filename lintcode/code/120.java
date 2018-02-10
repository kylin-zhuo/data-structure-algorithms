public class Solution {
    /*
     * @param start: a string
     * @param end: a string
     * @param dict: a set of string
     * @return: An integer
     */
    public int ladderLength(String start, String end, Set<String> dict) {
        // write your code here
        if (start == null || end == null || dict.isEmpty()) return 0;
        if (start.equals(end)) return 1;
        
        Queue<Wrapper> queue = new LinkedList<Wrapper>();
        queue.add(new Wrapper(start));
        dict.remove(start);
        
        while (!queue.isEmpty()) {
            Wrapper w = queue.poll();
            String word = w.str;
            // System.out.print(word + " ");
            // if (word.equals(end)) return w.len;
            char[] arr = word.toCharArray();
            for (int i = 0; i < arr.length; i++) {
                char orig = arr[i];
                for (char c = 'a'; c <= 'z'; c++) {
                    arr[i] = c;
                    String s = new String(arr);
                    if (s.equals(end)) return w.len+1;
                    if (dict.contains(s)) {
                        dict.remove(s);
                        queue.add(new Wrapper(s, w.len+1));
                    }
                    arr[i] = orig;
                }
            }
        }
        return 0;
    }
    
    private static class Wrapper {
        int len;
        String str;
        Wrapper(String str) {
            this.str = str;
            this.len = 1;
        }
        Wrapper(String str, int len) {
            this.str = str;
            this.len = len;
        }
    }
    
}

