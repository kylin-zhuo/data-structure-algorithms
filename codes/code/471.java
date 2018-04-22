public class Solution {
    /*
     * @param words: an array of string
     * @param k: An integer
     * @return: an array of string
     */
    class Tuple {
        String word;
        int count;
        Tuple (String word, int count) {
            this.word = word;
            this.count = count;
        }
    }
    
    public String[] topKFrequentWords(String[] words, int k) {
        // write your code here
        Map<String, Integer> map = new HashMap<>();
        for (String word:words) {
            if (map.containsKey(word)) map.put(word, map.get(word)+1);
            else map.put(word, 1);
        }
        Queue<Tuple> heap = new PriorityQueue<Tuple>(11, new Comparator<Tuple>() {
            public int compare(Tuple t1, Tuple t2) {
                if (t1.count < t2.count) return 1;
                else if (t1.count > t2.count) return -1;
                else if (t1.word.compareTo(t2.word) < 0) return -1;
                else if (t1.word.compareTo(t2.word) > 0) return 1;
                else return 0;
            }
        });
        for (String word:map.keySet()) {
            heap.offer(new Tuple(word, map.get(word)));
        }
        String[] res = new String[k];
        for (int i = 0; i < k; i++) {
            res[i] = heap.poll().word;
        }
        return res;
        
    }
}