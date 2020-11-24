# Negating propositions involving for all

Over the last few tasks, you have learned about the ___conjunction___, ___disjunction___, ___implication___ and ___biconditional___ connectives and how the truth values that for the propositions that are constructed from pairs of propositions using these connectives can be determined from the truth values of the two original propositions.  In these two tasks, we are now going to consider logical propositions that can be constructed if we are given more than two propositions.   

An example of a logical proposition that is constructed from many individual propositions is :

![](https://render.githubusercontent.com/render/math?math=\forall\a\in\A\quad\a>4)

This statement reads "for all a in the set A a is greater than 4."  

The function called `testForAll` that I have written in `main.py` returns a value of one if this proposition is true for the input numpy array `A` and a value of zero otherwise.  To complete the exercise I would like you to complete the function called `negationForAll`.  This function should return a value of 1 if the negation of the above statement is true for the data in the input array called `A`.
