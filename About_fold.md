# Description:
This is an implementation of the fold function in Python without using the 'reduce' built in function.

# About Fold function:
Fold function is a functional that takes a sequence of type A, an initial value of type B, and returns a value of type B.

## Types of fold function in:
1. Left  fold  (**foldl**) with initial value:    **reduce(func, list, initval)**
2. Left  fold  (**foldl**) without initial value: **reduce(func, list)**
3. Right fold  (**foldr**) with initial value:    **reduce(lambda x,y: func(y,x), reversed(list), initval)**
4. Right fold  (**foldr**) without initial value: **reduce(lambda x,y: func(y,x), reversed(list))**

* Left and right fold are determined by the operation inside the function(x,y).
* If initial value is not given, the initial value is set to be the first element of the sequence in left fold and the last element of the sequence in right fold.
* Empty list with no initial value results in an error.
* Special cases like divisoin by zero in diviison function should be taken care of inside function.

# Test examples:
For the list [1,2,3], initial value 0.0, subtract function:
1. foldl (-) 0    [1,2,3] --> ((0 - 1) - 2) - 3 = -6
2. foldl (-) None [1,2,3] --> (1 - 2) - 3 = -4
3. foldr (-) 0    [1,2,3] --> 1 - (2 - (3 - 0)) = 2
4. foldr (-) None [1,2,3] --> 1 - (2 - 3) = 2                  
*  Empty list and no inital value --> 'sequence is empty'

# Running tests:
$ python fold_test.py

---------------------------------
> Ran 5 tests in 0.001s

> OK

# More tests to do:
* Test for division: function is sensitive to division by zero
* Test for multiplication: special case when initial value is 0
* Test for addition function might be unnecessary
