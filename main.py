
__author__ = "Krzysztof Penar"
__version__ = "0.1.0"


import sys
from calculator import Calculator

def main():
    for arg in sys.argv[1:]:
        priceArg = int(arg)
        calcObj = Calculator(priceArg)
        print(calcObj.Calc())
    


if __name__ == "__main__":
    """ This is executed when run from the command line """
    main()