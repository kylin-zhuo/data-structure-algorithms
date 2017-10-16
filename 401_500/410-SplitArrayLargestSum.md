  ### Split Array Largest Sum

  Given an array which consists of non-negative integers and an integer m, you can split the array into m non-empty continuous subarrays. Write an algorithm to minimize the largest sum among these m subarrays.

  Note:
  If n is the length of array, assume the following constraints are satisfied:

  1 ≤ n ≤ 1000
  1 ≤ m ≤ min(50, n)
  Examples:

  Input:
  `nums = [7,2,5,10,8]
  m = 2`

  Output:
  `18`

  Explanation:
  There are four ways to split nums into two subarrays.
  The best way is to split it into ``[7,2,5]`` and ``[10,8]``,
  where the largest sum among the two subarrays is only `18`.

  -----
#### Approach 1: Binary Search

Noticed that the largest sum of a certain subarray is bounded:

- upper bound: `sum(nums)`
- lower bound: `max(nums)`

Therefore the result can be searched via binary search in the range between lower and upper bounds. Now a judging function is required to indicate how to shrink the search domain, and it can be a function returning whether the current value is too large or too small for fit m subarrays.

If it is too large, we can fit not less than m chunks of subarrays in `nums`, otherwise the number of subarrays will outbound m before reaching the end of `nums`.

```python

def splitArray(nums, m):

  def larger(val):
    cur = count = 0
    for n in nums:
      cur += n
      if cur >= val:
        count += 1
        if count >= m:
          return False
        cur = n
    return True

  lo, hi = max(nums), sum(nums)
  while lo < hi:
    mid = (lo+hi) / 2
    if larger(mid):
      hi = mid
    else:
      lo = mid + 1
  return lo
```
-----
#### Approach 2: Dynamic Programming
