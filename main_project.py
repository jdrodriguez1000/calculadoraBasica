from math_functions import Math_Functions

while True:
    try:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        if num2==0:
            print("zero Division error")
            raise ZeroDivisionError
        
        break
    except:
        print("Enter numerical information")
        #raise TypeError ("could not convert string to float")



functions_math = Math_Functions()

result_to_add = functions_math.to_add(num1, num2)
result_to_divide = functions_math.to_divide(num1, num2)
result_to_subtract = functions_math.to_subtract(num1, num2)
result_to_multiply = functions_math.to_multiply(num1, num2)

print(f"The result of the sum is: {result_to_add}")
print(f"The result of the subtraction the is: {result_to_subtract}")
print(f"The result of the multiplication is: {result_to_multiply}")
print(f"The result of the division is: {result_to_divide}")
