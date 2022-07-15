## Kadane's algorithm
#### Find the maximum sum of subarray
```
ans = cur = None   # or float("-inf")
for x in nums:
    cur = x + max(cur, 0)
    ans = max(ans, cur)
return ans
```
We can modify it to find the minimum sum of subarray as well
```
ans = cur = None   # or float("inf")
for x in nums:
    cur = x + min(cur, 0)
    ans = min(ans, cur)
return ans
```
#### Examples
- https://leetcode.com/problems/maximum-subarray/
- https://leetcode.com/problems/maximum-sum-circular-subarray/

#### :bulb: Thoughts
Along the journey, only bring the guys that may contribute to your goal with you, or you have to dispose them and start a new try. 
But do not forget to update the possibility based on your tries.
