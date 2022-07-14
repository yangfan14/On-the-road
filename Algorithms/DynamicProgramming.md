# Dynamic programming

Dynamic programming is both a mathematical optimization method and a computer programming method. In both contexts it refers to simplifying a complicated problem by breaking it down into simpler sub-problems in a recursive manner. While some decision problems cannot be taken apart this way, decisions that span several points in time do often break apart recursively.


### There are two ways to implement a DP algorithm:

Bottom-up, also known as tabulation.

Top-down, also known as memoization.

##### Which is better?

Any DP algorithm can be implemented with either method, and there are reasons for choosing either over the other. However, each method has one main advantage that stands out:

A bottom-up implementation's runtime is usually faster, as iteration does not have the overhead that recursion does.

A top-down implementation is usually much easier to write. This is because with recursion, the ordering of subproblems does not matter, whereas with tabulation, we need to go through a logical ordering of solving subproblems.

### :bulb: Life-long Dynamic Programming

It is an execution of dynamic programming in our life, and memory is the key of it! Specificly, life will go only once and can not go reversely, so it is one-iteration (at the time dimension) bottom-up pattern. The problem may be to anwser what the maximum/minimum/accumulate *** value is in your life.

We do not know what is the last needed answer until the last moment since all the values at past each year should be considered to get the last answer. Also, to avoid "back to the past", we should do the work (getting the data at each year) currently in each year. According to dynamic programming, we use a memo/dp array to carry on the data of each year with us(the array turns out to be our brain memory and archive!), so we are able to calculate the answer from the memo without go back (which is not possible). Otherwise, if you could not remember the data, nor have taken notes of the data, you would not get the data any more (data is lost).
