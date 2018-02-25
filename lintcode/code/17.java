public class Solution {
    
    /*
     * @param nums: A set of numbers
     * @return: A list of lists
     */
    List<List<Integer>> result = new ArrayList<>();
	
    public List<List<Integer>> subsets(int[] nums) {
        Arrays.sort(nums);
        backtracking(nums, 0, new ArrayList<>());
        return result;
    }
    
    public void backtracking(int[] nums, int i, ArrayList<Integer> arrayList){
    	result.add(new ArrayList<>(arrayList));
    	if (i< nums.length){
    		for (int j = i; j < nums.length ; j++){
    			arrayList.add(nums[j]);
        		backtracking(nums, j+1, arrayList);
        		arrayList.remove(arrayList.size()-1);
    		}
    	}
    }
}