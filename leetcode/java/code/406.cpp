class Solution {
public:
    /*
     * @param nums: an array of integers
     * @param s: An integer
     * @return: an integer representing the minimum size of subarray
     */
    int minimumSize(vector<int> nums, int s) {
        // write your code here
        if (nums.size() == 0) return -1;
        int i = 0, j = 0;
        int temp = 0;
        int minv = INT_MAX;
        while (j < nums.size()) {
            temp += nums[j++];
            while (temp >= s) {
                minv = min(minv, j-i);
                temp -= nums[i++];
            }
        }
        return minv == INT_MAX ? -1:minv;
    }
};