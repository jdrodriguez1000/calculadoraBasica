from math_functions import Math_Functions

while True:
    try:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        break
    except:
        print("Ingrese informacion numerica")
        #raise TypeError ("could not convert string to float")



functions_math = Math_Functions()

result_to_add = functions_math.to_add(num1, num2)
result_to_subtract = functions_math.to_subtract(num1, num2)
result_to_multiply = functions_math.to_multiply(num1, num2)
print(f"La suma es : {result_to_add}")
print(f"La resta es : {result_to_subtract}")
print(f"La multiplicacion es : {result_to_multiply}")

