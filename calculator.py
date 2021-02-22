# Requirements
# Minimum property purchase price	Maximum property purchase price	Stamp Duty rate (only applies to the part of the property price falling within each band)
# £0	£250,000	0%
# £250,001	£325,000	5%
# £325,001	£750,000	10%
# Over £750,000	 	12%

class Calculator:
    price = ()
    def __init__(self, price):
        self.price = price
    
    def Calc(self):
        firstBand = 0 
        secondBand = 0 
        thirdBand = 0 
        forthband = 0 
        #This is first band ciurrently zero 
        if(self.price <= 250000):
            firstBand = 0

        if(self.price > 250000 ): 
            if(self.price > 325000):
                secondBand = 75000 *  (5/100)
            else:
                taxable = self.price - 250000
                secondBand = taxable * (5/100)

        if(self.price > 325000):
            if(self.price > 750000):
                thirdBand = 425000 *  (10/100)
            else:
                taxable = self.price - 325000
                thirdBand = taxable * (10/100)

        if(self.price > 750000): 
            taxable = self.price - 750000
            forthband = taxable * (12/100)

            
        return (firstBand + secondBand +  thirdBand +forthband)
