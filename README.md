# Mixed-Radix-Numbers
A little module for doing arithmetic with mixed radix numbers like time.

The arithmetic this module can do is:
- add
- subtract

An example would be 1:20 + 2 hours and 41 mins = 4:01 or how it is represented in the code, [1, 20] + [2, 41] = [4, 1]. This module can also handle digits of given numbers that are greater than the given bases. For example, 9,000 minutes + 1 hour and 20 minutes = 6 days, 7 hours, and 20 minutes. Even though 9,000 is beyond base 60, you can just add the lists [9000] and [1, 20] together and still get the correct result, [6, 7, 20].

Numbers are represented as lists, so 10 and -99 would need to be converted into [1, 0] and [-9, 9]. Negative numbers have the most significant digit in the list representation as a negative.

For numbers with established representations like hexadecimal where 10 = a, there is no support for that kind of representation in this module. All the values are represented as their decimal equivalent. To work with hexadecimal, for example, the numbers would have to be converted from [2, A, B] to [2, 10, 11]. The reason for this is to allow for massive bases like base 9,000 since there isn't really a single character representation for 9,000.
