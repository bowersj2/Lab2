'''
   primecheckertests.py
   Jeff Ondich, 9 May 2012
   Updated for use in a lab exercise, 4 Nov 2013
'''

import primechecker
import unittest

class PrimeCheckerTester(unittest.TestCase):
    def setUp(self):
        #self.prime_checker = primechecker.PrimeChecker(100)
		
	print("Check 1")
	   #booksdatasource.BooksDataSource('books.csv')
	   #Jeff's code from class^^^

    def tearDown(self):
        pass
		
	print("Check 2")
    
	def test_zero(self):
        self.assertTrue(self.prime_checker.is_prime(0))

	print("Check 3")
	
    def test_two(self):
        self.assertTrue(self.prime_checker.is_prime(2))

	print("Check 4")
	
    def test_prime(self):
        self.assertTrue(self.prime_checker.is_prime(97))
	
	print("Check 5")
	
    def test_composite(self):
        self.assertFalse(self.prime_checker.is_prime(96))

	print("Check 6")
	
    def test_primes_below(self):
        self.assertEqual(self.prime_checker.get_primes_below(20), [2, 3, 5, 7, 11, 13, 17, 19])
	
	print("Check 7")
		
    def test_primes_neg(self):
	    self.assertFalse(self.prime_checker.is_prime(-1))
		
	print("Check 8")

if __name__ == '__main__':
    unittest.main()

