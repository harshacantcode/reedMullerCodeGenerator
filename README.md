# reedMullerCodeGenerator

Given the parameters r (the maximum degree of a monomial) and m (the number of binary variables),
the corresponding Reed Muller code is generated. This code is not a perfect code but has a cardinality of 
2^(dimension of the code). The dimension of the code is given by the summation of all mCi values where m is as 
defined above and i goes from 0 (the minimum degree of a monomial in the code) to r
(as defined above, the maximum degree of the monomial).

Instead of using the python syntax x ** y to calculate x ^ y (x to the power of y),
this code uses the binary representation of y to figure out how many times to multiply x by itself.
This small snippet of code is very handy to understand the power of binary representation of a number 
and is handy to understand binary operators.

This code doesn't use the typical python lists but uses arrays as an alternative
