from math import sqrt
from math import pow



class Math_Functions:

    
    def __init__(self):
        pass

    
    def to_add(self, number1, number2 ):
        try:
            number1 = float(number1)
            number2 = float(number2)
            resultadd = number1 + number2
            return resultadd
        except ValueError as err:
            print(err)
            raise

        
    def to_subtract(self, number1, number2):
        try:
            number1 = float(number1)
            number2 = float(number2)
            resultsubtract = number1 - number2
            return resultsubtract
        except ValueError as err:
            print(err)
            raise
            

    
    def to_multiply(self, number1, number2):
        try:
            number1 = float(number1)
            number2 = float(number2)
            resultmultiply = number1 * number2
            return resultmultiply
        except ValueError as err:
            print(err)
            raise
            
                
    def to_divide(self, number1, number2):
        try:
            number1 = float(number1)
            number2 = float(number2)
            if (number2==0):
                raise (ZeroDivisionError)
            resultdivide = number1 / number2
            return resultdivide
        except ValueError as err:
            print(err)
            raise
    
    
    def to_power(self, number1, number2):
        resultpower = pow(number1, number2)
        return resultpower
    
    
    def to_squareroot(self, number1):
        resultsqureroot = sqrt(number1)
        
#function_math = Math_Functions()
