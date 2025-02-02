#sum function definition 
#Output: Sum first element with each element of seq = [0,1, 2, 3, 4] Sum=  10
def sum(seq):
    if not seq:
        return 0
    else:
        return seq[0] + sum(seq[1:])

#Fold Right function definition. if the list seq ist empty the initial value will be init.
#if list is not empty the funtion output will be: foldr f z (x:xs) = f x (foldr f z xs)
def foldr(func, init, seq):
    if not seq:
        return init
    else:
        return func(seq[0], foldr(func, init, seq[1:]))

#Output Sum using the funktion foldr 
def sum_with_foldr(seq):
    return foldr(lambda seqval, acc: seqval + acc, 0, seq)



#------------------------------ Testing --------------------------------#

import unittest


class TestFold(unittest.TestCase):
    def test_sum(self):
        self.assertEqual(sum([0,1, 2, 3, 4]), 10)
        self.assertEqual(sum([12]), 12)
        self.assertEqual(sum([]), 0)

        self.assertEqual(sum_with_foldr([0, 1, 2, 3, 4]), 10)
        self.assertEqual(sum_with_foldr([12]), 12)
        self.assertEqual(sum_with_foldr([]), 0)

        
if __name__ == '__main__':
    unittest.main()

