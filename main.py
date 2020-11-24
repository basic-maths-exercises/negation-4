import numpy as np

def testForAll( A ) :
  v = 1 
  for a in A : 
    if a <= 4 : v = 0
  return v
  
def negationForAll( A ) :
  # Your code goes here 

  
# This code allows you to test the functions you have written
print(testForAll([5,6,7,8,9,10]), "the proposition is true for this set")
print(negationForAll([5,6,7,8,9,10]), "the negation is false for this set")
print(testForAll([3,4,5,6,7,8,9]), "the proposition is false for this set")
print(negationForAll([3,4,5,6,7,8,9]), "the negation is true for this set")
