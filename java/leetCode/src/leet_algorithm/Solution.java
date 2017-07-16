package leet_algorithm;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.Collection;
import java.util.Comparator;
import java.util.HashSet;
import java.util.List;
import java.util.Map;
import java.util.PriorityQueue;

import javax.swing.text.StyledEditorKit.ForegroundAction;
import javax.swing.tree.TreeNode;

public class Solution {
	
	// no_9 palindrome number
    public boolean isPalindrome(int x) {
        if (x < 0)
            return false;
        int div = 1;
        while (x / div >= 10) {
            div *= 10;
        }
        while (x != 0) {
            int l = x / div;
            int r = x % 10;
            if (l != r)
                return false;
            x = (x % div) / 10;
            div /= 100;
        }
        return true;
    }
    
    // no_13 roman to integer
    public int romandigitToInt(char c){
    	switch (c) {
		case 'I':
			return 1; 
		case 'V':
			return 5;
		case 'X':
			return 10;
		case 'L':
			return 50;
		case 'C':
			return 100;
		case 'D':
			return 500;
		case 'M':
			return 1000;
		default:
			return 0;
		}
    } 
    public int romanToInt(String s) {
        // consider if the input contains not only capital letters
    	String digs = "IVXLCDM";
    	//String specials = "IVLD";
    	
    	int res = 0;
    	if(s.length() == 1)
    		return romandigitToInt(s.charAt(0));
    	if(s.length() == 0)
    		return 0;
    	int i = 0;
    	while(i<s.length()){
    		char c1 = s.charAt(i);
    		// the condition which requires to examine only one digit
    		if((c1=='V' || c1=='L' || c1=='D' || c1=='M') || i==s.length()-1){
    			res = res + romandigitToInt(c1);
    			i = i+1;
    		} else {
    			// examine two digits
    			char c2 = s.charAt(i+1);
    			if(digs.indexOf(c2) > digs.indexOf(c1))
    			{
    				res = res + romandigitToInt(c2)- romandigitToInt(c1);
    				i = i+2;
    			}
    			else 
    			{
    				res = res + romandigitToInt(c1);
        			i = i+1;
    			}
    		}
    	}
        return res;
    }
    
    // no_14 longest common prefix
    public String longestCommonPrefix(String[] strs) {
		if(strs.length == 0)
			return "";
		if(strs.length == 1)
		    return strs[0];
		if(strs[0].length()==0)
			return "";
		String res = "";
		int i = 0;
		char c;
		boolean flag = true;
		while(flag){
			if(strs[0].length() <= i){
				flag = false;
				break;
			}
			c = strs[0].charAt(i);
			for(int j = 0; j<strs.length; j++){
				if(strs[j].length() <= i){
					flag = false;
					break;
				}
				if(strs[j].charAt(i) != c){
					flag = false;
					break;
				}
			}
			if(flag){
	    		i = i+1;
	    		res = res + (""+c);
			}
		}
		return res;
    }
    
    
    // no_27 remove element 
    public int removeElement(int[] nums, int val) {
        if(nums.length == 0){
            return 0;
        }
        int res = nums.length;
        for(int i=0; i<nums.length; i++){
        	if(val==nums[i])
        		res = res - 1;
        }
        return res;
    }
    
    
    public int titleToNumber(String s) {
        /* 1
        if(s.length()==1){
        return (int)s.charAt(0) - 64;
        }else 
        return titleToNumber(s.substring(1))+ ((int)s.charAt(0) - 64)*26;
        */
        
        // 2
        int len = s.length();
        int res = 0;
        while(len>0){
            res = res + (int)Math.pow(26,s.length()-len)*((int)s.charAt(len-1) - 64);
            len--;
        }
        return res;
        
    }
    
    // no_168
    public String convertToTitle(int n) {
        String tmp_result = new String();
        while(n > 0){  
        int temp = n%26;
        if (temp == 0) {tmp_result += 'Z'; n -= 26;}
        else {tmp_result += (char)(temp+64);}
        n = n / 26;
        }
        String result = "";
        for(int i=tmp_result.length()-1; i>=0; i--){
        	result = result + tmp_result.charAt(i);
        }
        return result;
   }
    
    // no_172
    public int trailingZeroes(int n) {
    	
        if (n < 5)
        {
            return 0;
        }
        else
        {
            return (n / 5 + trailingZeroes(n / 5));
        }
    }
    
    public int trailingZeroes1(int n) {
    	int res = 0;
        if (n < 5)
        {
            return 0;
        } else{
        
        for(int i = 5; i<=n; i++){
        	int tmp = i;
        	while(tmp%5==0){
        		res = res + 1;
        		tmp=tmp/5;
        	}
        }
        }
        return res;
    }
    
    // no_38 count and say
    public String countAndSay(int n) {
    	if(n==0)
    		return "";
    	if(n==1)
    		return "1";
    	String res = "";
    	String str = "1";
    	int i = 0;
    	int count = 1;
    	
    	for(int k = 2; k<=n; k++){
        	while(i<str.length()){
        		char current = str.charAt(i);
        		if(i==str.length()-1){
        			res += (""+count+current);
        			break;
        		} else{
            		if(str.charAt(i+1)==current){
            			count++;
            		} else {
            			res += (""+count+current);
            			count = 1;
            		}
        		}
        		i++;
        	}
        	if(k!=n){
        		str = res;
            	res = "";
            	i = 0;
            	count = 1;
        	}
    	}
    	return res;
    }
    
    // no_67 add binary
    public String addBinary(String a, String b) {
        String res = "";
        int i = 1;
        boolean carry = false;
        char c_a, c_b;
        char flag = 'a';
        // process the common part of two string
        //"110010"
        //" 10111"
        while(i <= a.length() || i <= b.length()){
        	if(i<=a.length())
        		c_a = a.charAt(a.length()-i);
        	else
        		break;
        	if(i<=b.length())
        		c_b = b.charAt(b.length()-i);
        	else{
        		flag = 'b';
        		break;
        	}
        	if(c_a != c_b){
        		if(carry)
        			res = res + "0";
        		else
        			res = res + "1";
        	} else if (c_a == '0'){
        		if(carry){
        			res = res + "1";
        			carry = false;
        		}else
        			res = res + "0";
        	} else {
        		if(carry)
        			res = res + "1";
        		else{
        			res = res + "0";
        			carry = true;
        		}
        	}
        	i++;
        }
        
        String remain;
        //
        if(flag=='b')
        	 remain = a;
        else
        	 remain = b;
        
        // 111001
        //   1001
        for(int j = i; j<=remain.length(); j++){
        	if(carry){
        		if(remain.charAt(remain.length()-j) == '1'){
        			res = res + "0";
        		} else {
        			res = res + "1";
        			carry = false;
        		}
        	}
        	else {
        		res = res + remain.charAt(remain.length()-j);
        	}
        }
        
        if(carry)
        	res = res + "1";
        
        String new_res = "";
        for (int k = res.length()-1; k>=0; k--) {
			new_res += res.charAt(k);
		}
        return new_res;
    }
    
    // no_113 path sum II
    public List<List<Integer>> pathSum(TreeNode root, int sum) {
        List<List<Integer>> res = new ArrayList<List<Integer>>();
        List<Integer> solution = new ArrayList<Integer>();
        
        
        return res;
    }
    
    // no_202 happy number
    public boolean isHappy(int n) {
    	return checkHappy(n, new ArrayList<Integer>());
    }
    
    public boolean checkHappy(int n, ArrayList<Integer> seen){
    	if(n<=0)
    		return false;
    	if(n==1)
    		return true;
    	
    	while(squareSum(n) != 1){
        	if(seen.contains(n)){
        		return false;
        	}
        	seen.add(n);
        	n = squareSum(n);
    	}
    	return true;
    }
    
    public int squareSum(int n){
    	int res = 0;
    	do{
    		res += (n%10)*(n%10);
    		n = n/10;
    	} while(n>0);
    	return res;
    }
    // no_202 ends
    
    // no_258 add digits
    public int addDigits(int num) {
        // the use of digital root
    	// digital root = 1 + (n-1)%9;
    	return 1 + (num-1)%9;
    }
    
    // no_263
    // Ugly numbers are positive numbers whose prime factors only include 2, 3, 5. 
    //For example, 6, 8 are ugly while 14 is not ugly since it includes another prime factor 7.
    public boolean isUgly(int num){
    	if(num==1)
    		return false;
    	else return isUgly2(num);
    }
    public boolean isUgly2(int num){
    	if(num == 0)
    		return false;
    	if(num==1)
    		return true;
    	return isUgly2(beUglier(num));
    }
    public int beUglier(int num){
    	if(num%2==0)
    		return num/2;
    	if(num%3==0)
    		return num/3;
    	if(num%5==0)
    		return num/5;
    	return 0;
    }
    
    // no_204 count primes
    public int countPrimes(int n) {
    	
    	if(n==0){
    		return 0;
    	}
    	
    	int[] p = new int[n];
    	for (int i = 0; i < p.length; i++) {
			p[i] = i;
		}
    	int target = 2;
    	int j = 2;
    	
    	while(target<n){
        	while(target*j < n){
        		p[target*j] = 0;
        		j++;
        	}
        	j = 2;
        	target++;
        	while(target<n-1 && p[target]==0){
        		target ++;
        	}
        	
    	}
    	int count = 0;
    	for (int i = 0; i < p.length; i++) {
			if(p[i]!=0)
				count++;
		}
    	return count-1;
    }
    
    // no_58 length of last word
    public int lengthOfLastWord(String s) {
        if(s.length() == 0 || s==null || s==" " || s==""){
            return 0;
        }else{
        String[] tmp = s.split(" ");
        String tmp2 = tmp[tmp.length-1];
        return tmp2.length();
        }
    }
    
    // no_279 perfect squares
    public int numSquares(int n) {
        return 0;
    }
    
    
    // no_403 frog jump
    // need debugging...
    
    public int res = 1;
    public int capacity = 1;

    public boolean canCross(int[] stones) {
    	if(stones.length == 1)
    		return true;
    	if(stones[1] > 1)
    		return false;
    	// res: the farthest stone frog can reach
    	int res = 1;
    	// capacity: the distance frog can jump currently
    	int capacity = 1;
    	// procedure refreshed the res and capacity and start point, until the end
    	procedure(stones, res, capacity, 1);
    	// after procedure, the res will have a final value, if is this value is less than stones[stones.length-1], return false
    	System.out.println(res);
    	System.out.println(this.res);
        return (this.res==stones[stones.length-1]);
    }
    
    void procedure(int[] stones, int res, int capacity, int start){
    	int i = start;	
    	if(stones[i+1] > stones[i]+capacity+1)
    		return ;
    	else{
    		int index = i+1;
    		// k-1 + old <= new <= k+1 +old
    		while(stones[index] <= stones[i] + capacity + 1 && stones[index] >= stones[i] + capacity - 1){
    			if(stones[index]>=this.res){
   					this.res = stones[index];
   					res = stones[index];
    			}
   				this.capacity = stones[index] - stones[i];
   				capacity = stones[index] - stones[i];
   				procedure(stones, res, capacity, index);
   				if(index++ >= stones.length)    					
   					break;
    		}
   		}
    }
    // end of no_403
    
    // no_36 valid sudoku 
    public boolean isValidSudoku(char[][] board) {
        boolean[] visited = new boolean[9];
        
        // row
        for(int i = 0; i<9; i++){
            Arrays.fill(visited, false);
            for(int j = 0; j<9; j++){
                if(!process(visited, board[i][j]))
                    return false;
            }
        }
        
        //col
        for(int i = 0; i<9; i++){
            Arrays.fill(visited, false);
            for(int j = 0; j<9; j++){
                if(!process(visited, board[j][i]))
                    return false;
            }
        }
        
        // sub matrix
        for(int i = 0; i<9; i+= 3){
            for(int j = 0; j<9; j+= 3){
                Arrays.fill(visited, false);
                for(int k = 0; k<9; k++){
                    if(!process(visited, board[i + k/3][ j + k%3]))
                    return false;                   
                }
            }
        }
        return true;
    }
    
    private boolean process(boolean[] visited, char digit){
        if(digit == '.'){
            return true;
        }
        
        int num = digit - '0';
        if ( num < 1 || num > 9 || visited[num-1]){
            return false;
        }
        
        visited[num-1] = true;
        return true;
    }
    // end no_36
    
    
    // no_179 Largest Number
    public static class numbersComparator implements Comparator<String>{
    	@Override
    	public int compare(String o1, String o2) {
    		// TODO Auto-generated method stub
    		String s1 = o1 + o2;
    		String s2 = o2 + o1;
    		return s2.compareTo(s1);
    	}
    }
    
    public static String largestNumber(int[] nums){
		PriorityQueue<String> queue = new PriorityQueue<String>();
        StringBuilder sb = new StringBuilder();
        for(int i = 0; i < nums.length; i++){
            queue.add(String.valueOf(nums[i]));
        }
        boolean zero_f = true;
        while(!queue.isEmpty()){
            String tmp = queue.poll();
            if(!tmp.equals("0")) zero_f = false;
            sb.append(tmp);
        }
        if(zero_f) return "0";
        return sb.toString();
    }
    
    // no_268 missing number
    public int missingNumber(int[] nums){
    	int len = nums.length;
    	int res = 0;
    	for (int i = 0; i < len; i++)
			res = (res ^ nums[i]);
    	res = res ^ (len+1);
    	return res;
    }
    
    public int missingNumber_v2(int[] nums){
    	int len = nums.length;
    	int expected = (len+1)*len/2;
    	for (int i = 0; i < len; i++)		
    		expected -= nums[i];
    	return expected;
    }
    
    // no_269 alien language

    // no_205 isomorphic
    public boolean isIsomorphic(String s, String t) {
    	
    	int len = s.length();
    	char[] tmp = new char[len];
    	for (int i = 0; i < len; i++) {
    		tmp[i] = t.charAt(i);
    		char c = s.charAt(i);
			for (int j = i; j < len; j++) {
				if(s.charAt(j) == c)
					tmp[j] = t.charAt(j);
			}
		}
    	String res = "";
    	for (int i = 0; i < len; i++) {
			res += tmp[i];
		}
        return res.equals(t);
    }
    
    // main function
    public static void main(String[] args){
    	long start = System.currentTimeMillis();
    	Solution s = new Solution();
    	System.out.println(s.isIsomorphic("titletitletitletitletitletitletitletitletitletitle", "paperpaperpaperpaperpaperpaperpaperpaperpaperpaper"));
    	//int[] nums = {0,1,2,3,4,5,6,8,9,10};
    	//System.out.println(s.missingNumber(nums));
    	//System.out.println(s.missingNumber_v2(nums));
    	//System.out.println(largestNumber(new int[]{3,33,30,6,61,67,60}));
    	//System.out.println(s.canCross(new int[]{0,1,3,5,6,8,12,17}));
    	//System.out.println(s.countPrimes(14));
    	//System.out.println(s.isUgly(1));
    	//String[] strs = {"cc","cc"};
    	//System.out.println(strs[0].charAt(0));
    	//System.out.println(s.longestCommonPrefix(strs));
    	//System.out.println(s.romanToInt("MMMDCXLIX"));
    	//int[] nums = {3};
    	//System.out.println(s.removeElement(nums, 3));
    	//System.out.println((int)'B');
    	//System.out.println(s.convertToTitle(703));
    	//System.out.println((char)66);
    	//System.out.println(s.trailingZeroes(1444444));
    	//System.out.println(s.trailingZeroes1(1444444));
    	long end = System.currentTimeMillis();
    	System.out.println("Time:" + (end-start));
    }
}