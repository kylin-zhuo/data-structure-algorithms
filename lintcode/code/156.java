/**
 * Definition of Interval:
 * public class Interval {
 *     int start, end;
 *     Interval(int start, int end) {
 *         this.start = start;
 *         this.end = end;
 *     }
 */


public class Solution {
    /*
     * @param intervals: interval list.
     * @return: A new interval list.
     */
    public List<Interval> merge(List<Interval> intervals) {
        // write your code here
        Collections.sort(intervals, new Comparator<Interval>() {
            public int compare(Interval i1, Interval i2) {
                if (i1.start < i2.start) return -1;
                else if (i1.start > i2.start) return 1;
                else if (i1.end < i2.end) return -1;
                else if (i1.end > i2.end) return 1;
                else return 0;
            }
        });
        
        List<Interval> result = new ArrayList<Interval>();
        for (int i = 0; i < intervals.size(); i++) {
            Interval it = intervals.get(i);
            if (result.size() == 0) {
                result.add(it);
            } else {
                Interval last = result.get(result.size()-1);
                if (last.end >= it.start) {
                    last.end = Math.max(last.end, it.end);
                } else {
                    result.add(it);
                }
            }
        }
        return result;
    }
}