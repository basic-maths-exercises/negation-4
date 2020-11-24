import unittest
from main import *

class UnitTests(unittest.TestCase) :
    def test_negation_function(self) :
        for i in range(1,10) :
            if i%2==0 : d = np.random.randint(5,10,size=10)
            else : d = np.random.randint(1,10,size=10)
            if testForAll(d)==1 : self.assertTrue( negationForAll(d)==0, "The negation function is not working" )
            else : self.assertTrue( negationForAll(d)==1, "The negation function is not working" )
