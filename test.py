import unittest
import sys
from calculator import Calculator

# Requirements
# Minimum property purchase price	Maximum property purchase price	Stamp Duty rate (only applies to the part of the property price falling within each band)
# £0	£250,000	0%
# £250,001	£325,000	5%
# £325,001	£750,000	10%
# Over £750,000	 	12%

class TestCalc(unittest.TestCase):

    def testFirstBand(self):

        calcObj = Calculator(200000)
        self.assertEqual(calcObj.Calc(),0,"Should be Zero")

    def testSecondBand(self):
    
        calcObj = Calculator(275000)
        self.assertEqual(calcObj.Calc(),1250,"Should be 1250")
    
    def testThirdBand(self):
        
        calcObj = Calculator(500000)
        self.assertEqual(calcObj.Calc(),21250,"Should be 21250")
    
    def testForthBand(self):
            
        calcObj = Calculator(900000)
        self.assertEqual(calcObj.Calc(),64250,"Should be 64250")
if __name__ == '__main__':
    unittest.main()