public class Solution {
    /*
     * @param nums: A list of integers
     * @return: the median of numbers
     */
    
    private PriorityQueue<Integer> minHeap = new PriorityQueue<>(11, new Comparator<Integer>() {
        public int compare(Integer o1, Integer o2) {
            return o1 - o2;
        }
    });
    
    private PriorityQueue<Integer> maxHeap = new PriorityQueue<>(11, new Comparator<Integer>() {
        public int compare(Integer o1, Integer o2) {
            return o2 - o1;
        }
    });
    
    private int count = 0;
    
    public void insert(Integer num) {
        count ++;
        if (count % 2 == 0) {
            maxHeap.offer(num);
            int i = maxHeap.poll();
            minHeap.offer(i);
        } else {
            minHeap.offer(num);
            int i = minHeap.poll();
            maxHeap.offer(i);
        }
    }
    
    public int getMedian() {
        return maxHeap.peek();
    }
    
    public int[] medianII(int[] nums) {
        // write your code here
        int[] res = new int[nums.length];
        for (int i = 0; i < nums.length; i ++) {
            insert(nums[i]);
            res[i] = getMedian();
        }
        return res;
    }
}