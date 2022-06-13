# Dynamic programming

Dynamic programming is both a mathematical optimization method and a computer programming method. In both contexts it refers to simplifying a complicated problem by breaking it down into simpler sub-problems in a recursive manner. While some decision problems cannot be taken apart this way, decisions that span several points in time do often break apart recursively.


### There are two ways to implement a DP algorithm:

Bottom-up, also known as tabulation.

Top-down, also known as memoization.

##### Which is better?

Any DP algorithm can be implemented with either method, and there are reasons for choosing either over the other. However, each method has one main advantage that stands out:

A bottom-up implementation's runtime is usually faster, as iteration does not have the overhead that recursion does.

A top-down implementation is usually much easier to write. This is because with recursion, the ordering of subproblems does not matter, whereas with tabulation, we need to go through a logical ordering of solving subproblems.
